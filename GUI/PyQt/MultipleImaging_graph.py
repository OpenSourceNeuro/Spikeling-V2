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

import Page201




def MultipleImagingPlot(self):
    #Imaging parameters
    self.MultipleImaging_sampleinterval = 0.1
    self.MultipleImaging_timewindow = 250
    self.MultipleImaging_penwidth = 1
    self.MultipleFrameRate = self.ui.MultipleImaging_FrameRate_Slider.value()
    self.MultipleImagingDelta = 1 / self.MultipleFrameRate * 10000  # imaging resolution in ms
    self.MultiplePMT = self.ui.MultipleImaging_PMT_Slider.value()/100
    self.MultipleLaser = self.ui.MultipleImaging_Laser_Slider.value()/100

    # Calcium parameters
    self.MultipleCalciumDecay = self.ui.MultipleImaging_CalciumDecay_Slider.value()/10000#Indicator decay constant in ms
    self.MultipleSpikeOccurence = 0 #number of spike at t
    self.MultipleSpikeConcentrationRise = self.ui.MultipleImaging_CalciumJump_Slider.value()#calcicum concentration rise for each spike in micromolar
    self.MultipleCalciumBaseline = self.ui.MultipleImaging_CalciumBaseline_Slider.value()/100 #in micromolar
    self.MultipleNoiseScale = self.ui.MultipleImaging_CalciumNoise_Slider.value()/10# sigmac
    self.MultipleSpikeThreshold = -30.0
    self.Multipleimaging_downsampling = 5

    # Fluorescence parameters
    self.MultipleFluoScale = self.ui.MultipleImaging_FluoScale_Slider.value()/10
    self.MultipleFluoOffset = self.ui.MultipleImaging_FluoOffset_Slider.value()
    self.MultipleFluoNoiseScale = self.ui.MultipleImaging_FluoNoise_Slider.value()/10
    self.MultipleHillCoef = self.ui.MultipleImaging_Hill_Slider.value()/100
    self.MultiplePhotoShotNoise = self.ui.MultipleImaging_PhotoShotNoise_Slider.value() / 10000 / 100
    self.MultipleDissociationConstant = self.ui.MultipleImaging_kd_Slider.value()*10 #micromolar

    SetMultipleImagingInitParameters(self)
    SetMultipleImagingPlotCurve(self)
    SetMultipleImagingPlot(self)

    self.MultipleCalciumData1 = self.MultipleCalciumBaseline
    self.MultipleCalciumData2 = self.MultipleCalciumBaseline
    self.MultipleCalciumData3 = self.MultipleCalciumBaseline

    if self.ui.MultipleImaging_pushButton.isChecked():
        self.Multipleimagingtimer = QtCore.QTimer()
        self.Multipleimagingtimer.timeout.connect(lambda: UpdateMultipleImagingPlot(self))
        self.Multipleimagingtimer.start()
    else:
        self.Multipleimagingtimer.stop()
        self.MultipleCurrentImagingPlots.clear()
        self.MultipleCurrentImagingPlots.removeItem(self.Stimcurve)
        self.ui.MultipleImaging_Oscilloscope_widget.clear()



    def UpdateMultipleImagingPlot(self):
        self.ui.MultipleImaging_Oscilloscope_widget.getViewBox().sigResized.connect(UpdateMultipleImagingViews(self))
        self.MultipleImagingData = GetMultipleData(self)
        BuffMultipleImagingData(self)                              # Append latest data into buffer deque
        #SaveMultipleImagingPlotData(self)                          # Create data array to be exported in .csv
        if self.i_Multipleimaging_downsampling == 0:               # Plot Data once every "downsampling" time
            PlotMultipleImagingCurve(self)
        self.i_Multipleimaging_downsampling += 1
        if self.i_Multipleimaging_downsampling == self.Multipleimaging_downsampling - 1:
            self.i_Multipleimaging_downsampling = 0


    # Read Serial and return data
    def GetMultipleData(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8').strip()
        self.data = self.rx_serial.split(',')
        return self.data


    # Append latest serial data point into buffer deque
    def BuffMultipleImagingData(self):
        self.MultipleVmData1 = self.MultipleImagingData[0]
        self.MultipleVmData2 = self.MultipleImagingData[3]
        self.MultipleVmData3 = self.MultipleImagingData[5]
        self.MultipleStimData = self.MultipleImagingData[1]

        if float(self.MultipleVmdatabuffer1[-1]) >= self.MultipleSpikeThreshold and float(self.MultipleVmdatabuffer1[-2]) <= self.MultipleSpikeThreshold:
             self.MultipleSpikeOccurence1 = 1
        else:
             self.MultipleSpikeOccurence1 = 0

        if float(self.MultipleVmdatabuffer2[-1]) >= self.MultipleSpikeThreshold and float(self.MultipleVmdatabuffer2[-2]) <= self.MultipleSpikeThreshold:
             self.MultipleSpikeOccurence2 = 1
        else:
             self.MultipleSpikeOccurence2 = 0

        if float(self.MultipleVmdatabuffer3[-1]) >= self.MultipleSpikeThreshold and float(self.MultipleVmdatabuffer3[-2]) <= self.MultipleSpikeThreshold:
             self.MultipleSpikeOccurence3 = 1
        else:
             self.MultipleSpikeOccurence3 = 0

        self.MultipleCalciumGaussianNoise1 = np.random.normal(0,1)
        self.MultipleCalciumData1 = self.MultipleCalciumData1 - self.MultipleCalciumDecay*self.MultipleCalciumData1 + self.MultipleCalciumBaseline + self.MultipleSpikeConcentrationRise*self.MultipleSpikeOccurence1 + self.MultipleNoiseScale*np.sqrt(self.MultipleImagingDelta/10000)*self.MultipleCalciumGaussianNoise1

        self.MultipleCalciumGaussianNoise2 = np.random.normal(0,1)
        self.MultipleCalciumData2 = self.MultipleCalciumData2 - self.MultipleCalciumDecay*self.MultipleCalciumData2 + self.MultipleCalciumBaseline + self.MultipleSpikeConcentrationRise*self.MultipleSpikeOccurence2 + self.MultipleNoiseScale*np.sqrt(self.MultipleImagingDelta/10000)*self.MultipleCalciumGaussianNoise2

        self.MultipleCalciumGaussianNoise3 = np.random.normal(0,1)
        self.MultipleCalciumData3 = self.MultipleCalciumData3 - self.MultipleCalciumDecay*self.MultipleCalciumData3 + self.MultipleCalciumBaseline + self.MultipleSpikeConcentrationRise*self.MultipleSpikeOccurence3 + self.MultipleNoiseScale*np.sqrt(self.MultipleImagingDelta/10000)*self.MultipleCalciumGaussianNoise3


        if self.MultipleSaturationFlag == False:
            self.MultipleFluoGaussianNoise1 = np.random.normal(0, 1)
            self.MultipleFluoData1 = self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*self.MultipleCalciumData1 + self.MultipleFluoOffset + self.MultipleFluoNoiseScale*self.MultipleFluoGaussianNoise1

            self.MultipleFluoGaussianNoise2 = np.random.normal(0, 1)
            self.MultipleFluoData2 = self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*self.MultipleCalciumData2 + self.MultipleFluoOffset + self.MultipleFluoNoiseScale*self.MultipleFluoGaussianNoise2

            self.MultipleFluoGaussianNoise3 = np.random.normal(0, 1)
            self.MultipleFluoData3 = self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*self.MultipleCalciumData3 + self.MultipleFluoOffset + self.MultipleFluoNoiseScale*self.MultipleFluoGaussianNoise3


        if self.MultipleSaturationFlag == True:
            self.MultipleFluoNoiseScale = self.MultipleFluoNoiseScale/10000

            self.MultipleFluoGaussianNoise1 = np.random.normal(0, 1)
            self.MultipleSatNoise1 = np.sqrt(self.MultiplePhotoShotNoise * self.MultipleCalciumData1**self.MultipleHillCoef / (self.MultipleCalciumData1**self.MultipleHillCoef + self.MultipleDissociationConstant) + self.MultipleFluoNoiseScale)*self.MultipleFluoGaussianNoise1
            self.MultipleFluoData1 = self.MultipleDissociationConstant * (self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*(self.MultipleCalciumData1**self.MultipleHillCoef/(self.MultipleCalciumData1**self.MultipleHillCoef+self.MultipleDissociationConstant)) + self.MultipleSatNoise1) + self.MultipleFluoOffset

            self.MultipleFluoGaussianNoise2 = np.random.normal(0, 1)
            self.MultipleSatNoise2 = np.sqrt(self.MultiplePhotoShotNoise * self.MultipleCalciumData2**self.MultipleHillCoef / (self.MultipleCalciumData2**self.MultipleHillCoef + self.MultipleDissociationConstant) + self.MultipleFluoNoiseScale)*self.MultipleFluoGaussianNoise2
            self.MultipleFluoData2 = self.MultipleDissociationConstant * (self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*(self.MultipleCalciumData2**self.MultipleHillCoef/(self.MultipleCalciumData2**self.MultipleHillCoef+self.MultipleDissociationConstant)) + self.MultipleSatNoise2) + self.MultipleFluoOffset

            self.MultipleFluoGaussianNoise3 = np.random.normal(0, 1)
            self.MultipleSatNoise3 = np.sqrt(self.MultiplePhotoShotNoise * self.MultipleCalciumData3**self.MultipleHillCoef / (self.MultipleCalciumData3**self.MultipleHillCoef + self.MultipleDissociationConstant) + self.MultipleFluoNoiseScale)*self.MultipleFluoGaussianNoise3
            self.MultipleFluoData3 = self.MultipleDissociationConstant * (self.MultipleLaser*self.MultiplePMT*self.MultipleFluoScale*(self.MultipleCalciumData3**self.MultipleHillCoef/(self.MultipleCalciumData3**self.MultipleHillCoef+self.MultipleDissociationConstant)) + self.MultipleSatNoise3) + self.MultipleFluoOffset

        self.MultipleCalciumdatabuffer1.append(self.MultipleCalciumData1)
        self.MultipleCalciumdatabuffer2.append(self.MultipleCalciumData2)
        self.MultipleCalciumdatabuffer3.append(self.MultipleCalciumData3)
        self.MultipleFluodatabuffer1.append(self.MultipleFluoData1)
        self.MultipleFluodatabuffer2.append(self.MultipleFluoData2)
        self.MultipleFluodatabuffer3.append(self.MultipleFluoData3)
        self.MultipleStimdatabuffer.append(self.MultipleStimData)
        self.MultipleVmdatabuffer1.append(self.MultipleVmData1)
        self.MultipleVmdatabuffer2.append(self.MultipleVmData2)
        self.MultipleVmdatabuffer3.append(self.MultipleVmData3)

    # If checked, plot latest buffer data points
    def PlotMultipleImagingCurve(self):
        if self.ui.MultipleImaging_Calcium1_Checkbox.isChecked():
            self.yMultipleCalcium1[:] = self.MultipleCalciumdatabuffer1
            self.MultipleCalciumcurve1.setData(self.MultipleImagingx, self.yMultipleCalcium1)
        else:
            self.MultipleCalciumcurve1.clear()

        if self.ui.MultipleImaging_Calcium2_Checkbox.isChecked():
            self.yMultipleCalcium2[:] = self.MultipleCalciumdatabuffer2
            self.MultipleCalciumcurve2.setData(self.MultipleImagingx, self.yMultipleCalcium2)
        else:
            self.MultipleCalciumcurve2.clear()

        if self.ui.MultipleImaging_Calcium3_Checkbox.isChecked():
            self.yMultipleCalcium3[:] = self.MultipleCalciumdatabuffer3
            self.MultipleCalciumcurve3.setData(self.MultipleImagingx, self.yMultipleCalcium3)
        else:
            self.MultipleCalciumcurve3.clear()


        if self.ui.MultipleImaging_Fluorescence1_Checkbox.isChecked():
            self.yMultipleFluo1[:] = self.MultipleFluodatabuffer1
            self.MultipleFluocurve1.setData(self.MultipleImagingx, self.yMultipleFluo1)
        else:
            self.MultipleFluocurve1.clear()

        if self.ui.MultipleImaging_Fluorescence2_Checkbox.isChecked():
            self.yMultipleFluo2[:] = self.MultipleFluodatabuffer2
            self.MultipleFluocurve2.setData(self.MultipleImagingx, self.yMultipleFluo2)
        else:
            self.MultipleFluocurve2.clear()

        if self.ui.MultipleImaging_Fluorescence3_Checkbox.isChecked():
            self.yMultipleFluo3[:] = self.MultipleFluodatabuffer3
            self.MultipleFluocurve3.setData(self.MultipleImagingx, self.yMultipleFluo3)
        else:
            self.MultipleFluocurve3.clear()


        if self.ui.MultipleImaging_Stimulus_Checkbox.isChecked():
            self.yMultipleStim[:] = self.MultipleStimdatabuffer
            self.MultipleStimcurve.setData(self.MultipleImagingx, self.yMultipleStim)
        else:
            self.MultipleStimcurve.clear()


        if self.ui.MultipleImaging_Vm1_Checkbox.isChecked():
            self.yMultipleVm1[:] = self.MultipleVmdatabuffer1
            self.MultipleVmcurve1.setData(self.MultipleImagingx, self.yMultipleVm1)
        else:
            self.MultipleVmcurve1.clear()

        if self.ui.MultipleImaging_Vm2_Checkbox.isChecked():
            self.yMultipleVm2[:] = self.MultipleVmdatabuffer2
            self.MultipleVmcurve2.setData(self.MultipleImagingx, self.yMultipleVm2)
        else:
            self.MultipleVmcurve2.clear()

        if self.ui.MultipleImaging_Vm3_Checkbox.isChecked():
            self.yMultipleVm3[:] = self.MultipleVmdatabuffer3
            self.MultipleVmcurve3.setData(self.MultipleImagingx, self.yMultipleVm3)
        else:
            self.MultipleVmcurve3.clear()



# def SaveImaginPlotData(self):                              # Save latest buffer data and export them as csv
#     if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == False and self.recordflag == True:
#         self.Dataset = np.empty([7, len(self.Dataset0)], dtype=float)
#         for i in range(len(self.Dataset0)):
#             self.Dataset[0][i] = self.Dataset0[i]
#             self.Dataset[1][i] = self.Dataset1[i]
#             self.Dataset[2][i] = self.Dataset2[i]
#             self.Dataset[3][i] = self.Dataset3[i]
#             self.Dataset[4][i] = self.Dataset4[i]
#             self.Dataset[5][i] = self.Dataset5[i]
#             self.Dataset[6][i] = self.Dataset6[i]
#
#         dict = {'Spikeling Vm': self.Dataset[0], 'Stimulus': self.Dataset[1], 'Total Current Input': self.Dataset[2],
#                 'Synapse 1 Vm': self.Dataset[3], 'Synapse 1 Input': self.Dataset[4],
#                 'Synapse 2 Vm': self.Dataset[5], 'Synapse 2 Input': self.Dataset[6]}
#         df = pd.DataFrame(dict)
#         self.RecordingFileName = str(self.ui.Spikeling_SelectedFolderLabel.text())
#         df.to_csv(self.RecordingFileName + '.csv', index=False)
#         self.recordflag = False
#
#     if self.ui.Spikeling_DataRecording_Record_pushButton.isChecked() == True:
#         self.recordflag = True
#
#         self.Dataset0.append(self.databuffer0[-1])
#         self.Dataset1.append(self.databuffer1[-1])
#         self.Dataset2.append(self.databuffer2[-1])
#         self.Dataset3.append(self.databuffer3[-1])
#         self.Dataset4.append(self.databuffer4[-1])
#         self.Dataset5.append(self.databuffer5[-1])
#         self.Dataset6.append(self.databuffer6[-1])


def SetMultipleImagingInitParameters(self):
    self.i_Multipleimaging_downsampling = 0
    self.Multiplerecordflag = False
    self.MultipleSaturationFlag = False
    self.ui.MultipleImaging_Oscilloscope_widget.clear()
    if self.ui.MultipleImaging_pushButton.isChecked():
        self.ui.MultipleImaging_pushButton.setText("Connected")
        self.ui.MultipleImaging_pushButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[3])) + ";\n"
                                                         "background-color: rgb" + str(tuple(Settings.DarkSolarized[11])) + ";\n"
                                                         "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                         "border-radius: 10px;"
                                                         )
    else:
        self.ui.MultipleImaging_pushButton.setText("Connect MultipleImaging screen to Spikeling screen")
        self.ui.MultipleImaging_pushButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                         "background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                         "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                         "border-radius: 10px;"
                                                        )

