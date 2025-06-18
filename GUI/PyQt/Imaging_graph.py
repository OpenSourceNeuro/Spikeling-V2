
########################################################################
#                          Libraries import                            #

from PySide6 import QtCore
from PySide6.QtCore import  QTimer
import pyqtgraph as pg

import numpy as np
import pandas as pd
import Settings
import time






def ImagingPlot(self):
    #Imaging parameters
    self.Imaging_sampleinterval = 0.1
    self.Imaging_timewindow = 250
    self.Imaging_penwidth = 1
    self.FrameRate = self.ui.Imaging_FrameRate_Slider.value()
    self.ImagingDelta = 1 / self.FrameRate * 10000  # imaging resolution in ms
    self.PMT = self.ui.Imaging_PMT_Slider.value()/100
    self.Laser = self.ui.Imaging_Laser_Slider.value()/100

    # Calcium parameters
    self.CalciumDecay = self.ui.Imaging_CalciumDecay_Slider.value()/10000#Indicator decay constant in ms
    self.SpikeOccurence = 0 #number of spike at t
    self.SpikeConcentrationRise = self.ui.Imaging_CalciumJump_Slider.value()#calcicum concentration rise for each spike in micromolar
    self.CalciumBaseline = self.ui.Imaging_CalciumBaseline_Slider.value()/100 #in micromolar
    self.NoiseScale = self.ui.Imaging_CalciumNoise_Slider.value()/10# sigmac
    self.SpikeThreshold = -30.0
    self.imaging_downsampling = 5

    # Fluorescence parameters
    self.FluoScale = self.ui.Imaging_FluoScale_Slider.value()/10
    self.FluoOffset = self.ui.Imaging_FluoOffset_Slider.value()
    self.FluoNoiseScale = self.ui.Imaging_FluoNoise_Slider.value()/10
    self.HillCoef = self.ui.Imaging_Hill_Slider.value()/100
    self.PhotoShotNoise = self.ui.Imaging_PhotoShotNoise_Slider.value() / 10000 / 100
    self.DissociationConstant = self.ui.Imaging_kd_Slider.value()*10 #micromolar

    SetImagingInitParameters(self)
    SetImagingPlotCurve(self)
    SetImagingPlot(self)

    self.CalciumData = self.CalciumBaseline

    if self.ui.Imaging_pushButton.isChecked():
        self.ImagingConnectionFlag = True
        self.imagingtimer = QtCore.QTimer()
        self.imagingtimer.timeout.connect(lambda: UpdateImagingPlot(self))
        self.imagingtimer.start()
    else:
        self.imagingtimer.stop()
        self.CurrentImagingPlots.clear()
        self.CurrentImagingPlots.removeItem(self.Stimcurve)
        self.ui.Imaging_Oscilloscope_widget.clear()



    def UpdateImagingPlot(self):
        self.ui.Imaging_Oscilloscope_widget.getViewBox().sigResized.connect(UpdateImagingViews(self))
        self.ImagingData = GetData(self)
        BuffImagingData(self)                              # Append latest data into buffer deque
        #SaveImagingPlotData(self)                          # Create data array to be exported in .csv
        if self.i_imaging_downsampling == 0:               # Plot Data once every "downsampling" time
            PlotImagingCurve(self)
        self.i_imaging_downsampling += 1
        if self.i_imaging_downsampling == self.imaging_downsampling - 1:
            self.i_imaging_downsampling = 0


    # Read Serial and return data
    def GetData(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8').strip()
        self.data = self.rx_serial.split(',')
        return self.data


    # Append latest serial data point into buffer deque
    def BuffImagingData(self):
        self.VmData = self.ImagingData[0]
        self.StimData = self.ImagingData[1]
        if float(self.Vmdatabuffer[-1]) >= self.SpikeThreshold and float(self.Vmdatabuffer[-2]) <= self.SpikeThreshold:
             self.SpikeOccurence = 1
        else:
             self.SpikeOccurence = 0

        self.CalciumGaussianNoise = np.random.normal(0,1)
        self.CalciumData = self.CalciumData - self.CalciumDecay*self.CalciumData + self.CalciumBaseline + self.SpikeConcentrationRise*self.SpikeOccurence + self.NoiseScale*np.sqrt(self.ImagingDelta/10000)*self.CalciumGaussianNoise

        if self.SaturationFlag == False:
            self.FluoGaussianNoise = np.random.normal(0, 1)
            self.FluoData = self.Laser*self.PMT*self.FluoScale*self.CalciumData + self.FluoOffset + self.FluoNoiseScale*self.FluoGaussianNoise

        if self.SaturationFlag == True:
            self.FluoGaussianNoise = np.random.normal(0, 1)
            self.FluoNoiseScale = self.FluoNoiseScale/10000
            self.SatNoise = np.sqrt(self.PhotoShotNoise * self.CalciumData**self.HillCoef / (self.CalciumData**self.HillCoef + self.DissociationConstant) + self.FluoNoiseScale)*self.FluoGaussianNoise
            self.FluoData = self.DissociationConstant * (self.Laser*self.PMT*self.FluoScale*(self.CalciumData**self.HillCoef/(self.CalciumData**self.HillCoef+self.DissociationConstant))  + self.SatNoise) + self.FluoOffset

        self.Calciumdatabuffer.append(self.CalciumData)
        self.Fluodatabuffer.append(self.FluoData)
        self.Stimdatabuffer.append(self.StimData)
        self.Vmdatabuffer.append(self.VmData)

    # If checked, plot latest buffer data points
    def PlotImagingCurve(self):
        if self.ui.Imaging_Calcium_Checkbox.isChecked():
            self.yCalcium[:] = self.Calciumdatabuffer
            self.Calciumcurve.setData(self.Imagingx, self.yCalcium)
        else:
            self.Calciumcurve.clear()

        if self.ui.Imaging_Fluorescence_Checkbox.isChecked():
            self.yFluo[:] = self.Fluodatabuffer
            self.Fluocurve.setData(self.Imagingx, self.yFluo)
        else:
            self.Fluocurve.clear()

        if self.ui.Imaging_Stimulus_Checkbox.isChecked():
            self.yStim[:] = self.Stimdatabuffer
            self.Stimcurve.setData(self.Imagingx, self.yStim)
        else:
            self.Stimcurve.clear()

        if self.ui.Imaging_Vm_Checkbox.isChecked():
            self.yVm[:] = self.Vmdatabuffer
            self.Vmcurve.setData(self.Imagingx, self.yVm)
        else:
            self.Vmcurve.clear()



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


def SetImagingInitParameters(self):
    self.i_imaging_downsampling = 0
    self.recordflag = False
    self.SaturationFlag = False
    self.ui.Imaging_Oscilloscope_widget.clear()
    if self.ui.Imaging_pushButton.isChecked():
        self.ui.Imaging_pushButton.setText("Connected")
        self.ui.Imaging_pushButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[3])) + ";\n"
                                                "background-color: rgb" + str(tuple(Settings.DarkSolarized[11])) + ";\n"
                                                "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                "border-radius: 10px;"
                                                )
    else:
        self.ui.Imaging_pushButton.setText("Connect Imaging screen to Spikeling screen")
        self.ui.Imaging_pushButton.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                "background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                "border: 1px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                "border-radius: 10px;"
                                                )

