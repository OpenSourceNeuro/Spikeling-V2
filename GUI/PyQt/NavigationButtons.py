
########################################################################
#                          Libraries import                            #

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QPropertyAnimation
from PySide6.QtSerialPort import QSerialPortInfo

from Neuron_Parameters import Ui_AdvancedParameters
import Page000, Page101, Page102, Page103, Page201, Page202, Page203, Page204, Page301, Page401, Page501, Page502, Page503, Page601, Page701, Page801, Page901
import Spikeling_graph, Emulator_graph, Imaging_graph, MultipleImaging_graph


########################################################################
#                          COM Port definitions                        #
########################################################################

# Setting UART parameters
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        portList.append(port.portName())


########################################################################
#                       Toggle Button Animations                       #
########################################################################

animation_speed = 500
leftMenu_min = 40
leftMenu_max = 180
centerMenu_min = 0
centerMenu_max = 200
spikecenterMenu_min = 0
spikecenterMenu_max = 200
spikerightMenu_min = 40
spikerightMenu_max = 200

def toggleMenu(self, menu, standard, maxWidth, duration, pushButton, icon_min, icon_max, enable):
        if enable:
                #Get width
                width = menu.width()

                #Extend
                if width == standard:
                        widthExtended = maxWidth
                        pushButton.setIcon(icon_max)
                #Retract
                else:
                        widthExtended = standard
                        pushButton.setIcon(icon_min)

                #Animation
                self.animation = QPropertyAnimation(menu, b"minimumWidth")
                self.animation.setDuration(duration)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation.start()

def expandMenu(self, menu, standard, maxWidth, duration, enable):
        if enable:
                width = menu.width()
                if width == standard:
                    #Animation
                    self.animation = QPropertyAnimation(menu, b"minimumWidth")
                    self.animation.setDuration(duration)
                    self.animation.setStartValue(standard)
                    self.animation.setEndValue(maxWidth)
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animation.start()

def collapseMenu(self, menu, standard, maxWidth, duration, enable):
        if enable:
                width = menu.width()
                if width == maxWidth:
                    #Animation
                    self.animation = QPropertyAnimation(menu, b"minimumWidth")
                    self.animation.setDuration(duration)
                    self.animation.setStartValue(maxWidth)
                    self.animation.setEndValue(standard)
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animation.start()



########################################################################
#                      Opening auxilliary windows                      #
########################################################################

def openWindow(self):
        self.aux_window.show()


def GetNeuronParameters(self):
        self.ui.NeuronParameter_PRGain = float(self.ui_aux.AdvancedParameters_PRGain_lineEdit.text())
        self.ui.NeuronParameter_PRDecay = float(self.ui_aux.AdvancedParameters_PRDecay_lineEdit.text())
        self.ui.NeuronParameter_PRRecovery = float(self.ui_aux.AdvancedParameters_PRRecovery_lineEdit.text())

        self.ui.NeuronParameter_Syn1Gain = float(self.ui_aux.AdvancedParameters_Syn1Gain_lineEdit.text())
        self.ui.NeuronParameter_Syn1Decay = float(self.ui_aux.AdvancedParameters_Syn1Decay_lineEdit.text())

        self.ui.NeuronParameter_Syn2Gain = float(self.ui_aux.AdvancedParameters_Syn2Gain_lineEdit.text())
        self.ui.NeuronParameter_Syn2Decay = float(self.ui_aux.AdvancedParameters_Syn2Decay_lineEdit.text())

        self.aux_window.close()

def CloseNeuronParameters(self):
        self.aux_window.close()


########################################################################
#                           Button Functions                           #
########################################################################

