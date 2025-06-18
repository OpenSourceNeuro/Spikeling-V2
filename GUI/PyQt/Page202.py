
########################################################################
#                          Libraries import                            #

from PySide6.QtWidgets import QFileDialog
import Settings


class Imaging202():

    def ShowPage(self):
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_202)
        self.ui.MultipleImaging_Oscilloscope_widget.setBackground(Settings.DarkSolarized[0])


    # Data Recording Functions
    def BrowseRecordFolder(self):
        FolderName = QFileDialog.getExistingDirectory(
            caption='Hey! Select the folder where your experiment will be saved',
            dir=".\Recordings")
        if FolderName:
            self.MultipleImaging_DataRecording_SelectRecordFolder_label.setText(FolderName)
            self.MultipleImaging_DataRecording_RecordFolder_value.setEnabled(True)
            self.MultipleImaging_DataRecording_RecordFolder_value.setPlaceholderText("Enter a file name")
            self.MultipleImagingFolderFlag = True


    def RecordFolderText(self):
        FolderName = self.ui.MultipleImaging_DataRecording_SelectRecordFolder_label.text()
        FileName = self.ui.MultipleImaging_DataRecording_RecordFolder_value.text()
        self.ui.MultipleImaging_SelectedFolderLabel.setText(FolderName + '/' + FileName + '   ')


    def RecordButton(self):
        ConnectionFlag = False
        FolderFlag = False
        FileFlag = False

        if self.MultipleImagingConnectionFlag == False:
            self.ui.MultipleImaging_DataRecording_Record_pushButton.setChecked(False)
            Settings.show_popup(self,
                                Title="Error: Spikeling not connected",
                                Text="Spikeling data stream first needs to be connected. Check that a spikeling is running on either the neuron interface or the neuron emulator tab")
        else:
            ConnectionFlag = True

        if self.ui.MultipleImagingFolderFlag == True:
            FolderFlag = True

        else:
            self.ui.MultipleImaging_DataRecording_Record_pushButton.setChecked(False)
            Settings.show_popup(self,
                                Title="Error: no folder selected",
                                Text="Select a folder where to record your data by clicking on the - browse directory - button")

        if self.ui.MultipleImaging_DataRecording_RecordFolder_value.text():
            FileFlag = True
        else:
            self.ui.MultipleImaging_DataRecording_Record_pushButton.setChecked(False)
            Settings.show_popup(self,
                                Title="Error: no file selected",
                                Text="Select a file where to record your data by clicking on the - browse directory - button")

        if ConnectionFlag == True and FolderFlag == True and FileFlag == True:
            if self.ui.MultipleImaging_DataRecording_Record_pushButton.isChecked():
                self.ui.MultipleImaging_DataRecording_Record_pushButton.setText("Stop Recording")
                self.ui.MultipleImaging_DataRecording_Record_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                                                      "background-color: rgb(50, 220, 47);")

            else:
                self.ui.MultipleImaging_DataRecording_Record_pushButton.setChecked(False)
                self.ui.MultipleImaging_DataRecording_Record_pushButton.setText("Record")
                self.ui.MultipleImaging_DataRecording_Record_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                                                      "background-color: rgb(220, 50, 47);")

    # FrameRate
    def ActivateMultipleFrameRate(self):
            if self.ui.MultipleImaging_FrameRate_toggleButton.isChecked():
                    self.ui.MultipleImaging_FrameRate_Slider.setEnabled(True)
                    self.MultipleFrameRateValue = self.ui.MultipleImaging_FrameRate_Slider.value()
                    self.ui.MultipleImaging_FrameRate_Readings.setText(str(self.MultipleFrameRateValue))
                    self.ui.MultipleImaging_FrameRate_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_FrameRate_Slider.setEnabled(False)
                    self.ui.MultipleImaging_FrameRate_Slider.setValue(250)
                    self.ui.MultipleImaging_FrameRate_Readings.setText('')

    def GetMultipleFrameRate(self):
            self.MultipleFrameRateValue = self.ui.MultipleImaging_FrameRate_Slider.value()
            self.ui.MultipleImaging_FrameRate_Readings.setText(str(self.MultipleFrameRateValue))
            self.ui.MultipleImaging_FrameRate_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleFrameRate = self.MultipleFrameRateValue

    # PMT
    def ActivateMultiplePMT(self):
            if self.ui.MultipleImaging_PMT_toggleButton.isChecked():
                    self.ui.MultipleImaging_PMT_Slider.setEnabled(True)
                    self.MultiplePMTValue = self.ui.MultipleImaging_PMT_Slider.value()
                    self.ui.MultipleImaging_PMT_Readings.setText(str(self.MultiplePMTValue))
                    self.ui.MultipleImaging_PMT_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_PMT_Slider.setEnabled(False)
                    self.ui.MultipleImaging_PMT_Slider.setValue(100)
                    self.ui.MultipleImaging_PMT_Readings.setText('')

    def GetMultiplePMT(self):
            self.MultiplePMTValue = self.ui.MultipleImaging_PMT_Slider.value()
            self.ui.MultipleImaging_PMT_Readings.setText(str(self.MultiplePMTValue))
            self.ui.MultipleImaging_PMT_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultiplePMT = self.MultiplePMTValue/100

    # Laser
    def ActivateMultipleLaser(self):
            if self.ui.MultipleImaging_Laser_toggleButton.isChecked():
                    self.ui.MultipleImaging_Laser_Slider.setEnabled(True)
                    self.MultipleLaserValue = self.ui.MultipleImaging_Laser_Slider.value()
                    self.ui.MultipleImaging_Laser_Readings.setText(str(self.MultipleLaserValue))
                    self.ui.MultipleImaging_Laser_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_Laser_Slider.setEnabled(False)
                    self.ui.MultipleImaging_Laser_Slider.setValue(100)
                    self.ui.MultipleImaging_Laser_Readings.setText('')

    def GetMultipleLaser(self):
            self.MultipleLaserValue = self.ui.MultipleImaging_Laser_Slider.value()
            self.ui.MultipleImaging_Laser_Readings.setText(str(self.MultipleLaserValue))
            self.ui.MultipleImaging_Laser_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleLaser = self.MultipleLaserValue/100




    # CalciumDecay
    def ActivateMultipleCalciumDecay(self):
            if self.ui.MultipleImaging_CalciumDecay_toggleButton.isChecked():
                    self.ui.MultipleImaging_CalciumDecay_Slider.setEnabled(True)
                    self.MultipleCalciumDecayValue = self.ui.MultipleImaging_CalciumDecay_Slider.value()
                    self.ui.MultipleImaging_CalciumDecay_Readings.setText(str(self.MultipleCalciumDecayValue/10000))
                    self.ui.MultipleImaging_CalciumDecay_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_CalciumDecay_Slider.setEnabled(False)
                    self.ui.MultipleImaging_CalciumDecay_Slider.setValue(50)
                    self.ui.MultipleImaging_CalciumDecay_Readings.setText('')

    def GetMultipleCalciumDecay(self):
            self.MultipleCalciumDecayValue = self.ui.MultipleImaging_CalciumDecay_Slider.value()
            self.ui.MultipleImaging_CalciumDecay_Readings.setText(str(self.MultipleCalciumDecayValue/10000))
            self.ui.MultipleImaging_CalciumDecay_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            self.MultipleCalciumDecay = self.MultipleCalciumDecayValue/10000

    # CalciumJump
    def ActivateMultipleCalciumJump(self):
            if self.ui.MultipleImaging_CalciumJump_toggleButton.isChecked():
                    self.ui.MultipleImaging_CalciumJump_Slider.setEnabled(True)
                    self.MultipleCalciumJumpValue = self.ui.MultipleImaging_CalciumJump_Slider.value()
                    self.ui.MultipleImaging_CalciumJump_Readings.setText(str(self.MultipleCalciumJumpValue))
                    self.ui.MultipleImaging_CalciumJump_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_CalciumJump_Slider.setEnabled(False)
                    self.ui.MultipleImaging_CalciumJump_Slider.setValue(5)
                    self.ui.MultipleImaging_CalciumJump_Readings.setText('')

    def GetMultipleCalciumJump(self):
            self.MultipleCalciumJumpValue = self.ui.MultipleImaging_CalciumJump_Slider.value()
            self.ui.MultipleImaging_CalciumJump_Readings.setText(str(self.MultipleCalciumJumpValue))
            self.ui.MultipleImaging_CalciumJump_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            self.MultipleSpikeConcentrationRise = self.MultipleCalciumJumpValue

    # CalciumNoise
    def ActivateMultipleCalciumNoise(self):
            if self.ui.MultipleImaging_CalciumNoise_toggleButton.isChecked():
                    self.ui.MultipleImaging_CalciumNoise_Slider.setEnabled(True)
                    self.MultipleCalciumNoiseValue = self.ui.MultipleImaging_CalciumNoise_Slider.value()
                    self.ui.MultipleImaging_CalciumNoise_Readings.setText(str(self.MultipleCalciumNoiseValue/10))
                    self.ui.MultipleImaging_CalciumNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_CalciumNoise_Slider.setEnabled(False)
                    self.ui.MultipleImaging_CalciumNoise_Slider.setValue(10)
                    self.ui.MultipleImaging_CalciumNoise_Readings.setText('')

    def GetMultipleCalciumNoise(self):
            self.MultipleCalciumNoiseValue = self.ui.MultipleImaging_CalciumNoise_Slider.value()
            self.ui.MultipleImaging_CalciumNoise_Readings.setText(str(self.MultipleCalciumNoiseValue/10))
            self.ui.MultipleImaging_CalciumNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            self.MultipleNoiseScale = self.MultipleCalciumNoiseValue / 10

    # CalciumBaseline
    def ActivateMultipleCalciumBaseline(self):
            if self.ui.MultipleImaging_CalciumBaseline_toggleButton.isChecked():
                    self.ui.MultipleImaging_CalciumBaseline_Slider.setEnabled(True)
                    self.MultipleCalciumBaselineValue = self.ui.MultipleImaging_CalciumBaseline_Slider.value()
                    self.ui.MultipleImaging_CalciumBaseline_Readings.setText(str(self.MultipleCalciumBaselineValue/100))
                    self.ui.MultipleImaging_CalciumBaseline_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_CalciumBaseline_Slider.setEnabled(False)
                    self.ui.MultipleImaging_CalciumBaseline_Slider.setValue(10)
                    self.ui.MultipleImaging_CalciumBaseline_Readings.setText('')

    def GetMultipleCalciumBaseline(self):
            self.MultipleCalciumBaselineValue = self.ui.MultipleImaging_CalciumBaseline_Slider.value()
            self.ui.MultipleImaging_CalciumBaseline_Readings.setText(str(self.MultipleCalciumBaselineValue/100))
            self.ui.MultipleImaging_CalciumBaseline_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[10])) + "; font: 700 10pt;")
            self.MultipleCalciumBaseline = self.MultipleCalciumBaselineValue /100




    # Dissociation constant kd
    def ActivateMultiplekd(self):
            if self.ui.MultipleImaging_kd_toggleButton.isChecked():
                    self.ui.MultipleImaging_kd_Slider.setEnabled(True)
                    self.MultiplekdValue = self.ui.MultipleImaging_kd_Slider.value()
                    self.ui.MultipleImaging_kd_Readings.setText(str(self.MultiplekdValue*10))
                    self.ui.MultipleImaging_kd_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_kd_Slider.setEnabled(False)
                    self.ui.MultipleImaging_kd_Slider.setValue(20)
                    self.ui.MultipleImaging_kd_Readings.setText('')

    def GetMultiplekd(self):
            self.MultiplekdValue = self.ui.MultipleImaging_kd_Slider.value()
            self.ui.MultipleImaging_kd_Readings.setText(str(self.MultiplekdValue*10))
            self.ui.MultipleImaging_kd_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleDissociationConstant = self.MultiplekdValue * 10

    # Affinity (Hill constant)
    def ActivateMultipleHill(self):
            if self.ui.MultipleImaging_Hill_toggleButton.isChecked():
                    self.ui.MultipleImaging_Hill_Slider.setEnabled(True)
                    self.MultipleHillValue = self.ui.MultipleImaging_Hill_Slider.value()
                    self.ui.MultipleImaging_Hill_Readings.setText(str(self.MultipleHillValue/100))
                    self.ui.MultipleImaging_Hill_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_Hill_Slider.setEnabled(False)
                    self.ui.MultipleImaging_Hill_Slider.setValue(100)
                    self.ui.MultipleImaging_Hill_Readings.setText('')

    def GetMultipleHill(self):
            self.MultipleHillValue = self.ui.MultipleImaging_Hill_Slider.value()
            self.ui.MultipleImaging_Hill_Readings.setText(str(self.MultipleHillValue/10))
            self.ui.MultipleImaging_Hill_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleHillCoef = self.MultipleHillValue /100

    # Photon Shot Noise
    def ActivateMultiplePhotoShotNoise(self):
        if self.ui.MultipleImaging_PhotoShotNoise_toggleButton.isChecked():
            self.ui.MultipleImaging_PhotoShotNoise_Slider.setEnabled(True)
            self.MultiplePSNValue = self.ui.MultipleImaging_PhotoShotNoise_Slider.value()
            self.ui.MultipleImaging_PhotoShotNoise_Readings.setText(str(self.MultiplePSNValue / 10000 / 100))
            self.ui.MultipleImaging_PhotoShotNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
        else:
            self.ui.MultipleImaging_PhotoShotNoise_Slider.setEnabled(False)
            self.ui.MultipleImaging_PhotoShotNoise_Slider.setValue(400)
            self.ui.MultipleImaging_PhotoShotNoise_Readings.setText('')

    def GetMultiplePhotoShotNoise(self):
        self.MultiplePSNValue = self.ui.MultipleImaging_PhotoShotNoise_Slider.value()
        self.ui.MultipleImaging_PhotoShotNoise_Readings.setText(str(self.MultiplePSNValue / 10000 / 100))
        self.ui.MultipleImaging_PhotoShotNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
        self.MultiplePhotoShotNoise = self.MultiplePSNValue / 10000 / 100

    # Fluorescence Noise
    def ActivateMultipleFluoNoise(self):
            if self.ui.MultipleImaging_FluoNoise_toggleButton.isChecked():
                    self.ui.MultipleImaging_FluoNoise_Slider.setEnabled(True)
                    self.MultipleFluoNoiseValue = self.ui.MultipleImaging_FluoNoise_Slider.value()
                    self.ui.MultipleImaging_FluoNoise_Readings.setText(str(self.MultipleFluoNoiseValue/10))
                    self.ui.MultipleImaging_FluoNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_FluoNoise_Slider.setEnabled(False)
                    self.ui.MultipleImaging_FluoNoise_Slider.setValue(10)
                    self.ui.MultipleImaging_FluoNoise_Readings.setText('')

    def GetMultipleFluoNoise(self):
            self.MultipleFluoNoiseValue = self.ui.MultipleImaging_FluoNoise_Slider.value()
            self.ui.MultipleImaging_FluoNoise_Readings.setText(str(self.MultipleFluoNoiseValue/10))
            self.ui.MultipleImaging_FluoNoise_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleFluoNoiseScale = self.MultipleFluoNoiseValue /10

    # Fluorescence Scale
    def ActivateMultipleFluoScale(self):
            if self.ui.MultipleImaging_FluoScale_toggleButton.isChecked():
                    self.ui.MultipleImaging_FluoScale_Slider.setEnabled(True)
                    self.MultipleFluoScaleValue = self.ui.MultipleImaging_FluoScale_Slider.value()
                    self.ui.MultipleImaging_FluoScale_Readings.setText(str(self.MultipleFluoScaleValue/10))
                    self.ui.MultipleImaging_FluoScale_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_FluoScale_Slider.setEnabled(False)
                    self.ui.MultipleImaging_FluoScale_Slider.setValue(10)
                    self.ui.MultipleImaging_FluoScale_Readings.setText('')

    def GetMultipleFluoScale(self):
            self.MultipleFluoScaleValue = self.ui.MultipleImaging_FluoScale_Slider.value()
            self.ui.MultipleImaging_FluoScale_Readings.setText(str(self.MultipleFluoScaleValue/10))
            self.ui.MultipleImaging_FluoScale_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleFluoScale = self.MultipleFluoScaleValue /10

    # Fluorescence Offset
    def ActivateMultipleFluoOffset(self):
            if self.ui.MultipleImaging_FluoOffset_toggleButton.isChecked():
                    self.ui.MultipleImaging_FluoOffset_Slider.setEnabled(True)
                    self.MultipleFluoOffsetValue = self.ui.MultipleImaging_FluoOffset_Slider.value()
                    self.ui.MultipleImaging_FluoOffset_Readings.setText(str(self.MultipleFluoOffsetValue))
                    self.ui.MultipleImaging_FluoOffset_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            else:
                    self.ui.MultipleImaging_FluoOffset_Slider.setEnabled(False)
                    self.ui.MultipleImaging_FluoOffset_Slider.setValue(5)
                    self.ui.MultipleImaging_FluoOffset_Readings.setText('')

    def GetMultipleFluoOffset(self):
            self.MultipleFluoOffsetValue = self.ui.MultipleImaging_FluoOffset_Slider.value()
            self.ui.MultipleImaging_FluoOffset_Readings.setText(str(self.MultipleFluoOffsetValue))
            self.ui.MultipleImaging_FluoOffset_Readings.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])) + "; font: 700 10pt;")
            self.MultipleFluoOffset = self.MultipleFluoOffsetValue


    def ActivateMultipleFluoSat(self):
            if self.ui.MultipleImaging_Saturation_toggleButton.isChecked():
                self.ui.MultipleImaging_FluoSat_Label.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[4])))
                self.ui.MultipleImaging_kd_frame.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[1])))
                self.ui.MultipleImaging_Saturation_Line.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[0])))
                self.ui.MultipleImaging_Hill_frame.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[1])))
                self.ui.MultipleImaging_Saturation_Line2.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[0])))
                self.ui.MultipleImaging_PhotoShotNoise_frame.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[1])))
                self.ui.MultipleImaging_kd_toggleButton.setEnabled(True)
                self.ui.MultipleImaging_Hill_toggleButton.setEnabled(True)
                self.ui.MultipleImaging_PhotoShotNoise_toggleButton.setEnabled(True)
                self.MultipleSaturationFlag = True
                self.MultipleFluoNoiseScale = self.ui.MultipleImaging_FluoNoise_Slider.value() / 10
            else:
                self.ui.MultipleImaging_FluoSat_Label.setStyleSheet("color: rgb" + str(tuple(Settings.DarkSolarized[14])))
                self.ui.MultipleImaging_kd_frame.setStyleSheet("background-color: rgb(80, 96, 100)")
                self.ui.MultipleImaging_Saturation_Line.setStyleSheet("background-color: rgb(80, 96, 100)")
                self.ui.MultipleImaging_Hill_frame.setStyleSheet("background-color: rgb(80, 96, 100)")
                self.ui.MultipleImaging_Saturation_Line2.setStyleSheet("background-color: rgb(80, 96, 100)")
                self.ui.MultipleImaging_PhotoShotNoise_frame.setStyleSheet("background-color: rgb(80, 96, 100)")
                self.ui.MultipleImaging_kd_toggleButton.setEnabled(False)
                self.ui.MultipleImaging_Hill_toggleButton.setEnabled(False)
                self.ui.MultipleImaging_PhotoShotNoise_toggleButton.setEnabled(False)
                self.ui.MultipleImaging_kd_toggleButton.setChecked(False)
                self.ui.MultipleImaging_Hill_toggleButton.setChecked(False)
                self.ui.MultipleImaging_PhotoShotNoise_toggleButton.setChecked(False)
                self.MultipleSaturationFlag = False
                self.MultipleFluoNoiseScale = self.ui.MultipleImaging_FluoNoise_Slider.value() / 10



