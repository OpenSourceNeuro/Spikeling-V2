import sys
import serial
from Main import MainWindow
import Spikeling_UI
import resources_rc
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QPropertyAnimation
from PySide6.QtWidgets import QSizeGrip


BaudRate = 115200


DarkSolarized = [[0, 30, 38], [0, 43, 54], [7, 54, 66],                                            # 0:DarkBase01, 1:DarkBase02, 2:DarkBase03
                 [220, 50, 47], [133, 153, 0], [38, 139, 210],                                     # 3:Red, 4:Green, 5:Blue
                 [203, 75, 22], [42, 161, 152], [181, 137, 0], [108, 113, 196], [211, 54, 130],    # 6:Orange, 7:Cyan, 8:Yellow, 9:Violet, 10:Magenta
                 [88, 110, 117], [101, 123, 131], [131, 148, 150], [147, 161, 161],                # 11:Content01, 12:Content02, 13:Content03, 14:Content04
                 [238, 232, 213],[253, 246, 227],                                                  # 15:LightBase01, 16:LightBase02
                 [0,153,176]]                                                                      # 17:OSH-Logo



animation_speed = 500
leftMenu_min = 40
leftMenu_max = 180
centerMenu_min = 0
centerMenu_max = 200
spikecenterMenu_min = 0
spikecenterMenu_max = 200
spikerightMenu_min = 40
spikerightMenu_max = 200

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

        def maximize_restore(self):
            global GLOBAL_STATE
            status = GLOBAL_STATE

            # IF NOT MAXIMIZED
            if status == 0:
                self.showMaximized()
                self.ui.expand_pushButton.setIcon(self.icon_reduce)

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1
                self.ui.expand_pushButton.setToolTip("Restore")

            else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.ui.expand_pushButton.setIcon(self.icon_expand)
                self.resize(self.width() + 1, self.height() + 1)
                self.ui.expand_pushButton.setToolTip("Maximize")

        ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
        def returnStatus():
            return GLOBAL_STATE


        ## ==> UI DEFINITIONS
        def uiDefinitions(self):

            # REMOVE TITLE BAR
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # MAXIMIZE / RESTORE
            self.ui.expand_pushButton.clicked.connect(lambda: UIFunctions.maximize_restore(self))

            # MINIMIZE
            self.ui.reduce_pushButton.clicked.connect(lambda: self.showMinimized())

            # CLOSE
            self.ui.exit_pushButton.clicked.connect(lambda: self.close())

            ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.sizegrip)
            self.sizegrip.setToolTip("Resize Window")



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


