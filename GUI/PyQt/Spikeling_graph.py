"""
Spikeling Graph Module

This module provides functionality for plotting and recording data from the Spikeling device.
It handles serial communication, data visualization, and data export.
"""

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPen
import pyqtgraph as pg

import collections
import numpy as np
import pandas as pd

import Settings
from serial_manager import serial_manager

# Constants
DOWNSAMPLING = 6
SAMPLE_INTERVAL = 0.1
TIME_WINDOW = 500
TIME_WINDOW_DISPLAY = 200
PEN_WIDTH = 1.5
VM_MIN = -90
VM_MAX = 30
CURRENT_MIN = -100
CURRENT_MAX = 100


class SpikelingGraph:
    """
    Class for handling Spikeling device data visualization and recording.

    This class manages the connection to the Spikeling device, data acquisition,
    plotting, and recording of the data to CSV files.
    """

    def __init__(self, parent):
        """
        Initialize the SpikelingGraph instance.

        Args:
            parent: The parent object (NavigationButtons instance) that contains UI elements
        """
        self.parent = parent
        self.ui = parent.ui
        self.timer = None
        self.data = ['0'] * 8  # Default data array
        self.serial_flag = False
        self.record_flag = False
        self.i_downsampling = 0
        self.stim_counter = 0
        self.current_plots = None
        self.buffer = ""  # Buffer for storing partial serial data
        self.last_valid_data = None  # Store the last valid data line

        # Set SerialFlag in parent for use in Page101
        self.parent.SerialFlag = False

        # Initialize attributes that will be set later
        self.df_Stim = None
        self.df_yStim = None

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

    def spikeling_plot(self):
        """
        Main function to handle Spikeling plotting.

        This function is called when the Connect button is clicked.
        It sets up the serial connection, initializes parameters, and starts the timer
        for data acquisition and plotting.
        """
        if self.ui.Spikeling_ConnectButton.isChecked():
            # Setup when connecting
            if not self.set_serial():
                # Failed to open serial port
                self.ui.Spikeling_ConnectButton.setChecked(False)
                return

            self.set_init_parameters()
            self.set_plot_curve()
            self.set_plot()

            self.serial_flag = True
            self.parent.SerialFlag = True  # Set SerialFlag in parent for use in Page101

            # Initialize stimulus counter
            self.stim_counter = 0

            # Connect to the data_received signal from the serial manager
            serial_manager.data_received.connect(self.on_data_received)

            # Set up timer for plot updates with explicit interval (1ms for fast updates)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_plot)
            self.timer.start(0)
        else:
            # Cleanup when disconnecting
            self.ui.Spikeling_ConnectButton.setText("Connect Spikeling Screen")
            self.ui.Spikeling_ConnectButton.setStyleSheet(
                f"color: rgb{tuple(Settings.DarkSolarized[14])};\n"
                f"background-color: rgb{tuple(Settings.DarkSolarized[2])};\n"
                f"border: 1px solid rgb{tuple(Settings.DarkSolarized[14])};\n"
                f"border-radius: 10px;"
            )

            # Clean up resources
            self.cleanup()
            self.ui.SpikelingConnectedFlag = False
            self.parent.SerialFlag = False  # Reset SerialFlag in parent

    def update_plot(self):
        """
        Update the plot with new data.

        This function is called by the timer to update the plot with new data
        from the Spikeling device.
        """
        try:
            # We don't need to call get_data() anymore since we're using the asynchronous approach
            # and data is updated directly in the on_data_received method

            # Append latest data into buffer deque
            self.buff_data()

            # Create data array to be exported in .csv if recording is enabled
            self.save_plot_data()

            # Update the plot - we can remove the downsampling since we're using a fixed timer interval
            # that's optimized for smooth visualization
            self.plot_curve()

            # Handle custom stimulus if enabled
            self.handle_custom_stimulus()

            # Handle noise if enabled
            self.handle_noise()
        except Exception as e:
            # Log the error but don't crash the application
            print(f"Error in update_plot: {e}")

            # If we're getting frequent errors, slow down the timer to reduce CPU load
            if hasattr(self, 'timer') and self.timer and self.timer.interval() < 100:
                new_interval = min(100, self.timer.interval() * 2)
                print(f"Increasing timer interval to {new_interval}ms to reduce load")
                self.timer.setInterval(new_interval)

    def on_data_received(self, data):
        """
        Handle data received from the serial port.

        This method is called when the data_received signal is emitted by the serial manager.
        It updates the data attribute with the received data.

        Args:
            data (list): The data received from the serial port
        """
        if data and len(data) == 8:
            self.data = data
            self.last_valid_data = data

    def get_data(self):
        """
        Get the latest data from the serial manager.

        This method is now simplified to use the get_latest_data method from the serial manager,
        which returns the latest valid data processed by the asynchronous data handler.

        Returns:
            list: Processed data array with 8 values, or default values if no data is available.
        """
        # Get the latest data from the serial manager
        latest_data = serial_manager.get_latest_data()

        if latest_data:
            self.data = latest_data
            self.last_valid_data = latest_data
        elif self.last_valid_data is not None:
            self.data = self.last_valid_data

        return self.data

    def buff_data(self):
        """
        Append latest serial data points into buffer deques.

        This method has been optimized to minimize string-to-float conversions
        and streamline error handling.
        """
        try:
            # Check if all required buffer attributes are initialized
            for i in range(8):
                buffer_name = f"databuffer{i}"
                if not hasattr(self, buffer_name) or getattr(self, buffer_name) is None:
                    print(f"Warning: {buffer_name} is not initialized")
                    return

            # The data should already be validated by the serial manager,
            # but we'll add a safety check just in case
            if not self.data or len(self.data) < 8:
                # If data is missing or incomplete, use zeros
                values = [0.0] * 8
            else:
                # Convert all values to float in one go with list comprehension
                # This is more efficient than converting them one by one
                try:
                    values = [float(val) if val and self._is_valid_number(val) else 0.0 for val in self.data]
                except Exception:
                    # If any conversion fails, use zeros
                    values = [0.0] * 8

            # Append values to buffers
            for i in range(8):
                getattr(self, f"databuffer{i}").append(values[i])
        except Exception as e:
            # Log the error but don't crash the application
            print(f"Error in buff_data: {e}")

    def plot_curve(self):
        """
        Update the plot curves with the latest data from buffers.
        """
        try:
            # Check if all required attributes are initialized
            required_attrs = ['x', 'y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 
                             'curve0', 'curve1', 'curve2', 'curve3', 'curve4', 'curve5', 'curve6',
                             'databuffer0', 'databuffer1', 'databuffer2', 'databuffer3', 
                             'databuffer4', 'databuffer5', 'databuffer6']

            for attr in required_attrs:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    print(f"Warning: {attr} is not initialized")
                    return

            # Plot membrane potentials on the main plot
            if self.ui.Spikeling_VmCheckbox.isChecked():
                self.y0[:] = self.databuffer0
                self.curve0.setData(self.x, self.y0)
            else:
                self.curve0.clear()

            if self.ui.Spikeling_StimulusCheckbox.isChecked():
                self.y1[:] = self.databuffer1
                self.curve1.setData(self.x, self.y1)
            else:
                self.curve1.clear()

            if self.ui.Spikeling_InputCurrentCheckbox.isChecked():
                self.y2[:] = self.databuffer2
                self.curve2.setData(self.x, self.y2)
            else:
                self.curve2.clear()

            if self.ui.Spikeling_Syn1VmCheckbox.isChecked():
                self.y3[:] = self.databuffer3
                self.curve3.setData(self.x, self.y3)
            else:
                self.curve3.clear()

            if self.ui.Spikeling_Syn1InputCheckbox.isChecked():
                self.y4[:] = self.databuffer4
                self.curve4.setData(self.x, self.y4)
            else:
                self.curve4.clear()

            if self.ui.Spikeling_Syn2VmCheckbox.isChecked():
                self.y5[:] = self.databuffer5
                self.curve5.setData(self.x, self.y5)
            else:
                self.curve5.clear()

            if self.ui.Spikeling_Syn2InputCheckbox.isChecked():
                self.y6[:] = self.databuffer6
                self.curve6.setData(self.x, self.y6)
            else:
                self.curve6.clear()
        except Exception as e:
            # Log the error but don't crash the application
            print(f"Error in plot_curve: {e}")

    def save_plot_data(self):
        """
        Save the latest buffer data and export them as CSV when recording is stopped.
        """
        # If recording was on and is now turned off, save the data
        if not self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() and self.record_flag:
            self.export_data_to_csv()
            self.record_flag = False
            # Clear data arrays
            for i in range(9):
                self.spikeling_data[i].clear()

        # If recording is on, append data to arrays
        if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked():
            self.record_flag = True

            # Append latest data points to recording arrays
            for i in range(8):
                buffer_name = f"databuffer{i}"
                if hasattr(self, buffer_name) and getattr(self, buffer_name):
                    self.spikeling_data[i + 1].append(getattr(self, buffer_name)[-1])

    def export_data_to_csv(self):
        """
        Export recorded data to a CSV file.
        """
        # Create a numpy array for the dataset
        dataset = np.empty([9, len(self.spikeling_data[1])], dtype=float)

        # Fill the dataset with recorded data
        for i in range(len(self.spikeling_data[1])):
            dataset[0][i] = i * SAMPLE_INTERVAL  # Time
            for j in range(1, 9):
                dataset[j][i] = self.spikeling_data[j][i]

        # Create a dictionary for pandas DataFrame
        data_dict = {
            'Time (ms)': dataset[0],
            'Spikeling Vm (mV)': dataset[1],
            'Stimulus (%)': dataset[2],
            'Total Current Input (a.u.)': dataset[3],
            'Synapse 1 Vm (mV)': dataset[4],
            'Synapse 1 Input (a.u.)': dataset[5],
            'Synapse 2 Vm (mV)': dataset[6],
            'Synapse 2 Input (a.u.)': dataset[7],
            'Trigger': dataset[8]
        }

        # Create DataFrame and save to CSV
        df = pd.DataFrame(data_dict)
        recording_file_name = str(self.ui.Spikeling_SelectedFolderLabel.text())
        df.to_csv(f"{recording_file_name}.csv", index=False)

    def set_init_parameters(self):
        """
        Initialize parameters for Spikeling plotting.
        """
        self.ui.SpikelingConnectedFlag = True
        self.i_downsampling = 0
        self.record_flag = False
        self.trigger = 0
        self.buffer = ""  # Reset the buffer
        self.last_valid_data = None  # Reset the last valid data
        self.ui.Spikeling_Oscilloscope_widget.clear()

        if self.ui.Spikeling_ConnectButton.isChecked() and serial_manager.is_open:
            self.ui.Spikeling_ConnectButton.setText("Connected")
            self.ui.Spikeling_ConnectButton.setStyleSheet(
                f"color: rgb{tuple(Settings.DarkSolarized[3])};\n"
                f"background-color: rgb{tuple(Settings.DarkSolarized[11])};\n"
                f"border: 1px solid rgb{tuple(Settings.DarkSolarized[14])};\n"
                f"border-radius: 10px;"
            )
        else:
            self.ui.Spikeling_ConnectButton.setText("Connect Spikeling Screen")
            self.ui.Spikeling_ConnectButton.setStyleSheet(
                f"color: rgb{tuple(Settings.DarkSolarized[14])};\n"
                f"background-color: rgb{tuple(Settings.DarkSolarized[2])};\n"
                f"border: 1px solid rgb{tuple(Settings.DarkSolarized[14])};\n"
                f"border-radius: 10px;"
            )

    def set_serial(self):
        """
        Set up the serial port connection.

        Returns:
            bool: True if the serial port was successfully opened, False otherwise.
        """
        try:
            port_name = self.ui.Spikeling_SelectPortComboBox.currentText()

            # Configure and open the port using the serial manager
            if not serial_manager.configure_port(port_name):
                return False

            if not serial_manager.open():
                return False

        except Exception as e:
            print(f"Serial port error: {e}")
            return False

        return True

    def set_plot_curve(self):
        """
        Initialize the plot curves and data buffers.
        """
        self._interval = SAMPLE_INTERVAL
        self._bufsize = int(TIME_WINDOW / SAMPLE_INTERVAL)

        # Initialize data buffers
        for i in range(8):
            setattr(self, f"databuffer{i}", collections.deque([0.0] * self._bufsize, self._bufsize))

        # Create arrays for plotting
        self.x = np.linspace(-TIME_WINDOW, 0.0, self._bufsize)
        for i in range(7):
            setattr(self, f"y{i}", np.zeros(self._bufsize, dtype=float))

        # Initialize data recording arrays
        self.spikeling_data = []
        for _ in range(9):
            self.spikeling_data.append([])

    def set_plot(self):
        """
        Set up the plot widget and curves.
        """
        # Configure main plot
        self.ui.Spikeling_Oscilloscope_widget.showGrid(x=True, y=True)
        self.ui.Spikeling_Oscilloscope_widget.setRange(xRange=[-TIME_WINDOW_DISPLAY, 0])
        self.ui.Spikeling_Oscilloscope_widget.setRange(yRange=[VM_MIN, VM_MAX])
        self.ui.Spikeling_Oscilloscope_widget.plotItem.setMouseEnabled(x=True, y=True)
        # Allow zooming beyond the default range while still keeping reasonable limits
        self.ui.Spikeling_Oscilloscope_widget.plotItem.vb.setLimits(xMin=-TIME_WINDOW*2, xMax=TIME_WINDOW/10)
        self.ui.Spikeling_Oscilloscope_widget.setLabel('left', 'Membrane potential', 'mV')
        self.ui.Spikeling_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')
        self.ui.Spikeling_Oscilloscope_widget.setLabel('right', 'Current Input', 'a.u.')

        # Store default ranges for reset functionality
        self.default_x_range = [-TIME_WINDOW_DISPLAY, 0]
        self.default_y_range = [VM_MIN, VM_MAX]

        # Connect double-click event to reset view
        self.ui.Spikeling_Oscilloscope_widget.plotItem.vb.sigStateChanged.connect(self.update_views)
        self.ui.Spikeling_Oscilloscope_widget.scene().sigMouseClicked.connect(self.on_plot_clicked)

        # Enable anti-aliasing for smoother curves
        self.ui.Spikeling_Oscilloscope_widget.setAntialiasing(True)

        # Connect the resize signal to update views
        self.ui.Spikeling_Oscilloscope_widget.getViewBox().sigResized.connect(self.update_views)

        # Set up secondary plot for current inputs
        self.current_plots = pg.ViewBox()
        self.ui.Spikeling_Oscilloscope_widget.scene().addItem(self.current_plots)
        self.current_plots.setXLink(self.ui.Spikeling_Oscilloscope_widget)
        self.current_plots.setRange(yRange=[CURRENT_MIN, CURRENT_MAX])
        self.ui.Spikeling_Oscilloscope_widget.getAxis("right").linkToView(self.current_plots)

        # Create plot curves for membrane potentials on the main plot with anti-aliasing
        self.curve0 = self.ui.Spikeling_Oscilloscope_widget.plot(
            self.x, self.y0, pen=pg.mkPen(Settings.DarkSolarized[3], width=PEN_WIDTH, cosmetic=True))
        self.curve0.clear()
        self.curve3 = self.ui.Spikeling_Oscilloscope_widget.plot(
            self.x, self.y3, pen=pg.mkPen(Settings.DarkSolarized[6], width=PEN_WIDTH, cosmetic=True))
        self.curve3.clear()
        self.curve5 = self.ui.Spikeling_Oscilloscope_widget.plot(
            self.x, self.y5, pen=pg.mkPen(Settings.DarkSolarized[8], width=PEN_WIDTH, cosmetic=True))
        self.curve5.clear()

        # Create plot curves for currents and stimulus (secondary plot - right y-axis) with anti-aliasing
        self.curve1 = pg.PlotCurveItem(
            self.x, self.y1, pen=pg.mkPen(Settings.DarkSolarized[5], width=PEN_WIDTH, cosmetic=True))
        self.curve1.clear()
        self.curve2 = pg.PlotCurveItem(
            self.x, self.y2, pen=pg.mkPen(Settings.DarkSolarized[4], width=PEN_WIDTH, cosmetic=True))
        self.curve2.clear()
        self.curve4 = pg.PlotCurveItem(
            self.x, self.y4, pen=pg.mkPen(Settings.DarkSolarized[7], width=PEN_WIDTH, cosmetic=True))
        self.curve4.clear()
        self.curve6 = pg.PlotCurveItem(
            self.x, self.y6, pen=pg.mkPen(Settings.DarkSolarized[10], width=PEN_WIDTH, cosmetic=True))
        self.curve6.clear()

        # Add current and stimulus curves to the secondary plot (right y-axis)
        self.current_plots.addItem(self.curve1)
        self.current_plots.addItem(self.curve2)
        self.current_plots.addItem(self.curve4)
        self.current_plots.addItem(self.curve6)

    def update_views(self):
        """
        Update the views when the plot is resized or zoomed.
        """
        # Set the geometry of the current_plots ViewBox to match the main plot's ViewBox
        self.current_plots.setGeometry(self.ui.Spikeling_Oscilloscope_widget.getViewBox().sceneBoundingRect())

        # Link the views for synchronized panning/zooming
        self.current_plots.linkedViewChanged(self.ui.Spikeling_Oscilloscope_widget.getViewBox(), self.current_plots.XAxis)

    def on_plot_clicked(self, event):
        """
        Handle mouse clicks on the plot.

        Double-click resets the view to the default range.

        Args:
            event: The mouse event
        """
        # Check if it's a double-click (click count is 2)
        if event.double():
            # Reset the view to the default range
            self.ui.Spikeling_Oscilloscope_widget.setRange(xRange=self.default_x_range, yRange=self.default_y_range)
            # Also reset the current_plots view
            self.current_plots.setRange(xRange=self.default_x_range, yRange=[CURRENT_MIN, CURRENT_MAX])

    def handle_custom_stimulus(self):
        """
        Handle custom stimulus if enabled.
        """
        try:
            if not hasattr(self.ui, 'StimCus_toggleButton'):
                return

            if self.ui.StimCus_toggleButton.isChecked():
                try:
                    # # Check if df_yStim and df_Stim are initialized
                    if not hasattr(self, 'df_yStim') or self.ui.df_yStim is None or not hasattr(self, 'df_Stim') or self.ui.df_Stim is None:
                        print("returning early from handle_custom_stimulus: df_yStim or df_Stim not defined")
                        return

                    # Check if stim_counter is within bounds
                    if self.stim_counter >= len(self.ui.df_yStim):
                        self.stim_counter = 0

                    self.stim_cus_value = self.ui.df_yStim[self.stim_counter]

                    if serial_manager.is_open:
                        serial_manager.write(f'SC1 {self.stim_cus_value}\n')
                        self.stim_counter += 1

                    if self.stim_counter > len(self.ui.df_Stim) - 1:
                        self.stim_counter = 0
                        if serial_manager.is_open:
                            serial_manager.write('TR\n')
                except (AttributeError, IndexError) as e:
                    # Handle case where df_yStim or df_Stim is not defined or index is out of range
                    print(f"Error in handle_custom_stimulus: {e}")
            else:
                if serial_manager.is_open:
                    serial_manager.write('SC0\n')
        except Exception as e:
            # Log the error but don't crash the application
            print(f"Error in handle_custom_stimulus: {e}")

    def handle_noise(self):
        """
        Generate and send a new noise value if noise is enabled.

        This function is called by the timer to continuously update the noise
        value sent to the device.
        """
        try:
            # Check if noise toggle button exists
            if not hasattr(self.ui, 'Noise_toggleButton'):
                return

            # Check if noise is enabled
            if self.ui.Noise_toggleButton.isChecked():
                try:
                    # Check if noise slider exists
                    if not hasattr(self.ui, 'Spikeling_Noise_slider'):
                        return

                    # Get the current noise amplitude
                    noise_value = self.ui.Spikeling_Noise_slider.value()

                    # Generate a new random noise value
                    noise = np.random.normal(0, noise_value / 2)

                    # Send the noise value to the device
                    if serial_manager.is_open:
                        serial_manager.write(f'NO1 {noise}\n')
                except Exception as e:
                    # Log specific errors in noise generation
                    print(f"Error generating noise: {e}")
        except Exception as e:
            # Log the error but don't crash the application
            print(f"Error in handle_noise: {e}")

    def cleanup(self):
        """
        Clean up resources when disconnecting.
        """
        # Stop the timer
        if hasattr(self, 'timer') and self.timer:
            self.timer.stop()

        # Disconnect the data_received signal to prevent memory leaks
        try:
            serial_manager.data_received.disconnect(self.on_data_received)
        except (TypeError, RuntimeError):
            # Signal might not be connected or already disconnected
            pass

        # Close the serial port using the serial manager
        serial_manager.close()

        # Reset buffer and last valid data
        self.buffer = ""
        self.last_valid_data = None

        # Clear data buffers to free memory
        for i in range(8):
            buffer_name = f"databuffer{i}"
            if hasattr(self, buffer_name):
                getattr(self, buffer_name).clear()

        # Clear UI elements
        self.ui.Spikeling_Oscilloscope_widget.clear()
        if hasattr(self, 'current_plots') and self.current_plots:
            self.current_plots.clear()
