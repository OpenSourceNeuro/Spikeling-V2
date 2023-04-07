########################################################################
# Libraries import

import sys
import os
import platform
import serial

# Import QT libraries
from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

# Import GUI .ui file
from Spikeling_UI import Ui_MainWindow
from Spikeling_SplashScreen import Ui_SplashScreen
from Settings import *
from py_toggle import PyToggle

# Import GUI page scripts
import Page000, Page101, Page102, Page103, Page201, Page202, Page203, Page204, Page301, Page401, Page501, Page502, Page601, Page701, Page801, Page901
import Spikeling_graph
import Imaging_graph, MultipleImaging_graph


# Setting UART parameters
#ports = Settings.COM()
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    if sys.platform == "linux" or sys.platform == "linux2":
        portList.append(port.systemLocation())
        print(port.systemLocation())
    else:
        portList.append(port.portName())

## ==> GLOBALS
counter = 0

########################################################################
## SplashScreen WINDOW CLASS
########################################################################
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.SplashFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

        # CHANGE DESCRIPTION

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.Status_Label.setText("<strong>Loading</strong> Database"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.Status_Label.setText("<strong>Loading</strong> User interface"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.Loading_ProgressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Custom Navigation bar buttons
        self.icon_expand = QIcon()
        self.icon_expand.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_reduce = QIcon()
        self.icon_reduce.addFile(u":/resources/resources/Reduce.png", QSize(), QIcon.Normal, QIcon.Off)


        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()


        # Generate toggle buttons for Spikeling Page
        self.ui.PatchClamp_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                   circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                   active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                   )
        self.ui.Noise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                              active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                              )
        self.ui.PhotoGain_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                  circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                  active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                  )
        self.ui.PhotoDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                   circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                   active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                   )
        self.ui.PhotoRecovery_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                      )
        self.ui.StimFre_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                active_color='#%02x%02x%02x' % tuple(DarkSolarized[5])
                                                )
        self.ui.StimStr_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                active_color='#%02x%02x%02x' % tuple(DarkSolarized[5])
                                                )
        self.ui.StimCus_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                active_color='#%02x%02x%02x' % tuple(DarkSolarized[5])
                                                )
        self.ui.Synapse1_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                 circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                 active_color='#%02x%02x%02x' % tuple(DarkSolarized[7])
                                                 )
        self.ui.Synapse1Decay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(DarkSolarized[7])
                                                      )
        self.ui.Synapse2_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                 circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                 active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                 )
        self.ui.Synapse2Decay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                      )
        self.ui.Spikeling_PatchClamp_toggle_layout.addWidget(self.ui.PatchClamp_toggleButton)
        self.ui.Spikeling_PatchClamp_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_Noise_toggle_layout.addWidget(self.ui.Noise_toggleButton)
        self.ui.Spikeling_Noise_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_Synapse1_toggle_layout.addWidget(self.ui.Synapse1_toggleButton)
        self.ui.Spikeling_Synapse1_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_Synapse1_Decay_toggle_layout.addWidget(self.ui.Synapse1Decay_toggleButton)
        self.ui.Spikeling_Synapse1_Decay_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_Synapse2_toggle_layout.addWidget(self.ui.Synapse2_toggleButton)
        self.ui.Spikeling_Synapse2_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_Synapse2_Decay_toggle_layout.addWidget(self.ui.Synapse2Decay_toggleButton)
        self.ui.Spikeling_Synapse2_Decay_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.Spikeling_StimFre_toggle_layout.addWidget(self.ui.StimFre_toggleButton)
        self.ui.Spikeling_StimFre_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_StimStr_toggle_layout.addWidget(self.ui.StimStr_toggleButton)
        self.ui.Spikeling_StimStr_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_CustomStimulus_toggle_layout.addWidget(self.ui.StimCus_toggleButton)
        self.ui.Spikeling_CustomStimulus_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_PR_toggle_layout.addWidget(self.ui.PhotoGain_toggleButton)
        self.ui.Spikeling_PR_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Spikeling_PRDecay_Toggle_layout.addWidget(self.ui.PhotoDecay_toggleButton)
        self.ui.Spikeling_PRDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.SpikelingPRRecovery_toggle_layout.addWidget(self.ui.PhotoRecovery_toggleButton)
        self.ui.SpikelingPRRecovery_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Generate toggle buttons for Imaging Page
        self.ui.Imaging_FrameRate_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                          circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                          active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                      )
        self.ui.Imaging_PMT_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                    circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                    active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                    )
        self.ui.Imaging_Laser_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                      )

        self.ui.Imaging_CalciumDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                             circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                             active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                             )
        self.ui.Imaging_CalciumJump_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                            circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                            active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                            )
        self.ui.Imaging_CalciumNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                             circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                             active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                             )
        self.ui.Imaging_CalciumBaseline_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                                )

        self.ui.Imaging_kd_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                   circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                   active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                   )
        self.ui.Imaging_Hill_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                     circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                     active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                     )
        self.ui.Imaging_PhotoShotNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                               circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                               active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                               )
        self.ui.Imaging_FluoNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                          circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                          active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                          )
        self.ui.Imaging_FluoScale_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                          circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                          active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                          )
        self.ui.Imaging_FluoOffset_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                           circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                           active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                           )
        self.ui.Imaging_Saturation_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                           circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                           active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                           )

        self.ui.Imaging_FrameRate_Toggle_layout.addWidget(self.ui.Imaging_FrameRate_toggleButton)
        self.ui.Imaging_FrameRate_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_PMT_Toggle_layout.addWidget(self.ui.Imaging_PMT_toggleButton)
        self.ui.Imaging_PMT_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_Laser_Toggle_layout.addWidget(self.ui.Imaging_Laser_toggleButton)
        self.ui.Imaging_Laser_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.Imaging_CalciumDecay_Toggle_layout.addWidget(self.ui.Imaging_CalciumDecay_toggleButton)
        self.ui.Imaging_CalciumDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_CalciumJump_Toggle_layout.addWidget(self.ui.Imaging_CalciumJump_toggleButton)
        self.ui.Imaging_CalciumJump_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_CalciumNoise_Toggle_layout.addWidget(self.ui.Imaging_CalciumNoise_toggleButton)
        self.ui.Imaging_CalciumNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_CalciumBaseline_Toggle_layout.addWidget(self.ui.Imaging_CalciumBaseline_toggleButton)
        self.ui.Imaging_CalciumBaseline_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.Imaging_kd_Toggle_layout.addWidget(self.ui.Imaging_kd_toggleButton)
        self.ui.Imaging_kd_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_Hill_Toggle_layout.addWidget(self.ui.Imaging_Hill_toggleButton)
        self.ui.Imaging_Hill_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_PhotoShotNoise_Toggle_layout.addWidget(self.ui.Imaging_PhotoShotNoise_toggleButton)
        self.ui.Imaging_PhotoShotNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_FluoNoise_Toggle_layout.addWidget(self.ui.Imaging_FluoNoise_toggleButton)
        self.ui.Imaging_FluoNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_FluoScale_Toggle_layout.addWidget(self.ui.Imaging_FluoScale_toggleButton)
        self.ui.Imaging_FluoScale_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_FluoOffset_Toggle_layout.addWidget(self.ui.Imaging_FluoOffset_toggleButton)
        self.ui.Imaging_FluoOffset_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.Imaging_Saturation_Toggle_layout.addWidget(self.ui.Imaging_Saturation_toggleButton)
        self.ui.Imaging_Saturation_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        # Generate toggle buttons for Multiple Imaging Page
        self.ui.MultipleImaging_FrameRate_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                  circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                  active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                  )
        self.ui.MultipleImaging_PMT_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                            circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                            active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                            )
        self.ui.MultipleImaging_Laser_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                              circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                              active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                              )

        self.ui.MultipleImaging_CalciumDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                     circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                     active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                                     )
        self.ui.MultipleImaging_CalciumJump_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                    circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                    active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                                    )
        self.ui.MultipleImaging_CalciumNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                     circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                     active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                                     )
        self.ui.MultipleImaging_CalciumBaseline_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                        circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                        active_color='#%02x%02x%02x' % tuple(DarkSolarized[10])
                                                                        )

        self.ui.MultipleImaging_kd_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                           circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                           active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                           )
        self.ui.MultipleImaging_Hill_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                             circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                             active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                             )
        self.ui.MultipleImaging_PhotoShotNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                       circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                       active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                       )
        self.ui.MultipleImaging_FluoNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                  circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                  active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                  )
        self.ui.MultipleImaging_FluoScale_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                  circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                  active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                  )
        self.ui.MultipleImaging_FluoOffset_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                   circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                   active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                   )
        self.ui.MultipleImaging_Saturation_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(DarkSolarized[11]),
                                                                   circle_color='#%02x%02x%02x' % tuple(DarkSolarized[15]),
                                                                   active_color='#%02x%02x%02x' % tuple(DarkSolarized[4])
                                                                   )

        self.ui.MultipleImaging_FrameRate_Toggle_layout.addWidget(self.ui.MultipleImaging_FrameRate_toggleButton)
        self.ui.MultipleImaging_FrameRate_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_PMT_Toggle_layout.addWidget(self.ui.MultipleImaging_PMT_toggleButton)
        self.ui.MultipleImaging_PMT_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_Laser_Toggle_layout.addWidget(self.ui.MultipleImaging_Laser_toggleButton)
        self.ui.MultipleImaging_Laser_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.MultipleImaging_CalciumDecay_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumDecay_toggleButton)
        self.ui.MultipleImaging_CalciumDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_CalciumJump_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumJump_toggleButton)
        self.ui.MultipleImaging_CalciumJump_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_CalciumNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumNoise_toggleButton)
        self.ui.MultipleImaging_CalciumNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_CalciumBaseline_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumBaseline_toggleButton)
        self.ui.MultipleImaging_CalciumBaseline_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.MultipleImaging_kd_Toggle_layout.addWidget(self.ui.MultipleImaging_kd_toggleButton)
        self.ui.MultipleImaging_kd_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_Hill_Toggle_layout.addWidget(self.ui.MultipleImaging_Hill_toggleButton)
        self.ui.MultipleImaging_Hill_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_PhotoShotNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_PhotoShotNoise_toggleButton)
        self.ui.MultipleImaging_PhotoShotNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_FluoNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoNoise_toggleButton)
        self.ui.MultipleImaging_FluoNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_FluoScale_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoScale_toggleButton)
        self.ui.MultipleImaging_FluoScale_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_FluoOffset_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoOffset_toggleButton)
        self.ui.MultipleImaging_FluoOffset_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.MultipleImaging_Saturation_Toggle_layout.addWidget(self.ui.MultipleImaging_Saturation_toggleButton)
        self.ui.MultipleImaging_Saturation_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Custom Navigation bar movement
        self.ui.header_widget.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)



    ########################################################################
    # Set menu/navigation buttons

        # Main Menu Container
        self.icon_DropMenuLeft = QIcon()
        self.icon_DropMenuLeft.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_MenuLeft = QIcon()
        self.icon_MenuLeft.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.leftMenuContainer.setMinimumSize(QSize(leftMenu_max, 16777215))
        self.ui.menu_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.leftMenuContainer, leftMenu_min, leftMenu_max, animation_speed,
                                                                               self.ui.menu_pushButton, self.icon_MenuLeft, self.icon_DropMenuLeft, True))


        # Left Menu Container
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.SpikelingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Spikeling_SubMenu_page))
        self.ui.ImagingMenu_pushButton.clicked.connect(lambda:  UIFunctions.expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.ImagingMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Imaging_SubMenu_page))
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.NeuronGeneratorMenu_pushButton.clicked.connect(lambda: Page301.ShowPage(self))
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: Page401.ShowPage(self))
        self.ui.StimuluGeneratorMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.ExercisesMenu_pushButton.clicked.connect(lambda: self.ui.centerMenuSubContainer_menu_stackedwidget.setCurrentWidget(self.ui.Exercises_SubMenu_page))
        self.ui.centerMenuSubContainer_exit_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.SettingsMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.AboutMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.HelpMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))
        self.ui.GitHubMenu_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.centerMenuContainer, centerMenu_min, centerMenu_max, animation_speed, True))


        # Spikeling 101 parameters navigation button
        self.icon_SpikelingDropMenuRight = QIcon()
        self.icon_SpikelingDropMenuRight.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_SpikelingMenuRight = QIcon()
        self.icon_SpikelingMenuRight.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.Spikeling_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.Spikeling_rightMenuContainer.setMinimumSize(QSize(spikerightMenu_max, 16777215))
        self.ui.Spikeling_rightMenuSubContainer_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Spikeling_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                                          self.ui.Spikeling_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Spikeling_parameter_exit_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.Spikeling_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))

        # Imaging 201 parameters navigation button
        self.ui.Imaging_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.Imaging_rightMenuContainer.setMinimumSize(QSize(spikerightMenu_max, 16777215))
        self.ui.Imaging_rightMenuSubContainer_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Imaging_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                                          self.ui.Imaging_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.Imaging_ImagingParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_CalciumParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_FluoParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.Imaging_parameter_exit_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.Imaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))


        # Imaging 202 parameters navigation button
        self.ui.MultipleImaging_CenterMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.ui.MultipleImaging_rightMenuContainer.setMinimumSize(QSize(spikerightMenu_max, 16777215))
        self.ui.MultipleImaging_rightMenuSubContainer_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.MultipleImaging_rightMenuContainer, spikerightMenu_min, spikerightMenu_max, animation_speed,
                                                                                                          self.ui.MultipleImaging_rightMenuSubContainer_pushButton, self.icon_SpikelingMenuRight, self.icon_SpikelingDropMenuRight, True))
        self.ui.MultipleImaging_ImagingParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_CalciumParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_FluoParameter_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))
        self.ui.MultipleImaging_parameter_exit_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.MultipleImaging_CenterMenuContainer, spikecenterMenu_min, spikecenterMenu_max, animation_speed, True))


    ########################################################################
    # Home Page - page000
        # Display Home page on start up
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_000)
        self.GifMovie = QtGui.QMovie("resources/spike.gif")
        self.ui.mainbody_content_SpikelingGif.setMovie(self.GifMovie)
        self.GifMovie.start()
        self.ui.appTitle_pushButton.clicked.connect(lambda: self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_000))

    ########################################################################
    # Spikeling Page - page101

        # Display page101 when spikeling button is clicked
        self.ui.Neuron_pushButton.clicked.connect(lambda: Page101.Spikeling101.ShowPage(self))

        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.Spikeling_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        # COM port connections
        self.ui.Spikeling_SelectPortComboBox.currentIndexChanged.connect(lambda: Page101.Spikeling101.ChangePort(self))

        # Start reading serial when connect button is clicked and plot the reading on the oscilloscope
        self.ui.Spikeling_ConnectButton.clicked.connect(lambda: Spikeling_graph.SpikelingPlot(self))

        # Load previously conceived neurons
        self.ui.Spikeling_NeuronBrowsePushButton.clicked.connect(lambda: Page101.Spikeling101.BrowseNeuron(self))

        # Select Neuron Mode from the list and applied Izhikevich parameters:
        self.ui.Spikeling_NeuronMode_pushButton.clicked.connect(lambda: Page101.Spikeling101.SelectNeuronMode(self))

        # Deactivate buzzer sound
        self.ui.Sound_pushButton.clicked.connect(lambda: Page101.Spikeling101.ControlBuzzer(self))

        # Deactivate LED light
        self.ui.LED_pushButton.clicked.connect(lambda: Page101.Spikeling101.ControlLED(self))

        # Create buffer data record folder
        self.ui.Spikeling_FolderNameLabel = QtWidgets.QLabel(self.ui.Spikeling_DataRecording_box)
        self.ui.Spikeling_FolderNameLabel.setObjectName("FolderNameLabel")

        # Data Recording
        self.ui.Spikeling_DataRecording_RecordFolder_value.textChanged.connect(lambda: Page101.Spikeling101.RecordFolderText(self))
        self.ui.Spikeling_DataRecording_RecordFolderDir_pushButton.clicked.connect(lambda: Page101.Spikeling101.BrowseRecordFolder(self.ui))
        self.ui.Spikeling_DataRecording_Record_pushButton.setCheckable(True)
        self.ui.Spikeling_DataRecording_Record_pushButton.clicked.connect(lambda: Page101.Spikeling101.RecordButton(self))

        # Stimulation parameters
        # Display stimulation parameter page when StimulusParameter button is clicked
        self.ui.Spikeling_StimulusParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.StimulusParameter_page))
        self.ui.StimFre_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateStimFre(self))
        self.ui.Spikeling_StimFre_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetStimFreSliderValue(self))
        self.ui.StimStr_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateStimStr(self))
        self.ui.Spikeling_StimStrSlider.valueChanged.connect(lambda: Page101.Spikeling101.GetStimStrSliderValue(self))
        self.ui.StimCus_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateCustomStimulus(self))

        self.ui.Spikeling_CustomStimulus_Load_pushButton.clicked.connect(lambda: Page101.Spikeling101.LoadStimulus(self))
        self.ui.PhotoGain_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivatePhotoGain(self))
        self.ui.Spikeling_PR_PhotoGain_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetPhotoGain(self))
        self.ui.PhotoDecay_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivatePRDecay(self))
        self.ui.Spikeling_PR_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetPRDecay(self))
        self.ui.PhotoRecovery_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivatePRRecovery(self))
        self.ui.Spikeling_PR_Recovery_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetPRRecovery(self))

        # Neuron parameters
        # Display neuron parameter page when NeuronParameter button is clicked
        self.ui.Spikeling_NeuronParameter_pushButton.clicked.connect(lambda: self.ui.Spikeling_parameter_stackedwidget.setCurrentWidget(self.ui.NeuronParameter_page))
        self.ui.PatchClamp_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateInjectedCurrent(self))
        self.ui.Spikeling_PatchClamp_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetInjectedCurrent(self))
        self.ui.Noise_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateNoiseLevel(self))
        self.ui.Spikeling_Noise_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetNoiseLevel(self))
        self.ui.Synapse1_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapticGain1(self))
        self.ui.Spikeling_Synapse1_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetSynapticGain1(self))
        self.ui.Synapse1Decay_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapseDecay1(self))
        self.ui.Spikeling_Synapse1_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetSynapticDecay1(self))
        self.ui.Synapse2_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapticGain2(self))
        self.ui.Spikeling_Synapse2_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetSynapticGain2(self))
        self.ui.Synapse2Decay_toggleButton.toggled.connect(lambda: Page101.Spikeling101.ActivateSynapseDecay2(self))
        self.ui.Spikeling_Synapse2_Decay_slider.valueChanged.connect(lambda: Page101.Spikeling101.GetSynapticDecay2(self))


    ########################################################################
    # Spikeling Tutorial - page 102
        # Display page102 when tutorial button is clicked
        self.ui.NeuronTutorial_pushButton.clicked.connect(lambda: Page102.Spikeling102.ShowPage(self))


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


    ########################################################################
    # Imaging Page - page201
        # Display page201 when imaging button is clicked
        self.ui.ImagingStimulation_pushButton.clicked.connect(lambda: Page201.Imaging201.ShowPage(self))

        # Connect the imaging Oscilloscope to the Spikeling Oscilloscope
        self.ui.Imaging_pushButton.clicked.connect(lambda: Imaging_graph.ImagingPlot(self))

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
        self.ui.DisplayNeuronPushButton.clicked.connect(lambda: Page301.NeuronGenerator.DrawNeuron(self))
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


    ########################################################################
    # Exercise-102 - page502
        # Display page502
        self.ui.Exercice102_pushButton.clicked.connect(lambda: Page502.ShowPage(self))


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
    # Display
        self.show()

    ## APP EVENTS
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(u":/resources/resources/Neuron.png"))
    window = SplashScreen()#MainWindow()
    sys.exit(app.exec())
########################################################################
## END===>
########################################################################  