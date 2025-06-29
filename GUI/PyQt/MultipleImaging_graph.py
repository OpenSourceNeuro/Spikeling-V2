
########################################################################
#                          Libraries import                            #

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPen
import pyqtgraph as pg

import numpy as np
import pandas as pd
import collections

import Settings



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
        self.MultipleImagingConnectionFlag = True
        self.Multipleimagingtimer = QTimer()
        self.Multipleimagingtimer.timeout.connect(lambda: UpdateMultipleImagingPlot(self))
        self.Multipleimagingtimer.start()
    else:
        self.Multipleimagingtimer.stop()
        self.CurrentMultipleImagingPlots.clear()
        self.CurrentMultipleImagingPlots.removeItem(self.MultipleStimcurve)
        self.ui.MultipleImaging_Oscilloscope_widget.clear()



    def UpdateMultipleImagingPlot(self):
        self.ui.MultipleImaging_Oscilloscope_widget.getViewBox().sigResized.connect(UpdateMultipleImagingViews(self))
        self.MultipleImagingData = GetMultipleData(self)
        BuffMultipleImagingData(self)                              # Append latest data into buffer deque
        SaveMultipleImagingPlotData(self)                          # Create data array to be exported in .csv
        if self.i_Multipleimaging_downsampling == 0:               # Plot Data once every "downsampling" time
            PlotMultipleImagingCurve(self)
        self.i_Multipleimaging_downsampling += 1
        if self.i_Multipleimaging_downsampling == self.Multipleimaging_downsampling - 1:
            self.i_Multipleimaging_downsampling = 0


    # Read Serial and return data
    def GetMultipleData(self):
        if self.ui.SpikelingConnectedFlag == True:
            self.rx = self.serial_port.readline()
            self.rx_serial = str(self.rx, 'utf8').strip()
            self.data = self.rx_serial.split(',')
            return self.data
        if self.ui.EmulatorConnectedFlag == True:
            self.data = self.ui.Emulator_data
            return self.data


    # Append latest serial data point into buffer deque
    def BuffMultipleImagingData(self):
        self.MultipleVmData1 = self.MultipleImagingData[0]
        self.MultipleVmData2 = self.MultipleImagingData[3]
        self.MultipleVmData3 = self.MultipleImagingData[5]
        self.MultipleTriggerData = self.MultipleImagingData[7]
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


        self.MultipleStimdatabuffer.append(self.MultipleStimData)
        self.MultipleTriggerdatabuffer.append(self.MultipleTriggerData)

        self.MultipleFluodatabuffer1.append(self.MultipleFluoData1)
        self.MultipleCalciumdatabuffer1.append(self.MultipleCalciumData1)
        self.MultipleVmdatabuffer1.append(self.MultipleVmData1)

        self.MultipleFluodatabuffer2.append(self.MultipleFluoData2)
        self.MultipleCalciumdatabuffer2.append(self.MultipleCalciumData2)
        self.MultipleVmdatabuffer2.append(self.MultipleVmData2)

        self.MultipleFluodatabuffer3.append(self.MultipleFluoData3)
        self.MultipleCalciumdatabuffer3.append(self.MultipleCalciumData3)
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