def Buttons(self):

        # Navigation buttons
        self.icon_SpikelingDropMenuRight = QIcon()
        self.icon_SpikelingDropMenuRight.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal,
                                                 QIcon.Off)
        self.icon_SpikelingMenuRight = QIcon()
        self.icon_SpikelingMenuRight.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)


        # Main Menu Container
        self.icon_DropMenuLeft = QIcon()
        self.icon_DropMenuLeft.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_MenuLeft = QIcon()
        self.icon_MenuLeft.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.leftMenuContainer.setMinimumSize(QSize(leftMenu_max, 16777215))
        self.ui.menu_pushButton.clicked.connect(lambda: toggleMenu(self, self.ui.leftMenuContainer, leftMenu_min, leftMenu_max, animation_speed,
                                                                self.ui.menu_pushButton, self.icon_MenuLeft, self.icon_DropMenuLeft, True))


        # Left Menu Container
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Spikeling_SubMenu_page))

        self.ui.ImagingMenu_pushButton.clicked.connect(lambda:  expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.ImagingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Imaging_SubMenu_page))

        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: Page301.ShowPage(self))

        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: Page401.ShowPage(self))
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))

        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Exercises_SubMenu_page))

        self.ui.centerMenuSubContainer_exit_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))

        self.ui.SettingsMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))

        self.ui.AboutMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))

        self.ui.HelpMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))

        self.ui.GitHubMenu_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))


        # Right Menu Container
        # Spikeling parameters navigation button
        self.ui.Spikeling_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.Spikeling_rightMenuContainer.setMinimumSize(QSize(spikerightMenu_max, 16777215))
        self.ui.Spikeling_rightMenuSubContainer_pushButton.clicked.connect(lambda: toggleMenu(self, self.ui.Spikeling_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                              self.ui.Spikeling_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Spikeling_parameter_exit_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))


        # Emulator parameters navigation button
        self.ui.Emulator_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.Emulator_rightMenuContainer.setMinimumSize(QSize(spikerightMenu_max, 16777215))
        self.ui.Emulator_rightMenuSubContainer_pushButton.clicked.connect(lambda: toggleMenu(self, self.ui.Emulator_rightMenuContainer, spikerightMenu_min, spikerightMenu_max,animation_speed,
                                                                                             self.ui.Emulator_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.Emulator_StimulusParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Emulator_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Emulator_NeuronParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Emulator_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Emulator_Synapse1_Parameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Emulator_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Emulator_Synapse2_Parameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Emulator_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Emulator_parameter_exit_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.Emulator_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))



        # Imaging  parameters navigation button
        self.ui.Imaging_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.Imaging_rightMenuContainer.setMinimumSize(QSize(0, 16777215))
        self.ui.Imaging_rightMenuSubContainer_pushButton.clicked.connect(lambda: toggleMenu(self, self.ui.Imaging_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                            self.ui.Imaging_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.Imaging_ImagingParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_CalciumParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_FluoParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_parameter_exit_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))


        # Multiple Imaging parameters navigation button
        self.ui.MultipleImaging_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.MultipleImaging_rightMenuContainer.setMinimumSize(QSize(0, 16777215))
        self.ui.MultipleImaging_rightMenuSubContainer_pushButton.clicked.connect(lambda: toggleMenu(self, self.ui.MultipleImaging_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                                    self.ui.MultipleImaging_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.MultipleImaging_ImagingParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_CalciumParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_FluoParameter_pushButton.clicked.connect(lambda: expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_parameter_exit_pushButton.clicked.connect(lambda: collapseMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))


    ########################################################################
    # Home Page - page000
        # Display Home page on start up
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_000)
        self.ui.appTitle_pushButton.clicked.connect(lambda: self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_000))

    ########################################################################
    # Spikeling Page - page101

        # Display page101 when spikeling button is clicked
        self.ui.Neuron_pushButton.clicked.connect(lambda: Page101.Spikeling.ShowPage(self))

        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        # COM port connections
        self.ui.Spikeling_SelectPortComboBox.currentIndexChanged.connect(lambda: Page101.Spikeling.ChangePort(self))

        # Start reading serial when connect button is clicked and plot the reading on the oscilloscope
        self.ui.Spikeling_ConnectButton.clicked.connect(lambda: Spikeling_graph.SpikelingPlot(self))

        # Load previously conceived neurons
        self.ui.Spikeling_NeuronBrowsePushButton.clicked.connect(lambda: Page101.Spikeling.BrowseNeuron(self))

        # Select Neuron Mode from the list and applied Izhikevich parameters:
        self.ui.ImportNeuron = []
        self.ui.Spikeling_NeuronMode_pushButton.clicked.connect(lambda: Page101.Spikeling.SelectNeuronMode(self))

        # Deactivate buzzer sound
        self.ui.Sound_pushButton.clicked.connect(lambda: Page101.Spikeling.ControlBuzzer(self))

        # Deactivate LED light
        self.ui.LED_pushButton.clicked.connect(lambda: Page101.Spikeling.ControlLED(self))

        # Create buffer data record folder
        self.ui.Spikeling_FolderNameLabel = QtWidgets.QLabel(self.ui.Spikeling_DataRecording_box)
        self.ui.Spikeling_FolderNameLabel.setObjectName("FolderNameLabel")

        # Data Recording
        self.ui.Spikeling_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page101.Spikeling.RecordFolderText(self))
        self.ui.Spikeling_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page101.Spikeling.BrowseRecordFolder(self.ui))
        self.ui.Spikeling_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.Spikeling_DataRecording_Record_pushButton.clicked.connect(lambda: Page101.Spikeling.RecordButton(self))

        # Stimulation parameters
        # Display stimulation parameter page when StimulusParameter button is clicked
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.StimulusParameter_page))
        self.ui.StimFre_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateStimFre(self))
        self.ui.Spikeling_StimFre_slider.valueChanged.connect(lambda: Page101.Spikeling.GetStimFreSliderValue(self))
        self.ui.StimStr_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateStimStr(self))
        self.ui.Spikeling_StimStrSlider.valueChanged.connect(lambda: Page101.Spikeling.GetStimStrSliderValue(self))
        self.ui.StimCus_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateCustomStimulus(self))

        self.ui.Spikeling_CustomStimulus_Load_pushButton.clicked.connect(lambda: Page101.Spikeling.LoadStimulus(self))
        self.ui.PhotoGain_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivatePhotoGain(self))
        self.ui.Spikeling_PR_PhotoGain_slider.valueChanged.connect(lambda: Page101.Spikeling.GetPhotoGain(self))
        self.ui.PhotoDecay_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivatePRDecay(self))
        self.ui.Spikeling_PR_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling.GetPRDecay(self))
        self.ui.PhotoRecovery_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivatePRRecovery(self))
        self.ui.Spikeling_PR_Recovery_slider.valueChanged.connect(lambda: Page101.Spikeling.GetPRRecovery(self))

        # Neuron parameters
        # Display neuron parameter page when NeuronParameter button is clicked
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.NeuronParameter_page))
        self.ui.PatchClamp_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateInjectedCurrent(self))
        self.ui.Spikeling_PatchClamp_slider.valueChanged.connect(lambda: Page101.Spikeling.GetInjectedCurrent(self))
        self.ui.Noise_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateNoiseLevel(self))
        self.ui.Spikeling_Noise_slider.valueChanged.connect(lambda: Page101.Spikeling.GetNoiseLevel(self))
        self.ui.Synapse1_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateSynapticGain1(self))
        self.ui.Spikeling_Synapse1_slider.valueChanged.connect(lambda: Page101.Spikeling.GetSynapticGain1(self))
        self.ui.Synapse1Decay_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateSynapseDecay1(self))
        self.ui.Spikeling_Synapse1_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling.GetSynapticDecay1(self))
        self.ui.Synapse2_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateSynapticGain2(self))
        self.ui.Spikeling_Synapse2_slider.valueChanged.connect(lambda: Page101.Spikeling.GetSynapticGain2(self))
        self.ui.Synapse2Decay_toggleButton.toggled.connect(lambda: Page101.Spikeling.ActivateSynapseDecay2(self))
        self.ui.Spikeling_Synapse2_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling.GetSynapticDecay2(self))


    ########################################################################
    # Emulator - page 102

        # Display page102 when emulator button is clicked
        self.ui.NeuronEmulator_pushButton.clicked.connect(lambda: Page102.Emulator.ShowPage(self))


        # Start the Emulator
        self.ui.Emulator_Connect_pushButton.clicked.connect(lambda: Emulator_graph.EmulatorPlot(self))


        # Load previously conceived neurons
        self.ui.Emulator_NeuronBrowse_pushButton.clicked.connect(lambda: Page102.Emulator.BrowseNeuron(self))


        # Select Neuron Mode from the list and applied Izhikevich parameters:
        self.ui.EmulatorImportNeuron = []
        self.ui.Emulator_NeuronApplyMode_pushButton.clicked.connect(lambda: Page102.Emulator.SelectNeuronMode(self))


        # Create buffer data record folder
        self.ui.Emulator_FolderNameLabel = QtWidgets.QLabel(self.ui.Emulator_DataRecording_box)
        self.ui.Emulator_FolderNameLabel.setObjectName("FolderNameLabel")


        # Data Recording
        self.ui.Emulator_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page102.Emulator.RecordFolderText(self))
        self.ui.Emulator_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page102.Emulator.BrowseRecordFolder(self.ui))
        self.ui.Emulator_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.Emulator_DataRecording_Record_pushButton.clicked.connect(lambda: Page102.Emulator.RecordButton(self))


        # Stimulation parameters
        self.ui.Emulator_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Emulator_parameter_stackedwidget.setCurrentWidget(self.ui.Emulator_StimulusParameter_page))
        self.ui.EmulatorStimFre_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateStimFre(self))
        self.ui.Emulator_StimFre_slider.valueChanged.connect(lambda: Page102.Emulator.GetStimFreSliderValue(self))
        self.ui.EmulatorStimStr_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateStimStr(self))
        self.ui.Emulator_StimStrSlider.valueChanged.connect(lambda: Page102.Emulator.GetStimStrSliderValue(self))
        self.ui.EmulatorStimCus_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateCustomStimulus(self))

        self.ui.Emulator_CustomStimulus_Load_pushButton.clicked.connect(lambda: Page102.Emulator.LoadStimulus(self))
        self.ui.EmulatorPhotoGain_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivatePhotoGain(self))
        self.ui.Emulator_PR_PhotoGain_slider.valueChanged.connect(lambda: Page102.Emulator.GetPhotoGain(self))
        self.ui.EmulatorPhotoDecay_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivatePRDecay(self))
        self.ui.Emulator_PR_Decay_slider.valueChanged.connect(lambda: Page102.Emulator.GetPRDecay(self))
        self.ui.EmulatorPhotoRecovery_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivatePRRecovery(self))
        self.ui.Emulator_PR_Recovery_slider.valueChanged.connect(lambda: Page102.Emulator.GetPRRecovery(self))


        # Neuron parameters
        self.ui.Emulator_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Emulator_parameter_stackedwidget.setCurrentWidget(self.ui.Emulator_NeuronParameter_page))
        self.ui.EmulatorPatchClamp_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateInjectedCurrent(self))
        self.ui.Emulator_PatchClamp_slider.valueChanged.connect(lambda: Page102.Emulator.GetInjectedCurrent(self))
        self.ui.EmulatorNoise_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateNoiseLevel(self))
        self.ui.Emulator_Noise_slider.valueChanged.connect(lambda: Page102.Emulator.GetNoiseLevel(self))
        self.ui.EmulatorSynapse1_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateSynapticGain1(self))
        self.ui.Emulator_Synapse1_slider.valueChanged.connect(lambda: Page102.Emulator.GetSynapticGain1(self))
        self.ui.EmulatorSynapse1Decay_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateSynapseDecay1(self))
        self.ui.Emulator_Synapse1_Decay_slider.valueChanged.connect(lambda: Page102.Emulator.GetSynapticDecay1(self))
        self.ui.EmulatorSynapse2_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateSynapticGain2(self))
        self.ui.Emulator_Synapse2_slider.valueChanged.connect(lambda: Page102.Emulator.GetSynapticGain2(self))
        self.ui.EmulatorSynapse2Decay_toggleButton.toggled.connect(lambda: Page102.Emulator.ActivateSynapseDecay2(self))
        self.ui.Emulator_Synapse2_Decay_slider.valueChanged.connect(lambda: Page102.Emulator.GetSynapticDecay2(self))


        # Auxiliary Neuron 1 parameters
        self.ui.Emulator_Synapse1_Parameter_pushButton.clicked.connect(lambda: self.ui.Emulator_parameter_stackedwidget.setCurrentWidget(self.ui.Emulator_Synapse1Parameter_page))

        # Load previously conceived neurons
        self.ui.Emulator_Syn1_Mode_Browse_pushButton.clicked.connect(lambda: Page102.EmulatorSyn1.BrowseNeuron(self))

        # Select Neuron Mode from the list and applied Izhikevich parameters:
        self.ui.EmulatorSyn1_ImportNeuron = []
        self.ui.Emulator_Syn1_Mode_Apply_pushButton.clicked.connect(lambda: Page102.EmulatorSyn1.SelectNeuronMode(self))

        self.ui.EmulatorSyn1_Synapse_toggleButton.clicked.connect(lambda: Page102.EmulatorSyn1.ActivateSynapse(self))
        self.ui.EmulatorSyn1_StimLight_toggleButton.clicked.connect(lambda: Page102.EmulatorSyn1.ActivatePhotoParameters(self))

        self.ui.EmulatorSyn1_PatchClamp_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn1.ActivateInjectedCurrent(self))
        self.ui.Emulator_Syn1_PatchClamp_slider.valueChanged.connect(lambda: Page102.EmulatorSyn1.GetInjectedCurrent(self))
        self.ui.EmulatorSyn1_Noise_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn1.ActivateNoiseLevel(self))
        self.ui.Emulator_Syn1_Noise_slider.valueChanged.connect(lambda: Page102.EmulatorSyn1.GetNoiseLevel(self))

        self.ui.EmulatorSyn1_PhotoGain_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn1.ActivatePhotoGain(self))
        self.ui.Emulator_Syn1_PR_PhotoGain_slider.valueChanged.connect(lambda: Page102.EmulatorSyn1.GetPhotoGain(self))
        self.ui.EmulatorSyn1_PhotoDecay_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn1.ActivatePRDecay(self))
        self.ui.Emulator_Syn1_PR_Decay_slider.valueChanged.connect(lambda: Page102.EmulatorSyn1.GetPRDecay(self))
        self.ui.EmulatorSyn1_PhotoRecovery_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn1.ActivatePRRecovery(self))
        self.ui.Emulator_Syn1_PR_Recovery_slider.valueChanged.connect(lambda: Page102.EmulatorSyn1.GetPRRecovery(self))


        # Auxiliary Neuron 2 parameters
        self.ui.Emulator_Synapse2_Parameter_pushButton.clicked.connect( lambda: self.ui.Emulator_parameter_stackedwidget.setCurrentWidget(self.ui.Emulator_Synapse2Parameter_page))

        # Load previously conceived neurons
        self.ui.Emulator_Syn2_Mode_Browse_pushButton.clicked.connect(lambda: Page102.EmulatorSyn2.BrowseNeuron(self))

        # Select Neuron Mode from the list and applied Izhikevich parameters:
        self.ui.EmulatorSyn2_ImportNeuron = []
        self.ui.Emulator_Syn2_Mode_Apply_pushButton.clicked.connect(lambda: Page102.EmulatorSyn2.SelectNeuronMode(self))

        self.ui.EmulatorSyn2_Synapse_toggleButton.clicked.connect(lambda: Page102.EmulatorSyn2.ActivateSynapse(self))
        self.ui.EmulatorSyn2_StimLight_toggleButton.clicked.connect(lambda: Page102.EmulatorSyn2.ActivatePhotoParameters(self))

        self.ui.EmulatorSyn2_PatchClamp_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn2.ActivateInjectedCurrent(self))
        self.ui.Emulator_Syn2_PatchClamp_slider.valueChanged.connect(lambda: Page102.EmulatorSyn2.GetInjectedCurrent(self))
        self.ui.EmulatorSyn2_Noise_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn2.ActivateNoiseLevel(self))
        self.ui.Emulator_Syn2_Noise_slider.valueChanged.connect(lambda: Page102.EmulatorSyn2.GetNoiseLevel(self))

        self.ui.EmulatorSyn2_PhotoGain_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn2.ActivatePhotoGain(self))
        self.ui.Emulator_Syn2_PR_PhotoGain_slider.valueChanged.connect(lambda: Page102.EmulatorSyn2.GetPhotoGain(self))
        self.ui.EmulatorSyn2_PhotoDecay_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn2.ActivatePRDecay(self))
        self.ui.Emulator_Syn2_PR_Decay_slider.valueChanged.connect(lambda: Page102.EmulatorSyn2.GetPRDecay(self))
        self.ui.EmulatorSyn2_PhotoRecovery_toggleButton.toggled.connect(lambda: Page102.EmulatorSyn2.ActivatePRRecovery(self))
        self.ui.Emulator_Syn2_PR_Recovery_slider.valueChanged.connect(lambda: Page102.EmulatorSyn2.GetPRRecovery(self))



    ########################################################################
    # Spikeling Data Analysis - page 103
        # Display page103 when data analysis button is clicked
        self.ui.NeuronDataAnalysis_pushButton.clicked.connect(lambda: Page103.Spikeling103.ShowPage(self))

        # Raw Data Analysis part
        self.ui.DataAnalysis_LoadData_pushButton.clicked.connect(lambda: Page103.Spikeling103.LoadData(self.ui))
        self.ui.DataAnalysis_LoadData_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.DisplayRawData(self))
        self.ui.DataAnalysis_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveRawDataImage(self))
        # Find spike analysis part
        self.ui.DataAnalysis_Spike_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.FindSpike(self))
        self.ui.DataAnalysis_Spike_Export_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveSpikeTraces(self))
        self.ui.DataAnalysis_Spike_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveSpikeImage(self))
        # Compute average trace and spike raster plot
        self.ui.DataAnalysis_Average_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.AverageTraces(self))
        self.ui.DataAnalysis_Average_Save_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveAverageTraces(self))
        self.ui.DataAnalysis_Average_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveAverageImage(self))
        # Switch Neuron display pages on raw data page
        self.ui.DataAnalysis_Neuron0Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        self.ui.DataAnalysis_Neuron0Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_0))
        # Switch Neuron display pages on find spike age
        self.ui.DataAnalysis_Neuron1Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        self.ui.DataAnalysis_Neuron1Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_1))
        # Switch Neuron display pages on compute and average page
        self.ui.DataAnalysis_Neuron2Vm_pushButton10.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton11.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton12.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_1_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton20.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton21.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton22.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_2_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton30.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton31.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))
        self.ui.DataAnalysis_Neuron2Vm_pushButton32.clicked.connect(lambda: self.ui.DataAnalysis_Display_StackedWidget.setCurrentWidget(self.ui.page_103_3_2))

        # Raw Data Analysis part
        self.ui.DataAnalysis_StepStim_LoadData_pushButton.clicked.connect(lambda: Page103.Spikeling103.LoadData(self.ui))
        self.ui.DataAnalysis_StepStim_LoadData_Display_pushButton.clicked.connect(lambda: Page103.Spikeling103.DisplayRawData(self))
        self.ui.DataAnalysis_StepStim_SaveImage_pushButton.clicked.connect(lambda: Page103.Spikeling103.SaveRawDataImage(self))

    ########################################################################
    # Imaging Page - page201
        # Display page201 when imaging button is clicked
        self.ui.ImagingStimulation_pushButton.clicked.connect(lambda: Page201.Imaging201.ShowPage(self))

        # Connect the imaging Oscilloscope to the Spikeling Oscilloscope
        self.ui.Imaging_pushButton.clicked.connect(lambda: Imaging_graph.ImagingPlot(self))

        # Data Recording
        self.ui.Imaging_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page201.Imaging201.RecordFolderText(self))
        self.ui.Imaging_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page201.Imaging201.BrowseRecordFolder(self.ui))
        self.ui.Imaging_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.Imaging_DataRecording_Record_pushButton.clicked.connect(lambda: Page201.Imaging201.RecordButton(self))

        # Imaging Parameters
        self.ui.Imaging_ImagingParameter_pushButton.clicked.connect(lambda: self.ui.Imaging_parameter_stackedWidget.setCurrentWidget(self.ui.Imaging_ImagingParameter_page))
        self.ui.Imaging_FrameRate_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateFrameRate(self))
        self.ui.Imaging_FrameRate_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetFrameRate(self))
        self.ui.Imaging_PMT_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivatePMT(self))
        self.ui.Imaging_PMT_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetPMT(self))
        self.ui.Imaging_Laser_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateLaser(self))
        self.ui.Imaging_Laser_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetLaser(self))

        # Calcium parameters
        self.ui.Imaging_CalciumParameter_pushButton.clicked.connect(lambda: self.ui.Imaging_parameter_stackedWidget.setCurrentWidget(self.ui.Imaging_CalciumParameter_page))
        self.ui.Imaging_CalciumDecay_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateCalciumDecay(self))
        self.ui.Imaging_CalciumDecay_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetCalciumDecay(self))
        self.ui.Imaging_CalciumJump_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateCalciumJump(self))
        self.ui.Imaging_CalciumJump_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetCalciumJump(self))
        self.ui.Imaging_CalciumNoise_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateCalciumNoise(self))
        self.ui.Imaging_CalciumNoise_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetCalciumNoise(self))
        self.ui.Imaging_CalciumBaseline_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateCalciumBaseline(self))
        self.ui.Imaging_CalciumBaseline_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetCalciumBaseline(self))

        # Fluorescence Parameters
        self.ui.Imaging_FluoParameter_pushButton.clicked.connect(lambda: self.ui.Imaging_parameter_stackedWidget.setCurrentWidget(self.ui.Imaging_FluoParameter_page))
        self.ui.Imaging_kd_toggleButton.setEnabled(False)
        self.ui.Imaging_kd_toggleButton.toggled.connect(lambda: Page201.Imaging201.Activatekd(self))
        self.ui.Imaging_kd_Slider.valueChanged.connect(lambda: Page201.Imaging201.Getkd(self))
        self.ui.Imaging_Hill_toggleButton.setEnabled(False)
        self.ui.Imaging_Hill_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateHill(self))
        self.ui.Imaging_Hill_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetHill(self))
        self.ui.Imaging_PhotoShotNoise_toggleButton.setEnabled(False)
        self.ui.Imaging_PhotoShotNoise_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivatePhotoShotNoise(self))
        self.ui.Imaging_PhotoShotNoise_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetPhotoShotNoise(self))
        self.ui.Imaging_FluoNoise_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateFluoNoise(self))
        self.ui.Imaging_FluoNoise_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetFluoNoise(self))
        self.ui.Imaging_FluoScale_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateFluoScale(self))
        self.ui.Imaging_FluoScale_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetFluoScale(self))
        self.ui.Imaging_FluoOffset_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateFluoOffset(self))
        self.ui.Imaging_FluoOffset_Slider.valueChanged.connect(lambda: Page201.Imaging201.GetFluoOffset(self))
        self.ui.Imaging_Saturation_toggleButton.toggled.connect(lambda: Page201.Imaging201.ActivateFluoSat(self))


    ########################################################################
    # Imaging Tutorial - page202
        # Display page202 when imaging button is clicked
        self.ui.MultipleImagingStimulation_pushButton.clicked.connect(lambda: Page202.Imaging202.ShowPage(self))

        # Connect the Multiple imaging Oscilloscope to the Spikeling Oscilloscope
        self.ui.MultipleImaging_pushButton.clicked.connect(lambda: MultipleImaging_graph.MultipleImagingPlot(self))

        # Data Recording
        self.MultipleImagingFolderFlag = False
        self.ui.MultipleImaging_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page202.Imaging202.RecordFolderText(self))
        self.ui.MultipleImaging_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page202.Imaging202.BrowseRecordFolder(self.ui))
        self.ui.MultipleImaging_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.MultipleImaging_DataRecording_Record_pushButton.clicked.connect(lambda: Page202.Imaging202.RecordButton(self))

        # Imaging Parameters
        self.ui.MultipleImaging_ImagingParameter_pushButton.clicked.connect(lambda: self.ui.MultipleImaging_parameter_stackedWidget.setCurrentWidget(self.ui.MultipleImaging_ImagingParameter_page))
        self.ui.MultipleImaging_FrameRate_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleFrameRate(self))
        self.ui.MultipleImaging_FrameRate_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleFrameRate(self))
        self.ui.MultipleImaging_PMT_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultiplePMT(self))
        self.ui.MultipleImaging_PMT_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultiplePMT(self))
        self.ui.MultipleImaging_Laser_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleLaser(self))
        self.ui.MultipleImaging_Laser_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleLaser(self))

        # Calcium parameters
        self.ui.MultipleImaging_CalciumParameter_pushButton.clicked.connect(lambda: self.ui.MultipleImaging_parameter_stackedWidget.setCurrentWidget(self.ui.MultipleImaging_CalciumParameter_page))
        self.ui.MultipleImaging_CalciumDecay_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleCalciumDecay(self))
        self.ui.MultipleImaging_CalciumDecay_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleCalciumDecay(self))
        self.ui.MultipleImaging_CalciumJump_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleCalciumJump(self))
        self.ui.MultipleImaging_CalciumJump_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleCalciumJump(self))
        self.ui.MultipleImaging_CalciumNoise_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleCalciumNoise(self))
        self.ui.MultipleImaging_CalciumNoise_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleCalciumNoise(self))
        self.ui.MultipleImaging_CalciumBaseline_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleCalciumBaseline(self))
        self.ui.MultipleImaging_CalciumBaseline_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleCalciumBaseline(self))

        # Fluorescence Parameters
        self.ui.MultipleImaging_FluoParameter_pushButton.clicked.connect(lambda: self.ui.MultipleImaging_parameter_stackedWidget.setCurrentWidget(self.ui.MultipleImaging_FluoParameter_page))
        self.ui.MultipleImaging_kd_toggleButton.setEnabled(False)
        self.ui.MultipleImaging_kd_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultiplekd(self))
        self.ui.MultipleImaging_kd_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultiplekd(self))
        self.ui.MultipleImaging_Hill_toggleButton.setEnabled(False)
        self.ui.MultipleImaging_Hill_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleHill(self))
        self.ui.MultipleImaging_Hill_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleHill(self))
        self.ui.MultipleImaging_PhotoShotNoise_toggleButton.setEnabled(False)
        self.ui.MultipleImaging_PhotoShotNoise_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultiplePhotoShotNoise(self))
        self.ui.MultipleImaging_PhotoShotNoise_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultiplePhotoShotNoise(self))
        self.ui.MultipleImaging_FluoNoise_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleFluoNoise(self))
        self.ui.MultipleImaging_FluoNoise_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleFluoNoise(self))
        self.ui.MultipleImaging_FluoScale_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleFluoScale(self))
        self.ui.MultipleImaging_FluoScale_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleFluoScale(self))
        self.ui.MultipleImaging_FluoOffset_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleFluoOffset(self))
        self.ui.MultipleImaging_FluoOffset_Slider.valueChanged.connect(lambda: Page202.Imaging202.GetMultipleFluoOffset(self))
        self.ui.MultipleImaging_Saturation_toggleButton.toggled.connect(lambda: Page202.Imaging202.ActivateMultipleFluoSat(self))



        ########################################################################
    # Imaging Data Analysis- page203
        # Display page201 when imaging button is clicked
        self.ui.ImagingTutorial_pushButton.clicked.connect(lambda: Page203.Imaging203.ShowPage(self))




    ########################################################################
    # Imaging Data Analysis- page204
        # Display page201 when imaging button is clicked
        self.ui.ImagingDataAnalysis_pushButton.clicked.connect(lambda: Page204.Imaging204.ShowPage(self))




        ########################################################################
    # Neuron Generator Page - page301
        # Display page301 when neuron button is clicked
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: Page301.ShowPage(self))

        # Draw Neuron model based on parameters a, b, c & d
        self.ui.DisplayNeuron_pushButton.clicked.connect(lambda: Page301.NeuronGenerator.DrawNeuron(self))

        # Display Advanced Neuron parameters window
        self.ui.AdvancedParameter_pushButton.clicked.connect(lambda: openWindow(self))
        self.ui_aux.AdvancedParameters_Button_Save_pushButton.clicked.connect(lambda: GetNeuronParameters(self))
        self.ui_aux.AdvancedParameters_Button_Exit_pushButton.clicked.connect(lambda: CloseNeuronParameters(self))

        # Load Pre-selected neurons
        self.ui.LoadNeuron_comboBox.currentIndexChanged.connect(lambda: Page301.NeuronGenerator.LoadNeuron(self))
        # Save current neuron
        self.ui.SaveNeuronPushButton.clicked.connect(lambda: Page301.NeuronGenerator.SaveNeuron(self))




    ########################################################################
    # Stimulus Generator Page - page401
        # Display page401
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: Page401.ShowPage(self))
        # Change Stimulus parameter page
        self.ui.StimulusGenerator_Selection_comboBox.currentIndexChanged.connect(lambda: Page401.ChangeStimulusParameter(self))
        # Display stimulus generated
        self.ui.StimulusGenerator_Display_pushButton.clicked.connect(lambda: Page401.StimulusGenerator.DrawStimulus(self))
        # Save current stimulus
        self.ui.StimulusGenerator_Save_pushButton.clicked.connect(lambda: Page401.StimulusGenerator.SaveStimulus(self))
        # Adapt Chirp page parameters to current selection
        self.ui.Chirp_comboBox.currentIndexChanged.connect(lambda: Page401.ChangeChirpParameter(self))




    ########################################################################
    # Exercise-101 - page501
        # Display page501
        self.ui.Exercice101_pushButton.clicked.connect(lambda: Page501.ShowPage(self))
        self.ui.Exercise101_PreviousButton_pushButton.clicked.connect(lambda: Page501.Previous(self))
        self.ui.Exercise101_AfterButton_pushButton.clicked.connect(lambda: Page501.After(self))

        self.ui.FI_Curve_pushButton.clicked.connect(lambda: Page501.FI.Plot_FI(self))
        self.ui.FI_Curve_pushButton_2.clicked.connect(lambda: Page501.FI.Plot_FI2(self))


    ########################################################################
    # Exercise-102 - page502
        # Display page502
        self.ui.Exercice102_pushButton.clicked.connect(lambda: Page502.ShowPage(self))
        self.ui.Exercise102_PreviousButton_pushButton.clicked.connect(lambda: Page502.Previous(self))
        self.ui.Exercise102_AfterButton_pushButton.clicked.connect(lambda: Page502.After(self))


    ########################################################################
    # Exercise-103 - page503
        # Display page503
        self.ui.Exercice103_pushButton.clicked.connect(lambda: Page503.ShowPage(self))
        self.ui.Exercise103_PreviousButton_pushButton.clicked.connect(lambda: Page503.Previous(self))
        self.ui.Exercise103_AfterButton_pushButton.clicked.connect(lambda: Page503.After(self))


        ########################################################################
    # Settings - page601
        # Display Settings
        self.ui.SettingsMenu_pushButton.clicked.connect(lambda: Page601.ShowPage(self))




    ########################################################################
    # About - page701
        # Display Info page
        self.ui.AboutMenu_pushButton.clicked.connect(lambda: Page701.ShowPage(self))




    ########################################################################
    # Help - page801
        # Display Help page
        self.ui.HelpMenu_pushButton.clicked.connect(lambda: Page801.ShowPage(self))




    ########################################################################
    # GitHub - page901
        # Display Git page
        self.ui.GitHubMenu_pushButton.clicked.connect(lambda: Page901.ShowPage(self))

        ########################################################################