def SetMultipleImagingPlotCurve(self):
    self._MultipleImaging_bufsize = int(self.MultipleImaging_timewindow / self.MultipleImaging_sampleinterval)

    self.MultipleCalciumdatabuffer1 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleCalciumdatabuffer2 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleCalciumdatabuffer3 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleFluodatabuffer1 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleFluodatabuffer2 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleFluodatabuffer3 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleStimdatabuffer = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer1 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer2 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer3 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)

    self.MultipleImagingx = np.linspace(-self.MultipleImaging_timewindow, 0.0, self._MultipleImaging_bufsize)            # Create arrays of self._Imaging_bufsize length
    self.yMultipleCalcium1 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleCalcium2 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleCalcium3 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo1 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo2 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo3 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleStim = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm1 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm2 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm3 = np.zeros(self._MultipleImaging_bufsize, dtype=float)

    self.MultipleCalciumDataset1 = Data_recording.DynamicArray()
    self.MultipleCalciumDataset2 = Data_recording.DynamicArray()
    self.MultipleCalciumDataset3 = Data_recording.DynamicArray()
    self.MultipleFluoDataset1 = Data_recording.DynamicArray()
    self.MultipleFluoDataset2 = Data_recording.DynamicArray()
    self.MultipleFluoDataset3 = Data_recording.DynamicArray()
    self.MultipleStimDataset = Data_recording.DynamicArray()
    self.MultipleVmDataset1 = Data_recording.DynamicArray()
    self.MultipleVmDataset2 = Data_recording.DynamicArray()
    self.MultipleVmDataset3 = Data_recording.DynamicArray()