def SaveMultipleImagingPlotData(self):                              # Save latest buffer data and export them as csv
    if self.ui.MultipleImaging_DataRecording_Record_pushButton.isChecked() == False and self.MultipleImagingrecordflag == True:
        MultipleImagingDataset = np.empty([12, len(self.DataSet[1])], dtype=float)

        for i in range(len(self.DataSet[1])):
            MultipleImagingDataset[0][i] = i * 0.1
            MultipleImagingDataset[1][i] = self.DataSet[1][i]
            MultipleImagingDataset[2][i] = self.DataSet[2][i]
            MultipleImagingDataset[3][i] = self.DataSet[3][i]
            MultipleImagingDataset[4][i] = self.DataSet[4][i]
            MultipleImagingDataset[5][i] = self.DataSet[5][i]
            MultipleImagingDataset[6][i] = self.DataSet[6][i]
            MultipleImagingDataset[7][i] = self.DataSet[7][i]
            MultipleImagingDataset[8][i] = self.DataSet[8][i]
            MultipleImagingDataset[9][i] = self.DataSet[9][i]
            MultipleImagingDataset[10][i] = self.DataSet[10][i]
            MultipleImagingDataset[11][i] = self.DataSet[11][i]

        dict = {'Time (ms)': MultipleImagingDataset[0], 'Stimulus (%)': MultipleImagingDataset[1], 'Trigger': MultipleImagingDataset[2],
                'Spikeling Fluorescence': MultipleImagingDataset[3], 'Spikeling Calcium': MultipleImagingDataset[4], 'Spikeling Vm (mV)': MultipleImagingDataset[5],
                'Neuron Aux1 Fluorescence': MultipleImagingDataset[6], 'Neuron Aux1 Calcium': MultipleImagingDataset[7], 'Neuron Aux1 Vm (mV)': MultipleImagingDataset[8],
                'Neuron Aux2 Fluorescence': MultipleImagingDataset[9], 'Neuron Aux2 Calcium': MultipleImagingDataset[10], 'Neuron Aux2 Vm (mV)': MultipleImagingDataset[11]
                }
        df = pd.DataFrame(dict)
        self.RecordingFileName = str(self.ui.MultipleImaging_SelectedFolderLabel.text())
        df.to_csv(self.RecordingFileName + '.csv', index=False)
        self.MultipleImagingrecordflag = False
        self.DataSet[0].clear()
        self.DataSet[1].clear()
        self.DataSet[2].clear()
        self.DataSet[3].clear()
        self.DataSet[4].clear()
        self.DataSet[5].clear()
        self.DataSet[6].clear()
        self.DataSet[7].clear()
        self.DataSet[8].clear()
        self.DataSet[9].clear()
        self.DataSet[10].clear()
        self.DataSet[11].clear()


    if self.ui.MultipleImaging_DataRecording_Record_pushButton.isChecked() == True:
        self.MultipleImagingrecordflag = True

        self.DataSet[1].append(self.MultipleStimdatabuffer[-1])
        self.DataSet[2].append(self.MultipleTriggerdatabuffer[-1])
        self.DataSet[3].append(self.MultipleFluodatabuffer1[-1])
        self.DataSet[4].append(self.MultipleCalciumdatabuffer1[-1])
        self.DataSet[5].append(self.MultipleVmdatabuffer1[-1])
        self.DataSet[6].append(self.MultipleFluodatabuffer2[-1])
        self.DataSet[7].append(self.MultipleCalciumdatabuffer2[-1])
        self.DataSet[8].append(self.MultipleVmdatabuffer2[-1])
        self.DataSet[9].append(self.MultipleFluodatabuffer3[-1])
        self.DataSet[10].append(self.MultipleCalciumdatabuffer3[-1])
        self.DataSet[11].append(self.MultipleVmdatabuffer3[-1])



def SetMultipleImagingInitParameters(self):
    self.i_Multipleimaging_downsampling = 0
    self.MultipleImagingrecordflag = False
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

    self.MultipleStimdatabuffer     = collections.deque([0.0] * self._MultipleImaging_bufsize,self._MultipleImaging_bufsize)
    self.MultipleTriggerdatabuffer  = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)

    self.MultipleFluodatabuffer1    = collections.deque([0.0] * self._MultipleImaging_bufsize,self._MultipleImaging_bufsize)
    self.MultipleCalciumdatabuffer1 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer1      = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)

    self.MultipleFluodatabuffer2    = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleCalciumdatabuffer2 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer2      = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)

    self.MultipleFluodatabuffer3    = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleCalciumdatabuffer3 = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)
    self.MultipleVmdatabuffer3      = collections.deque([0.0] * self._MultipleImaging_bufsize, self._MultipleImaging_bufsize)


    self.MultipleImagingx  = np.linspace(-self.MultipleImaging_timewindow, 0.0, self._MultipleImaging_bufsize)            # Create arrays of self._Imaging_bufsize length
    self.yMultipleCalcium1 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleCalcium2 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleCalcium3 = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo1    = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo2    = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleFluo3    = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleStim     = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm1      = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm2      = np.zeros(self._MultipleImaging_bufsize, dtype=float)
    self.yMultipleVm3      = np.zeros(self._MultipleImaging_bufsize, dtype=float)

    self.DataSet = []
    for _ in range(12):
        self.DataSet.append([])

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
    self.MultipleCalciumcurve3.clear()
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







