from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtCore import QIODevice, QTimer
import pyqtgraph as pg
import collections
import serial
import numpy as np
import pandas as pd
import Data_recording
import Settings
import time

downsampling = 6
sampleinterval = 0.1
timewindow = 250
timewindowdisplay = 125
penwidth = 1

def SpikelingPlot(self):

    SetSerial(self)
    SetInitParameters(self)
    SetPlotCurve(self)
    SetPlot(self)

    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(lambda: UpdatePlot(self))
    self.timer.start()


    def UpdatePlot(self):
        self.ui.Spikeling_Oscilloscope_widget.getViewBox().sigResized.connect(UpdateViews(self))
        self.Data = GetData(self)                   # Read Serial and return data array
        BuffData(self)                              # Append latest serial data into buffer deque
        SavePlotData(self)                          # Create data array to be exported in .csv
        if self.i_downsampling == 0:                # Plot Data once every "downsampling" time
            PlotCurve(self)
        self.i_downsampling += 1
        if self.i_downsampling == downsampling - 1:
            self.i_downsampling = 0

        if self.ui.StimCus_toggleButton.isChecked():
            self.StimCusValue = self.df_yStim[self.StimCounter]
            self.Trigger = self.df_yTrigger[self.StimCounter]
            if self.serial_port.is_open:
                self.serial_port.write(str('SC1 ' + str(self.StimCusValue) + '\n').encode('utf-8'))
                self.StimCounter += 1
            if self.StimCounter > len(self.df_Stim) - 1:
                self.StimCounter = 0
        else:
            if self.serial_port.is_open:
                self.serial_port.write(str('SC0' + '\n').encode('utf-8'))
            self.Trigger = 0


    # Read Serial and return data array (7)
    def GetData(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8').strip()
        self.data = self.rx_serial.split(',')
        return self.data


    # Append latest serial data point into buffer deque
    def BuffData(self):
        self.databuffer0.append(self.Data[0])
        self.databuffer1.append(self.Data[1])
        self.databuffer2.append(self.Data[2])
        self.databuffer3.append(self.Data[3])
        self.databuffer4.append(self.Data[4])
        self.databuffer5.append(self.Data[5])
        self.databuffer6.append(self.Data[6])
        self.databuffer7.append(self.Trigger)


    # If checked, plot latest buffer data points
    def PlotCurve(self):
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




def SavePlotData(self):                              # Save latest buffer data and export them as csv
    if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == False and self.recordflag == True:
        self.Dataset = np.empty([8, len(self.Dataset0)], dtype=float)
        for i in range(len(self.Dataset0)):
            self.Dataset[0][i] = self.Dataset0[i]
            self.Dataset[1][i] = self.Dataset1[i]
            self.Dataset[2][i] = self.Dataset2[i]
            self.Dataset[3][i] = self.Dataset3[i]
            self.Dataset[4][i] = self.Dataset4[i]
            self.Dataset[5][i] = self.Dataset5[i]
            self.Dataset[6][i] = self.Dataset6[i]
            self.Dataset[7][i] = self.Dataset7[i]

        dict = {'Spikeling Vm': self.Dataset[0], 'Stimulus': self.Dataset[1], 'Total Current Input': self.Dataset[2],
                'Synapse 1 Vm': self.Dataset[3], 'Synapse 1 Input': self.Dataset[4],
                'Synapse 2 Vm': self.Dataset[5], 'Synapse 2 Input': self.Dataset[6],
                'Trigger': self.Dataset[7]}
        df = pd.DataFrame(dict)
        self.RecordingFileName = str(self.ui.Spikeling_SelectedFolderLabel.text())
        df.to_csv(self.RecordingFileName + '.csv', index=False)
        self.recordflag = False

    if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == True:
        self.recordflag = True

        self.Dataset0.append(self.databuffer0[-1])
        self.Dataset1.append(self.databuffer1[-1])
        self.Dataset2.append(self.databuffer2[-1])
        self.Dataset3.append(self.databuffer3[-1])
        self.Dataset4.append(self.databuffer4[-1])
        self.Dataset5.append(self.databuffer5[-1])
        self.Dataset6.append(self.databuffer6[-1])
        self.Dataset7.append(self.databuffer7[-1])
        print(self.databuffer7[-1])




# __init__ functions

def SetInitParameters(self):
    self.i_downsampling = 0
    self.recordflag = False
    self.Trigger = 0
    self.ui.Spikeling_Oscilloscope_widget.clear()
    if self.ui.Spikeling_ConnectButton.isChecked() and self.serial_port.is_open:
        self.ui.Spikeling_ConnectButton.setText("Connected")
        self.ui.Spikeling_ConnectButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[3])) + ";\n"
                                                      "background-color: rgb" + str(tuple(Settings.DarkSolarized[11])) + ";\n"
                                                      "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                      "border-radius: 10px;"
                                                      )
    else:
        self.ui.Spikeling_ConnectButton.setText("Connect Spikeling Screen")
        self.ui.Spikeling_ConnectButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                      "background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                      "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                      "border-radius: 10px;"
                                                      )