def SetMultipleImagingPlot(self):
    self.ui.MultipleImaging_Oscilloscope_widget.showGrid(x=True, y=True)
    self.ui.MultipleImaging_Oscilloscope_widget.setRange(xRange=[-self.MultipleImaging_timewindow, 0])
    self.ui.MultipleImaging_Oscilloscope_widget.setLabel('left', 'Fluorescence  /  [Ca2+]    ', 'a.u.  /  µM')
    self.ui.MultipleImaging_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')
    self.ui.MultipleImaging_Oscilloscope_widget.setLabel('right', 'Stimulus Intensity / Vm', 'a.u. / mV')

    self.CurrentMultipleImagingPlots = pg.ViewBox()
    self.ui.MultipleImaging_Oscilloscope_widget.scene().addItem(self.CurrentMultipleImagingPlots)
    self.CurrentMultipleImagingPlots.setXLink(self.ui.MultipleImaging_Oscilloscope_widget)
    self.CurrentMultipleImagingPlots.setRange(yRange=[-100, 100])
    self.ui.MultipleImaging_Oscilloscope_widget.getAxis("right").linkToView(self.CurrentMultipleImagingPlots)

    self.MultipleCalciumcurve1 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleCalcium1, pen=pg.mkPen(Settings.DarkSolarized[10], width=self.MultipleImaging_penwidth))
    self.MultipleCalciumcurve1.clear()
    self.MultipleCalciumcurve2 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleCalcium2, pen=pg.mkPen(Settings.DarkSolarized[9], width=self.MultipleImaging_penwidth))
    self.MultipleCalciumcurve2.clear()
    self.MultipleCalciumcurve3 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleCalcium3, pen=pg.mkPen(Settings.DarkSolarized[7], width=self.MultipleImaging_penwidth))
    self.MultipleCalciumcurve1.clear()
    self.MultipleFluocurve1 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleFluo1, pen=pg.mkPen(Settings.DarkSolarized[4], width=self.MultipleImaging_penwidth))
    self.MultipleFluocurve1.clear()
    self.MultipleFluocurve2 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleFluo2, pen=pg.mkPen([0,255,133], width=self.MultipleImaging_penwidth))
    self.MultipleFluocurve2.clear()
    self.MultipleFluocurve3 = self.ui.MultipleImaging_Oscilloscope_widget.plot(self.MultipleImagingx, self.yMultipleFluo3, pen=pg.mkPen([133,255,0],width=self.MultipleImaging_penwidth))
    self.MultipleFluocurve3.clear()
    self.MultipleStimcurve = pg.PlotCurveItem(self.MultipleImagingx, self.yMultipleStim, pen=pg.mkPen(Settings.DarkSolarized[5], width=self.MultipleImaging_penwidth))
    self.MultipleStimcurve.clear()
    self.MultipleVmcurve1 = pg.PlotCurveItem(self.MultipleImagingx, self.yMultipleVm1, pen=pg.mkPen(Settings.DarkSolarized[3], width=self.MultipleImaging_penwidth))
    self.MultipleVmcurve1.clear()
    self.MultipleVmcurve2 = pg.PlotCurveItem(self.MultipleImagingx, self.yMultipleVm2, pen=pg.mkPen(Settings.DarkSolarized[6], width=self.MultipleImaging_penwidth))
    self.MultipleVmcurve2.clear()
    self.MultipleVmcurve3 = pg.PlotCurveItem(self.MultipleImagingx, self.yMultipleVm3, pen=pg.mkPen(Settings.DarkSolarized[8], width=self.MultipleImaging_penwidth))
    self.MultipleVmcurve3.clear()

    self.CurrentMultipleImagingPlots.addItem(self.MultipleStimcurve)
    self.CurrentMultipleImagingPlots.addItem(self.MultipleVmcurve1)
    self.CurrentMultipleImagingPlots.addItem(self.MultipleVmcurve2)
    self.CurrentMultipleImagingPlots.addItem(self.MultipleVmcurve3)


def UpdateMultipleImagingViews(self):
    self.CurrentMultipleImagingPlots.setGeometry(self.ui.MultipleImaging_Oscilloscope_widget.getViewBox().sceneBoundingRect())
    self.CurrentMultipleImagingPlots.linkedViewChanged(self.ui.MultipleImaging_Oscilloscope_widget.getViewBox(), self.CurrentMultipleImagingPlots.XAxis)







