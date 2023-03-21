import numpy as np
import pandas as pd
from scipy import signal
import pyqtgraph
import Settings
from PySide6.QtWidgets import QFileDialog, QWidget


def ShowPage(self):
    self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_401)
    self.ui.StimulusGenerator_Parameter_stackedWidget.setCurrentIndex(0)
    self.ui.StimulusGenerator_Selection_comboBox.setCurrentIndex(0)
    self.ui.StimulusGenerator_Oscilloscope_widget.clear()
    StimulusGenerator.SetGraph(self)

def ChangeStimulusParameter(self):
    self.StimulusIndex = self.ui.StimulusGenerator_Selection_comboBox.currentIndex()
    self.ui.StimulusGenerator_Parameter_stackedWidget.setCurrentIndex(self.StimulusIndex)



class StimulusGenerator():

    def SetGraph(self):
        self.ui.StimulusGenerator_Oscilloscope_widget.showGrid(x=True, y=True)
        self.ui.StimulusGenerator_Oscilloscope_widget.setRange(yRange=[-100, 100])
        self.ui.StimulusGenerator_Oscilloscope_widget.setBackground(Settings.DarkSolarized[0])
        self.ui.StimulusGenerator_Oscilloscope_widget.setLabel('left', 'Stimulus Intensity', 'a.u.')
        self.ui.StimulusGenerator_Oscilloscope_widget.setLabel('bottom', 'time', 'ms')

    def DrawStimulus(self):
        self.StimulusIndex = self.ui.StimulusGenerator_Selection_comboBox.currentIndex()
        if self.StimulusIndex == 0:
            StimulusGenerator.IntensitySteps(self)
        if self.StimulusIndex == 1:
            StimulusGenerator.SineWave(self)
        if self.StimulusIndex == 2:
            StimulusGenerator.TriangularWave(self)


    def SaveStimulus(self):
        self.StimulusIndex = self.ui.StimulusGenerator_Selection_comboBox.currentIndex()
        if self.StimulusIndex == 0:
            StimulusGenerator.IntensityStepsSave(self)
        if self.StimulusIndex == 1:
            StimulusGenerator.SineWaveSave(self)
        if self.StimulusIndex == 2:
            StimulusGenerator.TriangularWaveSave(self)


    def IntensitySteps(self):
        self.nStep = int(self.ui.Step_Number_Value.text())
        self.Increment = int(self.ui.Step_Increment_Value.text())
        self.FirstStep = int(self.ui.Step_First_Value.text())
        self.StepOn = int(self.ui.Step_On_Value.text())
        self.StepOff = int(self.ui.Step_Off_Value.text())
        self.iStepOff = int(self.ui.Step_OffInt_Value.text())
        self.tInter = int(self.ui.Step_Inter_Value.text())
        self.iInter = int(self.ui.Step_InterInt_Value.text())

        self.StepDur = self.StepOn + self.StepOff
        self.StimDur = self.StepDur * self.nStep + self.tInter
        self.xStep = np.zeros(self.StepDur)
        self.XStep = np.arange(self.StepDur)
        self.xStim = np.zeros(self.StimDur)
        self.XStim = np.arange(self.StimDur)

        self.ui.StimulusGenerator_Oscilloscope_widget.clear()

        for i in range(self.nStep):
            self.xStep[1 : self.StepOn] = self.FirstStep + i*self.Increment
            self.xStep[self.StepOn+1 :] = self.iStepOff
            self.xStim[i*self.StepDur : (i+1)*self.StepDur] = self.xStep[:]
            self.ui.StimulusGenerator_Oscilloscope_widget.plot(self.XStep, self.xStim[i*self.StepDur : (i+1)*self.StepDur], pen=(Settings.DarkSolarized[5]))


    def IntensityStepsSave(self):
        self.nStep = int(self.ui.Step_Number_Value.text())
        self.Increment = int(self.ui.Step_Increment_Value.text())
        self.FirstStep = int(self.ui.Step_First_Value.text())
        self.StepOn = int(self.ui.Step_On_Value.text())*10
        self.StepOff = int(self.ui.Step_Off_Value.text())*10
        self.iStepOff = int(self.ui.Step_OffInt_Value.text())
        self.tInter = int(self.ui.Step_Inter_Value.text())*10
        self.iInter = int(self.ui.Step_InterInt_Value.text())

        self.StepDur = self.StepOn + self.StepOff
        self.StimDur = self.StepDur * self.nStep + self.tInter
        self.nStim = np.zeros(self.StimDur)

        for i in range(self.nStep):
            self.nStim[i*self.StepDur : i*self.StepDur+self.StepOn] = self.FirstStep + i * self.Increment
            self.nStim[i*self.StepDur+self.StepOn : (i+1)*self.StepDur] = self.iStepOff
        self.nStim[self.StimDur-self.tInter : self.StimDur] = self.iInter

        self.nTrigger = np.zeros(self.StimDur)
        self.nTrigger[0] = 1

        FileName = QFileDialog.getSaveFileName(self.ui,
                                               caption='Save Stimulus on screen',
                                               dir="./Stimuli",
                                               filter='csv files (*.csv)')

        self.dict_SineStim = {'Stim': self.nStim, 'Trigger': self.nTrigger}
        self.df_SineStim = pd.DataFrame(self.dict_SineStim)

        self.df_SineStim.to_csv(FileName[0], index=False)

    def SineWave(self):
        self.Amplitude = int(self.ui.SineWave_Amplitude_Value.text())
        self.Frequency = int(self.ui.SineWave_Frequency_Value.text())
        self.Mean = int(self.ui.SineWave_Mean_Value.text())
        self.StimOn = int(self.ui.SineWave_StimOn_Value.text())
        self.StimOff = int(self.ui.SineWave_StimOff_Value.text())
        self.IntOff = int(self.ui.SineWave_IntOff_Value.text())

        self.StimDur = 2*self.StimOn + 2*self.StimOff
        self.nStim = np.zeros(self.StimDur)
        self.xStim = np.arange(self.StimDur)

        self.Sinex = np.arange(self.StimOn)
        self.Sinef = self.Frequency * self.StimOn / 1000
        self.Siney = np.sin(2 * np.pi * self.Sinef * self.Sinex / self.StimOn) * self.Amplitude + self.Mean

        self.nStim[0: self.StimOn] = self.Siney[0: self.StimOn]
        self.nStim[self.StimOn: self.StimOn + self.StimOff] = self.IntOff
        self.nStim[self.StimOn + self.StimOff: 2 * self.StimOn + self.StimOff] = self.Siney[0: self.StimOn]
        self.nStim[2 * self.StimOn + self.StimOff: 2 * self.StimOn + 2 * self.StimOff] = self.IntOff

        self.ui.StimulusGenerator_Oscilloscope_widget.clear()
        self.SineCurve = self.ui.StimulusGenerator_Oscilloscope_widget.plot(self.xStim, self.nStim, pen=(Settings.DarkSolarized[5]))


    def SineWaveSave(self):
        self.Amplitude = int(self.ui.SineWave_Amplitude_Value.text())
        self.Frequency = int(self.ui.SineWave_Frequency_Value.text())
        self.Mean = int(self.ui.SineWave_Mean_Value.text())
        self.StimOn = int(self.ui.SineWave_StimOn_Value.text())*10
        self.StimOff = int(self.ui.SineWave_StimOff_Value.text())*10
        self.IntOff = int(self.ui.SineWave_IntOff_Value.text())

        self.StimDur = self.StimOn + self.StimOff
        self.nStim = np.zeros(self.StimDur)
        self.xStim = np.arange(self.StimDur)

        self.Sinex = np.arange(self.StimOn)
        self.Sinef = self.Frequency * self.StimOn / 10000
        self.Siney = np.sin(2 * np.pi * self.Sinef * self.Sinex / self.StimOn) * self.Amplitude + self.Mean

        self.nStim[0: self.StimOn] = self.Siney[0: self.StimOn]
        self.nStim[self.StimOn: self.StimOn + self.StimOff] = self.IntOff

        self.nTrigger = np.zeros(self.StimDur)
        self.nTrigger[0] = 1


        FileName = QFileDialog.getSaveFileName(self.ui,
                                                      caption='Save Stimulus on screen',
                                                      dir="./Stimuli",
                                                      filter='csv files (*.csv)')

        self.dict_SineStim = {'Stim': self.nStim, 'Trigger': self.nTrigger}
        self.df_SineStim = pd.DataFrame(self.dict_SineStim)

        self.df_SineStim.to_csv(FileName[0], index = False)



    def TriangularWave(self):
        self.StimOn = int(self.ui.TriangleWave_StimOn_Value.text())
        self.Frequency = int(self.ui.TriangleWave_Frequency_Value.text())
        self.Amplitude = int(self.ui.TriangleWave_Amplitude_Value.text())
        self.Mean = int(self.ui.TriangleWave_Mean_Value.text())
        self.StimOff = int(self.ui.TriangleWave_StimOff_Value.text())
        self.IntOff = int(self.ui.TriangleWave_IntOff_Value.text())

        self.StimDur = self.StimOn + self.StimOff
        self.xStim = np.linspace (0, self.StimOn, self.StimOn)
        self.f = self.Frequency / 1000 * self.xStim

        self.Triangle = signal.sawtooth( 2 * np.pi * self.f - np.pi*3/2, 0.5)

        self.nStim = np.zeros(2*self.StimDur)
        self.nStim[0: self.StimOn] = self.Amplitude*self.Triangle
        self.nStim[self.StimDur: self.StimDur+self.StimOn] = self.Amplitude*self.Triangle

        self.nStim[self.StimOn : self.StimDur] = self.IntOff
        self.nStim[self.StimDur + self.StimOn: 2*self.StimDur] = self.IntOff

        self.XStim = np.arange(2*self.StimDur)

        self.ui.StimulusGenerator_Oscilloscope_widget.clear()
        self.SineCurve = self.ui.StimulusGenerator_Oscilloscope_widget.plot(self.XStim, self.nStim, pen=(Settings.DarkSolarized[5]))


    def TriangularWaveSave(self):
        self.StimOn = int(self.ui.TriangleWave_StimOn_Value.text())*10
        self.Frequency = int(self.ui.TriangleWave_Frequency_Value.text())
        self.Amplitude = int(self.ui.TriangleWave_Amplitude_Value.text())
        self.Mean = int(self.ui.TriangleWave_Mean_Value.text())
        self.StimOff = int(self.ui.TriangleWave_StimOff_Value.text())*10
        self.IntOff = int(self.ui.TriangleWave_IntOff_Value.text())

        self.StimDur = self.StimOn + self.StimOff
        self.xStim = np.linspace(0, self.StimOn, self.StimOn)
        self.f = self.Frequency / 10000 * self.xStim

        self.Triangle = signal.sawtooth(2 * np.pi * self.f - np.pi * 3 / 2, 0.5)

        self.nStim = np.zeros(self.StimOn + self.StimOff)
        self.nStim[0: self.StimOn] = self.Amplitude * self.Triangle
        self.nStim[self.StimOn: self.StimDur] = self.IntOff

        self.nTrigger = np.zeros(self.StimDur)
        self.nTrigger[0] = 1

        FileName = QFileDialog.getSaveFileName(self.ui,
                                               caption='Save Stimulus on screen',
                                               dir="./Stimuli",
                                               filter='csv files (*.csv)')

        self.dict_TriangleStim = {'Stim': self.nStim, 'Trigger': self.nTrigger}
        self.df_TriangleStim = pd.DataFrame(self.dict_TriangleStim)

        self.df_TriangleStim.to_csv(FileName[0], index=False)


