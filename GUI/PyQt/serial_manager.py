"""
Serial Port Manager Module

This module provides a singleton class for managing serial port connections
across different components of the application.
"""

from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QObject, Signal, QByteArray, QMutex, QMutexLocker
from collections import deque

import Settings


class SerialPortManager(QObject):
    """
    Singleton class for managing serial port connections.

    This class ensures that only one serial port connection is active at a time
    and provides methods for opening, closing, and communicating with the port.
    It also handles asynchronous data acquisition using the readyRead signal.
    """

    # Signals
    error_occurred = Signal(str)
    connection_changed = Signal(bool)
    data_received = Signal(list)  # Signal emitted when valid data is received

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SerialPortManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        super().__init__()
        self._serial_port = QSerialPort()
        self._port_name = ""
        self._baud_rate = Settings.BaudRate
        self._buffer = ""
        self._data_buffer = deque(maxlen=1000)  # Buffer for storing processed data
        self._mutex = QMutex()  # Mutex for thread-safe access to the data buffer
        self._last_valid_data = None
        self._initialized = True

        # Connect the readyRead signal to the data handler
        self._serial_port.readyRead.connect(self._handle_ready_read)

    @property
    def is_open(self):
        """Check if the serial port is open."""
        return self._serial_port.isOpen()

    @property
    def port_name(self):
        """Get the current port name."""
        return self._port_name

    def configure_port(self, port_name):
        """
        Configure the serial port with the specified port name.

        Args:
            port_name (str): The name of the port to configure

        Returns:
            bool: True if configuration was successful, False otherwise
        """
        try:
            # Close the port if it's already open
            if self._serial_port.isOpen():
                self._serial_port.close()

            self._port_name = port_name

            # Configure the port
            self._serial_port.setPortName(self._port_name)
            self._serial_port.setBaudRate(self._baud_rate)
            self._serial_port.setDataBits(QSerialPort.Data8)
            self._serial_port.setParity(QSerialPort.NoParity)
            self._serial_port.setStopBits(QSerialPort.OneStop)
            self._serial_port.setFlowControl(QSerialPort.NoFlowControl)

            return True

        except Exception as e:
            self.error_occurred.emit(f"Error configuring port: {str(e)}")
            return False

    def open(self):
        """
        Open the serial port.

        Returns:
            bool: True if the port was successfully opened, False otherwise
        """
        if not self._port_name:
            self.error_occurred.emit("No port selected")
            return False

        try:
            # Open the port
            if not self._serial_port.open(QSerialPort.ReadWrite):
                error_msg = f"Failed to open port {self._port_name}: {self._serial_port.errorString()}"
                self.error_occurred.emit(error_msg)
                return False

            self.connection_changed.emit(True)
            return True

        except Exception as e:
            self.error_occurred.emit(f"Error opening port: {str(e)}")
            return False

    def close(self):
        """Close the serial port."""
        if self._serial_port.isOpen():
            self._serial_port.close()
            self.connection_changed.emit(False)

    def write(self, data):
        """
        Write data to the serial port.

        Args:
            data (str): The data to write to the port

        Returns:
            bool: True if the data was successfully written, False otherwise
        """
        if not self._serial_port.isOpen():
            return False

        try:
            # Convert string to bytes and write to port
            bytes_written = self._serial_port.write(data.encode('utf-8'))
            return bytes_written > 0

        except Exception as e:
            self.error_occurred.emit(f"Error writing to port: {str(e)}")
            return False

    def _is_valid_number(self, value):
        """
        Check if a string can be converted to a float.

        Args:
            value (str): The string to check

        Returns:
            bool: True if the string can be converted to a float, False otherwise
        """
        # Check if the string is just a minus sign
        if value == '-':
            return False

        try:
            float(value)
            return True
        except ValueError:
            return False

    def _handle_ready_read(self):
        """
        Handle the readyRead signal from the serial port.

        This method is called automatically when data is available on the serial port.
        It reads the data, processes it, and emits the data_received signal if valid data is found.
        """
        if not self._serial_port.isOpen():
            return

        try:
            # Read all available data
            rx = self._serial_port.readAll().data()
            if not rx:
                return

            # Convert bytes to string and append to buffer
            rx_serial = str(rx, 'utf8')
            self._buffer += rx_serial

            # Process complete lines from the buffer
            if '\n' in self._buffer:
                lines = self._buffer.split('\n')

                # The last element might be an incomplete line
                self._buffer = lines[-1]

                # Process all complete lines
                complete_lines = lines[:-1]

                # Look for a valid line with values
                for line in reversed(complete_lines):  # Process newest lines first
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    # Split the line into values and clean them
                    values = []
                    for val in line.split(','):
                        # Clean the value (remove \r and other whitespace)
                        clean_val = val.strip().rstrip('\r')
                        # Only add valid numeric values
                        if clean_val and self._is_valid_number(clean_val):
                            values.append(clean_val)

                    # Try to use lines with any number of values
                    if len(values) > 0:
                        # If we have exactly 8 values, use them directly
                        if len(values) == 8:
                            processed_values = values
                        # If we have fewer than 8 values, pad with zeros
                        elif len(values) < 8:
                            processed_values = values + ['0.0'] * (8 - len(values))
                        # If we have more than 8 values, use the first 8
                        else:
                            processed_values = values[:8]

                        # Store the processed data
                        with QMutexLocker(self._mutex):
                            self._data_buffer.append(processed_values)
                            self._last_valid_data = processed_values

                        # Emit the data_received signal
                        self.data_received.emit(processed_values)
                        return

        except Exception as e:
            self.error_occurred.emit(f"Error processing serial data: {str(e)}")

    def get_latest_data(self):
        """
        Get the latest valid data from the buffer.

        Returns:
            list: The latest valid data, or None if no valid data is available
        """
        # First try to read directly from the serial port
        direct_data = self.read_and_process_data()
        if direct_data:
            return direct_data

        # If direct read fails, return the last valid data from the buffer
        with QMutexLocker(self._mutex):
            if self._last_valid_data:
                return self._last_valid_data.copy()
            else:
                return None

    def read_and_process_data(self):
        """
        Read data directly from the serial port and process it.

        This method provides an alternative to the signal-based approach.

        Returns:
            list: The processed data, or None if no valid data is available
        """
        if not self._serial_port.isOpen():
            return None

        try:
            # Check if there's data available - non-blocking approach
            bytes_available = self._serial_port.bytesAvailable()

            # If no data is available, return None immediately
            # This avoids blocking the UI thread
            if bytes_available <= 0:
                return None

            # Read data (we know bytes_available > 0 at this point)
            raw_data = self._serial_port.readAll().data()
            if not raw_data:
                return None

            # Convert bytes to string
            data_str = str(raw_data, 'utf8')

            # Process the data
            lines = data_str.split('\n')

            # Process all complete lines
            for line in reversed(lines):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                # Split the line into values
                values = []

                # Try different delimiters (comma, space, tab)
                for delimiter in [',', ' ', '\t']:
                    parts = line.split(delimiter)
                    if len(parts) > 1:  # If we found multiple parts
                        for val in parts:
                            clean_val = val.strip().rstrip('\r')
                            if clean_val and self._is_valid_number(clean_val):
                                values.append(clean_val)

                        if values:  # If we found valid values, stop trying delimiters
                            break

                # If no delimiter worked, try the whole line as a single value
                if not values:
                    clean_val = line.strip().rstrip('\r')
                    if clean_val and self._is_valid_number(clean_val):
                        values.append(clean_val)

                # If we have values, process them
                if values:
                    # Ensure we have exactly 8 values
                    if len(values) < 8:
                        values.extend(['0.0'] * (8 - len(values)))
                    elif len(values) > 8:
                        values = values[:8]

                    # Store the processed data
                    with QMutexLocker(self._mutex):
                        self._data_buffer.append(values)
                        self._last_valid_data = values

                    # Emit the data_received signal
                    self.data_received.emit(values)

                    return values

        except Exception as e:
            self.error_occurred.emit(f"Error in direct read: {str(e)}")

        return None

    def get_data_buffer(self):
        """
        Get a copy of the entire data buffer.

        Returns:
            list: A copy of the data buffer
        """
        with QMutexLocker(self._mutex):
            return list(self._data_buffer)

    def clear_data_buffer(self):
        """
        Clear the data buffer.
        """
        with QMutexLocker(self._mutex):
            self._data_buffer.clear()
            self._last_valid_data = None

    def clear_buffer(self):
        """
        Clear the input buffer.
        """
        self._buffer = ""
        self.clear_data_buffer()

    def read_all(self):
        """
        Read all available data from the serial port.

        This method is maintained for backward compatibility.
        It's recommended to use the asynchronous approach with the readyRead signal instead.

        Returns:
            bytes: The data read from the port, or None if an error occurred
        """
        if not self._serial_port.isOpen():
            return None

        try:
            return self._serial_port.readAll().data()

        except Exception as e:
            self.error_occurred.emit(f"Error reading from port: {str(e)}")
            return None

    def bytes_available(self):
        """
        Get the number of bytes available to read from the serial port.

        This method is maintained for backward compatibility.
        It's recommended to use the asynchronous approach with the readyRead signal instead.

        Returns:
            int: The number of bytes available, or 0 if the port is not open
        """
        if not self._serial_port.isOpen():
            return 0

        return self._serial_port.bytesAvailable()

    def get_serial_port(self):
        """
        Get the underlying QSerialPort object.

        Returns:
            QSerialPort: The serial port object
        """
        return self._serial_port


# Create a global instance of the serial port manager
serial_manager = SerialPortManager()
