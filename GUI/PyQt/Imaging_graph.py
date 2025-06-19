
########################################################################
#                          Libraries import                            #

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPen
import pyqtgraph as pg

import numpy as np
import pandas as pd
import collections

import Settings



def ImagingPlot(self):
    #Imaging parameters
    self.Imaging_sampleinterval = 0.1
    self.Imaging_timewindow = 250
    self.Imaging_penwidth = 1
    self.ImagingFrameRate = self.ui.Imaging_FrameRate_Slider.value()
    self.ImagingDelta = 1 / self.ImagingFrameRate * 10000  # imaging resolution in ms
    self.ImagingPMT = self.ui.Imaging_PMT_Slider.value()/100
    self.ImagingLaser = self.ui.Imaging_Laser_Slider.value()/100

    # Calcium parameters
    self.ImagingCalciumDecay = self.ui.Imaging_CalciumDecay_Slider.value()/10000#Indicator decay constant in ms
    self.ImagingSpikeOccurence = 0 #number of spike at t
    self.ImagingSpikeConcentrationRise = self.ui.Imaging_CalciumJump_Slider.value()#calcicum concentration rise for each spike in micromolar
    self.ImagingCalciumBaseline = self.ui.Imaging_CalciumBaseline_Slider.value()/100 #in micromolar
    self.ImagingNoiseScale = self.ui.Imaging_CalciumNoise_Slider.value()/10# sigmac
    self.ImagingSpikeThreshold = -30.0
    self.Imaging_downsampling = 5

    # Fluorescence parameters
    self.ImagingFluoScale = self.ui.Imaging_FluoScale_Slider.value()/10
    self.ImagingFluoOffset = self.ui.Imaging_FluoOffset_Slider.value()
    self.ImagingFluoNoiseScale = self.ui.Imaging_FluoNoise_Slider.value()/10
    self.ImagingHillCoef = self.ui.Imaging_Hill_Slider.value()/100
    self.ImagingPhotoShotNoise = self.ui.Imaging_PhotoShotNoise_Slider.value() / 10000 / 100
    self.ImagingDissociationConstant = self.ui.Imaging_kd_Slider.value()*10 #micromolar

    SetImagingInitParameters(self)
    SetImagingPlotCurve(self)
    SetImagingPlot(self)

    self.ImagingCalciumData = self.ImagingCalciumBaseline


    if self.ui.Imaging_pushButton.isChecked():
        self.ImagingConnectionFlag = True
        self.Imagingtimer = QTimer()
        self.Imagingtimer.timeout.connect(lambda: UpdateImagingPlot(self))
        self.Imagingtimer.start()
    else:
        self.Imagingtimer.stop()
        self.CurrentImagingPlots.clear()
        self.CurrentImagingPlots.removeItem(self.ImagingStimcurve)
        self.ui.Imaging_Oscilloscope_widget.clear()



    def UpdateImagingPlot(self):
        self.ui.Imaging_Oscilloscope_widget.getViewBox().sigResized.connect(UpdateImagingViews(self))
        self.ImagingData = GetImagingData(self)
        BuffImagingData(self)                              # Append latest data into buffer deque
        SaveImagingPlotData(self)                          # Create data array to be exported in .csv
        if self.i_Imaging_downsampling == 0:               # Plot Data once every "downsampling" time
            PlotImagingCurve(self)
        self.i_Imaging_downsampling += 1
        if self.i_Imaging_downsampling == self.Imaging_downsampling - 1:
            self.i_Imaging_downsampling = 0


    # Read Serial and return data
    def GetImagingData(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8').strip()
        self.data = self.rx_serial.split(',')
        return self.data


    # Append latest serial data point into buffer deque
    def BuffImagingData(self):
        self.ImagingVmData = self.ImagingData[0]
        self.ImagingTriggerData = self.ImagingData[7]
        self.ImagingStimData = self.ImagingData[1]

        if float(self.ImagingVmdatabuffer[-1]) >= self.ImagingSpikeThreshold and float(self.ImagingVmdatabuffer[-2]) <= self.ImagingSpikeThreshold:
             self.ImagingSpikeOccurence = 1
        else:
             self.ImagingSpikeOccurence = 0

        self.ImagingCalciumGaussianNoise = np.random.normal(0,1)
        self.ImagingCalciumData = self.ImagingCalciumData - self.ImagingCalciumDecay*self.ImagingCalciumData + self.ImagingCalciumBaseline + self.ImagingSpikeConcentrationRise*self.ImagingSpikeOccurence + self.ImagingNoiseScale*np.sqrt(self.ImagingDelta/10000)*self.ImagingCalciumGaussianNoise


        if self.ImagingSaturationFlag == False:
            self.ImagingFluoGaussianNoise = np.random.normal(0, 1)
            self.ImagingFluoData = self.ImagingLaser*self.ImagingPMT*self.ImagingFluoScale*self.ImagingCalciumData + self.ImagingFluoOffset + self.ImagingFluoNoiseScale*self.ImagingFluoGaussianNoise


        if self.ImagingSaturationFlag == True:
            self.ImagingFluoNoiseScale = self.ImagingFluoNoiseScale/10000

            self.ImagingFluoGaussianNoise = np.random.normal(0, 1)
            self.ImagingSatNoise = np.sqrt(self.ImagingPhotoShotNoise * self.ImagingCalciumData**self.ImagingHillCoef / (self.ImagingCalciumData**self.ImagingHillCoef + self.ImagingDissociationConstant) + self.ImagingFluoNoiseScale)*self.ImagingFluoGaussianNoise1
            self.ImagingFluoData = self.ImagingDissociationConstant * (self.ImagingLaser*self.ImagingPMT*self.ImagingFluoScale*(self.ImagingCalciumData**self.ImagingHillCoef/(self.ImagingCalciumData**self.ImagingHillCoef+self.ImagingDissociationConstant)) + self.ImagingSatNoise) + self.ImagingFluoOffset


        self.ImagingStimdatabuffer.append(self.ImagingStimData)
        self.ImagingTriggerdatabuffer.append(self.ImagingTriggerData)

        self.ImagingFluodatabuffer.append(self.ImagingFluoData)
        self.ImagingCalciumdatabuffer.append(self.ImagingCalciumData)
        self.ImagingVmdatabuffer.append(self.ImagingVmData)


    # If checked, plot latest buffer data points
    def PlotImagingCurve(self):
        if self.ui.Imaging_Calcium_Checkbox.isChecked():
            self.yCalcium[:] = self.Calciumdatabuffer
            self.Calciumcurve.setData(self.Imagingx, self.yImagingCalcium)
        else:
            self.ImagingCalciumcurve.clear()

        if self.ui.Imaging_Fluorescence_Checkbox.isChecked():
            self.yImagingFluo[:] = self.ImagingFluodatabuffer
            self.ImagingFluocurve.setData(self.Imagingx, self.yImagingFluo)
        else:
            self.ImagingFluocurve.clear()


        if self.ui.Imaging_Stimulus_Checkbox.isChecked():
            self.yImagingStim[:] = self.ImagingStimdatabuffer
            self.ImagingStimcurve.setData(self.Imagingx, self.yImagingStim)
        else:
            self.ImagingStimcurve.clear()


        if self.ui.Imaging_Vm_Checkbox.isChecked():
            self.yImagingVm[:] = self.ImagingVmdatabuffer
            self.ImagingVmcurve.setData(self.Imagingx, self.yImagingVm)
        else:
            self.ImagingVmcurve.clear()



def SaveImagingPlotData(self):                              # Save latest buffer data and export them as csv
    if self.ui.Imaging_DataRecording_Record_pushButton.isChecked() == False and self.Imagingrecordflag == True:
        ImagingDataset = np.empty([6, len(self.DataSet[1])], dtype=float)

        for i in range(len(self.DataSet[1])):
            ImagingDataset[0][i] = i * 0.1
            ImagingDataset[1][i] = self.DataSet[1][i]
            ImagingDataset[2][i] = self.DataSet[2][i]
            ImagingDataset[3][i] = self.DataSet[3][i]
            ImagingDataset[4][i] = self.DataSet[4][i]
            ImagingDataset[5][i] = self.DataSet[5][i]


        dict = {'Time (ms)': ImagingDataset[0], 'Stimulus (%)': ImagingDataset[1], 'Trigger': ImagingDataset[2],
                'Spikeling Fluorescence': ImagingDataset[3], 'Spikeling Calcium': ImagingDataset[4], 'Spikeling Vm (mV)': ImagingDataset[5]
                }
        df = pd.DataFrame(dict)
        self.RecordingFileName = str(self.ui.Imaging_SelectedFolderLabel.text())
        df.to_csv(self.RecordingFileName + '.csv', index=False)
        self.Imagingrecordflag = False
        self.DataSet[0].clear()
        self.DataSet[1].clear()
        self.DataSet[2].clear()
        self.DataSet[3].clear()
        self.DataSet[4].clear()
        self.DataSet[5].clear()


    if self.ui.Imaging_DataRecording_Record_pushButton.isChecked() == True:
        self.Imagingrecordflag = True

        self.DataSet[1].append(self.ImagingStimdatabuffer[-1])
        self.DataSet[2].append(self.ImagingTriggerdatabuffer[-1])
        self.DataSet[3].append(self.ImagingFluodatabuffer[-1])
        self.DataSet[4].append(self.ImagingCalciumdatabuffer[-1])
        self.DataSet[5].append(self.ImagingVmdatabuffer[-1])



def SetImagingInitParameters(self):
    self.i_Imaging_downsampling = 0
    self.Imagingrecordflag = False
    self.ImagingSaturationFlag = False
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

    self.ImagingStimdatabuffer     = collections.deque([0.0] * self._Imaging_bufsize,self._Imaging_bufsize)
    self.ImagingTriggerdatabuffer  = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)

    self.ImagingFluodatabuffer     = collections.deque([0.0] * self._Imaging_bufsize,self._Imaging_bufsize)
    self.ImagingCalciumdatabuffer  = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)
    self.ImagingVmdatabuffer       = collections.deque([0.0] * self._Imaging_bufsize, self._Imaging_bufsize)


    self.Imagingx  = np.linspace(-self.Imaging_timewindow, 0.0, self._Imaging_bufsize)            # Create arrays of self._Imaging_bufsize length
    self.yImagingCalcium = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yImagingFluo    = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yImagingStim     = np.zeros(self._Imaging_bufsize, dtype=float)
    self.yImagingVm      = np.zeros(self._Imaging_bufsize, dtype=float)

    self.DataSet = []
    for _ in range(6):
        self.DataSet.append([])

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

    self.ImagingCalciumcurve = self.ui.Imaging_Oscilloscope_widget.plot(self.Imagingx, self.yImagingCalcium, pen=pg.mkPen(Settings.DarkSolarized[10], width=self.Imaging_penwidth))
    self.ImagingCalciumcurve.clear()
    self.ImagingFluocurve = self.ui.Imaging_Oscilloscope_widget.plot(self.Imagingx, self.yImagingFluo, pen=pg.mkPen(Settings.DarkSolarized[4], width=self.Imaging_penwidth))
    self.ImagingFluocurve.clear()
    self.ImagingStimcurve = pg.PlotCurveItem(self.Imagingx, self.yImagingStim, pen=pg.mkPen(Settings.DarkSolarized[5], width=self.Imaging_penwidth))
    self.ImagingStimcurve.clear()
    self.ImagingVmcurve = pg.PlotCurveItem(self.Imagingx, self.yImagingVm, pen=pg.mkPen(Settings.DarkSolarized[3], width=self.Imaging_penwidth))
    self.ImagingVmcurve.clear()

    self.CurrentImagingPlots.addItem(self.ImagingStimcurve)
    self.CurrentImagingPlots.addItem(self.ImagingVmcurve)

def UpdateImagingViews(self):
    self.CurrentImagingPlots.setGeometry(self.ui.Imaging_Oscilloscope_widget.getViewBox().sceneBoundingRect())
    self.CurrentImagingPlots.linkedViewChanged(self.ui.Imaging_Oscilloscope_widget.getViewBox(), self.CurrentImagingPlots.XAxis)