def SetImagingPlotCurve(self):
    self._Imaging_bufsize = int(self.Imaging_timewindow / self.Imaging_sampleinterval)

    self.Calciumdatabuffer = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)
    self.Fluodatabuffer = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)
    self.Stimdatabuffer = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)
    self.Vmdatabuffer = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)

    self.Imagingx = np.linspace(-self.Imaging_timewindow, 0.0, self._Imaging_bufsize)            # Create arrays of self._Imaging_bufsize length
    self.yCalcium = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yFluo = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yStim = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yVm = np.zeros(self._Imaging_bufsize, dtype=float)

    self.CalciumDataset = Data_recording.DynamicArray()
    self.FluoDataset = Data_recording.DynamicArray()
    self.StimDataset = Data_recording.DynamicArray()
    self.VmDataset = Data_recording.DynamicArray()


def SetImagingPlot(self):
    self.ui.Imaging_Oscilloscope_widget.showGrid(x=True, y=True)
    self.ui.Imaging_Oscilloscope_widget.setRange(xRange=[-self.Imaging_timewindow, 0])
    self.ui.Imaging_Oscilloscope_widget.setLabel('left', 'Fluorescence  /  [Ca2+]    ', 'a.u.  /  µM')
    self.ui.Imaging_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')
    self.ui.Imaging_Oscilloscope_widget.setLabel('right', 'Stimulus Intensity / Vm', 'a.u. / mV')

    self.CurrentImagingPlots = pg.ViewBox()
    self.ui.Imaging_Oscilloscope_widget.scene().addItem(self.CurrentImagingPlots)
    self.CurrentImagingPlots.setXLink(self.ui.Imaging_Oscilloscope_widget)
    self.CurrentImagingPlots.setRange(yRange=[-100, 100])
    self.ui.Imaging_Oscilloscope_widget.getAxis("right").linkToView(self.CurrentImagingPlots)

    self.Calciumcurve = self.ui.Imaging_Oscilloscope_widget.plot(self.Imagingx, self.yCalcium, pen=pg.mkPen(Settings.DarkSolarized[10], width=self.Imaging_penwidth))
    self.Calciumcurve.clear()
    self.Fluocurve = self.ui.Imaging_Oscilloscope_widget.plot(self.Imagingx, self.yFluo, pen=pg.mkPen(Settings.DarkSolarized[4], width=self.Imaging_penwidth))
    self.Fluocurve.clear()
    self.Stimcurve = pg.PlotCurveItem(self.Imagingx, self.yStim, pen=pg.mkPen(Settings.DarkSolarized[5], width=self.Imaging_penwidth))
    self.Stimcurve.clear()
    self.Vmcurve = pg.PlotCurveItem(self.Imagingx, self.yVm, pen=pg.mkPen(Settings.DarkSolarized[3], width=self.Imaging_penwidth))
    self.Vmcurve.clear()

    self.CurrentImagingPlots.addItem(self.Stimcurve)
    self.CurrentImagingPlots.addItem(self.Vmcurve)


def UpdateImagingViews(self):
    self.CurrentImagingPlots.setGeometry(self.ui.Imaging_Oscilloscope_widget.getViewBox().sceneBoundingRect())
    self.CurrentImagingPlots.linkedViewChanged(self.ui.Imaging_Oscilloscope_widget.getViewBox(), self.CurrentImagingPlots.XAxis)