def SetSerial(self):
    self.COM = self.ui.Spikeling_SelectPortComboBox.currentText()
    self.BaudRate = Settings.BaudRate
    self.serial_port = serial.Serial(port=self.COM, baudrate=self.BaudRate)


def SetPlotCurve(self):
    self._interval = sampleinterval
    self._bufsize = int(timewindow / sampleinterval)

    self.databuffer0 = collections.deque([0.0] * self._bufsize, self._bufsize)    # Set a double-ended queue 0.0 floats to self._bufsize entries, for a self._bufsize max length
    self.databuffer1 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer2 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer3 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer4 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer5 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer6 = collections.deque([0.0] * self._bufsize, self._bufsize)
    self.databuffer7 = collections.deque([0.0] * self._bufsize, self._bufsize)


    self.x = np.linspace(-timewindow, 0.0, self._bufsize)            # Create arrays of self._bufsize length
    self.y0 = np.zeros(self._bufsize, dtype=float)
    self.y1 = np.zeros(self._bufsize, dtype=float)
    self.y2 = np.zeros(self._bufsize, dtype=float)
    self.y3 = np.zeros(self._bufsize, dtype=float)
    self.y4 = np.zeros(self._bufsize, dtype=float)
    self.y5 = np.zeros(self._bufsize, dtype=float)
    self.y6 = np.zeros(self._bufsize, dtype=float)

    self.Dataset0 = Data_recording.DynamicArray()                                 # Create dynamic arrays for storing latest data point to be further exported as csv
    self.Dataset1 = Data_recording.DynamicArray()
    self.Dataset2 = Data_recording.DynamicArray()
    self.Dataset3 = Data_recording.DynamicArray()
    self.Dataset4 = Data_recording.DynamicArray()
    self.Dataset5 = Data_recording.DynamicArray()
    self.Dataset6 = Data_recording.DynamicArray()
    self.Dataset7 = Data_recording.DynamicArray()


def SetPlot(self):
    self.ui.Spikeling_Oscilloscope_widget.showGrid(x=True, y=True)
    self.ui.Spikeling_Oscilloscope_widget.setRange(xRange=[-timewindowdisplay, 0])
    self.ui.Spikeling_Oscilloscope_widget.setRange(yRange=[-90, 30])
    self.ui.Spikeling_Oscilloscope_widget.plotItem.setMouseEnabled(y=False)
    self.ui.Spikeling_Oscilloscope_widget.plotItem.vb.setLimits(xMin=-timewindow,xMax=0)
    self.ui.Spikeling_Oscilloscope_widget.setLabel('left', 'Membrane potential', 'mV')
    self.ui.Spikeling_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')
    self.ui.Spikeling_Oscilloscope_widget.setLabel('right', 'Current Input', 'a.u.')

    self.CurrentPlots = pg.ViewBox()
    self.ui.Spikeling_Oscilloscope_widget.scene().addItem(self.CurrentPlots)
    self.CurrentPlots.setXLink(self.ui.Spikeling_Oscilloscope_widget)
    self.CurrentPlots.setRange(yRange=[-100, 100])
    self.ui.Spikeling_Oscilloscope_widget.getAxis("right").linkToView(self.CurrentPlots)


    self.curve0 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y0, pen=pg.mkPen(Settings.DarkSolarized[3], width=penwidth))
    self.curve0.clear()
    self.curve3 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y3, pen=pg.mkPen(Settings.DarkSolarized[6], width=penwidth))
    self.curve3.clear()
    self.curve5 = self.ui.Spikeling_Oscilloscope_widget.plot(self.x, self.y5, pen=pg.mkPen(Settings.DarkSolarized[8], width=penwidth))
    self.curve5.clear()

    self.curve1 = pg.PlotCurveItem(self.x, self.y1, pen=pg.mkPen(Settings.DarkSolarized[5], width=penwidth))
    self.curve1.clear()
    self.curve2 = pg.PlotCurveItem(self.x, self.y2, pen=pg.mkPen(Settings.DarkSolarized[4], width=penwidth))
    self.curve2.clear()
    self.curve4 = pg.PlotCurveItem(self.x, self.y4, pen=pg.mkPen(Settings.DarkSolarized[7], width=penwidth))
    self.curve4.clear()
    self.curve6 = pg.PlotCurveItem(self.x, self.y6, pen=pg.mkPen(Settings.DarkSolarized[10], width=penwidth))
    self.curve6.clear()

    self.CurrentPlots.addItem(self.curve1)
    self.CurrentPlots.addItem(self.curve2)
    self.CurrentPlots.addItem(self.curve4)
    self.CurrentPlots.addItem(self.curve6)



def UpdateViews(self):
    self.CurrentPlots.setGeometry(self.ui.Spikeling_Oscilloscope_widget.getViewBox().sceneBoundingRect())
    self.CurrentPlots.linkedViewChanged(self.ui.Spikeling_Oscilloscope_widget.getViewBox(), self.CurrentPlots.XAxis)

