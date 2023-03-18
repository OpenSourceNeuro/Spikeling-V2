import numpy as np
import pyqtgraph
import Settings


def ShowPage(self):
    self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_401)
    self.ui.StimulusGenerator_Parameter_stackedWidget.setCurrentIndex(0)
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
        if self.StimulusIndex == 1:
            StimulusGenerator.SineWave(self)

    def SaveStimulus(self):
        print("tada")

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