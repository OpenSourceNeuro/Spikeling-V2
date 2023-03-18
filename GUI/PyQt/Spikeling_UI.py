# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Spikeling_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin:0;\n"
"	color: rgb(147,161,161);    \n"
"}\n"
"\n"
"#app_ID_frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#mainbody_header_frame{\n"
"	background-color: rgb(7, 54, 66);\n"
"	color: rgb(238, 232, 213);\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:  rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 5px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#leftMenuSubContainer QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"\n"
"#centerMenuSubContainer{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#centerMenuSubContainer_exit_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"centerMenuSubContainer_menu_stackedwidge"
                        "t{\n"
"}\n"
"#centerMenuSubContainer_menu_stackedwidget QPushButton{\n"
"	text-align: center;\n"
"	padding: 10px 0px;\n"
"	border-radius:20px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"#centerMenuSubContainer_menu_stackedwidget QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#header_widget{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"#footer_widget{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"#Spikeling_rightMenuSubContainer{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Spikeling_parameter_stackedwidget{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"\n"
"#StimulusParameter_page QComboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(0, 30, 38);\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#Spikeling_DataRecording_box{\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#Spikeling_DataRecording_box QLineEdit{\n"
"	border: 2px solid rgb(147,161,161);\n"
"    background-color: rgb(7, 54, 66);\n"
"}\n"
"#Spikeling_DataRecording_box QC"
                        "omboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"\n"
"\n"
"#Spikeling_rightMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 20px 0px;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Spikeling_rightMenuSubContainer QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Spikeling_rightMenuSubContainer_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Spikeling_rightMenuSubContainer_frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Spikeling_CenterMenuContainer{\n"
"	background-color: rgb(7, 54, 66)\n"
"}\n"
"#Spikeling_parameter_exit_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"#Imaging_rightMenuSubContainer{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Imaging_parameter_stackedWidget{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Imaging_rightMenuSubContainer QPushButton{\n"
"	text-a"
                        "lign: left;\n"
"	padding: 20px 0px;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Imaging_rightMenuSubContainer QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Imaging_rightMenuSubContainer_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Imaging_rightMenuSubContainer_frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Imaging_CenterMenuContainer{\n"
"	background-color: rgb(7, 54, 66)\n"
"}\n"
"#Imaging_parameter_exit_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"#NeuronGenerator_subframe1_middle_frame QLineEdit{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#NeuronGenerator_subframe2 QLineEdit{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#NeuronGenerator_subframe2 QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	b"
                        "order-radius: 10px;\n"
"	padding: 5px 5px;\n"
"}\n"
"#NeuronGenerator_subframe2 QComboBox{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 5px 5px;\n"
"	margin: 5px\n"
"}\n"
"#NeuronGenerator_subframe1_Izhik_frame QTextBrowser{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#DataAnalysis_groupBox{\n"
"	background-color: rgb(7,54,66);\n"
"    border: 2px solid rgb(147,161,161);\n"
"}\n"
"#DataAnalysis_groupBox QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"#DataAnalysis_groupBox QLineEdit{\n"
"    border: 2px solid rgb(147,161,161);\n"
"}\n"
"#DataAnalysis_groupBox Line{\n"
"    border: 1px solid rgb(147,161,161);\n"
"}\n"
"\n"
"#DataAnalysis_Display_frame QPushButton{\n"
"	background-color: rgb(7,54,66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
""
                        "	padding: 2px;\n"
"}\n"
"\n"
"\n"
"#page_401 QPushButton{\n"
"	background-color: rgb(7,54,66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"#StimulusGenerator_Container QComboBox{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 5px 5px;\n"
"	margin: 5px\n"
"}\n"
"#StimulusGenerator_Container QLineEdit{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.verticalLayout_75 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.TopMainFrame = QFrame(self.centralwidget)
        self.TopMainFrame.setObjectName(u"TopMainFrame")
        self.TopMainFrame.setFrameShape(QFrame.StyledPanel)
        self.TopMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.TopMainFrame)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.TopMainFrame)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.app_ID_frame = QFrame(self.header_widget)
        self.app_ID_frame.setObjectName(u"app_ID_frame")
        self.app_ID_frame.setFrameShape(QFrame.StyledPanel)
        self.app_ID_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.app_ID_frame)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.appTitle_pushButton = QPushButton(self.app_ID_frame)
        self.appTitle_pushButton.setObjectName(u"appTitle_pushButton")
        font = QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.appTitle_pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/resources/resources/Spiky_Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appTitle_pushButton.setIcon(icon)
        self.appTitle_pushButton.setIconSize(QSize(60, 32))
        self.appTitle_pushButton.setCheckable(False)

        self.horizontalLayout_78.addWidget(self.appTitle_pushButton, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.app_ID_frame, 0, Qt.AlignLeft)

        self.app_frame = QFrame(self.header_widget)
        self.app_frame.setObjectName(u"app_frame")
        self.app_frame.setFrameShape(QFrame.StyledPanel)
        self.app_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.app_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.reduce_pushButton = QPushButton(self.app_frame)
        self.reduce_pushButton.setObjectName(u"reduce_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/resources/resources/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reduce_pushButton.setIcon(icon1)
        self.reduce_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.reduce_pushButton)

        self.expand_pushButton = QPushButton(self.app_frame)
        self.expand_pushButton.setObjectName(u"expand_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_pushButton.setIcon(icon2)
        self.expand_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.expand_pushButton)

        self.exit_pushButton = QPushButton(self.app_frame)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/Exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_pushButton.setIcon(icon3)
        self.exit_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.exit_pushButton)


        self.horizontalLayout_2.addWidget(self.app_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_113.addWidget(self.header_widget)


        self.verticalLayout_75.addWidget(self.TopMainFrame)

        self.CenterMainFrame = QFrame(self.centralwidget)
        self.CenterMainFrame.setObjectName(u"CenterMainFrame")
        self.CenterMainFrame.setMinimumSize(QSize(50, 0))
        self.CenterMainFrame.setFrameShape(QFrame.StyledPanel)
        self.CenterMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.CenterMainFrame)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.CenterMainFrame)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 15)
        self.menu_frame = QFrame(self.leftMenuSubContainer)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setStyleSheet(u"")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_64.setSpacing(10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 5)
        self.menu_pushButton = QPushButton(self.menu_frame)
        self.menu_pushButton.setObjectName(u"menu_pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.menu_pushButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_pushButton.setIcon(icon4)
        self.menu_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_64.addWidget(self.menu_pushButton)


        self.verticalLayout_4.addWidget(self.menu_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.menus_frame = QFrame(self.leftMenuSubContainer)
        self.menus_frame.setObjectName(u"menus_frame")
        self.menus_frame.setStyleSheet(u"")
        self.menus_frame.setFrameShape(QFrame.StyledPanel)
        self.menus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.menus_frame)
        self.verticalLayout_37.setSpacing(10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.SpikelingMenu_pushButton = QPushButton(self.menus_frame)
        self.SpikelingMenu_pushButton.setObjectName(u"SpikelingMenu_pushButton")
        self.SpikelingMenu_pushButton.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/resources/resources/Neuron.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SpikelingMenu_pushButton.setIcon(icon5)
        self.SpikelingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.SpikelingMenu_pushButton)

        self.ImagingMenu_pushButton = QPushButton(self.menus_frame)
        self.ImagingMenu_pushButton.setObjectName(u"ImagingMenu_pushButton")
        self.ImagingMenu_pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/Imaging.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ImagingMenu_pushButton.setIcon(icon6)
        self.ImagingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.ImagingMenu_pushButton)

        self.NeuronGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.NeuronGeneratorMenu_pushButton.setObjectName(u"NeuronGeneratorMenu_pushButton")
        self.NeuronGeneratorMenu_pushButton.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/StimGen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NeuronGeneratorMenu_pushButton.setIcon(icon7)
        self.NeuronGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.NeuronGeneratorMenu_pushButton)

        self.StimuluGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.StimuluGeneratorMenu_pushButton.setObjectName(u"StimuluGeneratorMenu_pushButton")
        self.StimuluGeneratorMenu_pushButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/Stimulus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.StimuluGeneratorMenu_pushButton.setIcon(icon8)
        self.StimuluGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.StimuluGeneratorMenu_pushButton)

        self.ExercisesMenu_pushButton = QPushButton(self.menus_frame)
        self.ExercisesMenu_pushButton.setObjectName(u"ExercisesMenu_pushButton")
        self.ExercisesMenu_pushButton.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/resources/resources/Exercices.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ExercisesMenu_pushButton.setIcon(icon9)
        self.ExercisesMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.ExercisesMenu_pushButton)


        self.verticalLayout_4.addWidget(self.menus_frame)

        self.options_frame = QFrame(self.leftMenuSubContainer)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setStyleSheet(u"")
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.options_frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.SettingsMenu_pushButton = QPushButton(self.options_frame)
        self.SettingsMenu_pushButton.setObjectName(u"SettingsMenu_pushButton")
        self.SettingsMenu_pushButton.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/resources/resources/Tutorial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsMenu_pushButton.setIcon(icon10)
        self.SettingsMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.SettingsMenu_pushButton)

        self.AboutMenu_pushButton = QPushButton(self.options_frame)
        self.AboutMenu_pushButton.setObjectName(u"AboutMenu_pushButton")
        self.AboutMenu_pushButton.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/resources/resources/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AboutMenu_pushButton.setIcon(icon11)
        self.AboutMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AboutMenu_pushButton)

        self.HelpMenu_pushButton = QPushButton(self.options_frame)
        self.HelpMenu_pushButton.setObjectName(u"HelpMenu_pushButton")
        self.HelpMenu_pushButton.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpMenu_pushButton.setIcon(icon12)
        self.HelpMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.HelpMenu_pushButton)

        self.GitHubMenu_pushButton = QPushButton(self.options_frame)
        self.GitHubMenu_pushButton.setObjectName(u"GitHubMenu_pushButton")
        self.GitHubMenu_pushButton.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHubMenu_pushButton.setIcon(icon13)
        self.GitHubMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.GitHubMenu_pushButton)


        self.verticalLayout_4.addWidget(self.options_frame)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout_112.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.CenterMainFrame)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer_exit_frame = QFrame(self.centerMenuSubContainer)
        self.centerMenuSubContainer_exit_frame.setObjectName(u"centerMenuSubContainer_exit_frame")
        self.centerMenuSubContainer_exit_frame.setMinimumSize(QSize(0, 28))
        self.centerMenuSubContainer_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.centerMenuSubContainer_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.centerMenuSubContainer_exit_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer_exit_pushButton = QPushButton(self.centerMenuSubContainer_exit_frame)
        self.centerMenuSubContainer_exit_pushButton.setObjectName(u"centerMenuSubContainer_exit_pushButton")
        self.centerMenuSubContainer_exit_pushButton.setLayoutDirection(Qt.RightToLeft)
        icon14 = QIcon()
        icon14.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.centerMenuSubContainer_exit_pushButton.setIcon(icon14)
        self.centerMenuSubContainer_exit_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.centerMenuSubContainer_exit_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer_exit_frame, 0, Qt.AlignTop)

        self.centerMenuSubContainer_menu_stackedwidget = QStackedWidget(self.centerMenuSubContainer)
        self.centerMenuSubContainer_menu_stackedwidget.setObjectName(u"centerMenuSubContainer_menu_stackedwidget")
        self.centerMenuSubContainer_menu_stackedwidget.setMinimumSize(QSize(200, 0))
        self.centerMenuSubContainer_menu_stackedwidget.setStyleSheet(u"")
        self.Spikeling_SubMenu_page = QWidget()
        self.Spikeling_SubMenu_page.setObjectName(u"Spikeling_SubMenu_page")
        self.verticalLayout_8 = QVBoxLayout(self.Spikeling_SubMenu_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SubMenu_label_frame = QFrame(self.Spikeling_SubMenu_page)
        self.Spikeling_SubMenu_label_frame.setObjectName(u"Spikeling_SubMenu_label_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Spikeling_SubMenu_label_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_SubMenu_label_frame.setSizePolicy(sizePolicy1)
        self.Spikeling_SubMenu_label_frame.setMinimumSize(QSize(0, 25))
        self.Spikeling_SubMenu_label_frame.setMaximumSize(QSize(16777215, 25))
        self.Spikeling_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Spikeling_SubMenu_label_frame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_SubMenu_label = QLabel(self.Spikeling_SubMenu_label_frame)
        self.Spikeling_SubMenu_label.setObjectName(u"Spikeling_SubMenu_label")

        self.verticalLayout_18.addWidget(self.Spikeling_SubMenu_label)


        self.verticalLayout_8.addWidget(self.Spikeling_SubMenu_label_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Spikeling_SubMenu_button_frame = QFrame(self.Spikeling_SubMenu_page)
        self.Spikeling_SubMenu_button_frame.setObjectName(u"Spikeling_SubMenu_button_frame")
        self.Spikeling_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Spikeling_SubMenu_button_frame)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_5)

        self.Neuron_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.Neuron_pushButton.setObjectName(u"Neuron_pushButton")
        self.Neuron_pushButton.setFont(font1)
        self.Neuron_pushButton.setIcon(icon5)
        self.Neuron_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.Neuron_pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.NeuronTutorial_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronTutorial_pushButton.setObjectName(u"NeuronTutorial_pushButton")
        self.NeuronTutorial_pushButton.setFont(font1)
        self.NeuronTutorial_pushButton.setIcon(icon10)
        self.NeuronTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronTutorial_pushButton)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.NeuronDataAnalysis_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronDataAnalysis_pushButton.setObjectName(u"NeuronDataAnalysis_pushButton")
        self.NeuronDataAnalysis_pushButton.setFont(font1)
        icon15 = QIcon()
        icon15.addFile(u":/resources/resources/DataAnalysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NeuronDataAnalysis_pushButton.setIcon(icon15)
        self.NeuronDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronDataAnalysis_pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addWidget(self.Spikeling_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Spikeling_SubMenu_page)
        self.Imaging_SubMenu_page = QWidget()
        self.Imaging_SubMenu_page.setObjectName(u"Imaging_SubMenu_page")
        self.verticalLayout_10 = QVBoxLayout(self.Imaging_SubMenu_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SubMenu_label_frame = QFrame(self.Imaging_SubMenu_page)
        self.Imaging_SubMenu_label_frame.setObjectName(u"Imaging_SubMenu_label_frame")
        self.Imaging_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.Imaging_SubMenu_label_frame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SubMenu_label = QLabel(self.Imaging_SubMenu_label_frame)
        self.Imaging_SubMenu_label.setObjectName(u"Imaging_SubMenu_label")

        self.verticalLayout_20.addWidget(self.Imaging_SubMenu_label)


        self.verticalLayout_10.addWidget(self.Imaging_SubMenu_label_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Imaging_SubMenu_button_frame = QFrame(self.Imaging_SubMenu_page)
        self.Imaging_SubMenu_button_frame.setObjectName(u"Imaging_SubMenu_button_frame")
        self.Imaging_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.Imaging_SubMenu_button_frame)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_9)

        self.ImagingStimulation_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingStimulation_pushButton.setObjectName(u"ImagingStimulation_pushButton")
        self.ImagingStimulation_pushButton.setFont(font1)
        self.ImagingStimulation_pushButton.setIcon(icon6)
        self.ImagingStimulation_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingStimulation_pushButton)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_10)

        self.ImagingTutorial_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingTutorial_pushButton.setObjectName(u"ImagingTutorial_pushButton")
        self.ImagingTutorial_pushButton.setFont(font1)
        self.ImagingTutorial_pushButton.setIcon(icon10)
        self.ImagingTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingTutorial_pushButton)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_11)

        self.ImagingDataAnalysis_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingDataAnalysis_pushButton.setObjectName(u"ImagingDataAnalysis_pushButton")
        self.ImagingDataAnalysis_pushButton.setFont(font1)
        self.ImagingDataAnalysis_pushButton.setIcon(icon15)
        self.ImagingDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingDataAnalysis_pushButton)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_12)


        self.verticalLayout_10.addWidget(self.Imaging_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Imaging_SubMenu_page)
        self.NeuronGenerator_SubMenu_page = QWidget()
        self.NeuronGenerator_SubMenu_page.setObjectName(u"NeuronGenerator_SubMenu_page")
        self.verticalLayout_11 = QVBoxLayout(self.NeuronGenerator_SubMenu_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.NeuronGenerator_SubMenu_page)
        self.StimulusGenerator_SubMenu_page = QWidget()
        self.StimulusGenerator_SubMenu_page.setObjectName(u"StimulusGenerator_SubMenu_page")
        self.verticalLayout_15 = QVBoxLayout(self.StimulusGenerator_SubMenu_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.StimulusGenerator_SubMenu_page)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_15.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.StimulusGenerator_SubMenu_page)
        self.Exercises_SubMenu_page = QWidget()
        self.Exercises_SubMenu_page.setObjectName(u"Exercises_SubMenu_page")
        self.verticalLayout_16 = QVBoxLayout(self.Exercises_SubMenu_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Exercices_SubMenu_label_frame = QFrame(self.Exercises_SubMenu_page)
        self.Exercices_SubMenu_label_frame.setObjectName(u"Exercices_SubMenu_label_frame")
        self.Exercices_SubMenu_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercices_SubMenu_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.Exercices_SubMenu_label_frame)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.Exercices_SubMenu_label = QLabel(self.Exercices_SubMenu_label_frame)
        self.Exercices_SubMenu_label.setObjectName(u"Exercices_SubMenu_label")

        self.verticalLayout_60.addWidget(self.Exercices_SubMenu_label)


        self.verticalLayout_16.addWidget(self.Exercices_SubMenu_label_frame)

        self.Exercices_SubMenu_button_frame = QFrame(self.Exercises_SubMenu_page)
        self.Exercices_SubMenu_button_frame.setObjectName(u"Exercices_SubMenu_button_frame")
        self.Exercices_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercices_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.Exercices_SubMenu_button_frame)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_13)

        self.Exercice101_pushButton = QPushButton(self.Exercices_SubMenu_button_frame)
        self.Exercice101_pushButton.setObjectName(u"Exercice101_pushButton")
        font2 = QFont()
        font2.setPointSize(10)
        self.Exercice101_pushButton.setFont(font2)

        self.verticalLayout_61.addWidget(self.Exercice101_pushButton)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_15)

        self.Exercice102_pushButton = QPushButton(self.Exercices_SubMenu_button_frame)
        self.Exercice102_pushButton.setObjectName(u"Exercice102_pushButton")
        self.Exercice102_pushButton.setFont(font2)

        self.verticalLayout_61.addWidget(self.Exercice102_pushButton)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_14)


        self.verticalLayout_16.addWidget(self.Exercices_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Exercises_SubMenu_page)
        self.Settings_SubMenu_page = QWidget()
        self.Settings_SubMenu_page.setObjectName(u"Settings_SubMenu_page")
        self.verticalLayout_38 = QVBoxLayout(self.Settings_SubMenu_page)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.Settings_SubMenu_page)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_38.addWidget(self.label_11)

        self.label_3 = QLabel(self.Settings_SubMenu_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_38.addWidget(self.label_3)

        self.label_6 = QLabel(self.Settings_SubMenu_page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_38.addWidget(self.label_6)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Settings_SubMenu_page)
        self.About_SubMenu_page = QWidget()
        self.About_SubMenu_page.setObjectName(u"About_SubMenu_page")
        self.verticalLayout_50 = QVBoxLayout(self.About_SubMenu_page)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.About_SubMenu_page)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_50.addWidget(self.label_12)

        self.label_10 = QLabel(self.About_SubMenu_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.verticalLayout_50.addWidget(self.label_10)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.About_SubMenu_page)
        self.Help_SubMenu_page = QWidget()
        self.Help_SubMenu_page.setObjectName(u"Help_SubMenu_page")
        self.verticalLayout_51 = QVBoxLayout(self.Help_SubMenu_page)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.Help_SubMenu_page)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_51.addWidget(self.label_13)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Help_SubMenu_page)
        self.GitHub_SubMenu_page = QWidget()
        self.GitHub_SubMenu_page.setObjectName(u"GitHub_SubMenu_page")
        self.verticalLayout_52 = QVBoxLayout(self.GitHub_SubMenu_page)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.GitHub_SubMenu_page)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_52.addWidget(self.label_14)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.GitHub_SubMenu_page)

        self.verticalLayout_6.addWidget(self.centerMenuSubContainer_menu_stackedwidget)


        self.verticalLayout_7.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout_112.addWidget(self.centerMenuContainer)

        self.mainWindowContainer = QWidget(self.CenterMainFrame)
        self.mainWindowContainer.setObjectName(u"mainWindowContainer")
        self.mainWindowContainer.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.mainWindowContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainbodyContainer = QWidget(self.mainWindowContainer)
        self.mainbodyContainer.setObjectName(u"mainbodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainbodyContainer.sizePolicy().hasHeightForWidth())
        self.mainbodyContainer.setSizePolicy(sizePolicy2)
        self.mainbodyContainer.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.mainbodyContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainbody_stackedWidget = QStackedWidget(self.mainbodyContainer)
        self.mainbody_stackedWidget.setObjectName(u"mainbody_stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainbody_stackedWidget.sizePolicy().hasHeightForWidth())
        self.mainbody_stackedWidget.setSizePolicy(sizePolicy3)
        self.mainbody_stackedWidget.setMinimumSize(QSize(600, 600))
        self.mainbody_stackedWidget.setStyleSheet(u"")
        self.page_000 = QWidget()
        self.page_000.setObjectName(u"page_000")
        self.verticalLayout_30 = QVBoxLayout(self.page_000)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.mainbody_header_frame = QFrame(self.page_000)
        self.mainbody_header_frame.setObjectName(u"mainbody_header_frame")
        self.mainbody_header_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.mainbody_header_frame)
        self.horizontalLayout_115.setSpacing(0)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(10, 0, 10, 5)
        self.mainbody_header_text = QLabel(self.mainbody_header_frame)
        self.mainbody_header_text.setObjectName(u"mainbody_header_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainbody_header_text.sizePolicy().hasHeightForWidth())
        self.mainbody_header_text.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setBold(False)
        self.mainbody_header_text.setFont(font3)
        self.mainbody_header_text.setStyleSheet(u"")

        self.horizontalLayout_115.addWidget(self.mainbody_header_text)


        self.verticalLayout_30.addWidget(self.mainbody_header_frame)

        self.mainbody_content_frame = QFrame(self.page_000)
        self.mainbody_content_frame.setObjectName(u"mainbody_content_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainbody_content_frame.sizePolicy().hasHeightForWidth())
        self.mainbody_content_frame.setSizePolicy(sizePolicy5)
        self.mainbody_content_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.mainbody_content_frame)
        self.horizontalLayout_76.setSpacing(20)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(10, 0, 10, 0)
        self.mainbody_content_text = QLabel(self.mainbody_content_frame)
        self.mainbody_content_text.setObjectName(u"mainbody_content_text")
        sizePolicy5.setHeightForWidth(self.mainbody_content_text.sizePolicy().hasHeightForWidth())
        self.mainbody_content_text.setSizePolicy(sizePolicy5)
        self.mainbody_content_text.setWordWrap(True)

        self.horizontalLayout_76.addWidget(self.mainbody_content_text, 0, Qt.AlignVCenter)

        self.mainbody_content_SpikelingGif = QLabel(self.mainbody_content_frame)
        self.mainbody_content_SpikelingGif.setObjectName(u"mainbody_content_SpikelingGif")
        sizePolicy5.setHeightForWidth(self.mainbody_content_SpikelingGif.sizePolicy().hasHeightForWidth())
        self.mainbody_content_SpikelingGif.setSizePolicy(sizePolicy5)
        self.mainbody_content_SpikelingGif.setMinimumSize(QSize(0, 0))
        self.mainbody_content_SpikelingGif.setMaximumSize(QSize(16777215, 16777215))
        self.mainbody_content_SpikelingGif.setAutoFillBackground(False)
        self.mainbody_content_SpikelingGif.setPixmap(QPixmap(u":/resources2/resources/spike.gif"))
        self.mainbody_content_SpikelingGif.setScaledContents(True)

        self.horizontalLayout_76.addWidget(self.mainbody_content_SpikelingGif)


        self.verticalLayout_30.addWidget(self.mainbody_content_frame, 0, Qt.AlignVCenter)

        self.mainbody_footer_frame = QFrame(self.page_000)
        self.mainbody_footer_frame.setObjectName(u"mainbody_footer_frame")
        self.mainbody_footer_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.mainbody_footer_frame)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(10, 0, 10, 5)
        self.mainbody_footer_text = QLabel(self.mainbody_footer_frame)
        self.mainbody_footer_text.setObjectName(u"mainbody_footer_text")
        sizePolicy3.setHeightForWidth(self.mainbody_footer_text.sizePolicy().hasHeightForWidth())
        self.mainbody_footer_text.setSizePolicy(sizePolicy3)
        self.mainbody_footer_text.setMinimumSize(QSize(0, 100))
        self.mainbody_footer_text.setScaledContents(False)
        self.mainbody_footer_text.setWordWrap(True)

        self.horizontalLayout_114.addWidget(self.mainbody_footer_text)


        self.verticalLayout_30.addWidget(self.mainbody_footer_frame)

        self.mainbody_stackedWidget.addWidget(self.page_000)
        self.page_101 = QWidget()
        self.page_101.setObjectName(u"page_101")
        self.horizontalLayout_34 = QHBoxLayout(self.page_101)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_widget = QWidget(self.page_101)
        self.Spikeling_widget.setObjectName(u"Spikeling_widget")
        sizePolicy4.setHeightForWidth(self.Spikeling_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_33 = QHBoxLayout(self.Spikeling_widget)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_frame = QFrame(self.Spikeling_widget)
        self.Spikeling_frame.setObjectName(u"Spikeling_frame")
        self.Spikeling_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Spikeling_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_top_subframe1 = QFrame(self.Spikeling_frame)
        self.Spikeling_top_subframe1.setObjectName(u"Spikeling_top_subframe1")
        sizePolicy1.setHeightForWidth(self.Spikeling_top_subframe1.sizePolicy().hasHeightForWidth())
        self.Spikeling_top_subframe1.setSizePolicy(sizePolicy1)
        self.Spikeling_top_subframe1.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_top_subframe1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.Spikeling_top_subframe1)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 0, 5, 0)
        self.Spikeling_connection_frame = QFrame(self.Spikeling_top_subframe1)
        self.Spikeling_connection_frame.setObjectName(u"Spikeling_connection_frame")
        sizePolicy3.setHeightForWidth(self.Spikeling_connection_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_connection_frame.setSizePolicy(sizePolicy3)
        self.Spikeling_connection_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_connection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.Spikeling_connection_frame)
        self.horizontalLayout_59.setSpacing(20)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.Connection_frame = QFrame(self.Spikeling_connection_frame)
        self.Connection_frame.setObjectName(u"Connection_frame")
        self.Connection_frame.setFrameShape(QFrame.StyledPanel)
        self.Connection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.Connection_frame)
        self.horizontalLayout_117.setSpacing(10)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SelectPortLabel = QLabel(self.Connection_frame)
        self.Spikeling_SelectPortLabel.setObjectName(u"Spikeling_SelectPortLabel")
        self.Spikeling_SelectPortLabel.setFont(font1)

        self.horizontalLayout_117.addWidget(self.Spikeling_SelectPortLabel)

        self.Spikeling_SelectPortComboBox = QComboBox(self.Connection_frame)
        self.Spikeling_SelectPortComboBox.addItem("")
        self.Spikeling_SelectPortComboBox.setObjectName(u"Spikeling_SelectPortComboBox")

        self.horizontalLayout_117.addWidget(self.Spikeling_SelectPortComboBox)

        self.Spikeling_ConnectButton = QRadioButton(self.Connection_frame)
        self.Spikeling_ConnectButton.setObjectName(u"Spikeling_ConnectButton")
        self.Spikeling_ConnectButton.setEnabled(False)
        self.Spikeling_ConnectButton.setFont(font1)

        self.horizontalLayout_117.addWidget(self.Spikeling_ConnectButton)


        self.horizontalLayout_59.addWidget(self.Connection_frame, 0, Qt.AlignLeft)

        self.Spikeling_interaction_frame = QFrame(self.Spikeling_connection_frame)
        self.Spikeling_interaction_frame.setObjectName(u"Spikeling_interaction_frame")
        self.Spikeling_interaction_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_interaction_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_174 = QHBoxLayout(self.Spikeling_interaction_frame)
        self.horizontalLayout_174.setSpacing(5)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(0, 2, 0, 0)
        self.LED_frame = QFrame(self.Spikeling_interaction_frame)
        self.LED_frame.setObjectName(u"LED_frame")
        self.LED_frame.setFrameShape(QFrame.StyledPanel)
        self.LED_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.LED_frame)
        self.horizontalLayout_172.setSpacing(0)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.LED_pushButton = QPushButton(self.LED_frame)
        self.LED_pushButton.setObjectName(u"LED_pushButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.LED_pushButton.sizePolicy().hasHeightForWidth())
        self.LED_pushButton.setSizePolicy(sizePolicy6)
        self.LED_pushButton.setMinimumSize(QSize(100, 0))
        self.LED_pushButton.setLayoutDirection(Qt.RightToLeft)
        self.LED_pushButton.setStyleSheet(u"background-color: rgb(7,54,66);\n"
"padding: 2px 5px;\n"
"border-radius:10px;")
        icon16 = QIcon()
        icon16.addFile(u":/resources/resources/LEDON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LED_pushButton.setIcon(icon16)
        self.LED_pushButton.setIconSize(QSize(20, 20))
        self.LED_pushButton.setCheckable(True)

        self.horizontalLayout_172.addWidget(self.LED_pushButton, 0, Qt.AlignLeft)


        self.horizontalLayout_174.addWidget(self.LED_frame)

        self.Sound_frame = QFrame(self.Spikeling_interaction_frame)
        self.Sound_frame.setObjectName(u"Sound_frame")
        self.Sound_frame.setFrameShape(QFrame.StyledPanel)
        self.Sound_frame.setFrameShadow(QFrame.Raised)
        self.Sound_Buzzer_Layout = QHBoxLayout(self.Sound_frame)
        self.Sound_Buzzer_Layout.setSpacing(0)
        self.Sound_Buzzer_Layout.setObjectName(u"Sound_Buzzer_Layout")
        self.Sound_Buzzer_Layout.setContentsMargins(0, 0, 0, 0)
        self.Sound_pushButton = QPushButton(self.Sound_frame)
        self.Sound_pushButton.setObjectName(u"Sound_pushButton")
        sizePolicy6.setHeightForWidth(self.Sound_pushButton.sizePolicy().hasHeightForWidth())
        self.Sound_pushButton.setSizePolicy(sizePolicy6)
        self.Sound_pushButton.setMinimumSize(QSize(100, 0))
        self.Sound_pushButton.setLayoutDirection(Qt.RightToLeft)
        self.Sound_pushButton.setStyleSheet(u"background-color: rgb(7,54,66);\n"
"padding: 2px 5px;\n"
"border-radius:10px;")
        icon17 = QIcon()
        icon17.addFile(u":/resources/resources/SoundON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Sound_pushButton.setIcon(icon17)
        self.Sound_pushButton.setIconSize(QSize(20, 20))
        self.Sound_pushButton.setCheckable(True)

        self.Sound_Buzzer_Layout.addWidget(self.Sound_pushButton)


        self.horizontalLayout_174.addWidget(self.Sound_frame)


        self.horizontalLayout_59.addWidget(self.Spikeling_interaction_frame, 0, Qt.AlignRight)


        self.verticalLayout_29.addWidget(self.Spikeling_connection_frame, 0, Qt.AlignTop)

        self.Spikeling_top_subframe2 = QFrame(self.Spikeling_top_subframe1)
        self.Spikeling_top_subframe2.setObjectName(u"Spikeling_top_subframe2")
        self.Spikeling_top_subframe2.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_top_subframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.Spikeling_top_subframe2)
        self.horizontalLayout_58.setSpacing(5)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_NeuronModeLabel = QLabel(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronModeLabel.setObjectName(u"Spikeling_NeuronModeLabel")
        self.Spikeling_NeuronModeLabel.setStyleSheet(u"")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronModeLabel)

        self.Spikeling_NeuronModeComboBox = QComboBox(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.addItem("")
        self.Spikeling_NeuronModeComboBox.setObjectName(u"Spikeling_NeuronModeComboBox")
        self.Spikeling_NeuronModeComboBox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronModeComboBox)

        self.Spikeling_NeuronBrowsePushButton = QPushButton(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronBrowsePushButton.setObjectName(u"Spikeling_NeuronBrowsePushButton")
        self.Spikeling_NeuronBrowsePushButton.setStyleSheet(u"background-color: rgb(7,54,66);\n"
"padding: 2px 10px;\n"
"border-radius:10px;")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronBrowsePushButton)

        self.Spikeling_NeuronMode_pushButton = QPushButton(self.Spikeling_top_subframe2)
        self.Spikeling_NeuronMode_pushButton.setObjectName(u"Spikeling_NeuronMode_pushButton")
        self.Spikeling_NeuronMode_pushButton.setStyleSheet(u"background-color: rgb(7,54,66);\n"
"padding: 2px 10px;\n"
"border-radius:10px;")

        self.horizontalLayout_58.addWidget(self.Spikeling_NeuronMode_pushButton)


        self.verticalLayout_29.addWidget(self.Spikeling_top_subframe2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.Spikeling_top_subframe1)

        self.Spikeling_Oscilloscope_frame = QFrame(self.Spikeling_frame)
        self.Spikeling_Oscilloscope_frame.setObjectName(u"Spikeling_Oscilloscope_frame")
        self.Spikeling_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.Spikeling_Oscilloscope_frame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Oscilloscope_widget = PlotWidget(self.Spikeling_Oscilloscope_frame)
        self.Spikeling_Oscilloscope_widget.setObjectName(u"Spikeling_Oscilloscope_widget")
        sizePolicy5.setHeightForWidth(self.Spikeling_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_Oscilloscope_widget.setSizePolicy(sizePolicy5)
        self.Spikeling_Oscilloscope_widget.setAutoFillBackground(False)
        self.Spikeling_Oscilloscope_widget.setStyleSheet(u"")
        self.horizontalLayout_183 = QHBoxLayout(self.Spikeling_Oscilloscope_widget)
        self.horizontalLayout_183.setSpacing(0)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(5, 5, 5, 0)
        self.Spikeling_Oscilloscope_Traces_frame = QFrame(self.Spikeling_Oscilloscope_widget)
        self.Spikeling_Oscilloscope_Traces_frame.setObjectName(u"Spikeling_Oscilloscope_Traces_frame")
        self.Spikeling_Oscilloscope_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_Traces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.Spikeling_Oscilloscope_Traces_frame)
        self.horizontalLayout_182.setSpacing(50)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Oscilloscope_FirstTraces_frame = QFrame(self.Spikeling_Oscilloscope_Traces_frame)
        self.Spikeling_Oscilloscope_FirstTraces_frame.setObjectName(u"Spikeling_Oscilloscope_FirstTraces_frame")
        self.Spikeling_Oscilloscope_FirstTraces_frame.setMaximumSize(QSize(250, 16777215))
        self.Spikeling_Oscilloscope_FirstTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_FirstTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_179 = QHBoxLayout(self.Spikeling_Oscilloscope_FirstTraces_frame)
        self.horizontalLayout_179.setSpacing(5)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_FirstTraces_frame)
        self.Spikeling_VmCheckbox.setObjectName(u"Spikeling_VmCheckbox")
        self.Spikeling_VmCheckbox.setEnabled(True)
        self.Spikeling_VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_VmCheckbox.setStyleSheet(u"color: rgb(220, 50, 47);")
        self.Spikeling_VmCheckbox.setChecked(True)

        self.horizontalLayout_179.addWidget(self.Spikeling_VmCheckbox, 0, Qt.AlignTop)

        self.Spikeling_InputCurrentCheckbox = QCheckBox(self.Spikeling_Oscilloscope_FirstTraces_frame)
        self.Spikeling_InputCurrentCheckbox.setObjectName(u"Spikeling_InputCurrentCheckbox")
        self.Spikeling_InputCurrentCheckbox.setEnabled(True)
        self.Spikeling_InputCurrentCheckbox.setAutoFillBackground(False)
        self.Spikeling_InputCurrentCheckbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.Spikeling_InputCurrentCheckbox.setChecked(True)

        self.horizontalLayout_179.addWidget(self.Spikeling_InputCurrentCheckbox, 0, Qt.AlignTop)

        self.Spikeling_StimulusCheckbox = QCheckBox(self.Spikeling_Oscilloscope_FirstTraces_frame)
        self.Spikeling_StimulusCheckbox.setObjectName(u"Spikeling_StimulusCheckbox")
        self.Spikeling_StimulusCheckbox.setEnabled(True)
        self.Spikeling_StimulusCheckbox.setAutoFillBackground(False)
        self.Spikeling_StimulusCheckbox.setStyleSheet(u"color: rgb(38, 139, 210);")
        self.Spikeling_StimulusCheckbox.setChecked(True)

        self.horizontalLayout_179.addWidget(self.Spikeling_StimulusCheckbox, 0, Qt.AlignTop)


        self.horizontalLayout_182.addWidget(self.Spikeling_Oscilloscope_FirstTraces_frame)

        self.Spikeling_Oscilloscope_SecondTraces_frame = QFrame(self.Spikeling_Oscilloscope_Traces_frame)
        self.Spikeling_Oscilloscope_SecondTraces_frame.setObjectName(u"Spikeling_Oscilloscope_SecondTraces_frame")
        self.Spikeling_Oscilloscope_SecondTraces_frame.setMaximumSize(QSize(250, 16777215))
        self.Spikeling_Oscilloscope_SecondTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_SecondTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_180 = QHBoxLayout(self.Spikeling_Oscilloscope_SecondTraces_frame)
        self.horizontalLayout_180.setSpacing(0)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Syn1VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_SecondTraces_frame)
        self.Spikeling_Syn1VmCheckbox.setObjectName(u"Spikeling_Syn1VmCheckbox")
        self.Spikeling_Syn1VmCheckbox.setEnabled(True)
        self.Spikeling_Syn1VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn1VmCheckbox.setStyleSheet(u"color: rgb(203, 75, 22);")
        self.Spikeling_Syn1VmCheckbox.setChecked(False)

        self.horizontalLayout_180.addWidget(self.Spikeling_Syn1VmCheckbox, 0, Qt.AlignTop)

        self.Spikeling_Syn1InputCheckbox = QCheckBox(self.Spikeling_Oscilloscope_SecondTraces_frame)
        self.Spikeling_Syn1InputCheckbox.setObjectName(u"Spikeling_Syn1InputCheckbox")
        self.Spikeling_Syn1InputCheckbox.setEnabled(True)
        self.Spikeling_Syn1InputCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn1InputCheckbox.setStyleSheet(u"color: rgb(42, 161, 152);")
        self.Spikeling_Syn1InputCheckbox.setChecked(False)

        self.horizontalLayout_180.addWidget(self.Spikeling_Syn1InputCheckbox, 0, Qt.AlignTop)


        self.horizontalLayout_182.addWidget(self.Spikeling_Oscilloscope_SecondTraces_frame)

        self.Spikeling_Oscilloscope_ThirdTraces_frame = QFrame(self.Spikeling_Oscilloscope_Traces_frame)
        self.Spikeling_Oscilloscope_ThirdTraces_frame.setObjectName(u"Spikeling_Oscilloscope_ThirdTraces_frame")
        self.Spikeling_Oscilloscope_ThirdTraces_frame.setMaximumSize(QSize(250, 16777215))
        self.Spikeling_Oscilloscope_ThirdTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Oscilloscope_ThirdTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.Spikeling_Oscilloscope_ThirdTraces_frame)
        self.horizontalLayout_181.setSpacing(0)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Syn2VmCheckbox = QCheckBox(self.Spikeling_Oscilloscope_ThirdTraces_frame)
        self.Spikeling_Syn2VmCheckbox.setObjectName(u"Spikeling_Syn2VmCheckbox")
        self.Spikeling_Syn2VmCheckbox.setEnabled(True)
        self.Spikeling_Syn2VmCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn2VmCheckbox.setStyleSheet(u"color: rgb(181, 137, 0);")
        self.Spikeling_Syn2VmCheckbox.setChecked(False)

        self.horizontalLayout_181.addWidget(self.Spikeling_Syn2VmCheckbox, 0, Qt.AlignTop)

        self.Spikeling_Syn2InputCheckbox = QCheckBox(self.Spikeling_Oscilloscope_ThirdTraces_frame)
        self.Spikeling_Syn2InputCheckbox.setObjectName(u"Spikeling_Syn2InputCheckbox")
        self.Spikeling_Syn2InputCheckbox.setEnabled(True)
        self.Spikeling_Syn2InputCheckbox.setAutoFillBackground(False)
        self.Spikeling_Syn2InputCheckbox.setStyleSheet(u"color: rgb(211, 54, 130);")
        self.Spikeling_Syn2InputCheckbox.setChecked(False)

        self.horizontalLayout_181.addWidget(self.Spikeling_Syn2InputCheckbox, 0, Qt.AlignTop)


        self.horizontalLayout_182.addWidget(self.Spikeling_Oscilloscope_ThirdTraces_frame)


        self.horizontalLayout_183.addWidget(self.Spikeling_Oscilloscope_Traces_frame)


        self.horizontalLayout_50.addWidget(self.Spikeling_Oscilloscope_widget)


        self.verticalLayout_26.addWidget(self.Spikeling_Oscilloscope_frame)

        self.Spikeling_bottom_subframe = QFrame(self.Spikeling_frame)
        self.Spikeling_bottom_subframe.setObjectName(u"Spikeling_bottom_subframe")
        self.Spikeling_bottom_subframe.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_bottom_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.Spikeling_bottom_subframe)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_box = QGroupBox(self.Spikeling_bottom_subframe)
        self.Spikeling_DataRecording_box.setObjectName(u"Spikeling_DataRecording_box")
        sizePolicy1.setHeightForWidth(self.Spikeling_DataRecording_box.sizePolicy().hasHeightForWidth())
        self.Spikeling_DataRecording_box.setSizePolicy(sizePolicy1)
        self.Spikeling_DataRecording_box.setMinimumSize(QSize(0, 100))
        self.Spikeling_DataRecording_box.setMaximumSize(QSize(16777215, 100))
        self.Spikeling_DataRecording_box.setStyleSheet(u"")
        self.horizontalLayout_52 = QHBoxLayout(self.Spikeling_DataRecording_box)
        self.horizontalLayout_52.setSpacing(20)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.Spikeling_DataRecording_left_frame = QFrame(self.Spikeling_DataRecording_box)
        self.Spikeling_DataRecording_left_frame.setObjectName(u"Spikeling_DataRecording_left_frame")
        self.Spikeling_DataRecording_left_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.Spikeling_DataRecording_left_frame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_recordingMode_frame = QFrame(self.Spikeling_DataRecording_left_frame)
        self.Spikeling_DataRecording_recordingMode_frame.setObjectName(u"Spikeling_DataRecording_recordingMode_frame")
        self.Spikeling_DataRecording_recordingMode_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_recordingMode_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.Spikeling_DataRecording_recordingMode_frame)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_ComboBox = QComboBox(self.Spikeling_DataRecording_recordingMode_frame)
        self.Spikeling_DataRecording_ComboBox.addItem("")
        self.Spikeling_DataRecording_ComboBox.addItem("")
        self.Spikeling_DataRecording_ComboBox.setObjectName(u"Spikeling_DataRecording_ComboBox")

        self.horizontalLayout_54.addWidget(self.Spikeling_DataRecording_ComboBox)


        self.verticalLayout_27.addWidget(self.Spikeling_DataRecording_recordingMode_frame)

        self.Spikeling_DataRecording_Loops_frame = QFrame(self.Spikeling_DataRecording_left_frame)
        self.Spikeling_DataRecording_Loops_frame.setObjectName(u"Spikeling_DataRecording_Loops_frame")
        self.Spikeling_DataRecording_Loops_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_Loops_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.Spikeling_DataRecording_Loops_frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_Loop_frame = QFrame(self.Spikeling_DataRecording_Loops_frame)
        self.Spikeling_DataRecording_Loop_frame.setObjectName(u"Spikeling_DataRecording_Loop_frame")
        self.Spikeling_DataRecording_Loop_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_Loop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.Spikeling_DataRecording_Loop_frame)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_NumberOfLoops_abel = QLabel(self.Spikeling_DataRecording_Loop_frame)
        self.Spikeling_DataRecording_NumberOfLoops_abel.setObjectName(u"Spikeling_DataRecording_NumberOfLoops_abel")

        self.horizontalLayout_55.addWidget(self.Spikeling_DataRecording_NumberOfLoops_abel)


        self.horizontalLayout_53.addWidget(self.Spikeling_DataRecording_Loop_frame, 0, Qt.AlignLeft)

        self.Spikeling_DataRecording_numberofloop_frame = QFrame(self.Spikeling_DataRecording_Loops_frame)
        self.Spikeling_DataRecording_numberofloop_frame.setObjectName(u"Spikeling_DataRecording_numberofloop_frame")
        self.Spikeling_DataRecording_numberofloop_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_numberofloop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.Spikeling_DataRecording_numberofloop_frame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_NumberOfLoops_value = QLineEdit(self.Spikeling_DataRecording_numberofloop_frame)
        self.Spikeling_DataRecording_NumberOfLoops_value.setObjectName(u"Spikeling_DataRecording_NumberOfLoops_value")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.Spikeling_DataRecording_NumberOfLoops_value.setFont(font4)
        self.Spikeling_DataRecording_NumberOfLoops_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.Spikeling_DataRecording_NumberOfLoops_value)


        self.horizontalLayout_53.addWidget(self.Spikeling_DataRecording_numberofloop_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.Spikeling_DataRecording_Loops_frame)


        self.horizontalLayout_52.addWidget(self.Spikeling_DataRecording_left_frame)

        self.Spikeling_DataRecording_right_frame = QFrame(self.Spikeling_DataRecording_box)
        self.Spikeling_DataRecording_right_frame.setObjectName(u"Spikeling_DataRecording_right_frame")
        self.Spikeling_DataRecording_right_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.Spikeling_DataRecording_right_frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_directory_frame = QFrame(self.Spikeling_DataRecording_right_frame)
        self.Spikeling_DataRecording_directory_frame.setObjectName(u"Spikeling_DataRecording_directory_frame")
        self.Spikeling_DataRecording_directory_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_directory_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.Spikeling_DataRecording_directory_frame)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_DataRecording_SelectRecordFolder_label = QLabel(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_SelectRecordFolder_label.setObjectName(u"Spikeling_DataRecording_SelectRecordFolder_label")

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_SelectRecordFolder_label)

        self.Spikeling_DataRecording_RecordFolder_value = QLineEdit(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_RecordFolder_value.setObjectName(u"Spikeling_DataRecording_RecordFolder_value")
        self.Spikeling_DataRecording_RecordFolder_value.setEnabled(False)

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_RecordFolder_value)

        self.Spikeling_DataRecording_RecordFolderDir_pushButton = QPushButton(self.Spikeling_DataRecording_directory_frame)
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setObjectName(u"Spikeling_DataRecording_RecordFolderDir_pushButton")
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setFont(font4)

        self.horizontalLayout_56.addWidget(self.Spikeling_DataRecording_RecordFolderDir_pushButton)


        self.verticalLayout_28.addWidget(self.Spikeling_DataRecording_directory_frame)

        self.Spikeling_DataRecording_record_frame = QFrame(self.Spikeling_DataRecording_right_frame)
        self.Spikeling_DataRecording_record_frame.setObjectName(u"Spikeling_DataRecording_record_frame")
        self.Spikeling_DataRecording_record_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_DataRecording_record_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.Spikeling_DataRecording_record_frame)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_SelectedFolderLabel = QLabel(self.Spikeling_DataRecording_record_frame)
        self.Spikeling_SelectedFolderLabel.setObjectName(u"Spikeling_SelectedFolderLabel")
        sizePolicy4.setHeightForWidth(self.Spikeling_SelectedFolderLabel.sizePolicy().hasHeightForWidth())
        self.Spikeling_SelectedFolderLabel.setSizePolicy(sizePolicy4)
        self.Spikeling_SelectedFolderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.Spikeling_SelectedFolderLabel)

        self.Spikeling_DataRecording_Record_pushButton = QPushButton(self.Spikeling_DataRecording_record_frame)
        self.Spikeling_DataRecording_Record_pushButton.setObjectName(u"Spikeling_DataRecording_Record_pushButton")
        sizePolicy6.setHeightForWidth(self.Spikeling_DataRecording_Record_pushButton.sizePolicy().hasHeightForWidth())
        self.Spikeling_DataRecording_Record_pushButton.setSizePolicy(sizePolicy6)
        self.Spikeling_DataRecording_Record_pushButton.setMinimumSize(QSize(150, 0))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.Spikeling_DataRecording_Record_pushButton.setFont(font5)
        self.Spikeling_DataRecording_Record_pushButton.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"background-color: rgb(220, 50, 47);")

        self.horizontalLayout_57.addWidget(self.Spikeling_DataRecording_Record_pushButton)


        self.verticalLayout_28.addWidget(self.Spikeling_DataRecording_record_frame)


        self.horizontalLayout_52.addWidget(self.Spikeling_DataRecording_right_frame)


        self.horizontalLayout_51.addWidget(self.Spikeling_DataRecording_box)


        self.verticalLayout_26.addWidget(self.Spikeling_bottom_subframe)


        self.horizontalLayout_33.addWidget(self.Spikeling_frame)


        self.horizontalLayout_34.addWidget(self.Spikeling_widget)

        self.line_41 = QFrame(self.page_101)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setAutoFillBackground(False)
        self.line_41.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_41.setFrameShape(QFrame.VLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_34.addWidget(self.line_41)

        self.Spikeling_CenterMenuContainer = QWidget(self.page_101)
        self.Spikeling_CenterMenuContainer.setObjectName(u"Spikeling_CenterMenuContainer")
        self.Spikeling_CenterMenuContainer.setMinimumSize(QSize(0, 0))
        self.Spikeling_CenterMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_54 = QVBoxLayout(self.Spikeling_CenterMenuContainer)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_parameter_exit_frame = QFrame(self.Spikeling_CenterMenuContainer)
        self.Spikeling_parameter_exit_frame.setObjectName(u"Spikeling_parameter_exit_frame")
        self.Spikeling_parameter_exit_frame.setMinimumSize(QSize(200, 0))
        self.Spikeling_parameter_exit_frame.setMaximumSize(QSize(200, 16777215))
        self.Spikeling_parameter_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_parameter_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.Spikeling_parameter_exit_frame)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_parameter_exit_pushButton = QPushButton(self.Spikeling_parameter_exit_frame)
        self.Spikeling_parameter_exit_pushButton.setObjectName(u"Spikeling_parameter_exit_pushButton")
        icon18 = QIcon()
        icon18.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spikeling_parameter_exit_pushButton.setIcon(icon18)
        self.Spikeling_parameter_exit_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_86.addWidget(self.Spikeling_parameter_exit_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_54.addWidget(self.Spikeling_parameter_exit_frame)

        self.Spikeling_parameter_stackedwidget = QStackedWidget(self.Spikeling_CenterMenuContainer)
        self.Spikeling_parameter_stackedwidget.setObjectName(u"Spikeling_parameter_stackedwidget")
        self.Spikeling_parameter_stackedwidget.setMinimumSize(QSize(200, 0))
        self.Spikeling_parameter_stackedwidget.setMaximumSize(QSize(200, 16777215))
        self.StimulusParameter_page = QWidget()
        self.StimulusParameter_page.setObjectName(u"StimulusParameter_page")
        self.StimulusParameter_page.setMinimumSize(QSize(200, 0))
        self.StimulusParameter_page.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_58 = QVBoxLayout(self.StimulusParameter_page)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Stimulus_label_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_Stimulus_label_frame.setObjectName(u"Spikeling_Stimulus_label_frame")
        self.Spikeling_Stimulus_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Stimulus_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.Spikeling_Stimulus_label_frame)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.StimulusLabel = QLabel(self.Spikeling_Stimulus_label_frame)
        self.StimulusLabel.setObjectName(u"StimulusLabel")
        self.StimulusLabel.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_83.addWidget(self.StimulusLabel, 0, Qt.AlignTop)


        self.verticalLayout_58.addWidget(self.Spikeling_Stimulus_label_frame)

        self.Spikeling_StimFre_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_StimFre_frame.setObjectName(u"Spikeling_StimFre_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_StimFre_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_StimFre_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Spikeling_StimFre_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 5, 5)
        self.Spikeling_StimFre_Title_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_Title_frame.setObjectName(u"Spikeling_StimFre_Title_frame")
        self.Spikeling_StimFre_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.Spikeling_StimFre_Title_frame)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_StimFre_toggle_frame = QFrame(self.Spikeling_StimFre_Title_frame)
        self.Spikeling_StimFre_toggle_frame.setObjectName(u"Spikeling_StimFre_toggle_frame")
        sizePolicy3.setHeightForWidth(self.Spikeling_StimFre_toggle_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_toggle_frame.setSizePolicy(sizePolicy3)
        self.Spikeling_StimFre_toggle_frame.setMaximumSize(QSize(45, 16777215))
        self.Spikeling_StimFre_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_StimFre_toggle_layout = QHBoxLayout(self.Spikeling_StimFre_toggle_frame)
        self.Spikeling_StimFre_toggle_layout.setSpacing(0)
        self.Spikeling_StimFre_toggle_layout.setObjectName(u"Spikeling_StimFre_toggle_layout")
        self.Spikeling_StimFre_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_36.addWidget(self.Spikeling_StimFre_toggle_frame)

        self.Spikeling_StimFre_Label_frame = QFrame(self.Spikeling_StimFre_Title_frame)
        self.Spikeling_StimFre_Label_frame.setObjectName(u"Spikeling_StimFre_Label_frame")
        self.Spikeling_StimFre_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_Label_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_StimFre_Layout = QHBoxLayout(self.Spikeling_StimFre_Label_frame)
        self.Spikeling_StimFre_Layout.setSpacing(0)
        self.Spikeling_StimFre_Layout.setObjectName(u"Spikeling_StimFre_Layout")
        self.Spikeling_StimFre_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_Label = QLabel(self.Spikeling_StimFre_Label_frame)
        self.Spikeling_StimFre_Label.setObjectName(u"Spikeling_StimFre_Label")

        self.Spikeling_StimFre_Layout.addWidget(self.Spikeling_StimFre_Label, 0, Qt.AlignLeft)


        self.horizontalLayout_36.addWidget(self.Spikeling_StimFre_Label_frame, 0, Qt.AlignLeft)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_Title_frame)

        self.Spikeling_StimFre_readings_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_readings_frame.setObjectName(u"Spikeling_StimFre_readings_frame")
        self.Spikeling_StimFre_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.Spikeling_StimFre_readings_frame)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_readings = QLabel(self.Spikeling_StimFre_readings_frame)
        self.Spikeling_StimFre_readings.setObjectName(u"Spikeling_StimFre_readings")
        self.Spikeling_StimFre_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.Spikeling_StimFre_readings)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_readings_frame)

        self.Spikeling_StimFre_slider_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_slider_frame.setObjectName(u"Spikeling_StimFre_slider_frame")
        self.Spikeling_StimFre_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.Spikeling_StimFre_slider_frame)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_slider = QSlider(self.Spikeling_StimFre_slider_frame)
        self.Spikeling_StimFre_slider.setObjectName(u"Spikeling_StimFre_slider")
        self.Spikeling_StimFre_slider.setEnabled(False)
        self.Spikeling_StimFre_slider.setStyleSheet(u"")
        self.Spikeling_StimFre_slider.setMinimum(-100)
        self.Spikeling_StimFre_slider.setMaximum(100)
        self.Spikeling_StimFre_slider.setSingleStep(1)
        self.Spikeling_StimFre_slider.setPageStep(10)
        self.Spikeling_StimFre_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_StimFre_slider.setInvertedAppearance(False)
        self.Spikeling_StimFre_slider.setInvertedControls(False)
        self.Spikeling_StimFre_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_StimFre_slider.setTickInterval(20)

        self.horizontalLayout_40.addWidget(self.Spikeling_StimFre_slider)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_slider_frame)

        self.Spikeling_StimFre_values_frames = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_values_frames.setObjectName(u"Spikeling_StimFre_values_frames")
        self.Spikeling_StimFre_values_frames.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_values_frames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.Spikeling_StimFre_values_frames)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_values_min = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_min.setObjectName(u"Spikeling_StimFre_values_min")

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_min)

        self.Spikeling_StimFre_values_0 = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_0.setObjectName(u"Spikeling_StimFre_values_0")
        self.Spikeling_StimFre_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_0)

        self.Spikeling_StimFre_values_max = QLabel(self.Spikeling_StimFre_values_frames)
        self.Spikeling_StimFre_values_max.setObjectName(u"Spikeling_StimFre_values_max")
        self.Spikeling_StimFre_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_77.addWidget(self.Spikeling_StimFre_values_max)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_values_frames, 0, Qt.AlignTop)

        self.Spikeling_StimFre_image_frame = QFrame(self.Spikeling_StimFre_frame)
        self.Spikeling_StimFre_image_frame.setObjectName(u"Spikeling_StimFre_image_frame")
        self.Spikeling_StimFre_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimFre_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.Spikeling_StimFre_image_frame)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimFre_image = QLabel(self.Spikeling_StimFre_image_frame)
        self.Spikeling_StimFre_image.setObjectName(u"Spikeling_StimFre_image")
        sizePolicy.setHeightForWidth(self.Spikeling_StimFre_image.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_image.setSizePolicy(sizePolicy)
        self.Spikeling_StimFre_image.setMinimumSize(QSize(0, 20))
        self.Spikeling_StimFre_image.setMaximumSize(QSize(16777215, 20))
        self.Spikeling_StimFre_image.setPixmap(QPixmap(u":/resources/resources/StimFrequency.png"))
        self.Spikeling_StimFre_image.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.Spikeling_StimFre_image)


        self.verticalLayout_22.addWidget(self.Spikeling_StimFre_image_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_StimFre_frame)

        self.Spikeling_parameter_top_line = QFrame(self.StimulusParameter_page)
        self.Spikeling_parameter_top_line.setObjectName(u"Spikeling_parameter_top_line")
        self.Spikeling_parameter_top_line.setAutoFillBackground(False)
        self.Spikeling_parameter_top_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_parameter_top_line.setFrameShape(QFrame.HLine)
        self.Spikeling_parameter_top_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_top_line)

        self.Spikeling_StimStr_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_StimStr_frame.setObjectName(u"Spikeling_StimStr_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_StimStr_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_StimStr_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Spikeling_StimStr_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.Spikeling_StimStr_Title_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_Title_frame.setObjectName(u"Spikeling_StimStr_Title_frame")
        self.Spikeling_StimStr_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.Spikeling_StimStr_Title_frame)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_StimStr_toggle_frame = QFrame(self.Spikeling_StimStr_Title_frame)
        self.Spikeling_StimStr_toggle_frame.setObjectName(u"Spikeling_StimStr_toggle_frame")
        self.Spikeling_StimStr_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_StimStr_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_StimStr_toggle_layout = QHBoxLayout(self.Spikeling_StimStr_toggle_frame)
        self.Spikeling_StimStr_toggle_layout.setSpacing(0)
        self.Spikeling_StimStr_toggle_layout.setObjectName(u"Spikeling_StimStr_toggle_layout")
        self.Spikeling_StimStr_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_37.addWidget(self.Spikeling_StimStr_toggle_frame)

        self.Spikeling_StimStr_Label_frame = QFrame(self.Spikeling_StimStr_Title_frame)
        self.Spikeling_StimStr_Label_frame.setObjectName(u"Spikeling_StimStr_Label_frame")
        self.Spikeling_StimStr_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.Spikeling_StimStr_Label_frame)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_Label = QLabel(self.Spikeling_StimStr_Label_frame)
        self.Spikeling_StimStr_Label.setObjectName(u"Spikeling_StimStr_Label")

        self.horizontalLayout_38.addWidget(self.Spikeling_StimStr_Label)


        self.horizontalLayout_37.addWidget(self.Spikeling_StimStr_Label_frame)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_Title_frame)

        self.Spikeling_StimStr_readings_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_readings_frame.setObjectName(u"Spikeling_StimStr_readings_frame")
        self.Spikeling_StimStr_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_readings_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_StimStr_Layout = QHBoxLayout(self.Spikeling_StimStr_readings_frame)
        self.Spikeling_StimStr_Layout.setSpacing(0)
        self.Spikeling_StimStr_Layout.setObjectName(u"Spikeling_StimStr_Layout")
        self.Spikeling_StimStr_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_readings = QLabel(self.Spikeling_StimStr_readings_frame)
        self.Spikeling_StimStr_readings.setObjectName(u"Spikeling_StimStr_readings")
        self.Spikeling_StimStr_readings.setAlignment(Qt.AlignCenter)

        self.Spikeling_StimStr_Layout.addWidget(self.Spikeling_StimStr_readings)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_readings_frame)

        self.Spikeling_StimStr_Slider_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_Slider_frame.setObjectName(u"Spikeling_StimStr_Slider_frame")
        self.Spikeling_StimStr_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.Spikeling_StimStr_Slider_frame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStrSlider = QSlider(self.Spikeling_StimStr_Slider_frame)
        self.Spikeling_StimStrSlider.setObjectName(u"Spikeling_StimStrSlider")
        self.Spikeling_StimStrSlider.setEnabled(False)
        self.Spikeling_StimStrSlider.setMinimum(-100)
        self.Spikeling_StimStrSlider.setMaximum(100)
        self.Spikeling_StimStrSlider.setOrientation(Qt.Horizontal)
        self.Spikeling_StimStrSlider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_StimStrSlider.setTickInterval(20)

        self.horizontalLayout_43.addWidget(self.Spikeling_StimStrSlider)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_Slider_frame)

        self.Spikeling_StimStr_values_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_values_frame.setObjectName(u"Spikeling_StimStr_values_frame")
        self.Spikeling_StimStr_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.Spikeling_StimStr_values_frame)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimStr_values_min = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_min.setObjectName(u"Spikeling_StimStr_values_min")

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_min)

        self.Spikeling_StimStr_values_0 = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_0.setObjectName(u"Spikeling_StimStr_values_0")
        self.Spikeling_StimStr_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_0)

        self.Spikeling_StimStr_values_max = QLabel(self.Spikeling_StimStr_values_frame)
        self.Spikeling_StimStr_values_max.setObjectName(u"Spikeling_StimStr_values_max")
        self.Spikeling_StimStr_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.Spikeling_StimStr_values_max)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_values_frame, 0, Qt.AlignTop)

        self.Spikeling_StimStr_image_frame = QFrame(self.Spikeling_StimStr_frame)
        self.Spikeling_StimStr_image_frame.setObjectName(u"Spikeling_StimStr_image_frame")
        self.Spikeling_StimStr_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_StimStr_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.Spikeling_StimStr_image_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_StimStr_image = QLabel(self.Spikeling_StimStr_image_frame)
        self.Spikeling_StimStr_image.setObjectName(u"Spikeling_StimStr_image")
        sizePolicy1.setHeightForWidth(self.Spikeling_StimStr_image.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_image.setSizePolicy(sizePolicy1)
        self.Spikeling_StimStr_image.setMinimumSize(QSize(40, 0))
        self.Spikeling_StimStr_image.setMaximumSize(QSize(16777215, 40))
        self.Spikeling_StimStr_image.setPixmap(QPixmap(u":/resources/resources/StimStrenght.png"))
        self.Spikeling_StimStr_image.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.Spikeling_StimStr_image)


        self.verticalLayout_23.addWidget(self.Spikeling_StimStr_image_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_StimStr_frame)

        self.Spikeling_parameter_middle_line = QFrame(self.StimulusParameter_page)
        self.Spikeling_parameter_middle_line.setObjectName(u"Spikeling_parameter_middle_line")
        self.Spikeling_parameter_middle_line.setAutoFillBackground(False)
        self.Spikeling_parameter_middle_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_parameter_middle_line.setLineWidth(4)
        self.Spikeling_parameter_middle_line.setFrameShape(QFrame.HLine)
        self.Spikeling_parameter_middle_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_middle_line)

        self.Spikeling_CustomStimulus_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_CustomStimulus_frame.setObjectName(u"Spikeling_CustomStimulus_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_CustomStimulus_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_CustomStimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.Spikeling_CustomStimulus_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 0, 5, 2)
        self.Spikeling_CustomStimulus_Title_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_Title_frame.setObjectName(u"Spikeling_CustomStimulus_Title_frame")
        self.Spikeling_CustomStimulus_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_Title_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_StimCus_Layout = QHBoxLayout(self.Spikeling_CustomStimulus_Title_frame)
        self.Spikeling_StimCus_Layout.setSpacing(0)
        self.Spikeling_StimCus_Layout.setObjectName(u"Spikeling_StimCus_Layout")
        self.Spikeling_StimCus_Layout.setContentsMargins(0, 5, 0, 0)
        self.Spikeling_CustomStimulus_toggle_frame = QFrame(self.Spikeling_CustomStimulus_Title_frame)
        self.Spikeling_CustomStimulus_toggle_frame.setObjectName(u"Spikeling_CustomStimulus_toggle_frame")
        self.Spikeling_CustomStimulus_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_CustomStimulus_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_CustomStimulus_toggle_layout = QHBoxLayout(self.Spikeling_CustomStimulus_toggle_frame)
        self.Spikeling_CustomStimulus_toggle_layout.setSpacing(0)
        self.Spikeling_CustomStimulus_toggle_layout.setObjectName(u"Spikeling_CustomStimulus_toggle_layout")
        self.Spikeling_CustomStimulus_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.Spikeling_StimCus_Layout.addWidget(self.Spikeling_CustomStimulus_toggle_frame)

        self.Spikeling_CustomStimulus_Label_frame = QFrame(self.Spikeling_CustomStimulus_Title_frame)
        self.Spikeling_CustomStimulus_Label_frame.setObjectName(u"Spikeling_CustomStimulus_Label_frame")
        self.Spikeling_CustomStimulus_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.Spikeling_CustomStimulus_Label_frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_Label = QLabel(self.Spikeling_CustomStimulus_Label_frame)
        self.Spikeling_CustomStimulus_Label.setObjectName(u"Spikeling_CustomStimulus_Label")

        self.horizontalLayout_42.addWidget(self.Spikeling_CustomStimulus_Label)


        self.Spikeling_StimCus_Layout.addWidget(self.Spikeling_CustomStimulus_Label_frame)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_Title_frame)

        self.Spikeling_CustomStimulus_comboBox_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_comboBox_frame.setObjectName(u"Spikeling_CustomStimulus_comboBox_frame")
        self.Spikeling_CustomStimulus_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.Spikeling_CustomStimulus_comboBox_frame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_comboBox = QComboBox(self.Spikeling_CustomStimulus_comboBox_frame)
        self.Spikeling_CustomStimulus_comboBox.setObjectName(u"Spikeling_CustomStimulus_comboBox")
        self.Spikeling_CustomStimulus_comboBox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.Spikeling_CustomStimulus_comboBox.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_comboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_45.addWidget(self.Spikeling_CustomStimulus_comboBox)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_comboBox_frame)

        self.Spikeling_CustomStimulus_display_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_display_frame.setObjectName(u"Spikeling_CustomStimulus_display_frame")
        self.Spikeling_CustomStimulus_display_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_display_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.Spikeling_CustomStimulus_display_frame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_display = QWidget(self.Spikeling_CustomStimulus_display_frame)
        self.Spikeling_CustomStimulus_display.setObjectName(u"Spikeling_CustomStimulus_display")
        self.Spikeling_CustomStimulus_display.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.Spikeling_CustomStimulus_display.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_display.setSizePolicy(sizePolicy1)
        self.Spikeling_CustomStimulus_display.setMinimumSize(QSize(0, 40))
        self.Spikeling_CustomStimulus_display.setMaximumSize(QSize(16777215, 50))
        self.Spikeling_CustomStimulus_display.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.horizontalLayout_44.addWidget(self.Spikeling_CustomStimulus_display)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_display_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_CustomStimulus_frame)

        self.Spikeling_parameter_bottom_line = QFrame(self.StimulusParameter_page)
        self.Spikeling_parameter_bottom_line.setObjectName(u"Spikeling_parameter_bottom_line")
        self.Spikeling_parameter_bottom_line.setAutoFillBackground(False)
        self.Spikeling_parameter_bottom_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_parameter_bottom_line.setLineWidth(10)
        self.Spikeling_parameter_bottom_line.setFrameShape(QFrame.HLine)
        self.Spikeling_parameter_bottom_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_bottom_line)

        self.Spikeling_PR_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_PR_frame.setObjectName(u"Spikeling_PR_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_PR_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_PR_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_PR_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.Spikeling_PR_frame)
        self.verticalLayout_31.setSpacing(1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(5, 0, 5, 1)
        self.Spikeling_PR_label_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_label_frame.setObjectName(u"Spikeling_PR_label_frame")
        self.Spikeling_PR_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.Spikeling_PR_label_frame)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_PR_label = QLabel(self.Spikeling_PR_label_frame)
        self.Spikeling_PR_label.setObjectName(u"Spikeling_PR_label")
        self.Spikeling_PR_label.setStyleSheet(u"")

        self.verticalLayout_71.addWidget(self.Spikeling_PR_label)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_label_frame)

        self.Spikeling_PR_Title_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Title_frame.setObjectName(u"Spikeling_PR_Title_frame")
        self.Spikeling_PR_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.Spikeling_PR_Title_frame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_toggle_frame = QFrame(self.Spikeling_PR_Title_frame)
        self.Spikeling_PR_toggle_frame.setObjectName(u"Spikeling_PR_toggle_frame")
        self.Spikeling_PR_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_PR_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PR_toggle_layout = QHBoxLayout(self.Spikeling_PR_toggle_frame)
        self.Spikeling_PR_toggle_layout.setSpacing(0)
        self.Spikeling_PR_toggle_layout.setObjectName(u"Spikeling_PR_toggle_layout")
        self.Spikeling_PR_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_49.addWidget(self.Spikeling_PR_toggle_frame)

        self.Spikeling_PR_Label_frame = QFrame(self.Spikeling_PR_Title_frame)
        self.Spikeling_PR_Label_frame.setObjectName(u"Spikeling_PR_Label_frame")
        self.Spikeling_PR_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.Spikeling_PR_Label_frame)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Label = QLabel(self.Spikeling_PR_Label_frame)
        self.Spikeling_PR_Label.setObjectName(u"Spikeling_PR_Label")

        self.horizontalLayout_85.addWidget(self.Spikeling_PR_Label)


        self.horizontalLayout_49.addWidget(self.Spikeling_PR_Label_frame)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Title_frame)

        self.Spikeling_PR_Photogain_readings_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Photogain_readings_frame.setObjectName(u"Spikeling_PR_Photogain_readings_frame")
        self.Spikeling_PR_Photogain_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Photogain_readings_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PR_PhotoGain_Layout = QHBoxLayout(self.Spikeling_PR_Photogain_readings_frame)
        self.Spikeling_PR_PhotoGain_Layout.setSpacing(0)
        self.Spikeling_PR_PhotoGain_Layout.setObjectName(u"Spikeling_PR_PhotoGain_Layout")
        self.Spikeling_PR_PhotoGain_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Photogain_readings = QLabel(self.Spikeling_PR_Photogain_readings_frame)
        self.Spikeling_PR_Photogain_readings.setObjectName(u"Spikeling_PR_Photogain_readings")
        self.Spikeling_PR_Photogain_readings.setAlignment(Qt.AlignCenter)

        self.Spikeling_PR_PhotoGain_Layout.addWidget(self.Spikeling_PR_Photogain_readings)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Photogain_readings_frame)

        self.Spikeling_PR_PhotoGain_slider_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_PhotoGain_slider_frame.setObjectName(u"Spikeling_PR_PhotoGain_slider_frame")
        self.Spikeling_PR_PhotoGain_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_PhotoGain_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.Spikeling_PR_PhotoGain_slider_frame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_slider = QSlider(self.Spikeling_PR_PhotoGain_slider_frame)
        self.Spikeling_PR_PhotoGain_slider.setObjectName(u"Spikeling_PR_PhotoGain_slider")
        self.Spikeling_PR_PhotoGain_slider.setEnabled(False)
        self.Spikeling_PR_PhotoGain_slider.setMinimum(-100)
        self.Spikeling_PR_PhotoGain_slider.setMaximum(100)
        self.Spikeling_PR_PhotoGain_slider.setSingleStep(1)
        self.Spikeling_PR_PhotoGain_slider.setPageStep(10)
        self.Spikeling_PR_PhotoGain_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PR_PhotoGain_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PR_PhotoGain_slider.setTickInterval(20)

        self.horizontalLayout_48.addWidget(self.Spikeling_PR_PhotoGain_slider)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_PhotoGain_slider_frame)

        self.Spikeling_PR_PhotoGain_values_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_PhotoGain_values_frame.setObjectName(u"Spikeling_PR_PhotoGain_values_frame")
        self.Spikeling_PR_PhotoGain_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_PhotoGain_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.Spikeling_PR_PhotoGain_values_frame)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_PhotoGain_values_min = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_min.setObjectName(u"Spikeling_PR_PhotoGain_values_min")

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_min)

        self.Spikeling_PR_PhotoGain_values_0 = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_0.setObjectName(u"Spikeling_PR_PhotoGain_values_0")

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_0, 0, Qt.AlignHCenter)

        self.Spikeling_PR_PhotoGain_values_max = QLabel(self.Spikeling_PR_PhotoGain_values_frame)
        self.Spikeling_PR_PhotoGain_values_max.setObjectName(u"Spikeling_PR_PhotoGain_values_max")
        self.Spikeling_PR_PhotoGain_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.Spikeling_PR_PhotoGain_values_max)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_PhotoGain_values_frame, 0, Qt.AlignTop)

        self.Spikeling_PRDecay_Title = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PRDecay_Title.setObjectName(u"Spikeling_PRDecay_Title")
        self.Spikeling_PRDecay_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PRDecay_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.Spikeling_PRDecay_Title)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PRDecay_Toggle_frame = QFrame(self.Spikeling_PRDecay_Title)
        self.Spikeling_PRDecay_Toggle_frame.setObjectName(u"Spikeling_PRDecay_Toggle_frame")
        self.Spikeling_PRDecay_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_PRDecay_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PRDecay_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PRDecay_Toggle_layout = QHBoxLayout(self.Spikeling_PRDecay_Toggle_frame)
        self.Spikeling_PRDecay_Toggle_layout.setSpacing(0)
        self.Spikeling_PRDecay_Toggle_layout.setObjectName(u"Spikeling_PRDecay_Toggle_layout")
        self.Spikeling_PRDecay_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_94.addWidget(self.Spikeling_PRDecay_Toggle_frame)

        self.Spikeling_PRDecay_Label_frame = QFrame(self.Spikeling_PRDecay_Title)
        self.Spikeling_PRDecay_Label_frame.setObjectName(u"Spikeling_PRDecay_Label_frame")
        self.Spikeling_PRDecay_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PRDecay_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.Spikeling_PRDecay_Label_frame)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PRDecay_Label = QLabel(self.Spikeling_PRDecay_Label_frame)
        self.Spikeling_PRDecay_Label.setObjectName(u"Spikeling_PRDecay_Label")

        self.horizontalLayout_46.addWidget(self.Spikeling_PRDecay_Label)


        self.horizontalLayout_94.addWidget(self.Spikeling_PRDecay_Label_frame)


        self.verticalLayout_31.addWidget(self.Spikeling_PRDecay_Title)

        self.Spikeling_PR_Decay_readings_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Decay_readings_frame.setObjectName(u"Spikeling_PR_Decay_readings_frame")
        self.Spikeling_PR_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PR_Decay_Layout = QHBoxLayout(self.Spikeling_PR_Decay_readings_frame)
        self.Spikeling_PR_Decay_Layout.setSpacing(0)
        self.Spikeling_PR_Decay_Layout.setObjectName(u"Spikeling_PR_Decay_Layout")
        self.Spikeling_PR_Decay_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Decay_readings = QLabel(self.Spikeling_PR_Decay_readings_frame)
        self.Spikeling_PR_Decay_readings.setObjectName(u"Spikeling_PR_Decay_readings")
        self.Spikeling_PR_Decay_readings.setAlignment(Qt.AlignCenter)

        self.Spikeling_PR_Decay_Layout.addWidget(self.Spikeling_PR_Decay_readings)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Decay_readings_frame)

        self.Spikeling_PR_Decay_slider_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Decay_slider_frame.setObjectName(u"Spikeling_PR_Decay_slider_frame")
        self.Spikeling_PR_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.Spikeling_PR_Decay_slider_frame)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Decay_slider = QSlider(self.Spikeling_PR_Decay_slider_frame)
        self.Spikeling_PR_Decay_slider.setObjectName(u"Spikeling_PR_Decay_slider")
        self.Spikeling_PR_Decay_slider.setEnabled(False)
        self.Spikeling_PR_Decay_slider.setMinimum(10)
        self.Spikeling_PR_Decay_slider.setMaximum(125)
        self.Spikeling_PR_Decay_slider.setSingleStep(1)
        self.Spikeling_PR_Decay_slider.setPageStep(10)
        self.Spikeling_PR_Decay_slider.setValue(100)
        self.Spikeling_PR_Decay_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PR_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PR_Decay_slider.setTickInterval(10)

        self.verticalLayout_66.addWidget(self.Spikeling_PR_Decay_slider)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Decay_slider_frame)

        self.Spikeling_PR_Decay_values_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Decay_values_frame.setObjectName(u"Spikeling_PR_Decay_values_frame")
        self.Spikeling_PR_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.Spikeling_PR_Decay_values_frame)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Decay_values_slow = QLabel(self.Spikeling_PR_Decay_values_frame)
        self.Spikeling_PR_Decay_values_slow.setObjectName(u"Spikeling_PR_Decay_values_slow")
        self.Spikeling_PR_Decay_values_slow.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.Spikeling_PR_Decay_values_slow)

        self.Spikeling_PR_Decay_values_fast = QLabel(self.Spikeling_PR_Decay_values_frame)
        self.Spikeling_PR_Decay_values_fast.setObjectName(u"Spikeling_PR_Decay_values_fast")
        self.Spikeling_PR_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.Spikeling_PR_Decay_values_fast)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Decay_values_frame)

        self.Spikeling_PRRecovery_Title = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PRRecovery_Title.setObjectName(u"Spikeling_PRRecovery_Title")
        self.Spikeling_PRRecovery_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PRRecovery_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.Spikeling_PRRecovery_Title)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.SpikelingPRRecovery_toggle_frame = QFrame(self.Spikeling_PRRecovery_Title)
        self.SpikelingPRRecovery_toggle_frame.setObjectName(u"SpikelingPRRecovery_toggle_frame")
        self.SpikelingPRRecovery_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.SpikelingPRRecovery_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.SpikelingPRRecovery_toggle_frame.setFrameShadow(QFrame.Raised)
        self.SpikelingPRRecovery_toggle_layout = QHBoxLayout(self.SpikelingPRRecovery_toggle_frame)
        self.SpikelingPRRecovery_toggle_layout.setSpacing(0)
        self.SpikelingPRRecovery_toggle_layout.setObjectName(u"SpikelingPRRecovery_toggle_layout")
        self.SpikelingPRRecovery_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_99.addWidget(self.SpikelingPRRecovery_toggle_frame)

        self.SpikelingPRRecovery_Label_frame = QFrame(self.Spikeling_PRRecovery_Title)
        self.SpikelingPRRecovery_Label_frame.setObjectName(u"SpikelingPRRecovery_Label_frame")
        self.SpikelingPRRecovery_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SpikelingPRRecovery_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.SpikelingPRRecovery_Label_frame)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.SpikelingPRRecovery_Label = QLabel(self.SpikelingPRRecovery_Label_frame)
        self.SpikelingPRRecovery_Label.setObjectName(u"SpikelingPRRecovery_Label")

        self.horizontalLayout_98.addWidget(self.SpikelingPRRecovery_Label)


        self.horizontalLayout_99.addWidget(self.SpikelingPRRecovery_Label_frame)


        self.verticalLayout_31.addWidget(self.Spikeling_PRRecovery_Title)

        self.Spikeling_PR_Recovery_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Recovery_frame.setObjectName(u"Spikeling_PR_Recovery_frame")
        self.Spikeling_PR_Recovery_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Recovery_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PR_Recovery_Layout = QHBoxLayout(self.Spikeling_PR_Recovery_frame)
        self.Spikeling_PR_Recovery_Layout.setSpacing(0)
        self.Spikeling_PR_Recovery_Layout.setObjectName(u"Spikeling_PR_Recovery_Layout")
        self.Spikeling_PR_Recovery_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Recovery_readings_frame = QFrame(self.Spikeling_PR_Recovery_frame)
        self.Spikeling_PR_Recovery_readings_frame.setObjectName(u"Spikeling_PR_Recovery_readings_frame")
        self.Spikeling_PR_Recovery_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Recovery_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.Spikeling_PR_Recovery_readings_frame)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Recovery_readings = QLabel(self.Spikeling_PR_Recovery_readings_frame)
        self.Spikeling_PR_Recovery_readings.setObjectName(u"Spikeling_PR_Recovery_readings")
        self.Spikeling_PR_Recovery_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.Spikeling_PR_Recovery_readings)


        self.Spikeling_PR_Recovery_Layout.addWidget(self.Spikeling_PR_Recovery_readings_frame)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Recovery_frame)

        self.Spikeling_PR_Recovery_slider_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Recovery_slider_frame.setObjectName(u"Spikeling_PR_Recovery_slider_frame")
        self.Spikeling_PR_Recovery_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Recovery_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.Spikeling_PR_Recovery_slider_frame)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Recovery_slider = QSlider(self.Spikeling_PR_Recovery_slider_frame)
        self.Spikeling_PR_Recovery_slider.setObjectName(u"Spikeling_PR_Recovery_slider")
        self.Spikeling_PR_Recovery_slider.setEnabled(False)
        self.Spikeling_PR_Recovery_slider.setMinimum(1)
        self.Spikeling_PR_Recovery_slider.setMaximum(100)
        self.Spikeling_PR_Recovery_slider.setSingleStep(1)
        self.Spikeling_PR_Recovery_slider.setPageStep(10)
        self.Spikeling_PR_Recovery_slider.setValue(25)
        self.Spikeling_PR_Recovery_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PR_Recovery_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PR_Recovery_slider.setTickInterval(10)

        self.verticalLayout_68.addWidget(self.Spikeling_PR_Recovery_slider)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Recovery_slider_frame)

        self.Spikeling_PR_Recovery_values_frame = QFrame(self.Spikeling_PR_frame)
        self.Spikeling_PR_Recovery_values_frame.setObjectName(u"Spikeling_PR_Recovery_values_frame")
        self.Spikeling_PR_Recovery_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PR_Recovery_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.Spikeling_PR_Recovery_values_frame)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PR_Recovery_values_slow = QLabel(self.Spikeling_PR_Recovery_values_frame)
        self.Spikeling_PR_Recovery_values_slow.setObjectName(u"Spikeling_PR_Recovery_values_slow")

        self.horizontalLayout_102.addWidget(self.Spikeling_PR_Recovery_values_slow)

        self.Spikeling_PR_Recovery_values_fast = QLabel(self.Spikeling_PR_Recovery_values_frame)
        self.Spikeling_PR_Recovery_values_fast.setObjectName(u"Spikeling_PR_Recovery_values_fast")
        self.Spikeling_PR_Recovery_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_102.addWidget(self.Spikeling_PR_Recovery_values_fast)


        self.verticalLayout_31.addWidget(self.Spikeling_PR_Recovery_values_frame)


        self.verticalLayout_58.addWidget(self.Spikeling_PR_frame)

        self.Spikeling_parameter_stackedwidget.addWidget(self.StimulusParameter_page)
        self.NeuronParameter_page = QWidget()
        self.NeuronParameter_page.setObjectName(u"NeuronParameter_page")
        self.NeuronParameter_page.setMinimumSize(QSize(200, 0))
        self.NeuronParameter_page.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_57 = QVBoxLayout(self.NeuronParameter_page)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_NeuronParameter_frame = QFrame(self.NeuronParameter_page)
        self.Spikeling_NeuronParameter_frame.setObjectName(u"Spikeling_NeuronParameter_frame")
        sizePolicy3.setHeightForWidth(self.Spikeling_NeuronParameter_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_NeuronParameter_frame.setSizePolicy(sizePolicy3)
        self.Spikeling_NeuronParameter_frame.setMinimumSize(QSize(200, 0))
        self.Spikeling_NeuronParameter_frame.setMaximumSize(QSize(175, 16777215))
        self.Spikeling_NeuronParameter_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_NeuronParameter_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Spikeling_NeuronParameter_frame)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 5, 0, 5)
        self.Spikeling_PatchClamp_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_PatchClamp_frame.setObjectName(u"Spikeling_PatchClamp_frame")
        self.Spikeling_PatchClamp_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Spikeling_PatchClamp_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 0, 5, 0)
        self.Spikeling_PatchClamp_label_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_label_frame.setObjectName(u"Spikeling_PatchClamp_label_frame")
        self.Spikeling_PatchClamp_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.Spikeling_PatchClamp_label_frame)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_PatchClamp_label = QLabel(self.Spikeling_PatchClamp_label_frame)
        self.Spikeling_PatchClamp_label.setObjectName(u"Spikeling_PatchClamp_label")
        self.Spikeling_PatchClamp_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_84.addWidget(self.Spikeling_PatchClamp_label)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_label_frame)

        self.Spikeling_PatchClamp_checkBox_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_checkBox_frame.setObjectName(u"Spikeling_PatchClamp_checkBox_frame")
        self.Spikeling_PatchClamp_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.Spikeling_PatchClamp_checkBox_frame)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_Title = QFrame(self.Spikeling_PatchClamp_checkBox_frame)
        self.Spikeling_PatchClamp_Title.setObjectName(u"Spikeling_PatchClamp_Title")
        self.Spikeling_PatchClamp_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.Spikeling_PatchClamp_Title)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_toggle_frame = QFrame(self.Spikeling_PatchClamp_Title)
        self.Spikeling_PatchClamp_toggle_frame.setObjectName(u"Spikeling_PatchClamp_toggle_frame")
        self.Spikeling_PatchClamp_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_PatchClamp_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_PatchClamp_toggle_layout = QHBoxLayout(self.Spikeling_PatchClamp_toggle_frame)
        self.Spikeling_PatchClamp_toggle_layout.setSpacing(0)
        self.Spikeling_PatchClamp_toggle_layout.setObjectName(u"Spikeling_PatchClamp_toggle_layout")
        self.Spikeling_PatchClamp_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_91.addWidget(self.Spikeling_PatchClamp_toggle_frame)

        self.Spikeling_PatchClamp_Label_frame = QFrame(self.Spikeling_PatchClamp_Title)
        self.Spikeling_PatchClamp_Label_frame.setObjectName(u"Spikeling_PatchClamp_Label_frame")
        self.Spikeling_PatchClamp_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.Spikeling_PatchClamp_Label_frame)
        self.horizontalLayout_163.setSpacing(0)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_Label = QLabel(self.Spikeling_PatchClamp_Label_frame)
        self.Spikeling_PatchClamp_Label.setObjectName(u"Spikeling_PatchClamp_Label")

        self.horizontalLayout_163.addWidget(self.Spikeling_PatchClamp_Label)


        self.horizontalLayout_91.addWidget(self.Spikeling_PatchClamp_Label_frame)


        self.verticalLayout_63.addWidget(self.Spikeling_PatchClamp_Title)

        self.Spikeling_PatchClamp_reading_frame = QFrame(self.Spikeling_PatchClamp_checkBox_frame)
        self.Spikeling_PatchClamp_reading_frame.setObjectName(u"Spikeling_PatchClamp_reading_frame")
        self.Spikeling_PatchClamp_reading_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_reading_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.Spikeling_PatchClamp_reading_frame)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_reading = QLabel(self.Spikeling_PatchClamp_reading_frame)
        self.Spikeling_PatchClamp_reading.setObjectName(u"Spikeling_PatchClamp_reading")
        self.Spikeling_PatchClamp_reading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.Spikeling_PatchClamp_reading)


        self.verticalLayout_63.addWidget(self.Spikeling_PatchClamp_reading_frame)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_checkBox_frame)

        self.Spikeling_PatchClamp_slider_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_slider_frame.setObjectName(u"Spikeling_PatchClamp_slider_frame")
        self.Spikeling_PatchClamp_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.Spikeling_PatchClamp_slider_frame)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_slider = QSlider(self.Spikeling_PatchClamp_slider_frame)
        self.Spikeling_PatchClamp_slider.setObjectName(u"Spikeling_PatchClamp_slider")
        self.Spikeling_PatchClamp_slider.setEnabled(False)
        self.Spikeling_PatchClamp_slider.setMinimum(-100)
        self.Spikeling_PatchClamp_slider.setMaximum(100)
        self.Spikeling_PatchClamp_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_PatchClamp_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_PatchClamp_slider.setTickInterval(20)

        self.horizontalLayout_63.addWidget(self.Spikeling_PatchClamp_slider)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_slider_frame)

        self.Spikeling_PatchClamp_values_frame = QFrame(self.Spikeling_PatchClamp_frame)
        self.Spikeling_PatchClamp_values_frame.setObjectName(u"Spikeling_PatchClamp_values_frame")
        self.Spikeling_PatchClamp_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_PatchClamp_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.Spikeling_PatchClamp_values_frame)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_PatchClamp_values_min = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_min.setObjectName(u"Spikeling_PatchClamp_values_min")

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_min)

        self.Spikeling_PatchClamp_values_0 = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_0.setObjectName(u"Spikeling_PatchClamp_values_0")
        self.Spikeling_PatchClamp_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_0)

        self.Spikeling_PatchClamp_values_max = QLabel(self.Spikeling_PatchClamp_values_frame)
        self.Spikeling_PatchClamp_values_max.setObjectName(u"Spikeling_PatchClamp_values_max")
        self.Spikeling_PatchClamp_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.Spikeling_PatchClamp_values_max)


        self.verticalLayout_21.addWidget(self.Spikeling_PatchClamp_values_frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.Spikeling_PatchClamp_frame)

        self.Spikeling_neuronparameters_top_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_top_line.setObjectName(u"Spikeling_neuronparameters_top_line")
        self.Spikeling_neuronparameters_top_line.setAutoFillBackground(False)
        self.Spikeling_neuronparameters_top_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_neuronparameters_top_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_top_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_top_line)

        self.Spikeling_Noise_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Noise_frame.setObjectName(u"Spikeling_Noise_frame")
        self.Spikeling_Noise_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Spikeling_Noise_frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 0, 5, 0)
        self.Spikeling_Noise_label_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_label_frame.setObjectName(u"Spikeling_Noise_label_frame")
        self.Spikeling_Noise_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.Spikeling_Noise_label_frame)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_label = QLabel(self.Spikeling_Noise_label_frame)
        self.Spikeling_Noise_label.setObjectName(u"Spikeling_Noise_label")
        self.Spikeling_Noise_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_88.addWidget(self.Spikeling_Noise_label)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_label_frame)

        self.Spikeling_Noise_checkBox_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_checkBox_frame.setObjectName(u"Spikeling_Noise_checkBox_frame")
        self.Spikeling_Noise_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.Spikeling_Noise_checkBox_frame)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_Title_frame = QFrame(self.Spikeling_Noise_checkBox_frame)
        self.Spikeling_Noise_Title_frame.setObjectName(u"Spikeling_Noise_Title_frame")
        self.Spikeling_Noise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.Spikeling_Noise_Title_frame)
        self.horizontalLayout_164.setSpacing(0)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_toggle_frame = QFrame(self.Spikeling_Noise_Title_frame)
        self.Spikeling_Noise_toggle_frame.setObjectName(u"Spikeling_Noise_toggle_frame")
        self.Spikeling_Noise_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_Noise_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Noise_toggle_layout = QHBoxLayout(self.Spikeling_Noise_toggle_frame)
        self.Spikeling_Noise_toggle_layout.setSpacing(0)
        self.Spikeling_Noise_toggle_layout.setObjectName(u"Spikeling_Noise_toggle_layout")
        self.Spikeling_Noise_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_164.addWidget(self.Spikeling_Noise_toggle_frame)

        self.Spikeling_Noise_Label_frame = QFrame(self.Spikeling_Noise_Title_frame)
        self.Spikeling_Noise_Label_frame.setObjectName(u"Spikeling_Noise_Label_frame")
        self.Spikeling_Noise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.Spikeling_Noise_Label_frame)
        self.horizontalLayout_166.setSpacing(0)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_Label = QLabel(self.Spikeling_Noise_Label_frame)
        self.Spikeling_Noise_Label.setObjectName(u"Spikeling_Noise_Label")

        self.horizontalLayout_166.addWidget(self.Spikeling_Noise_Label)


        self.horizontalLayout_164.addWidget(self.Spikeling_Noise_Label_frame)


        self.verticalLayout_65.addWidget(self.Spikeling_Noise_Title_frame)

        self.Spikeling_Noise_readings_frame = QFrame(self.Spikeling_Noise_checkBox_frame)
        self.Spikeling_Noise_readings_frame.setObjectName(u"Spikeling_Noise_readings_frame")
        self.Spikeling_Noise_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticaLayout_74 = QVBoxLayout(self.Spikeling_Noise_readings_frame)
        self.verticaLayout_74.setSpacing(0)
        self.verticaLayout_74.setObjectName(u"verticaLayout_74")
        self.verticaLayout_74.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_readings = QLabel(self.Spikeling_Noise_readings_frame)
        self.Spikeling_Noise_readings.setObjectName(u"Spikeling_Noise_readings")
        self.Spikeling_Noise_readings.setAlignment(Qt.AlignCenter)

        self.verticaLayout_74.addWidget(self.Spikeling_Noise_readings)


        self.verticalLayout_65.addWidget(self.Spikeling_Noise_readings_frame)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_checkBox_frame)

        self.Spikeling_Noise_slider_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_slider_frame.setObjectName(u"Spikeling_Noise_slider_frame")
        self.Spikeling_Noise_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.Spikeling_Noise_slider_frame)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_slider = QSlider(self.Spikeling_Noise_slider_frame)
        self.Spikeling_Noise_slider.setObjectName(u"Spikeling_Noise_slider")
        self.Spikeling_Noise_slider.setEnabled(False)
        self.Spikeling_Noise_slider.setMaximum(100)
        self.Spikeling_Noise_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Noise_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Noise_slider.setTickInterval(10)

        self.horizontalLayout_90.addWidget(self.Spikeling_Noise_slider)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_slider_frame)

        self.Spikeling_Noise_value_frame = QFrame(self.Spikeling_Noise_frame)
        self.Spikeling_Noise_value_frame.setObjectName(u"Spikeling_Noise_value_frame")
        self.Spikeling_Noise_value_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Noise_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.Spikeling_Noise_value_frame)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Noise_0_value = QLabel(self.Spikeling_Noise_value_frame)
        self.Spikeling_Noise_0_value.setObjectName(u"Spikeling_Noise_0_value")
        self.Spikeling_Noise_0_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.Spikeling_Noise_0_value, 0, Qt.AlignLeft)

        self.Spikeling_Noise_max_value = QLabel(self.Spikeling_Noise_value_frame)
        self.Spikeling_Noise_max_value.setObjectName(u"Spikeling_Noise_max_value")
        self.Spikeling_Noise_max_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.Spikeling_Noise_max_value, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.Spikeling_Noise_value_frame, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.Spikeling_Noise_frame)

        self.Spikeling_neuronparameters_middle_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_middle_line.setObjectName(u"Spikeling_neuronparameters_middle_line")
        self.Spikeling_neuronparameters_middle_line.setAutoFillBackground(False)
        self.Spikeling_neuronparameters_middle_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_neuronparameters_middle_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_middle_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_middle_line)

        self.Spikeling_Synapse1_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Synapse1_frame.setObjectName(u"Spikeling_Synapse1_frame")
        self.Spikeling_Synapse1_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Spikeling_Synapse1_frame)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(5, 0, 5, 0)
        self.Spikeling_Synapse1_label_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_label_frame.setObjectName(u"Spikeling_Synapse1_label_frame")
        self.Spikeling_Synapse1_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.Spikeling_Synapse1_label_frame)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 10)
        self.Spikeling_Synapse1_label = QLabel(self.Spikeling_Synapse1_label_frame)
        self.Spikeling_Synapse1_label.setObjectName(u"Spikeling_Synapse1_label")
        self.Spikeling_Synapse1_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_92.addWidget(self.Spikeling_Synapse1_label)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_label_frame)

        self.Spikeling_Synapse1_checkBox_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_checkBox_frame.setObjectName(u"Spikeling_Synapse1_checkBox_frame")
        self.Spikeling_Synapse1_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.Spikeling_Synapse1_checkBox_frame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Title = QFrame(self.Spikeling_Synapse1_checkBox_frame)
        self.Spikeling_Synapse1_Title.setObjectName(u"Spikeling_Synapse1_Title")
        self.Spikeling_Synapse1_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.Spikeling_Synapse1_Title)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_toggle_frame = QFrame(self.Spikeling_Synapse1_Title)
        self.Spikeling_Synapse1_toggle_frame.setObjectName(u"Spikeling_Synapse1_toggle_frame")
        self.Spikeling_Synapse1_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_Synapse1_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse1_toggle_layout = QHBoxLayout(self.Spikeling_Synapse1_toggle_frame)
        self.Spikeling_Synapse1_toggle_layout.setSpacing(0)
        self.Spikeling_Synapse1_toggle_layout.setObjectName(u"Spikeling_Synapse1_toggle_layout")
        self.Spikeling_Synapse1_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_104.addWidget(self.Spikeling_Synapse1_toggle_frame)

        self.Spikeling_Synapse1_Label_frame = QFrame(self.Spikeling_Synapse1_Title)
        self.Spikeling_Synapse1_Label_frame.setObjectName(u"Spikeling_Synapse1_Label_frame")
        self.Spikeling_Synapse1_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.Spikeling_Synapse1_Label_frame)
        self.horizontalLayout_167.setSpacing(0)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Label = QLabel(self.Spikeling_Synapse1_Label_frame)
        self.Spikeling_Synapse1_Label.setObjectName(u"Spikeling_Synapse1_Label")

        self.horizontalLayout_167.addWidget(self.Spikeling_Synapse1_Label)


        self.horizontalLayout_104.addWidget(self.Spikeling_Synapse1_Label_frame)


        self.verticalLayout_67.addWidget(self.Spikeling_Synapse1_Title)

        self.Spikeling_Synapse1_readings_frame = QFrame(self.Spikeling_Synapse1_checkBox_frame)
        self.Spikeling_Synapse1_readings_frame.setObjectName(u"Spikeling_Synapse1_readings_frame")
        self.Spikeling_Synapse1_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.Spikeling_Synapse1_readings_frame)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_readings = QLabel(self.Spikeling_Synapse1_readings_frame)
        self.Spikeling_Synapse1_readings.setObjectName(u"Spikeling_Synapse1_readings")
        self.Spikeling_Synapse1_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.Spikeling_Synapse1_readings)


        self.verticalLayout_67.addWidget(self.Spikeling_Synapse1_readings_frame)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_checkBox_frame)

        self.Spikeling_Synapse1_slider_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_slider_frame.setObjectName(u"Spikeling_Synapse1_slider_frame")
        self.Spikeling_Synapse1_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.Spikeling_Synapse1_slider_frame)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_slider = QSlider(self.Spikeling_Synapse1_slider_frame)
        self.Spikeling_Synapse1_slider.setObjectName(u"Spikeling_Synapse1_slider")
        self.Spikeling_Synapse1_slider.setEnabled(False)
        self.Spikeling_Synapse1_slider.setMinimum(-100)
        self.Spikeling_Synapse1_slider.setMaximum(100)
        self.Spikeling_Synapse1_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse1_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse1_slider.setTickInterval(20)

        self.horizontalLayout_95.addWidget(self.Spikeling_Synapse1_slider)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_slider_frame)

        self.Spikeling_Synapse1_values_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_values_frame.setObjectName(u"Spikeling_Synapse1_values_frame")
        self.Spikeling_Synapse1_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.Spikeling_Synapse1_values_frame)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_Synapse1_min = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_min.setObjectName(u"Spikeling_Synapse1_min")

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_min)

        self.Spikeling_Synapse1_0 = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_0.setObjectName(u"Spikeling_Synapse1_0")

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_0, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Spikeling_Synapse1_max = QLabel(self.Spikeling_Synapse1_values_frame)
        self.Spikeling_Synapse1_max.setObjectName(u"Spikeling_Synapse1_max")
        self.Spikeling_Synapse1_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_96.addWidget(self.Spikeling_Synapse1_max)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_values_frame)

        self.Spikeling_Synapse1_Decay_checkBox_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_Decay_checkBox_frame.setObjectName(u"Spikeling_Synapse1_Decay_checkBox_frame")
        self.Spikeling_Synapse1_Decay_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.Spikeling_Synapse1_Decay_checkBox_frame)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_Title = QFrame(self.Spikeling_Synapse1_Decay_checkBox_frame)
        self.Spikeling_Synapse1_Decay_Title.setObjectName(u"Spikeling_Synapse1_Decay_Title")
        self.Spikeling_Synapse1_Decay_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.Spikeling_Synapse1_Decay_Title)
        self.horizontalLayout_165.setSpacing(0)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_toggle_frame = QFrame(self.Spikeling_Synapse1_Decay_Title)
        self.Spikeling_Synapse1_Decay_toggle_frame.setObjectName(u"Spikeling_Synapse1_Decay_toggle_frame")
        self.Spikeling_Synapse1_Decay_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_Synapse1_Decay_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse1_Decay_toggle_layout = QHBoxLayout(self.Spikeling_Synapse1_Decay_toggle_frame)
        self.Spikeling_Synapse1_Decay_toggle_layout.setSpacing(0)
        self.Spikeling_Synapse1_Decay_toggle_layout.setObjectName(u"Spikeling_Synapse1_Decay_toggle_layout")
        self.Spikeling_Synapse1_Decay_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_165.addWidget(self.Spikeling_Synapse1_Decay_toggle_frame)

        self.Spikeling_Synapse1_Decay_Label_frame = QFrame(self.Spikeling_Synapse1_Decay_Title)
        self.Spikeling_Synapse1_Decay_Label_frame.setObjectName(u"Spikeling_Synapse1_Decay_Label_frame")
        self.Spikeling_Synapse1_Decay_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_169 = QHBoxLayout(self.Spikeling_Synapse1_Decay_Label_frame)
        self.horizontalLayout_169.setSpacing(0)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_Label = QLabel(self.Spikeling_Synapse1_Decay_Label_frame)
        self.Spikeling_Synapse1_Decay_Label.setObjectName(u"Spikeling_Synapse1_Decay_Label")

        self.horizontalLayout_169.addWidget(self.Spikeling_Synapse1_Decay_Label)


        self.horizontalLayout_165.addWidget(self.Spikeling_Synapse1_Decay_Label_frame)


        self.verticalLayout_74.addWidget(self.Spikeling_Synapse1_Decay_Title)

        self.Spikeling_Synapse1_Decay_readings_frame = QFrame(self.Spikeling_Synapse1_Decay_checkBox_frame)
        self.Spikeling_Synapse1_Decay_readings_frame.setObjectName(u"Spikeling_Synapse1_Decay_readings_frame")
        self.Spikeling_Synapse1_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.Spikeling_Synapse1_Decay_readings_frame)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_readings = QLabel(self.Spikeling_Synapse1_Decay_readings_frame)
        self.Spikeling_Synapse1_Decay_readings.setObjectName(u"Spikeling_Synapse1_Decay_readings")
        self.Spikeling_Synapse1_Decay_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.Spikeling_Synapse1_Decay_readings)


        self.verticalLayout_74.addWidget(self.Spikeling_Synapse1_Decay_readings_frame)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_Decay_checkBox_frame)

        self.Spikeling_Synapse1_Decay_slider_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_Decay_slider_frame.setObjectName(u"Spikeling_Synapse1_Decay_slider_frame")
        self.Spikeling_Synapse1_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.Spikeling_Synapse1_Decay_slider_frame)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_slider = QSlider(self.Spikeling_Synapse1_Decay_slider_frame)
        self.Spikeling_Synapse1_Decay_slider.setObjectName(u"Spikeling_Synapse1_Decay_slider")
        self.Spikeling_Synapse1_Decay_slider.setEnabled(False)
        self.Spikeling_Synapse1_Decay_slider.setMinimum(975)
        self.Spikeling_Synapse1_Decay_slider.setMaximum(1000)
        self.Spikeling_Synapse1_Decay_slider.setSliderPosition(995)
        self.Spikeling_Synapse1_Decay_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse1_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse1_Decay_slider.setTickInterval(2)

        self.verticalLayout_78.addWidget(self.Spikeling_Synapse1_Decay_slider)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_Decay_slider_frame)

        self.Spikeling_Synapse1_Decay_values_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_Decay_values_frame.setObjectName(u"Spikeling_Synapse1_Decay_values_frame")
        self.Spikeling_Synapse1_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.Spikeling_Synapse1_Decay_values_frame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse1_Decay_values_slow = QLabel(self.Spikeling_Synapse1_Decay_values_frame)
        self.Spikeling_Synapse1_Decay_values_slow.setObjectName(u"Spikeling_Synapse1_Decay_values_slow")

        self.horizontalLayout_35.addWidget(self.Spikeling_Synapse1_Decay_values_slow)

        self.Spikeling_Synapse1_Decay_values_fast = QLabel(self.Spikeling_Synapse1_Decay_values_frame)
        self.Spikeling_Synapse1_Decay_values_fast.setObjectName(u"Spikeling_Synapse1_Decay_values_fast")
        self.Spikeling_Synapse1_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.Spikeling_Synapse1_Decay_values_fast)


        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_Decay_values_frame)

        self.Spikeling_Synapse1_Decay_frame = QFrame(self.Spikeling_Synapse1_frame)
        self.Spikeling_Synapse1_Decay_frame.setObjectName(u"Spikeling_Synapse1_Decay_frame")
        self.Spikeling_Synapse1_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse1_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.Spikeling_Synapse1_Decay_frame)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_32.addWidget(self.Spikeling_Synapse1_Decay_frame)


        self.verticalLayout_17.addWidget(self.Spikeling_Synapse1_frame)

        self.Spikeling_neuronparameters_bottom_line = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_neuronparameters_bottom_line.setObjectName(u"Spikeling_neuronparameters_bottom_line")
        self.Spikeling_neuronparameters_bottom_line.setAutoFillBackground(False)
        self.Spikeling_neuronparameters_bottom_line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Spikeling_neuronparameters_bottom_line.setFrameShape(QFrame.HLine)
        self.Spikeling_neuronparameters_bottom_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.Spikeling_neuronparameters_bottom_line)

        self.Spikeling_Synapse2_frame = QFrame(self.Spikeling_NeuronParameter_frame)
        self.Spikeling_Synapse2_frame.setObjectName(u"Spikeling_Synapse2_frame")
        self.Spikeling_Synapse2_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Spikeling_Synapse2_frame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(5, 0, 5, 0)
        self.Spikeling_Synapse2_label_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_label_frame.setObjectName(u"Spikeling_Synapse2_label_frame")
        self.Spikeling_Synapse2_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.Spikeling_Synapse2_label_frame)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_Synapse2_label = QLabel(self.Spikeling_Synapse2_label_frame)
        self.Spikeling_Synapse2_label.setObjectName(u"Spikeling_Synapse2_label")
        self.Spikeling_Synapse2_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_97.addWidget(self.Spikeling_Synapse2_label)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_label_frame)

        self.Spikeling_Synapse2_Title = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Title.setObjectName(u"Spikeling_Synapse2_Title")
        self.Spikeling_Synapse2_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.Spikeling_Synapse2_Title)
        self.horizontalLayout_168.setSpacing(0)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_toggle_frame = QFrame(self.Spikeling_Synapse2_Title)
        self.Spikeling_Synapse2_toggle_frame.setObjectName(u"Spikeling_Synapse2_toggle_frame")
        self.Spikeling_Synapse2_toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_Synapse2_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse2_toggle_layout = QHBoxLayout(self.Spikeling_Synapse2_toggle_frame)
        self.Spikeling_Synapse2_toggle_layout.setSpacing(0)
        self.Spikeling_Synapse2_toggle_layout.setObjectName(u"Spikeling_Synapse2_toggle_layout")
        self.Spikeling_Synapse2_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_168.addWidget(self.Spikeling_Synapse2_toggle_frame)

        self.Spikeling_Synapse2_Label_frame = QFrame(self.Spikeling_Synapse2_Title)
        self.Spikeling_Synapse2_Label_frame.setObjectName(u"Spikeling_Synapse2_Label_frame")
        self.Spikeling_Synapse2_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_171 = QHBoxLayout(self.Spikeling_Synapse2_Label_frame)
        self.horizontalLayout_171.setSpacing(0)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.horizontalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Label = QLabel(self.Spikeling_Synapse2_Label_frame)
        self.Spikeling_Synapse2_Label.setObjectName(u"Spikeling_Synapse2_Label")

        self.horizontalLayout_171.addWidget(self.Spikeling_Synapse2_Label)


        self.horizontalLayout_168.addWidget(self.Spikeling_Synapse2_Label_frame)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Title)

        self.Spikeling_Synapse2_readings_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_readings_frame.setObjectName(u"Spikeling_Synapse2_readings_frame")
        self.Spikeling_Synapse2_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.Spikeling_Synapse2_readings_frame)
        self.horizontalLayout_106.setSpacing(0)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_readings = QLabel(self.Spikeling_Synapse2_readings_frame)
        self.Spikeling_Synapse2_readings.setObjectName(u"Spikeling_Synapse2_readings")
        self.Spikeling_Synapse2_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_106.addWidget(self.Spikeling_Synapse2_readings)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_readings_frame)

        self.Spikeling_Synapse2_checkBox_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_checkBox_frame.setObjectName(u"Spikeling_Synapse2_checkBox_frame")
        self.Spikeling_Synapse2_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse2_Layout = QHBoxLayout(self.Spikeling_Synapse2_checkBox_frame)
        self.Spikeling_Synapse2_Layout.setSpacing(0)
        self.Spikeling_Synapse2_Layout.setObjectName(u"Spikeling_Synapse2_Layout")
        self.Spikeling_Synapse2_Layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_checkBox_frame)

        self.Spikeling_Synapse2_slider_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_slider_frame.setObjectName(u"Spikeling_Synapse2_slider_frame")
        self.Spikeling_Synapse2_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.Spikeling_Synapse2_slider_frame)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_slider = QSlider(self.Spikeling_Synapse2_slider_frame)
        self.Spikeling_Synapse2_slider.setObjectName(u"Spikeling_Synapse2_slider")
        self.Spikeling_Synapse2_slider.setEnabled(False)
        self.Spikeling_Synapse2_slider.setMinimum(-100)
        self.Spikeling_Synapse2_slider.setMaximum(100)
        self.Spikeling_Synapse2_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse2_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse2_slider.setTickInterval(20)

        self.horizontalLayout_100.addWidget(self.Spikeling_Synapse2_slider)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_slider_frame)

        self.Spikeling_Synapse2_values_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_values_frame.setObjectName(u"Spikeling_Synapse2_values_frame")
        self.Spikeling_Synapse2_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.Spikeling_Synapse2_values_frame)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 5)
        self.Spikeling_Synapse2_min = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_min.setObjectName(u"Spikeling_Synapse2_min")

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_min)

        self.Spikeling_Synapse2_0 = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_0.setObjectName(u"Spikeling_Synapse2_0")
        self.Spikeling_Synapse2_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_0)

        self.Spikeling_Synapse2_max = QLabel(self.Spikeling_Synapse2_values_frame)
        self.Spikeling_Synapse2_max.setObjectName(u"Spikeling_Synapse2_max")
        self.Spikeling_Synapse2_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.Spikeling_Synapse2_max)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_values_frame, 0, Qt.AlignTop)

        self.Spikeling_Synapse2_Decay_Title = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_Title.setObjectName(u"Spikeling_Synapse2_Decay_Title")
        self.Spikeling_Synapse2_Decay_Title.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.Spikeling_Synapse2_Decay_Title)
        self.horizontalLayout_170.setSpacing(0)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_toggle_frame = QFrame(self.Spikeling_Synapse2_Decay_Title)
        self.Spikeling_Synapse2_Decay_toggle_frame.setObjectName(u"Spikeling_Synapse2_Decay_toggle_frame")
        self.Spikeling_Synapse2_Decay_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_toggle_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse2_Decay_toggle_layout = QHBoxLayout(self.Spikeling_Synapse2_Decay_toggle_frame)
        self.Spikeling_Synapse2_Decay_toggle_layout.setSpacing(0)
        self.Spikeling_Synapse2_Decay_toggle_layout.setObjectName(u"Spikeling_Synapse2_Decay_toggle_layout")
        self.Spikeling_Synapse2_Decay_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_170.addWidget(self.Spikeling_Synapse2_Decay_toggle_frame)

        self.Spikeling_Synapse2_Decay_Label_frame = QFrame(self.Spikeling_Synapse2_Decay_Title)
        self.Spikeling_Synapse2_Decay_Label_frame.setObjectName(u"Spikeling_Synapse2_Decay_Label_frame")
        self.Spikeling_Synapse2_Decay_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_173 = QHBoxLayout(self.Spikeling_Synapse2_Decay_Label_frame)
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_Label = QLabel(self.Spikeling_Synapse2_Decay_Label_frame)
        self.Spikeling_Synapse2_Decay_Label.setObjectName(u"Spikeling_Synapse2_Decay_Label")

        self.horizontalLayout_173.addWidget(self.Spikeling_Synapse2_Decay_Label)


        self.horizontalLayout_170.addWidget(self.Spikeling_Synapse2_Decay_Label_frame)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_Title)

        self.Spikeling_Synapse2_Decay_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_frame.setObjectName(u"Spikeling_Synapse2_Decay_frame")
        sizePolicy4.setHeightForWidth(self.Spikeling_Synapse2_Decay_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_Synapse2_Decay_frame.setSizePolicy(sizePolicy4)
        self.Spikeling_Synapse2_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_frame.setFrameShadow(QFrame.Raised)
        self.Spikeling_Synapse2_Decay_Layout = QHBoxLayout(self.Spikeling_Synapse2_Decay_frame)
        self.Spikeling_Synapse2_Decay_Layout.setSpacing(0)
        self.Spikeling_Synapse2_Decay_Layout.setObjectName(u"Spikeling_Synapse2_Decay_Layout")
        self.Spikeling_Synapse2_Decay_Layout.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_readings = QLabel(self.Spikeling_Synapse2_Decay_frame)
        self.Spikeling_Synapse2_Decay_readings.setObjectName(u"Spikeling_Synapse2_Decay_readings")
        self.Spikeling_Synapse2_Decay_readings.setAlignment(Qt.AlignCenter)

        self.Spikeling_Synapse2_Decay_Layout.addWidget(self.Spikeling_Synapse2_Decay_readings)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_frame)

        self.Spikeling_Synapse2_Decay_readings_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_readings_frame.setObjectName(u"Spikeling_Synapse2_Decay_readings_frame")
        self.Spikeling_Synapse2_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.Spikeling_Synapse2_Decay_readings_frame)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_readings_frame)

        self.Spikeling_Synapse2_Decay_slider_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_slider_frame.setObjectName(u"Spikeling_Synapse2_Decay_slider_frame")
        self.Spikeling_Synapse2_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.Spikeling_Synapse2_Decay_slider_frame)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_slider = QSlider(self.Spikeling_Synapse2_Decay_slider_frame)
        self.Spikeling_Synapse2_Decay_slider.setObjectName(u"Spikeling_Synapse2_Decay_slider")
        self.Spikeling_Synapse2_Decay_slider.setEnabled(False)
        self.Spikeling_Synapse2_Decay_slider.setMinimum(975)
        self.Spikeling_Synapse2_Decay_slider.setMaximum(1000)
        self.Spikeling_Synapse2_Decay_slider.setPageStep(10)
        self.Spikeling_Synapse2_Decay_slider.setValue(995)
        self.Spikeling_Synapse2_Decay_slider.setSliderPosition(995)
        self.Spikeling_Synapse2_Decay_slider.setOrientation(Qt.Horizontal)
        self.Spikeling_Synapse2_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Spikeling_Synapse2_Decay_slider.setTickInterval(2)

        self.verticalLayout_81.addWidget(self.Spikeling_Synapse2_Decay_slider)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_slider_frame)

        self.Spikeling_Synapse2_Decay_values_frame = QFrame(self.Spikeling_Synapse2_frame)
        self.Spikeling_Synapse2_Decay_values_frame.setObjectName(u"Spikeling_Synapse2_Decay_values_frame")
        self.Spikeling_Synapse2_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_Synapse2_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.Spikeling_Synapse2_Decay_values_frame)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_Synapse2_Decay_values_slow = QLabel(self.Spikeling_Synapse2_Decay_values_frame)
        self.Spikeling_Synapse2_Decay_values_slow.setObjectName(u"Spikeling_Synapse2_Decay_values_slow")

        self.horizontalLayout_47.addWidget(self.Spikeling_Synapse2_Decay_values_slow)

        self.Spikeling_Synapse2_Decay_values_fast = QLabel(self.Spikeling_Synapse2_Decay_values_frame)
        self.Spikeling_Synapse2_Decay_values_fast.setObjectName(u"Spikeling_Synapse2_Decay_values_fast")
        self.Spikeling_Synapse2_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.Spikeling_Synapse2_Decay_values_fast)


        self.verticalLayout_33.addWidget(self.Spikeling_Synapse2_Decay_values_frame)


        self.verticalLayout_17.addWidget(self.Spikeling_Synapse2_frame)


        self.verticalLayout_57.addWidget(self.Spikeling_NeuronParameter_frame)

        self.Spikeling_parameter_stackedwidget.addWidget(self.NeuronParameter_page)

        self.verticalLayout_54.addWidget(self.Spikeling_parameter_stackedwidget)


        self.horizontalLayout_34.addWidget(self.Spikeling_CenterMenuContainer)

        self.Spikeling_rightMenuContainer = QWidget(self.page_101)
        self.Spikeling_rightMenuContainer.setObjectName(u"Spikeling_rightMenuContainer")
        self.Spikeling_rightMenuContainer.setMinimumSize(QSize(40, 0))
        self.Spikeling_rightMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout_53 = QVBoxLayout(self.Spikeling_rightMenuContainer)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_rightMenuSubContainer = QWidget(self.Spikeling_rightMenuContainer)
        self.Spikeling_rightMenuSubContainer.setObjectName(u"Spikeling_rightMenuSubContainer")
        self.verticalLayout_55 = QVBoxLayout(self.Spikeling_rightMenuSubContainer)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 5, 0)
        self.Spikeling_rightMenuSubContainer_frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.Spikeling_rightMenuSubContainer_frame.setObjectName(u"Spikeling_rightMenuSubContainer_frame")
        self.Spikeling_rightMenuSubContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_rightMenuSubContainer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.Spikeling_rightMenuSubContainer_frame)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 20, 0, 0)
        self.Spikeling_rightMenuSubContainer_pushButton = QPushButton(self.Spikeling_rightMenuSubContainer_frame)
        self.Spikeling_rightMenuSubContainer_pushButton.setObjectName(u"Spikeling_rightMenuSubContainer_pushButton")
        self.Spikeling_rightMenuSubContainer_pushButton.setMinimumSize(QSize(0, 0))
        self.Spikeling_rightMenuSubContainer_pushButton.setFont(font1)
        self.Spikeling_rightMenuSubContainer_pushButton.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spikeling_rightMenuSubContainer_pushButton.setIcon(icon19)
        self.Spikeling_rightMenuSubContainer_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_79.addWidget(self.Spikeling_rightMenuSubContainer_pushButton)


        self.verticalLayout_55.addWidget(self.Spikeling_rightMenuSubContainer_frame, 0, Qt.AlignTop)

        self.Spikeling_rightMenuParameterContainer_frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.Spikeling_rightMenuParameterContainer_frame.setObjectName(u"Spikeling_rightMenuParameterContainer_frame")
        self.Spikeling_rightMenuParameterContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_rightMenuParameterContainer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.Spikeling_rightMenuParameterContainer_frame)
        self.verticalLayout_56.setSpacing(50)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_StimulusParameter_pushButton = QPushButton(self.Spikeling_rightMenuParameterContainer_frame)
        self.Spikeling_StimulusParameter_pushButton.setObjectName(u"Spikeling_StimulusParameter_pushButton")
        self.Spikeling_StimulusParameter_pushButton.setFont(font1)
        self.Spikeling_StimulusParameter_pushButton.setIcon(icon8)
        self.Spikeling_StimulusParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_56.addWidget(self.Spikeling_StimulusParameter_pushButton)

        self.Spikeling_NeuronParameter_pushButton = QPushButton(self.Spikeling_rightMenuParameterContainer_frame)
        self.Spikeling_NeuronParameter_pushButton.setObjectName(u"Spikeling_NeuronParameter_pushButton")
        self.Spikeling_NeuronParameter_pushButton.setFont(font1)
        self.Spikeling_NeuronParameter_pushButton.setIcon(icon5)
        self.Spikeling_NeuronParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_56.addWidget(self.Spikeling_NeuronParameter_pushButton)


        self.verticalLayout_55.addWidget(self.Spikeling_rightMenuParameterContainer_frame)

        self.frame = QFrame(self.Spikeling_rightMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_55.addWidget(self.frame)


        self.verticalLayout_53.addWidget(self.Spikeling_rightMenuSubContainer)


        self.horizontalLayout_34.addWidget(self.Spikeling_rightMenuContainer)

        self.mainbody_stackedWidget.addWidget(self.page_101)
        self.page_102 = QWidget()
        self.page_102.setObjectName(u"page_102")
        self.horizontalLayout_66 = QHBoxLayout(self.page_102)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.page_102)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_42)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_67.addWidget(self.label_2)


        self.horizontalLayout_66.addWidget(self.frame_42)

        self.mainbody_stackedWidget.addWidget(self.page_102)
        self.page_103 = QWidget()
        self.page_103.setObjectName(u"page_103")
        self.horizontalLayout_68 = QHBoxLayout(self.page_103)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_frame = QFrame(self.page_103)
        self.DataAnalysis_frame.setObjectName(u"DataAnalysis_frame")
        self.DataAnalysis_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.DataAnalysis_frame)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Display_frame = QFrame(self.DataAnalysis_frame)
        self.DataAnalysis_Display_frame.setObjectName(u"DataAnalysis_Display_frame")
        self.DataAnalysis_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Display_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.DataAnalysis_Display_frame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Display_StackedWidget = QStackedWidget(self.DataAnalysis_Display_frame)
        self.DataAnalysis_Display_StackedWidget.setObjectName(u"DataAnalysis_Display_StackedWidget")
        self.page_103_1_0 = QWidget()
        self.page_103_1_0.setObjectName(u"page_103_1_0")
        self.verticalLayout_39 = QVBoxLayout(self.page_103_1_0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_0_0 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_0)

        self.line_7 = QFrame(self.page_103_1_0)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_7)

        self.DataAnalysis_Oscilloscope_widget1_0_1 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_1)

        self.line_31 = QFrame(self.page_103_1_0)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_31)

        self.DataAnalysis_Oscilloscope_widget1_0_2 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_2)

        self.line_8 = QFrame(self.page_103_1_0)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_8)

        self.DataAnalysis_Oscilloscope_widget1_0_3 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_3)

        self.line_32 = QFrame(self.page_103_1_0)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_32)

        self.DataAnalysis_Neurons_pushButton10_frame = QFrame(self.page_103_1_0)
        self.DataAnalysis_Neurons_pushButton10_frame.setObjectName(u"DataAnalysis_Neurons_pushButton10_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton10_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton10_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton10_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton10_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton10_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton10_frame)
        self.horizontalLayout_80.setSpacing(5)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron0Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton10")
        self.DataAnalysis_Neuron0Vm_pushButton10.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton10.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton10.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron0Vm_pushButton10)

        self.DataAnalysis_Neuron1Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron1Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton10")
        self.DataAnalysis_Neuron1Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton10.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron1Vm_pushButton10)

        self.DataAnalysis_Neuron2Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron2Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(25)
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton10.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton10.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton10.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron2Vm_pushButton10)


        self.verticalLayout_39.addWidget(self.DataAnalysis_Neurons_pushButton10_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_0)
        self.page_103_1_1 = QWidget()
        self.page_103_1_1.setObjectName(u"page_103_1_1")
        self.verticalLayout_48 = QVBoxLayout(self.page_103_1_1)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_1_0 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_0)

        self.line_10 = QFrame(self.page_103_1_1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_10)

        self.DataAnalysis_Oscilloscope_widget1_1_1 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_1)

        self.line_9 = QFrame(self.page_103_1_1)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_9)

        self.DataAnalysis_Oscilloscope_widget1_1_2 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_2)

        self.line_33 = QFrame(self.page_103_1_1)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_48.addWidget(self.line_33)

        self.DataAnalysis_Neurons_pushButton11_frame = QFrame(self.page_103_1_1)
        self.DataAnalysis_Neurons_pushButton11_frame.setObjectName(u"DataAnalysis_Neurons_pushButton11_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton11_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton11_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton11_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton11_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton11_frame)
        self.horizontalLayout_101.setSpacing(5)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron0Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton11")
        self.DataAnalysis_Neuron0Vm_pushButton11.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton11.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton11.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron0Vm_pushButton11)

        self.DataAnalysis_Neuron1Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron1Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton11")
        self.DataAnalysis_Neuron1Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton11.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron1Vm_pushButton11)

        self.DataAnalysis_Neuron2Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron2Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton11")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton11.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton11.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton11.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron2Vm_pushButton11)


        self.verticalLayout_48.addWidget(self.DataAnalysis_Neurons_pushButton11_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_1)
        self.page_103_1_2 = QWidget()
        self.page_103_1_2.setObjectName(u"page_103_1_2")
        self.verticalLayout_49 = QVBoxLayout(self.page_103_1_2)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget1_2_0 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_0)

        self.line_30 = QFrame(self.page_103_1_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_30)

        self.DataAnalysis_Oscilloscope_widget1_2_1 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMinimumSize(QSize(0, 0))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMaximumSize(QSize(16777215, 16777215))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_1)

        self.line_29 = QFrame(self.page_103_1_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_29)

        self.DataAnalysis_Oscilloscope_widget1_2_2 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMaximumSize(QSize(16777215, 150))
        font6 = QFont()
        font6.setPointSize(11)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setFont(font6)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_2)

        self.line_34 = QFrame(self.page_103_1_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_49.addWidget(self.line_34)

        self.DataAnalysis_Neurons_pushButton12_frame = QFrame(self.page_103_1_2)
        self.DataAnalysis_Neurons_pushButton12_frame.setObjectName(u"DataAnalysis_Neurons_pushButton12_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton12_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton12_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton12_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton12_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton12_frame)
        self.horizontalLayout_103.setSpacing(5)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron0Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton12")
        self.DataAnalysis_Neuron0Vm_pushButton12.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton12.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton12.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron0Vm_pushButton12)

        self.DataAnalysis_Neuron1Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron1Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton12")
        self.DataAnalysis_Neuron1Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton12.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron1Vm_pushButton12)

        self.DataAnalysis_Neuron2Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron2Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton12")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton12.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton12.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton12.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron2Vm_pushButton12)


        self.verticalLayout_49.addWidget(self.DataAnalysis_Neurons_pushButton12_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_1_2)
        self.page_103_2_0 = QWidget()
        self.page_103_2_0.setObjectName(u"page_103_2_0")
        self.verticalLayout_42 = QVBoxLayout(self.page_103_2_0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_0_0 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_0)

        self.line_14 = QFrame(self.page_103_2_0)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_14)

        self.DataAnalysis_Oscilloscope_widget2_0_1 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_1)

        self.line_13 = QFrame(self.page_103_2_0)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_13)

        self.DataAnalysis_Oscilloscope_widget2_0_2 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_2)

        self.line_11 = QFrame(self.page_103_2_0)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_11)

        self.DataAnalysis_Oscilloscope_widget2_0_3 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_3)

        self.line_35 = QFrame(self.page_103_2_0)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_42.addWidget(self.line_35)

        self.DataAnalysis_Neurons_pushButton20_frame = QFrame(self.page_103_2_0)
        self.DataAnalysis_Neurons_pushButton20_frame.setObjectName(u"DataAnalysis_Neurons_pushButton20_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton20_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton20_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton20_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton20_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton20_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton20_frame)
        self.horizontalLayout_105.setSpacing(5)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron0Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton20")
        self.DataAnalysis_Neuron0Vm_pushButton20.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton20.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton20.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron0Vm_pushButton20)

        self.DataAnalysis_Neuron1Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron1Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton20")
        self.DataAnalysis_Neuron1Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton20.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron1Vm_pushButton20)

        self.DataAnalysis_Neuron2Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron2Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton20")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton20.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton20.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton20.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron2Vm_pushButton20)


        self.verticalLayout_42.addWidget(self.DataAnalysis_Neurons_pushButton20_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_0)
        self.page_103_2_1 = QWidget()
        self.page_103_2_1.setObjectName(u"page_103_2_1")
        self.verticalLayout_43 = QVBoxLayout(self.page_103_2_1)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_1_0 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_0)

        self.line_16 = QFrame(self.page_103_2_1)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_16)

        self.DataAnalysis_Oscilloscope_widget2_1_1 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_1)

        self.line_15 = QFrame(self.page_103_2_1)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_15)

        self.DataAnalysis_Oscilloscope_widget2_1_2 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_2)

        self.line_12 = QFrame(self.page_103_2_1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_12)

        self.DataAnalysis_Oscilloscope_widget2_1_3 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_3)

        self.line_36 = QFrame(self.page_103_2_1)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_43.addWidget(self.line_36)

        self.DataAnalysis_Neurons_pushButton21_frame = QFrame(self.page_103_2_1)
        self.DataAnalysis_Neurons_pushButton21_frame.setObjectName(u"DataAnalysis_Neurons_pushButton21_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton21_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton21_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton21_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton21_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton21_frame)
        self.horizontalLayout_107.setSpacing(5)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron0Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton21")
        self.DataAnalysis_Neuron0Vm_pushButton21.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton21.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton21.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron0Vm_pushButton21)

        self.DataAnalysis_Neuron1Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron1Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton21")
        self.DataAnalysis_Neuron1Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton21.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron1Vm_pushButton21)

        self.DataAnalysis_Neuron2Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron2Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton21")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton21.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton21.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton21.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron2Vm_pushButton21)


        self.verticalLayout_43.addWidget(self.DataAnalysis_Neurons_pushButton21_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_1)
        self.page_103_2_2 = QWidget()
        self.page_103_2_2.setObjectName(u"page_103_2_2")
        self.verticalLayout_44 = QVBoxLayout(self.page_103_2_2)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget2_2_0 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_0)

        self.line_18 = QFrame(self.page_103_2_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_18)

        self.DataAnalysis_Oscilloscope_widget2_2_1 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_1)

        self.line_17 = QFrame(self.page_103_2_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_17)

        self.DataAnalysis_Oscilloscope_widget2_2_2 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_2)

        self.line_19 = QFrame(self.page_103_2_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_19)

        self.DataAnalysis_Oscilloscope_widget2_2_3 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_3)

        self.line_37 = QFrame(self.page_103_2_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_44.addWidget(self.line_37)

        self.DataAnalysis_Neurons_pushButton22_frame = QFrame(self.page_103_2_2)
        self.DataAnalysis_Neurons_pushButton22_frame.setObjectName(u"DataAnalysis_Neurons_pushButton22_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton22_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton22_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton22_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton22_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton22_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton22_frame)
        self.horizontalLayout_108.setSpacing(5)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron0Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton22")
        self.DataAnalysis_Neuron0Vm_pushButton22.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton22.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton22.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron0Vm_pushButton22)

        self.DataAnalysis_Neuron1Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron1Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton22")
        self.DataAnalysis_Neuron1Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton22.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron1Vm_pushButton22)

        self.DataAnalysis_Neuron2Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron2Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton22")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton22.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton22.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton22.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron2Vm_pushButton22)


        self.verticalLayout_44.addWidget(self.DataAnalysis_Neurons_pushButton22_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_2_2)
        self.page_103_3_0 = QWidget()
        self.page_103_3_0.setObjectName(u"page_103_3_0")
        self.verticalLayout_45 = QVBoxLayout(self.page_103_3_0)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_0_0 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_0)

        self.line_20 = QFrame(self.page_103_3_0)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_20)

        self.DataAnalysis_Oscilloscope_widget3_0_1 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_1")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_1.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_1)

        self.line_22 = QFrame(self.page_103_3_0)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_22)

        self.DataAnalysis_Oscilloscope_widget3_0_2 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_2)

        self.line_21 = QFrame(self.page_103_3_0)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_21)

        self.DataAnalysis_Oscilloscope_widget3_0_3 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_3)

        self.line_38 = QFrame(self.page_103_3_0)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_38)

        self.DataAnalysis_Neurons_pushButton30_frame = QFrame(self.page_103_3_0)
        self.DataAnalysis_Neurons_pushButton30_frame.setObjectName(u"DataAnalysis_Neurons_pushButton30_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton30_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton30_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton30_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton30_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton30_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton30_frame)
        self.horizontalLayout_109.setSpacing(5)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron0Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton30")
        self.DataAnalysis_Neuron0Vm_pushButton30.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton30.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton30.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron0Vm_pushButton30)

        self.DataAnalysis_Neuron1Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron1Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton30")
        self.DataAnalysis_Neuron1Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton30.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron1Vm_pushButton30)

        self.DataAnalysis_Neuron2Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron2Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton30")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton30.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton30.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton30.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron2Vm_pushButton30)


        self.verticalLayout_45.addWidget(self.DataAnalysis_Neurons_pushButton30_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_0)
        self.page_103_3_1 = QWidget()
        self.page_103_3_1.setObjectName(u"page_103_3_1")
        self.verticalLayout_46 = QVBoxLayout(self.page_103_3_1)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_1_0 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_0)

        self.line_23 = QFrame(self.page_103_3_1)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_23)

        self.DataAnalysis_Oscilloscope_widget3_1_1 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_1)

        self.line_25 = QFrame(self.page_103_3_1)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_25)

        self.DataAnalysis_Oscilloscope_widget3_1_2 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_2)

        self.line_24 = QFrame(self.page_103_3_1)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_24)

        self.DataAnalysis_Oscilloscope_widget3_1_3 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_3)

        self.line_39 = QFrame(self.page_103_3_1)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_39)

        self.DataAnalysis_Neurons_pushButton31_frame = QFrame(self.page_103_3_1)
        self.DataAnalysis_Neurons_pushButton31_frame.setObjectName(u"DataAnalysis_Neurons_pushButton31_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton31_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton31_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton31_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton31_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton31_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton31_frame)
        self.horizontalLayout_110.setSpacing(5)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron0Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton31")
        self.DataAnalysis_Neuron0Vm_pushButton31.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton31.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton31.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron0Vm_pushButton31)

        self.DataAnalysis_Neuron1Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron1Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton31")
        self.DataAnalysis_Neuron1Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton31.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron1Vm_pushButton31)

        self.DataAnalysis_Neuron2Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron2Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton31")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton31.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton31.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton31.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron2Vm_pushButton31)


        self.verticalLayout_46.addWidget(self.DataAnalysis_Neurons_pushButton31_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_1)
        self.page_103_3_2 = QWidget()
        self.page_103_3_2.setObjectName(u"page_103_3_2")
        self.verticalLayout_47 = QVBoxLayout(self.page_103_3_2)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget3_2_0 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_0.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_0")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_0.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_0)

        self.line_26 = QFrame(self.page_103_3_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_26)

        self.DataAnalysis_Oscilloscope_widget3_2_1 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_1)

        self.line_28 = QFrame(self.page_103_3_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_28)

        self.DataAnalysis_Oscilloscope_widget3_2_2 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_2")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_2.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_2)

        self.line_27 = QFrame(self.page_103_3_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_27)

        self.DataAnalysis_Oscilloscope_widget3_2_3 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_3")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_3.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_3)

        self.line_40 = QFrame(self.page_103_3_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_40)

        self.DataAnalysis_Neurons_pushButton32_frame = QFrame(self.page_103_3_2)
        self.DataAnalysis_Neurons_pushButton32_frame.setObjectName(u"DataAnalysis_Neurons_pushButton32_frame")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Neurons_pushButton32_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton32_frame.setSizePolicy(sizePolicy3)
        self.DataAnalysis_Neurons_pushButton32_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton32_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton32_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton32_frame)
        self.horizontalLayout_111.setSpacing(5)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron0Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton32")
        self.DataAnalysis_Neuron0Vm_pushButton32.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton32.setFont(font2)
        self.DataAnalysis_Neuron0Vm_pushButton32.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron0Vm_pushButton32)

        self.DataAnalysis_Neuron1Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron1Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton32")
        self.DataAnalysis_Neuron1Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setFont(font2)
        self.DataAnalysis_Neuron1Vm_pushButton32.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron1Vm_pushButton32)

        self.DataAnalysis_Neuron2Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron2Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton32")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton32.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton32.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setFont(font2)
        self.DataAnalysis_Neuron2Vm_pushButton32.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron2Vm_pushButton32)


        self.verticalLayout_47.addWidget(self.DataAnalysis_Neurons_pushButton32_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_2)

        self.verticalLayout_35.addWidget(self.DataAnalysis_Display_StackedWidget)


        self.horizontalLayout_61.addWidget(self.DataAnalysis_Display_frame)

        self.DataAnalysis_groupBox = QGroupBox(self.DataAnalysis_frame)
        self.DataAnalysis_groupBox.setObjectName(u"DataAnalysis_groupBox")
        sizePolicy.setHeightForWidth(self.DataAnalysis_groupBox.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_groupBox.setSizePolicy(sizePolicy)
        self.DataAnalysis_groupBox.setMinimumSize(QSize(250, 0))
        self.DataAnalysis_groupBox.setMaximumSize(QSize(250, 16777215))
        self.DataAnalysis_groupBox.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.DataAnalysis_groupBox)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 1)
        self.DataAnalysis_LoadData_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_LoadData_frame.setObjectName(u"DataAnalysis_LoadData_frame")
        self.DataAnalysis_LoadData_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_LoadData_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.DataAnalysis_LoadData_frame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(15, -1, 15, -1)
        self.DataAnalysis_LoadData_subframe = QFrame(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_LoadData_subframe.setObjectName(u"DataAnalysis_LoadData_subframe")
        self.DataAnalysis_LoadData_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_LoadData_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.DataAnalysis_LoadData_subframe)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_LoadData_label = QLabel(self.DataAnalysis_LoadData_subframe)
        self.DataAnalysis_LoadData_label.setObjectName(u"DataAnalysis_LoadData_label")
        sizePolicy4.setHeightForWidth(self.DataAnalysis_LoadData_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_LoadData_label.setSizePolicy(sizePolicy4)
        self.DataAnalysis_LoadData_label.setWordWrap(True)

        self.horizontalLayout_62.addWidget(self.DataAnalysis_LoadData_label)

        self.DataAnalysis_LoadData_pushButton = QPushButton(self.DataAnalysis_LoadData_subframe)
        self.DataAnalysis_LoadData_pushButton.setObjectName(u"DataAnalysis_LoadData_pushButton")
        self.DataAnalysis_LoadData_pushButton.setIconSize(QSize(14, 16))

        self.horizontalLayout_62.addWidget(self.DataAnalysis_LoadData_pushButton)


        self.verticalLayout_36.addWidget(self.DataAnalysis_LoadData_subframe)

        self.DataAnalysis_LoadData_Display_pushButton = QPushButton(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_LoadData_Display_pushButton.setObjectName(u"DataAnalysis_LoadData_Display_pushButton")

        self.verticalLayout_36.addWidget(self.DataAnalysis_LoadData_Display_pushButton)

        self.DataAnalysis_SaveImage_pushButton = QPushButton(self.DataAnalysis_LoadData_frame)
        self.DataAnalysis_SaveImage_pushButton.setObjectName(u"DataAnalysis_SaveImage_pushButton")

        self.verticalLayout_36.addWidget(self.DataAnalysis_SaveImage_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_LoadData_frame)

        self.DataAnalysis_LoadData_line = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_LoadData_line.setObjectName(u"DataAnalysis_LoadData_line")
        self.DataAnalysis_LoadData_line.setFrameShape(QFrame.HLine)
        self.DataAnalysis_LoadData_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.DataAnalysis_LoadData_line)

        self.DataAnalysis_Spike_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_Spike_frame.setObjectName(u"DataAnalysis_Spike_frame")
        self.DataAnalysis_Spike_frame.setStyleSheet(u"")
        self.DataAnalysis_Spike_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Spike_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.DataAnalysis_Spike_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(15, -1, 15, -1)
        self.DataAnalysis_Spike_label = QLabel(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_label.setObjectName(u"DataAnalysis_Spike_label")
        self.DataAnalysis_Spike_label.setFont(font4)

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_label, 0, Qt.AlignHCenter)

        self.DataAnalysis_Spike_subframe = QFrame(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_subframe.setObjectName(u"DataAnalysis_Spike_subframe")
        self.DataAnalysis_Spike_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Spike_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.DataAnalysis_Spike_subframe)
        self.horizontalLayout_69.setSpacing(5)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Spike_threshold_label = QLabel(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_threshold_label.setObjectName(u"DataAnalysis_Spike_threshold_label")
        sizePolicy4.setHeightForWidth(self.DataAnalysis_Spike_threshold_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Spike_threshold_label.setSizePolicy(sizePolicy4)

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_threshold_label)

        self.DataAnalysis_Spike_lineEdit = QLineEdit(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_lineEdit.setObjectName(u"DataAnalysis_Spike_lineEdit")
        self.DataAnalysis_Spike_lineEdit.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.DataAnalysis_Spike_lineEdit.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Spike_lineEdit.setSizePolicy(sizePolicy6)
        self.DataAnalysis_Spike_lineEdit.setMinimumSize(QSize(50, 0))
        self.DataAnalysis_Spike_lineEdit.setMaximumSize(QSize(50, 16777215))
        self.DataAnalysis_Spike_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_lineEdit, 0, Qt.AlignRight)

        self.DataAnalysis_Spike_mV_label = QLabel(self.DataAnalysis_Spike_subframe)
        self.DataAnalysis_Spike_mV_label.setObjectName(u"DataAnalysis_Spike_mV_label")

        self.horizontalLayout_69.addWidget(self.DataAnalysis_Spike_mV_label, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_subframe)

        self.DataAnalysis_Spike_result_label = QLabel(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_result_label.setObjectName(u"DataAnalysis_Spike_result_label")
        self.DataAnalysis_Spike_result_label.setFont(font4)
        self.DataAnalysis_Spike_result_label.setStyleSheet(u"")
        self.DataAnalysis_Spike_result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_result_label)

        self.DataAnalysis_Spike_Display_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_Display_pushButton.setObjectName(u"DataAnalysis_Spike_Display_pushButton")
        self.DataAnalysis_Spike_Display_pushButton.setEnabled(False)

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_Display_pushButton)

        self.DataAnalysis_Spike_SaveImage_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_SaveImage_pushButton.setObjectName(u"DataAnalysis_Spike_SaveImage_pushButton")

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_SaveImage_pushButton)

        self.DataAnalysis_Spike_Export_pushButton = QPushButton(self.DataAnalysis_Spike_frame)
        self.DataAnalysis_Spike_Export_pushButton.setObjectName(u"DataAnalysis_Spike_Export_pushButton")

        self.verticalLayout_41.addWidget(self.DataAnalysis_Spike_Export_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_Spike_frame)

        self.DataAnalysis_Spike_line = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_Spike_line.setObjectName(u"DataAnalysis_Spike_line")
        self.DataAnalysis_Spike_line.setFrameShape(QFrame.HLine)
        self.DataAnalysis_Spike_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.DataAnalysis_Spike_line)

        self.DataAnalysis_Average_frame = QFrame(self.DataAnalysis_groupBox)
        self.DataAnalysis_Average_frame.setObjectName(u"DataAnalysis_Average_frame")
        self.DataAnalysis_Average_frame.setStyleSheet(u"")
        self.DataAnalysis_Average_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Average_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.DataAnalysis_Average_frame)
        self.verticalLayout_40.setSpacing(6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(15, 9, 15, 5)
        self.DataAnalysis_Average_result_label = QLabel(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_result_label.setObjectName(u"DataAnalysis_Average_result_label")
        self.DataAnalysis_Average_result_label.setFont(font4)
        self.DataAnalysis_Average_result_label.setScaledContents(False)
        self.DataAnalysis_Average_result_label.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_result_label, 0, Qt.AlignHCenter)

        self.DataAnalysis_Average_label = QLabel(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_label.setObjectName(u"DataAnalysis_Average_label")
        self.DataAnalysis_Average_label.setFont(font4)
        self.DataAnalysis_Average_label.setStyleSheet(u"")
        self.DataAnalysis_Average_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_label)

        self.DataAnalysis_Average_Display_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_Display_pushButton.setObjectName(u"DataAnalysis_Average_Display_pushButton")
        self.DataAnalysis_Average_Display_pushButton.setEnabled(False)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_Display_pushButton)

        self.DataAnalysis_Average_SaveImage_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_SaveImage_pushButton.setObjectName(u"DataAnalysis_Average_SaveImage_pushButton")

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_SaveImage_pushButton)

        self.DataAnalysis_Average_Save_pushButton = QPushButton(self.DataAnalysis_Average_frame)
        self.DataAnalysis_Average_Save_pushButton.setObjectName(u"DataAnalysis_Average_Save_pushButton")
        self.DataAnalysis_Average_Save_pushButton.setEnabled(False)

        self.verticalLayout_40.addWidget(self.DataAnalysis_Average_Save_pushButton)


        self.verticalLayout_34.addWidget(self.DataAnalysis_Average_frame)


        self.horizontalLayout_61.addWidget(self.DataAnalysis_groupBox)


        self.horizontalLayout_68.addWidget(self.DataAnalysis_frame)

        self.mainbody_stackedWidget.addWidget(self.page_103)
        self.page_201 = QWidget()
        self.page_201.setObjectName(u"page_201")
        self.horizontalLayout_70 = QHBoxLayout(self.page_201)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Imaging_widget = QFrame(self.page_201)
        self.Imaging_widget.setObjectName(u"Imaging_widget")
        self.Imaging_widget.setFrameShape(QFrame.StyledPanel)
        self.Imaging_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.Imaging_widget)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Imaging_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_119.setSpacing(0)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_158.setSpacing(0)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_158.addWidget(self.label_4)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_158.addWidget(self.comboBox)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_158.addWidget(self.frame_6)


        self.horizontalLayout_119.addWidget(self.frame_4)


        self.verticalLayout_109.addWidget(self.frame_3)

        self.Imaging_Oscilloscope_frame = QFrame(self.Imaging_widget)
        self.Imaging_Oscilloscope_frame.setObjectName(u"Imaging_Oscilloscope_frame")
        self.Imaging_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.Imaging_Oscilloscope_frame)
        self.horizontalLayout_157.setSpacing(0)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Oscilloscope_widget = PlotWidget(self.Imaging_Oscilloscope_frame)
        self.Imaging_Oscilloscope_widget.setObjectName(u"Imaging_Oscilloscope_widget")
        sizePolicy5.setHeightForWidth(self.Imaging_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.Imaging_Oscilloscope_widget.setSizePolicy(sizePolicy5)
        self.Imaging_Oscilloscope_widget.setAutoFillBackground(False)
        self.Imaging_Oscilloscope_widget.setStyleSheet(u"")
        self.horizontalLayout_178 = QHBoxLayout(self.Imaging_Oscilloscope_widget)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.Imaging_Oscilloscope_Traces_frame = QFrame(self.Imaging_Oscilloscope_widget)
        self.Imaging_Oscilloscope_Traces_frame.setObjectName(u"Imaging_Oscilloscope_Traces_frame")
        self.Imaging_Oscilloscope_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_Traces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.Imaging_Oscilloscope_Traces_frame)
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Oscilloscope_FirstTraces_frame = QFrame(self.Imaging_Oscilloscope_Traces_frame)
        self.Imaging_Oscilloscope_FirstTraces_frame.setObjectName(u"Imaging_Oscilloscope_FirstTraces_frame")
        self.Imaging_Oscilloscope_FirstTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_FirstTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.Imaging_InputCurrentCheckbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_InputCurrentCheckbox.setObjectName(u"Imaging_InputCurrentCheckbox")
        self.Imaging_InputCurrentCheckbox.setEnabled(True)
        self.Imaging_InputCurrentCheckbox.setAutoFillBackground(False)
        self.Imaging_InputCurrentCheckbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.Imaging_InputCurrentCheckbox.setChecked(True)

        self.horizontalLayout_116.addWidget(self.Imaging_InputCurrentCheckbox)

        self.Imaging_VmCheckbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_VmCheckbox.setObjectName(u"Imaging_VmCheckbox")
        self.Imaging_VmCheckbox.setEnabled(True)
        self.Imaging_VmCheckbox.setAutoFillBackground(False)
        self.Imaging_VmCheckbox.setStyleSheet(u"color: rgb(220, 50, 47);")
        self.Imaging_VmCheckbox.setChecked(True)

        self.horizontalLayout_116.addWidget(self.Imaging_VmCheckbox)

        self.Imaging_StimulusCheckbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_StimulusCheckbox.setObjectName(u"Imaging_StimulusCheckbox")
        self.Imaging_StimulusCheckbox.setEnabled(True)
        self.Imaging_StimulusCheckbox.setAutoFillBackground(False)
        self.Imaging_StimulusCheckbox.setStyleSheet(u"color: rgb(38, 139, 210);")
        self.Imaging_StimulusCheckbox.setChecked(True)

        self.horizontalLayout_116.addWidget(self.Imaging_StimulusCheckbox)


        self.horizontalLayout_177.addWidget(self.Imaging_Oscilloscope_FirstTraces_frame)

        self.Imaging_Oscilloscope_SecondTraces_frame = QFrame(self.Imaging_Oscilloscope_Traces_frame)
        self.Imaging_Oscilloscope_SecondTraces_frame.setObjectName(u"Imaging_Oscilloscope_SecondTraces_frame")
        self.Imaging_Oscilloscope_SecondTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_SecondTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_175 = QHBoxLayout(self.Imaging_Oscilloscope_SecondTraces_frame)
        self.horizontalLayout_175.setSpacing(0)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Syn1VmCheckbox = QCheckBox(self.Imaging_Oscilloscope_SecondTraces_frame)
        self.Imaging_Syn1VmCheckbox.setObjectName(u"Imaging_Syn1VmCheckbox")
        self.Imaging_Syn1VmCheckbox.setEnabled(True)
        self.Imaging_Syn1VmCheckbox.setAutoFillBackground(False)
        self.Imaging_Syn1VmCheckbox.setStyleSheet(u"color: rgb(203, 75, 22);")
        self.Imaging_Syn1VmCheckbox.setChecked(False)

        self.horizontalLayout_175.addWidget(self.Imaging_Syn1VmCheckbox)

        self.Imaging_Syn1InputCheckbox = QCheckBox(self.Imaging_Oscilloscope_SecondTraces_frame)
        self.Imaging_Syn1InputCheckbox.setObjectName(u"Imaging_Syn1InputCheckbox")
        self.Imaging_Syn1InputCheckbox.setEnabled(True)
        self.Imaging_Syn1InputCheckbox.setAutoFillBackground(False)
        self.Imaging_Syn1InputCheckbox.setStyleSheet(u"color: rgb(42, 161, 152);")
        self.Imaging_Syn1InputCheckbox.setChecked(False)

        self.horizontalLayout_175.addWidget(self.Imaging_Syn1InputCheckbox)


        self.horizontalLayout_177.addWidget(self.Imaging_Oscilloscope_SecondTraces_frame)

        self.Imaging_Oscilloscope_ThirdTraces_frame = QFrame(self.Imaging_Oscilloscope_Traces_frame)
        self.Imaging_Oscilloscope_ThirdTraces_frame.setObjectName(u"Imaging_Oscilloscope_ThirdTraces_frame")
        self.Imaging_Oscilloscope_ThirdTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_ThirdTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.Imaging_Oscilloscope_ThirdTraces_frame)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Syn2VmCheckbox = QCheckBox(self.Imaging_Oscilloscope_ThirdTraces_frame)
        self.Imaging_Syn2VmCheckbox.setObjectName(u"Imaging_Syn2VmCheckbox")
        self.Imaging_Syn2VmCheckbox.setEnabled(True)
        self.Imaging_Syn2VmCheckbox.setAutoFillBackground(False)
        self.Imaging_Syn2VmCheckbox.setStyleSheet(u"color: rgb(181, 137, 0);")
        self.Imaging_Syn2VmCheckbox.setChecked(False)

        self.horizontalLayout_176.addWidget(self.Imaging_Syn2VmCheckbox)

        self.Imaging_Syn2InputCheckbox = QCheckBox(self.Imaging_Oscilloscope_ThirdTraces_frame)
        self.Imaging_Syn2InputCheckbox.setObjectName(u"Imaging_Syn2InputCheckbox")
        self.Imaging_Syn2InputCheckbox.setEnabled(True)
        self.Imaging_Syn2InputCheckbox.setAutoFillBackground(False)
        self.Imaging_Syn2InputCheckbox.setStyleSheet(u"color: rgb(108, 113, 196);")
        self.Imaging_Syn2InputCheckbox.setChecked(False)

        self.horizontalLayout_176.addWidget(self.Imaging_Syn2InputCheckbox)


        self.horizontalLayout_177.addWidget(self.Imaging_Oscilloscope_ThirdTraces_frame)


        self.horizontalLayout_178.addWidget(self.Imaging_Oscilloscope_Traces_frame)


        self.horizontalLayout_157.addWidget(self.Imaging_Oscilloscope_widget, 0, Qt.AlignTop)


        self.verticalLayout_109.addWidget(self.Imaging_Oscilloscope_frame)


        self.horizontalLayout_70.addWidget(self.Imaging_widget)

        self.line_43 = QFrame(self.page_201)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_43.setFrameShape(QFrame.VLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_70.addWidget(self.line_43)

        self.Imaging_CenterMenuContainer = QFrame(self.page_201)
        self.Imaging_CenterMenuContainer.setObjectName(u"Imaging_CenterMenuContainer")
        self.Imaging_CenterMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.Imaging_CenterMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CenterMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.Imaging_CenterMenuContainer)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.Imaging_parameter_exit_frame = QFrame(self.Imaging_CenterMenuContainer)
        self.Imaging_parameter_exit_frame.setObjectName(u"Imaging_parameter_exit_frame")
        self.Imaging_parameter_exit_frame.setMinimumSize(QSize(200, 0))
        self.Imaging_parameter_exit_frame.setMaximumSize(QSize(200, 16777215))
        self.Imaging_parameter_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_parameter_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.Imaging_parameter_exit_frame)
        self.horizontalLayout_118.setSpacing(0)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Imaging_parameter_exit_pushButton = QPushButton(self.Imaging_parameter_exit_frame)
        self.Imaging_parameter_exit_pushButton.setObjectName(u"Imaging_parameter_exit_pushButton")
        self.Imaging_parameter_exit_pushButton.setIcon(icon18)
        self.Imaging_parameter_exit_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_118.addWidget(self.Imaging_parameter_exit_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_76.addWidget(self.Imaging_parameter_exit_frame)

        self.Imaging_parameter_stackedWidget = QStackedWidget(self.Imaging_CenterMenuContainer)
        self.Imaging_parameter_stackedWidget.setObjectName(u"Imaging_parameter_stackedWidget")
        self.Imaging_parameter_stackedWidget.setMaximumSize(QSize(200, 16777215))
        self.Imaging_StimulusParameter_page = QWidget()
        self.Imaging_StimulusParameter_page.setObjectName(u"Imaging_StimulusParameter_page")
        self.verticalLayout_84 = QVBoxLayout(self.Imaging_StimulusParameter_page)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Stimulus_frame = QFrame(self.Imaging_StimulusParameter_page)
        self.Imaging_Stimulus_frame.setObjectName(u"Imaging_Stimulus_frame")
        self.Imaging_Stimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Stimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.Imaging_Stimulus_frame)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Stimulus_label_frame = QFrame(self.Imaging_Stimulus_frame)
        self.Imaging_Stimulus_label_frame.setObjectName(u"Imaging_Stimulus_label_frame")
        self.Imaging_Stimulus_label_frame.setMaximumSize(QSize(16777215, 31))
        self.Imaging_Stimulus_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Stimulus_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.Imaging_Stimulus_label_frame)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(5, 0, 5, 0)
        self.Imaging_Stimulus_label = QLabel(self.Imaging_Stimulus_label_frame)
        self.Imaging_Stimulus_label.setObjectName(u"Imaging_Stimulus_label")
        self.Imaging_Stimulus_label.setStyleSheet(u"")

        self.verticalLayout_86.addWidget(self.Imaging_Stimulus_label)


        self.verticalLayout_96.addWidget(self.Imaging_Stimulus_label_frame)

        self.Imaging_StimFre_frame = QFrame(self.Imaging_Stimulus_frame)
        self.Imaging_StimFre_frame.setObjectName(u"Imaging_StimFre_frame")
        sizePolicy3.setHeightForWidth(self.Imaging_StimFre_frame.sizePolicy().hasHeightForWidth())
        self.Imaging_StimFre_frame.setSizePolicy(sizePolicy3)
        self.Imaging_StimFre_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.Imaging_StimFre_frame)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(5, 0, 5, 5)
        self.Imaging_StimFre_checkBox_frame = QFrame(self.Imaging_StimFre_frame)
        self.Imaging_StimFre_checkBox_frame.setObjectName(u"Imaging_StimFre_checkBox_frame")
        self.Imaging_StimFre_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.Imaging_StimFre_checkBox_frame)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimFre_checkBox = QCheckBox(self.Imaging_StimFre_checkBox_frame)
        self.Imaging_StimFre_checkBox.setObjectName(u"Imaging_StimFre_checkBox")

        self.horizontalLayout_71.addWidget(self.Imaging_StimFre_checkBox)

        self.Imaging_StimFre_readings_frame = QFrame(self.Imaging_StimFre_checkBox_frame)
        self.Imaging_StimFre_readings_frame.setObjectName(u"Imaging_StimFre_readings_frame")
        self.Imaging_StimFre_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.Imaging_StimFre_readings_frame)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimFre_readings = QLabel(self.Imaging_StimFre_readings_frame)
        self.Imaging_StimFre_readings.setObjectName(u"Imaging_StimFre_readings")

        self.verticalLayout_82.addWidget(self.Imaging_StimFre_readings)


        self.horizontalLayout_71.addWidget(self.Imaging_StimFre_readings_frame)


        self.verticalLayout_79.addWidget(self.Imaging_StimFre_checkBox_frame)

        self.Imaging_StimFre_slider_frame = QFrame(self.Imaging_StimFre_frame)
        self.Imaging_StimFre_slider_frame.setObjectName(u"Imaging_StimFre_slider_frame")
        self.Imaging_StimFre_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.Imaging_StimFre_slider_frame)
        self.horizontalLayout_120.setSpacing(0)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimFre_slider = QSlider(self.Imaging_StimFre_slider_frame)
        self.Imaging_StimFre_slider.setObjectName(u"Imaging_StimFre_slider")
        self.Imaging_StimFre_slider.setEnabled(False)
        self.Imaging_StimFre_slider.setMinimum(-100)
        self.Imaging_StimFre_slider.setMaximum(100)
        self.Imaging_StimFre_slider.setSingleStep(1)
        self.Imaging_StimFre_slider.setPageStep(10)
        self.Imaging_StimFre_slider.setOrientation(Qt.Horizontal)
        self.Imaging_StimFre_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_StimFre_slider.setTickInterval(20)

        self.horizontalLayout_120.addWidget(self.Imaging_StimFre_slider)


        self.verticalLayout_79.addWidget(self.Imaging_StimFre_slider_frame)

        self.Imaging_StimFre_values_frames = QFrame(self.Imaging_StimFre_frame)
        self.Imaging_StimFre_values_frames.setObjectName(u"Imaging_StimFre_values_frames")
        self.Imaging_StimFre_values_frames.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_values_frames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.Imaging_StimFre_values_frames)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimFre_values_min = QLabel(self.Imaging_StimFre_values_frames)
        self.Imaging_StimFre_values_min.setObjectName(u"Imaging_StimFre_values_min")

        self.horizontalLayout_121.addWidget(self.Imaging_StimFre_values_min)

        self.Imaging_StimFre_values = QLabel(self.Imaging_StimFre_values_frames)
        self.Imaging_StimFre_values.setObjectName(u"Imaging_StimFre_values")
        self.Imaging_StimFre_values.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_121.addWidget(self.Imaging_StimFre_values)

        self.Imaging_StimFre_values_max = QLabel(self.Imaging_StimFre_values_frames)
        self.Imaging_StimFre_values_max.setObjectName(u"Imaging_StimFre_values_max")
        self.Imaging_StimFre_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_121.addWidget(self.Imaging_StimFre_values_max)


        self.verticalLayout_79.addWidget(self.Imaging_StimFre_values_frames, 0, Qt.AlignTop)

        self.Imaging_StimFre_image_frame = QFrame(self.Imaging_StimFre_frame)
        self.Imaging_StimFre_image_frame.setObjectName(u"Imaging_StimFre_image_frame")
        self.Imaging_StimFre_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimFre_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.Imaging_StimFre_image_frame)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(5, 5, 5, 0)
        self.Imaging_StimFre_image = QLabel(self.Imaging_StimFre_image_frame)
        self.Imaging_StimFre_image.setObjectName(u"Imaging_StimFre_image")
        sizePolicy.setHeightForWidth(self.Imaging_StimFre_image.sizePolicy().hasHeightForWidth())
        self.Imaging_StimFre_image.setSizePolicy(sizePolicy)
        self.Imaging_StimFre_image.setMinimumSize(QSize(0, 20))
        self.Imaging_StimFre_image.setMaximumSize(QSize(16777215, 20))
        self.Imaging_StimFre_image.setPixmap(QPixmap(u":/resources/resources/StimFrequency.png"))
        self.Imaging_StimFre_image.setScaledContents(True)

        self.horizontalLayout_122.addWidget(self.Imaging_StimFre_image)


        self.verticalLayout_79.addWidget(self.Imaging_StimFre_image_frame)


        self.verticalLayout_96.addWidget(self.Imaging_StimFre_frame)

        self.Imaging_Stimulus_TopLine = QFrame(self.Imaging_Stimulus_frame)
        self.Imaging_Stimulus_TopLine.setObjectName(u"Imaging_Stimulus_TopLine")
        self.Imaging_Stimulus_TopLine.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Imaging_Stimulus_TopLine.setFrameShape(QFrame.HLine)
        self.Imaging_Stimulus_TopLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_96.addWidget(self.Imaging_Stimulus_TopLine)

        self.Imaging_StimStr_frame = QFrame(self.Imaging_Stimulus_frame)
        self.Imaging_StimStr_frame.setObjectName(u"Imaging_StimStr_frame")
        self.Imaging_StimStr_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.Imaging_StimStr_frame)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(5, 0, 5, 0)
        self.Imaging_StimStr_checkBox_frame = QFrame(self.Imaging_StimStr_frame)
        self.Imaging_StimStr_checkBox_frame.setObjectName(u"Imaging_StimStr_checkBox_frame")
        self.Imaging_StimStr_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.Imaging_StimStr_checkBox_frame)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 5, 0, 0)
        self.Imaging_StimStr_checkBox = QCheckBox(self.Imaging_StimStr_checkBox_frame)
        self.Imaging_StimStr_checkBox.setObjectName(u"Imaging_StimStr_checkBox")

        self.horizontalLayout_125.addWidget(self.Imaging_StimStr_checkBox)

        self.Imaging_StimStr_readings = QLabel(self.Imaging_StimStr_checkBox_frame)
        self.Imaging_StimStr_readings.setObjectName(u"Imaging_StimStr_readings")
        self.Imaging_StimStr_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.Imaging_StimStr_readings)


        self.verticalLayout_85.addWidget(self.Imaging_StimStr_checkBox_frame)

        self.Imaging_StimStr_readings_frame = QFrame(self.Imaging_StimStr_frame)
        self.Imaging_StimStr_readings_frame.setObjectName(u"Imaging_StimStr_readings_frame")
        self.Imaging_StimStr_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.Imaging_StimStr_readings_frame)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_85.addWidget(self.Imaging_StimStr_readings_frame)

        self.Imaging_StimStr_Slider_frame = QFrame(self.Imaging_StimStr_frame)
        self.Imaging_StimStr_Slider_frame.setObjectName(u"Imaging_StimStr_Slider_frame")
        self.Imaging_StimStr_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.Imaging_StimStr_Slider_frame)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimStrSlider = QSlider(self.Imaging_StimStr_Slider_frame)
        self.Imaging_StimStrSlider.setObjectName(u"Imaging_StimStrSlider")
        self.Imaging_StimStrSlider.setEnabled(False)
        self.Imaging_StimStrSlider.setMinimum(-100)
        self.Imaging_StimStrSlider.setMaximum(100)
        self.Imaging_StimStrSlider.setOrientation(Qt.Horizontal)
        self.Imaging_StimStrSlider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_StimStrSlider.setTickInterval(20)

        self.horizontalLayout_124.addWidget(self.Imaging_StimStrSlider)


        self.verticalLayout_85.addWidget(self.Imaging_StimStr_Slider_frame)

        self.Imaging_StimStr_values_frame = QFrame(self.Imaging_StimStr_frame)
        self.Imaging_StimStr_values_frame.setObjectName(u"Imaging_StimStr_values_frame")
        self.Imaging_StimStr_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.Imaging_StimStr_values_frame)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimStr_values_min = QLabel(self.Imaging_StimStr_values_frame)
        self.Imaging_StimStr_values_min.setObjectName(u"Imaging_StimStr_values_min")

        self.horizontalLayout_126.addWidget(self.Imaging_StimStr_values_min)

        self.Imaging_StimStr_values_0 = QLabel(self.Imaging_StimStr_values_frame)
        self.Imaging_StimStr_values_0.setObjectName(u"Imaging_StimStr_values_0")
        self.Imaging_StimStr_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_126.addWidget(self.Imaging_StimStr_values_0)

        self.Imaging_StimStr_values_max = QLabel(self.Imaging_StimStr_values_frame)
        self.Imaging_StimStr_values_max.setObjectName(u"Imaging_StimStr_values_max")
        self.Imaging_StimStr_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_126.addWidget(self.Imaging_StimStr_values_max)


        self.verticalLayout_85.addWidget(self.Imaging_StimStr_values_frame)

        self.Imaging_StimStr_image_frame = QFrame(self.Imaging_StimStr_frame)
        self.Imaging_StimStr_image_frame.setObjectName(u"Imaging_StimStr_image_frame")
        self.Imaging_StimStr_image_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_StimStr_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.Imaging_StimStr_image_frame)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 5)
        self.Imaging_StimStr_image = QLabel(self.Imaging_StimStr_image_frame)
        self.Imaging_StimStr_image.setObjectName(u"Imaging_StimStr_image")
        sizePolicy1.setHeightForWidth(self.Imaging_StimStr_image.sizePolicy().hasHeightForWidth())
        self.Imaging_StimStr_image.setSizePolicy(sizePolicy1)
        self.Imaging_StimStr_image.setMinimumSize(QSize(40, 0))
        self.Imaging_StimStr_image.setMaximumSize(QSize(16777215, 40))
        self.Imaging_StimStr_image.setPixmap(QPixmap(u":/resources/resources/StimStrenght.png"))
        self.Imaging_StimStr_image.setScaledContents(True)

        self.horizontalLayout_123.addWidget(self.Imaging_StimStr_image)


        self.verticalLayout_85.addWidget(self.Imaging_StimStr_image_frame)


        self.verticalLayout_96.addWidget(self.Imaging_StimStr_frame)


        self.verticalLayout_84.addWidget(self.Imaging_Stimulus_frame)

        self.Imaging_Stimulus_BottomLine = QFrame(self.Imaging_StimulusParameter_page)
        self.Imaging_Stimulus_BottomLine.setObjectName(u"Imaging_Stimulus_BottomLine")
        self.Imaging_Stimulus_BottomLine.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Imaging_Stimulus_BottomLine.setFrameShape(QFrame.HLine)
        self.Imaging_Stimulus_BottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_84.addWidget(self.Imaging_Stimulus_BottomLine)

        self.Imaging_PR_frame = QFrame(self.Imaging_StimulusParameter_page)
        self.Imaging_PR_frame.setObjectName(u"Imaging_PR_frame")
        self.Imaging_PR_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.Imaging_PR_frame)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(5, 0, 5, 0)
        self.Imaging_PR_label_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_label_frame.setObjectName(u"Imaging_PR_label_frame")
        self.Imaging_PR_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.Imaging_PR_label_frame)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 5, 0, 0)
        self.Imaging_PR_label = QLabel(self.Imaging_PR_label_frame)
        self.Imaging_PR_label.setObjectName(u"Imaging_PR_label")
        self.Imaging_PR_label.setStyleSheet(u"")

        self.verticalLayout_90.addWidget(self.Imaging_PR_label)


        self.verticalLayout_93.addWidget(self.Imaging_PR_label_frame)

        self.Imaging_PR_PhotoGain_checkBox_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_PhotoGain_checkBox_frame.setObjectName(u"Imaging_PR_PhotoGain_checkBox_frame")
        self.Imaging_PR_PhotoGain_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_PhotoGain_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.Imaging_PR_PhotoGain_checkBox_frame)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_PhotoGain_checkBox = QCheckBox(self.Imaging_PR_PhotoGain_checkBox_frame)
        self.Imaging_PR_PhotoGain_checkBox.setObjectName(u"Imaging_PR_PhotoGain_checkBox")

        self.horizontalLayout_128.addWidget(self.Imaging_PR_PhotoGain_checkBox)

        self.Imaging_PR_Photogain_readings = QLabel(self.Imaging_PR_PhotoGain_checkBox_frame)
        self.Imaging_PR_Photogain_readings.setObjectName(u"Imaging_PR_Photogain_readings")
        self.Imaging_PR_Photogain_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_128.addWidget(self.Imaging_PR_Photogain_readings)


        self.verticalLayout_93.addWidget(self.Imaging_PR_PhotoGain_checkBox_frame)

        self.Imaging_PR_Photogain_readings_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Photogain_readings_frame.setObjectName(u"Imaging_PR_Photogain_readings_frame")
        self.Imaging_PR_Photogain_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Photogain_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.Imaging_PR_Photogain_readings_frame)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_93.addWidget(self.Imaging_PR_Photogain_readings_frame)

        self.Imaging_PR_PhotoGain_slider_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_PhotoGain_slider_frame.setObjectName(u"Imaging_PR_PhotoGain_slider_frame")
        self.Imaging_PR_PhotoGain_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_PhotoGain_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.Imaging_PR_PhotoGain_slider_frame)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_PhotoGain_slider = QSlider(self.Imaging_PR_PhotoGain_slider_frame)
        self.Imaging_PR_PhotoGain_slider.setObjectName(u"Imaging_PR_PhotoGain_slider")
        self.Imaging_PR_PhotoGain_slider.setEnabled(False)
        self.Imaging_PR_PhotoGain_slider.setMinimum(-100)
        self.Imaging_PR_PhotoGain_slider.setMaximum(100)
        self.Imaging_PR_PhotoGain_slider.setSingleStep(1)
        self.Imaging_PR_PhotoGain_slider.setPageStep(10)
        self.Imaging_PR_PhotoGain_slider.setOrientation(Qt.Horizontal)
        self.Imaging_PR_PhotoGain_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PR_PhotoGain_slider.setTickInterval(20)

        self.horizontalLayout_129.addWidget(self.Imaging_PR_PhotoGain_slider)


        self.verticalLayout_93.addWidget(self.Imaging_PR_PhotoGain_slider_frame)

        self.Imaging_PR_PhotoGain_values_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_PhotoGain_values_frame.setObjectName(u"Imaging_PR_PhotoGain_values_frame")
        self.Imaging_PR_PhotoGain_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_PhotoGain_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.Imaging_PR_PhotoGain_values_frame)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_PhotoGain_values_min = QLabel(self.Imaging_PR_PhotoGain_values_frame)
        self.Imaging_PR_PhotoGain_values_min.setObjectName(u"Imaging_PR_PhotoGain_values_min")

        self.horizontalLayout_133.addWidget(self.Imaging_PR_PhotoGain_values_min)

        self.Imaging_PR_PhotoGain_values = QLabel(self.Imaging_PR_PhotoGain_values_frame)
        self.Imaging_PR_PhotoGain_values.setObjectName(u"Imaging_PR_PhotoGain_values")

        self.horizontalLayout_133.addWidget(self.Imaging_PR_PhotoGain_values, 0, Qt.AlignHCenter)

        self.Imaging_PR_PhotoGain_values_max = QLabel(self.Imaging_PR_PhotoGain_values_frame)
        self.Imaging_PR_PhotoGain_values_max.setObjectName(u"Imaging_PR_PhotoGain_values_max")
        self.Imaging_PR_PhotoGain_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_133.addWidget(self.Imaging_PR_PhotoGain_values_max)


        self.verticalLayout_93.addWidget(self.Imaging_PR_PhotoGain_values_frame)

        self.Imaging_PR_Decay_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Decay_frame.setObjectName(u"Imaging_PR_Decay_frame")
        self.Imaging_PR_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.Imaging_PR_Decay_frame)
        self.horizontalLayout_130.setSpacing(0)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Decay_checkBox = QCheckBox(self.Imaging_PR_Decay_frame)
        self.Imaging_PR_Decay_checkBox.setObjectName(u"Imaging_PR_Decay_checkBox")

        self.horizontalLayout_130.addWidget(self.Imaging_PR_Decay_checkBox, 0, Qt.AlignLeft)

        self.Imaging_PR_Decay_readings = QLabel(self.Imaging_PR_Decay_frame)
        self.Imaging_PR_Decay_readings.setObjectName(u"Imaging_PR_Decay_readings")
        self.Imaging_PR_Decay_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.Imaging_PR_Decay_readings)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Decay_frame)

        self.Imaging_PR_Decay_readings_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Decay_readings_frame.setObjectName(u"Imaging_PR_Decay_readings_frame")
        self.Imaging_PR_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.Imaging_PR_Decay_readings_frame)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_93.addWidget(self.Imaging_PR_Decay_readings_frame)

        self.Imaging_PR_Decay_slider_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Decay_slider_frame.setObjectName(u"Imaging_PR_Decay_slider_frame")
        self.Imaging_PR_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.Imaging_PR_Decay_slider_frame)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Decay_slider = QSlider(self.Imaging_PR_Decay_slider_frame)
        self.Imaging_PR_Decay_slider.setObjectName(u"Imaging_PR_Decay_slider")
        self.Imaging_PR_Decay_slider.setEnabled(False)
        self.Imaging_PR_Decay_slider.setMinimum(10)
        self.Imaging_PR_Decay_slider.setMaximum(125)
        self.Imaging_PR_Decay_slider.setSingleStep(1)
        self.Imaging_PR_Decay_slider.setPageStep(10)
        self.Imaging_PR_Decay_slider.setValue(100)
        self.Imaging_PR_Decay_slider.setOrientation(Qt.Horizontal)
        self.Imaging_PR_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PR_Decay_slider.setTickInterval(10)

        self.verticalLayout_92.addWidget(self.Imaging_PR_Decay_slider)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Decay_slider_frame)

        self.Imaging_PR_Decay_values_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Decay_values_frame.setObjectName(u"Imaging_PR_Decay_values_frame")
        self.Imaging_PR_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.Imaging_PR_Decay_values_frame)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Decay_values_slow = QLabel(self.Imaging_PR_Decay_values_frame)
        self.Imaging_PR_Decay_values_slow.setObjectName(u"Imaging_PR_Decay_values_slow")
        self.Imaging_PR_Decay_values_slow.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_131.addWidget(self.Imaging_PR_Decay_values_slow)

        self.Imaging_PR_Decay_values_fast = QLabel(self.Imaging_PR_Decay_values_frame)
        self.Imaging_PR_Decay_values_fast.setObjectName(u"Imaging_PR_Decay_values_fast")
        self.Imaging_PR_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_131.addWidget(self.Imaging_PR_Decay_values_fast)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Decay_values_frame)

        self.Imaging_PR_Recovery_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Recovery_frame.setObjectName(u"Imaging_PR_Recovery_frame")
        self.Imaging_PR_Recovery_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Recovery_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.Imaging_PR_Recovery_frame)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Recovery_checkBox = QCheckBox(self.Imaging_PR_Recovery_frame)
        self.Imaging_PR_Recovery_checkBox.setObjectName(u"Imaging_PR_Recovery_checkBox")

        self.horizontalLayout_127.addWidget(self.Imaging_PR_Recovery_checkBox, 0, Qt.AlignLeft)

        self.Imaging_PR_Recovery_readings_frame = QFrame(self.Imaging_PR_Recovery_frame)
        self.Imaging_PR_Recovery_readings_frame.setObjectName(u"Imaging_PR_Recovery_readings_frame")
        self.Imaging_PR_Recovery_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Recovery_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.Imaging_PR_Recovery_readings_frame)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Recovery_readings = QLabel(self.Imaging_PR_Recovery_readings_frame)
        self.Imaging_PR_Recovery_readings.setObjectName(u"Imaging_PR_Recovery_readings")
        self.Imaging_PR_Recovery_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.Imaging_PR_Recovery_readings)


        self.horizontalLayout_127.addWidget(self.Imaging_PR_Recovery_readings_frame)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Recovery_frame)

        self.Imaging_PR_Recovery_slider_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Recovery_slider_frame.setObjectName(u"Imaging_PR_Recovery_slider_frame")
        self.Imaging_PR_Recovery_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Recovery_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.Imaging_PR_Recovery_slider_frame)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Recovery_slider = QSlider(self.Imaging_PR_Recovery_slider_frame)
        self.Imaging_PR_Recovery_slider.setObjectName(u"Imaging_PR_Recovery_slider")
        self.Imaging_PR_Recovery_slider.setEnabled(False)
        self.Imaging_PR_Recovery_slider.setMinimum(1)
        self.Imaging_PR_Recovery_slider.setMaximum(100)
        self.Imaging_PR_Recovery_slider.setSingleStep(1)
        self.Imaging_PR_Recovery_slider.setPageStep(10)
        self.Imaging_PR_Recovery_slider.setValue(25)
        self.Imaging_PR_Recovery_slider.setOrientation(Qt.Horizontal)
        self.Imaging_PR_Recovery_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PR_Recovery_slider.setTickInterval(10)

        self.verticalLayout_87.addWidget(self.Imaging_PR_Recovery_slider)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Recovery_slider_frame)

        self.Imaging_PR_Recovery_values_frame = QFrame(self.Imaging_PR_frame)
        self.Imaging_PR_Recovery_values_frame.setObjectName(u"Imaging_PR_Recovery_values_frame")
        self.Imaging_PR_Recovery_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PR_Recovery_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.Imaging_PR_Recovery_values_frame)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PR_Recovery_values_slow = QLabel(self.Imaging_PR_Recovery_values_frame)
        self.Imaging_PR_Recovery_values_slow.setObjectName(u"Imaging_PR_Recovery_values_slow")

        self.horizontalLayout_132.addWidget(self.Imaging_PR_Recovery_values_slow)

        self.Imaging_PR_Recovery_values_fast = QLabel(self.Imaging_PR_Recovery_values_frame)
        self.Imaging_PR_Recovery_values_fast.setObjectName(u"Imaging_PR_Recovery_values_fast")
        self.Imaging_PR_Recovery_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_132.addWidget(self.Imaging_PR_Recovery_values_fast)


        self.verticalLayout_93.addWidget(self.Imaging_PR_Recovery_values_frame)


        self.verticalLayout_84.addWidget(self.Imaging_PR_frame)

        self.Imaging_parameter_stackedWidget.addWidget(self.Imaging_StimulusParameter_page)
        self.Imaging_NeuronParameter_page = QWidget()
        self.Imaging_NeuronParameter_page.setObjectName(u"Imaging_NeuronParameter_page")
        self.verticalLayout_108 = QVBoxLayout(self.Imaging_NeuronParameter_page)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_frame = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_PatchClamp_frame.setObjectName(u"Imaging_PatchClamp_frame")
        self.Imaging_PatchClamp_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.Imaging_PatchClamp_frame)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(5, 0, 5, 0)
        self.Imaging_PatchClamp_label_frame = QFrame(self.Imaging_PatchClamp_frame)
        self.Imaging_PatchClamp_label_frame.setObjectName(u"Imaging_PatchClamp_label_frame")
        self.Imaging_PatchClamp_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.Imaging_PatchClamp_label_frame)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_label = QLabel(self.Imaging_PatchClamp_label_frame)
        self.Imaging_PatchClamp_label.setObjectName(u"Imaging_PatchClamp_label")
        self.Imaging_PatchClamp_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_135.addWidget(self.Imaging_PatchClamp_label)


        self.verticalLayout_97.addWidget(self.Imaging_PatchClamp_label_frame)

        self.Imaging_PatchClamp_checkBox_frame = QFrame(self.Imaging_PatchClamp_frame)
        self.Imaging_PatchClamp_checkBox_frame.setObjectName(u"Imaging_PatchClamp_checkBox_frame")
        self.Imaging_PatchClamp_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.Imaging_PatchClamp_checkBox_frame)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_checkBox = QCheckBox(self.Imaging_PatchClamp_checkBox_frame)
        self.Imaging_PatchClamp_checkBox.setObjectName(u"Imaging_PatchClamp_checkBox")
        self.Imaging_PatchClamp_checkBox.setFont(font2)
        self.Imaging_PatchClamp_checkBox.setTristate(False)

        self.horizontalLayout_136.addWidget(self.Imaging_PatchClamp_checkBox)

        self.Imaging_PatchClamp_reading_frame = QFrame(self.Imaging_PatchClamp_checkBox_frame)
        self.Imaging_PatchClamp_reading_frame.setObjectName(u"Imaging_PatchClamp_reading_frame")
        self.Imaging_PatchClamp_reading_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_reading_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.Imaging_PatchClamp_reading_frame)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_reading = QLabel(self.Imaging_PatchClamp_reading_frame)
        self.Imaging_PatchClamp_reading.setObjectName(u"Imaging_PatchClamp_reading")
        self.Imaging_PatchClamp_reading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.Imaging_PatchClamp_reading)


        self.horizontalLayout_136.addWidget(self.Imaging_PatchClamp_reading_frame)


        self.verticalLayout_97.addWidget(self.Imaging_PatchClamp_checkBox_frame)

        self.Imaging_PatchClamp_slider_frame = QFrame(self.Imaging_PatchClamp_frame)
        self.Imaging_PatchClamp_slider_frame.setObjectName(u"Imaging_PatchClamp_slider_frame")
        self.Imaging_PatchClamp_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.Imaging_PatchClamp_slider_frame)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_slider = QSlider(self.Imaging_PatchClamp_slider_frame)
        self.Imaging_PatchClamp_slider.setObjectName(u"Imaging_PatchClamp_slider")
        self.Imaging_PatchClamp_slider.setEnabled(False)
        self.Imaging_PatchClamp_slider.setMinimum(-100)
        self.Imaging_PatchClamp_slider.setMaximum(100)
        self.Imaging_PatchClamp_slider.setOrientation(Qt.Horizontal)
        self.Imaging_PatchClamp_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PatchClamp_slider.setTickInterval(20)

        self.horizontalLayout_137.addWidget(self.Imaging_PatchClamp_slider)


        self.verticalLayout_97.addWidget(self.Imaging_PatchClamp_slider_frame)

        self.Imaging_PatchClamp_values_frame = QFrame(self.Imaging_PatchClamp_frame)
        self.Imaging_PatchClamp_values_frame.setObjectName(u"Imaging_PatchClamp_values_frame")
        self.Imaging_PatchClamp_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PatchClamp_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.Imaging_PatchClamp_values_frame)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PatchClamp_values_min = QLabel(self.Imaging_PatchClamp_values_frame)
        self.Imaging_PatchClamp_values_min.setObjectName(u"Imaging_PatchClamp_values_min")

        self.horizontalLayout_138.addWidget(self.Imaging_PatchClamp_values_min)

        self.Imaging_PatchClamp_values_0 = QLabel(self.Imaging_PatchClamp_values_frame)
        self.Imaging_PatchClamp_values_0.setObjectName(u"Imaging_PatchClamp_values_0")
        self.Imaging_PatchClamp_values_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_138.addWidget(self.Imaging_PatchClamp_values_0)

        self.Imaging_PatchClamp_values_max = QLabel(self.Imaging_PatchClamp_values_frame)
        self.Imaging_PatchClamp_values_max.setObjectName(u"Imaging_PatchClamp_values_max")
        self.Imaging_PatchClamp_values_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_138.addWidget(self.Imaging_PatchClamp_values_max)


        self.verticalLayout_97.addWidget(self.Imaging_PatchClamp_values_frame, 0, Qt.AlignTop)


        self.verticalLayout_108.addWidget(self.Imaging_PatchClamp_frame)

        self.Imaging_Neuron_TopLine = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Neuron_TopLine.setObjectName(u"Imaging_Neuron_TopLine")
        self.Imaging_Neuron_TopLine.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Imaging_Neuron_TopLine.setFrameShape(QFrame.HLine)
        self.Imaging_Neuron_TopLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_108.addWidget(self.Imaging_Neuron_TopLine)

        self.Imaging_Noise_frame = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Noise_frame.setObjectName(u"Imaging_Noise_frame")
        self.Imaging_Noise_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.Imaging_Noise_frame)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(5, 0, 5, 0)
        self.Imaging_Noise_label_frame = QFrame(self.Imaging_Noise_frame)
        self.Imaging_Noise_label_frame.setObjectName(u"Imaging_Noise_label_frame")
        self.Imaging_Noise_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.Imaging_Noise_label_frame)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Noise_label = QLabel(self.Imaging_Noise_label_frame)
        self.Imaging_Noise_label.setObjectName(u"Imaging_Noise_label")
        self.Imaging_Noise_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_139.addWidget(self.Imaging_Noise_label)


        self.verticalLayout_99.addWidget(self.Imaging_Noise_label_frame)

        self.Imaging_Noise_checkBox_frame = QFrame(self.Imaging_Noise_frame)
        self.Imaging_Noise_checkBox_frame.setObjectName(u"Imaging_Noise_checkBox_frame")
        self.Imaging_Noise_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.Imaging_Noise_checkBox_frame)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Noise_checkBox = QCheckBox(self.Imaging_Noise_checkBox_frame)
        self.Imaging_Noise_checkBox.setObjectName(u"Imaging_Noise_checkBox")

        self.horizontalLayout_140.addWidget(self.Imaging_Noise_checkBox)

        self.Imaging_Noise_readings_frame = QFrame(self.Imaging_Noise_checkBox_frame)
        self.Imaging_Noise_readings_frame.setObjectName(u"Imaging_Noise_readings_frame")
        self.Imaging_Noise_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.Imaging_Noise_readings_frame)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Noise_readings = QLabel(self.Imaging_Noise_readings_frame)
        self.Imaging_Noise_readings.setObjectName(u"Imaging_Noise_readings")
        self.Imaging_Noise_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.Imaging_Noise_readings)


        self.horizontalLayout_140.addWidget(self.Imaging_Noise_readings_frame)


        self.verticalLayout_99.addWidget(self.Imaging_Noise_checkBox_frame)

        self.Imaging_Noise_slider_frame = QFrame(self.Imaging_Noise_frame)
        self.Imaging_Noise_slider_frame.setObjectName(u"Imaging_Noise_slider_frame")
        self.Imaging_Noise_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.Imaging_Noise_slider_frame)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Noise_slider = QSlider(self.Imaging_Noise_slider_frame)
        self.Imaging_Noise_slider.setObjectName(u"Imaging_Noise_slider")
        self.Imaging_Noise_slider.setEnabled(False)
        self.Imaging_Noise_slider.setMaximum(100)
        self.Imaging_Noise_slider.setOrientation(Qt.Horizontal)
        self.Imaging_Noise_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Noise_slider.setTickInterval(10)

        self.horizontalLayout_141.addWidget(self.Imaging_Noise_slider)


        self.verticalLayout_99.addWidget(self.Imaging_Noise_slider_frame)

        self.Imaging_Noise_value_frame = QFrame(self.Imaging_Noise_frame)
        self.Imaging_Noise_value_frame.setObjectName(u"Imaging_Noise_value_frame")
        self.Imaging_Noise_value_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Noise_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.Imaging_Noise_value_frame)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 5)
        self.Imaging_Noise_0_value = QLabel(self.Imaging_Noise_value_frame)
        self.Imaging_Noise_0_value.setObjectName(u"Imaging_Noise_0_value")
        self.Imaging_Noise_0_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.Imaging_Noise_0_value, 0, Qt.AlignLeft)

        self.Imaging_Noise_max_value = QLabel(self.Imaging_Noise_value_frame)
        self.Imaging_Noise_max_value.setObjectName(u"Imaging_Noise_max_value")
        self.Imaging_Noise_max_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_142.addWidget(self.Imaging_Noise_max_value, 0, Qt.AlignRight)


        self.verticalLayout_99.addWidget(self.Imaging_Noise_value_frame, 0, Qt.AlignTop)


        self.verticalLayout_108.addWidget(self.Imaging_Noise_frame)

        self.Imaging_Neuron_MiddleLine = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Neuron_MiddleLine.setObjectName(u"Imaging_Neuron_MiddleLine")
        self.Imaging_Neuron_MiddleLine.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Imaging_Neuron_MiddleLine.setFrameShape(QFrame.HLine)
        self.Imaging_Neuron_MiddleLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_108.addWidget(self.Imaging_Neuron_MiddleLine)

        self.Imaging_Synapse1_frame = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Synapse1_frame.setObjectName(u"Imaging_Synapse1_frame")
        self.Imaging_Synapse1_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.Imaging_Synapse1_frame)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(5, 0, 5, 0)
        self.Imaging_Synapse1_label_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_label_frame.setObjectName(u"Imaging_Synapse1_label_frame")
        self.Imaging_Synapse1_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.Imaging_Synapse1_label_frame)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 5, 0, 5)
        self.Imaging_Synapse1_label = QLabel(self.Imaging_Synapse1_label_frame)
        self.Imaging_Synapse1_label.setObjectName(u"Imaging_Synapse1_label")
        self.Imaging_Synapse1_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_143.addWidget(self.Imaging_Synapse1_label)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_label_frame)

        self.Imaging_Synapse1_checkBox_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_checkBox_frame.setObjectName(u"Imaging_Synapse1_checkBox_frame")
        self.Imaging_Synapse1_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.Imaging_Synapse1_checkBox_frame)
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_checkBox = QCheckBox(self.Imaging_Synapse1_checkBox_frame)
        self.Imaging_Synapse1_checkBox.setObjectName(u"Imaging_Synapse1_checkBox")

        self.horizontalLayout_144.addWidget(self.Imaging_Synapse1_checkBox)

        self.Imaging_Synapse1_readings_frame = QFrame(self.Imaging_Synapse1_checkBox_frame)
        self.Imaging_Synapse1_readings_frame.setObjectName(u"Imaging_Synapse1_readings_frame")
        self.Imaging_Synapse1_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.Imaging_Synapse1_readings_frame)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_readings = QLabel(self.Imaging_Synapse1_readings_frame)
        self.Imaging_Synapse1_readings.setObjectName(u"Imaging_Synapse1_readings")
        self.Imaging_Synapse1_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.Imaging_Synapse1_readings)


        self.horizontalLayout_144.addWidget(self.Imaging_Synapse1_readings_frame)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_checkBox_frame)

        self.Imaging_Synapse1_slider_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_slider_frame.setObjectName(u"Imaging_Synapse1_slider_frame")
        self.Imaging_Synapse1_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.Imaging_Synapse1_slider_frame)
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_slider = QSlider(self.Imaging_Synapse1_slider_frame)
        self.Imaging_Synapse1_slider.setObjectName(u"Imaging_Synapse1_slider")
        self.Imaging_Synapse1_slider.setEnabled(False)
        self.Imaging_Synapse1_slider.setMinimum(-100)
        self.Imaging_Synapse1_slider.setMaximum(100)
        self.Imaging_Synapse1_slider.setOrientation(Qt.Horizontal)
        self.Imaging_Synapse1_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Synapse1_slider.setTickInterval(20)

        self.horizontalLayout_145.addWidget(self.Imaging_Synapse1_slider)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_slider_frame)

        self.Imaging_Synapse1_values_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_values_frame.setObjectName(u"Imaging_Synapse1_values_frame")
        self.Imaging_Synapse1_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.Imaging_Synapse1_values_frame)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 5)
        self.Imaging_Synapse1_min = QLabel(self.Imaging_Synapse1_values_frame)
        self.Imaging_Synapse1_min.setObjectName(u"Imaging_Synapse1_min")

        self.horizontalLayout_146.addWidget(self.Imaging_Synapse1_min)

        self.Imaging_Synapse1_0 = QLabel(self.Imaging_Synapse1_values_frame)
        self.Imaging_Synapse1_0.setObjectName(u"Imaging_Synapse1_0")

        self.horizontalLayout_146.addWidget(self.Imaging_Synapse1_0, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Imaging_Synapse1_max = QLabel(self.Imaging_Synapse1_values_frame)
        self.Imaging_Synapse1_max.setObjectName(u"Imaging_Synapse1_max")
        self.Imaging_Synapse1_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_146.addWidget(self.Imaging_Synapse1_max)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_values_frame)

        self.Imaging_Synapse1_Decay_checkBox_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_Decay_checkBox_frame.setObjectName(u"Imaging_Synapse1_Decay_checkBox_frame")
        self.Imaging_Synapse1_Decay_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_Decay_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.Imaging_Synapse1_Decay_checkBox_frame)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_Decay_checkBox = QCheckBox(self.Imaging_Synapse1_Decay_checkBox_frame)
        self.Imaging_Synapse1_Decay_checkBox.setObjectName(u"Imaging_Synapse1_Decay_checkBox")

        self.horizontalLayout_147.addWidget(self.Imaging_Synapse1_Decay_checkBox)

        self.Imaging_Synapse1_Decay_readings_frame = QFrame(self.Imaging_Synapse1_Decay_checkBox_frame)
        self.Imaging_Synapse1_Decay_readings_frame.setObjectName(u"Imaging_Synapse1_Decay_readings_frame")
        self.Imaging_Synapse1_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.Imaging_Synapse1_Decay_readings_frame)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_Decay_readings = QLabel(self.Imaging_Synapse1_Decay_readings_frame)
        self.Imaging_Synapse1_Decay_readings.setObjectName(u"Imaging_Synapse1_Decay_readings")
        self.Imaging_Synapse1_Decay_readings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_103.addWidget(self.Imaging_Synapse1_Decay_readings)


        self.horizontalLayout_147.addWidget(self.Imaging_Synapse1_Decay_readings_frame)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_Decay_checkBox_frame)

        self.Imaging_Synapse1_Decay_slider_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_Decay_slider_frame.setObjectName(u"Imaging_Synapse1_Decay_slider_frame")
        self.Imaging_Synapse1_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.Imaging_Synapse1_Decay_slider_frame)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse1_Decay_slider = QSlider(self.Imaging_Synapse1_Decay_slider_frame)
        self.Imaging_Synapse1_Decay_slider.setObjectName(u"Imaging_Synapse1_Decay_slider")
        self.Imaging_Synapse1_Decay_slider.setEnabled(False)
        self.Imaging_Synapse1_Decay_slider.setMinimum(975)
        self.Imaging_Synapse1_Decay_slider.setMaximum(1000)
        self.Imaging_Synapse1_Decay_slider.setSliderPosition(995)
        self.Imaging_Synapse1_Decay_slider.setOrientation(Qt.Horizontal)
        self.Imaging_Synapse1_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Synapse1_Decay_slider.setTickInterval(2)

        self.verticalLayout_104.addWidget(self.Imaging_Synapse1_Decay_slider)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_Decay_slider_frame)

        self.Imaging_Synapse1_Decay_values_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_Decay_values_frame.setObjectName(u"Imaging_Synapse1_Decay_values_frame")
        self.Imaging_Synapse1_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.Imaging_Synapse1_Decay_values_frame)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 5)
        self.Imaging_Synapse1_Decay_values_slow = QLabel(self.Imaging_Synapse1_Decay_values_frame)
        self.Imaging_Synapse1_Decay_values_slow.setObjectName(u"Imaging_Synapse1_Decay_values_slow")

        self.horizontalLayout_148.addWidget(self.Imaging_Synapse1_Decay_values_slow)

        self.Imaging_Synapse1_Decay_values_fast = QLabel(self.Imaging_Synapse1_Decay_values_frame)
        self.Imaging_Synapse1_Decay_values_fast.setObjectName(u"Imaging_Synapse1_Decay_values_fast")
        self.Imaging_Synapse1_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_148.addWidget(self.Imaging_Synapse1_Decay_values_fast)


        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_Decay_values_frame)

        self.Imaging_Synapse1_Decay_frame = QFrame(self.Imaging_Synapse1_frame)
        self.Imaging_Synapse1_Decay_frame.setObjectName(u"Imaging_Synapse1_Decay_frame")
        self.Imaging_Synapse1_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse1_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.Imaging_Synapse1_Decay_frame)
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_101.addWidget(self.Imaging_Synapse1_Decay_frame)


        self.verticalLayout_108.addWidget(self.Imaging_Synapse1_frame)

        self.Imaging_Neuron_BottomLine = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Neuron_BottomLine.setObjectName(u"Imaging_Neuron_BottomLine")
        self.Imaging_Neuron_BottomLine.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.Imaging_Neuron_BottomLine.setFrameShape(QFrame.HLine)
        self.Imaging_Neuron_BottomLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_108.addWidget(self.Imaging_Neuron_BottomLine)

        self.Imaging_Synapse2_frame = QFrame(self.Imaging_NeuronParameter_page)
        self.Imaging_Synapse2_frame.setObjectName(u"Imaging_Synapse2_frame")
        self.Imaging_Synapse2_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.Imaging_Synapse2_frame)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(5, 0, 5, 5)
        self.Imaging_Synapse2_label_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_label_frame.setObjectName(u"Imaging_Synapse2_label_frame")
        self.Imaging_Synapse2_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.Imaging_Synapse2_label_frame)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 5, 0, 5)
        self.Imaging_Synapse2_label = QLabel(self.Imaging_Synapse2_label_frame)
        self.Imaging_Synapse2_label.setObjectName(u"Imaging_Synapse2_label")
        self.Imaging_Synapse2_label.setStyleSheet(u"color: rgb(147, 161, 161);")

        self.horizontalLayout_150.addWidget(self.Imaging_Synapse2_label)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_label_frame)

        self.Imaging_Synapse2_readings_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_readings_frame.setObjectName(u"Imaging_Synapse2_readings_frame")
        self.Imaging_Synapse2_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.Imaging_Synapse2_readings_frame)
        self.horizontalLayout_151.setSpacing(0)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse2_checkBox = QCheckBox(self.Imaging_Synapse2_readings_frame)
        self.Imaging_Synapse2_checkBox.setObjectName(u"Imaging_Synapse2_checkBox")
        self.Imaging_Synapse2_checkBox.setEnabled(True)

        self.horizontalLayout_151.addWidget(self.Imaging_Synapse2_checkBox)

        self.Imaging_Synapse2_readings = QLabel(self.Imaging_Synapse2_readings_frame)
        self.Imaging_Synapse2_readings.setObjectName(u"Imaging_Synapse2_readings")
        self.Imaging_Synapse2_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_151.addWidget(self.Imaging_Synapse2_readings)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_readings_frame)

        self.Imaging_Synapse2_checkBox_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_checkBox_frame.setObjectName(u"Imaging_Synapse2_checkBox_frame")
        self.Imaging_Synapse2_checkBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_checkBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.Imaging_Synapse2_checkBox_frame)
        self.horizontalLayout_152.setSpacing(0)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_checkBox_frame)

        self.Imaging_Synapse2_slider_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_slider_frame.setObjectName(u"Imaging_Synapse2_slider_frame")
        self.Imaging_Synapse2_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.Imaging_Synapse2_slider_frame)
        self.horizontalLayout_153.setSpacing(0)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse2_slider = QSlider(self.Imaging_Synapse2_slider_frame)
        self.Imaging_Synapse2_slider.setObjectName(u"Imaging_Synapse2_slider")
        self.Imaging_Synapse2_slider.setEnabled(False)
        self.Imaging_Synapse2_slider.setMinimum(-100)
        self.Imaging_Synapse2_slider.setMaximum(100)
        self.Imaging_Synapse2_slider.setOrientation(Qt.Horizontal)
        self.Imaging_Synapse2_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Synapse2_slider.setTickInterval(20)

        self.horizontalLayout_153.addWidget(self.Imaging_Synapse2_slider)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_slider_frame)

        self.Imaging_Synapse2_values_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_values_frame.setObjectName(u"Imaging_Synapse2_values_frame")
        self.Imaging_Synapse2_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.Imaging_Synapse2_values_frame)
        self.horizontalLayout_154.setSpacing(0)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 5)
        self.Imaging_Synapse2_min = QLabel(self.Imaging_Synapse2_values_frame)
        self.Imaging_Synapse2_min.setObjectName(u"Imaging_Synapse2_min")

        self.horizontalLayout_154.addWidget(self.Imaging_Synapse2_min)

        self.Imaging_Synapse2_0 = QLabel(self.Imaging_Synapse2_values_frame)
        self.Imaging_Synapse2_0.setObjectName(u"Imaging_Synapse2_0")
        self.Imaging_Synapse2_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_154.addWidget(self.Imaging_Synapse2_0)

        self.Imaging_Synapse2_max = QLabel(self.Imaging_Synapse2_values_frame)
        self.Imaging_Synapse2_max.setObjectName(u"Imaging_Synapse2_max")
        self.Imaging_Synapse2_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_154.addWidget(self.Imaging_Synapse2_max)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_values_frame, 0, Qt.AlignTop)

        self.Imaging_Synapse2_Decay_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_Decay_frame.setObjectName(u"Imaging_Synapse2_Decay_frame")
        sizePolicy4.setHeightForWidth(self.Imaging_Synapse2_Decay_frame.sizePolicy().hasHeightForWidth())
        self.Imaging_Synapse2_Decay_frame.setSizePolicy(sizePolicy4)
        self.Imaging_Synapse2_Decay_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_Decay_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.Imaging_Synapse2_Decay_frame)
        self.horizontalLayout_155.setSpacing(0)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse2_Decay_checkBox = QCheckBox(self.Imaging_Synapse2_Decay_frame)
        self.Imaging_Synapse2_Decay_checkBox.setObjectName(u"Imaging_Synapse2_Decay_checkBox")

        self.horizontalLayout_155.addWidget(self.Imaging_Synapse2_Decay_checkBox)

        self.Imaging_Synapse2_Decay_readings = QLabel(self.Imaging_Synapse2_Decay_frame)
        self.Imaging_Synapse2_Decay_readings.setObjectName(u"Imaging_Synapse2_Decay_readings")
        self.Imaging_Synapse2_Decay_readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.Imaging_Synapse2_Decay_readings)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_Decay_frame)

        self.Imaging_Synapse2_Decay_readings_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_Decay_readings_frame.setObjectName(u"Imaging_Synapse2_Decay_readings_frame")
        self.Imaging_Synapse2_Decay_readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_Decay_readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.Imaging_Synapse2_Decay_readings_frame)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_Decay_readings_frame)

        self.Imaging_Synapse2_Decay_slider_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_Decay_slider_frame.setObjectName(u"Imaging_Synapse2_Decay_slider_frame")
        self.Imaging_Synapse2_Decay_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_Decay_slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.Imaging_Synapse2_Decay_slider_frame)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse2_Decay_slider = QSlider(self.Imaging_Synapse2_Decay_slider_frame)
        self.Imaging_Synapse2_Decay_slider.setObjectName(u"Imaging_Synapse2_Decay_slider")
        self.Imaging_Synapse2_Decay_slider.setEnabled(False)
        self.Imaging_Synapse2_Decay_slider.setMinimum(975)
        self.Imaging_Synapse2_Decay_slider.setMaximum(1000)
        self.Imaging_Synapse2_Decay_slider.setPageStep(10)
        self.Imaging_Synapse2_Decay_slider.setValue(995)
        self.Imaging_Synapse2_Decay_slider.setSliderPosition(995)
        self.Imaging_Synapse2_Decay_slider.setOrientation(Qt.Horizontal)
        self.Imaging_Synapse2_Decay_slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Synapse2_Decay_slider.setTickInterval(2)

        self.verticalLayout_107.addWidget(self.Imaging_Synapse2_Decay_slider)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_Decay_slider_frame)

        self.Imaging_Synapse2_Decay_values_frame = QFrame(self.Imaging_Synapse2_frame)
        self.Imaging_Synapse2_Decay_values_frame.setObjectName(u"Imaging_Synapse2_Decay_values_frame")
        self.Imaging_Synapse2_Decay_values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Synapse2_Decay_values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.Imaging_Synapse2_Decay_values_frame)
        self.horizontalLayout_156.setSpacing(0)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Synapse2_Decay_values_slow = QLabel(self.Imaging_Synapse2_Decay_values_frame)
        self.Imaging_Synapse2_Decay_values_slow.setObjectName(u"Imaging_Synapse2_Decay_values_slow")

        self.horizontalLayout_156.addWidget(self.Imaging_Synapse2_Decay_values_slow)

        self.Imaging_Synapse2_Decay_values_fast = QLabel(self.Imaging_Synapse2_Decay_values_frame)
        self.Imaging_Synapse2_Decay_values_fast.setObjectName(u"Imaging_Synapse2_Decay_values_fast")
        self.Imaging_Synapse2_Decay_values_fast.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.Imaging_Synapse2_Decay_values_fast)


        self.verticalLayout_105.addWidget(self.Imaging_Synapse2_Decay_values_frame)


        self.verticalLayout_108.addWidget(self.Imaging_Synapse2_frame)

        self.Imaging_parameter_stackedWidget.addWidget(self.Imaging_NeuronParameter_page)

        self.verticalLayout_76.addWidget(self.Imaging_parameter_stackedWidget)


        self.horizontalLayout_70.addWidget(self.Imaging_CenterMenuContainer)

        self.Imaging_rightMenuContainer = QFrame(self.page_201)
        self.Imaging_rightMenuContainer.setObjectName(u"Imaging_rightMenuContainer")
        self.Imaging_rightMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.Imaging_rightMenuContainer.setLayoutDirection(Qt.LeftToRight)
        self.Imaging_rightMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.Imaging_rightMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.Imaging_rightMenuContainer)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.Imaging_rightMenuSubContainer = QFrame(self.Imaging_rightMenuContainer)
        self.Imaging_rightMenuSubContainer.setObjectName(u"Imaging_rightMenuSubContainer")
        self.Imaging_rightMenuSubContainer.setFrameShape(QFrame.StyledPanel)
        self.Imaging_rightMenuSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.Imaging_rightMenuSubContainer)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 5, 0)
        self.Imaging_rightMenuSubContainer_frame = QFrame(self.Imaging_rightMenuSubContainer)
        self.Imaging_rightMenuSubContainer_frame.setObjectName(u"Imaging_rightMenuSubContainer_frame")
        self.Imaging_rightMenuSubContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_rightMenuSubContainer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.Imaging_rightMenuSubContainer_frame)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 20, 0, 0)
        self.Imaging_rightMenuSubContainer_pushButton = QPushButton(self.Imaging_rightMenuSubContainer_frame)
        self.Imaging_rightMenuSubContainer_pushButton.setObjectName(u"Imaging_rightMenuSubContainer_pushButton")
        self.Imaging_rightMenuSubContainer_pushButton.setMinimumSize(QSize(0, 0))
        self.Imaging_rightMenuSubContainer_pushButton.setFont(font1)
        self.Imaging_rightMenuSubContainer_pushButton.setStyleSheet(u"")
        self.Imaging_rightMenuSubContainer_pushButton.setIcon(icon19)
        self.Imaging_rightMenuSubContainer_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_134.addWidget(self.Imaging_rightMenuSubContainer_pushButton)


        self.verticalLayout_95.addWidget(self.Imaging_rightMenuSubContainer_frame, 0, Qt.AlignTop)

        self.Imaging_rightMenuParameterContainer_frame = QFrame(self.Imaging_rightMenuSubContainer)
        self.Imaging_rightMenuParameterContainer_frame.setObjectName(u"Imaging_rightMenuParameterContainer_frame")
        self.Imaging_rightMenuParameterContainer_frame.setLayoutDirection(Qt.LeftToRight)
        self.Imaging_rightMenuParameterContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_rightMenuParameterContainer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.Imaging_rightMenuParameterContainer_frame)
        self.verticalLayout_94.setSpacing(50)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Imaging_StimulusParameter_pushButton = QPushButton(self.Imaging_rightMenuParameterContainer_frame)
        self.Imaging_StimulusParameter_pushButton.setObjectName(u"Imaging_StimulusParameter_pushButton")
        self.Imaging_StimulusParameter_pushButton.setFont(font1)
        self.Imaging_StimulusParameter_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.Imaging_StimulusParameter_pushButton.setIcon(icon8)
        self.Imaging_StimulusParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_94.addWidget(self.Imaging_StimulusParameter_pushButton)

        self.Imaging_NeuronParameter_pushButton = QPushButton(self.Imaging_rightMenuParameterContainer_frame)
        self.Imaging_NeuronParameter_pushButton.setObjectName(u"Imaging_NeuronParameter_pushButton")
        self.Imaging_NeuronParameter_pushButton.setFont(font1)
        self.Imaging_NeuronParameter_pushButton.setIcon(icon5)
        self.Imaging_NeuronParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_94.addWidget(self.Imaging_NeuronParameter_pushButton)


        self.verticalLayout_95.addWidget(self.Imaging_rightMenuParameterContainer_frame)

        self.frame_2 = QFrame(self.Imaging_rightMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_95.addWidget(self.frame_2)


        self.verticalLayout_77.addWidget(self.Imaging_rightMenuSubContainer)


        self.horizontalLayout_70.addWidget(self.Imaging_rightMenuContainer)

        self.mainbody_stackedWidget.addWidget(self.page_201)
        self.page_202 = QWidget()
        self.page_202.setObjectName(u"page_202")
        self.horizontalLayout_72 = QHBoxLayout(self.page_202)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.page_202)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_45)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_73.addWidget(self.label_5)


        self.horizontalLayout_72.addWidget(self.frame_45)

        self.mainbody_stackedWidget.addWidget(self.page_202)
        self.page_203 = QWidget()
        self.page_203.setObjectName(u"page_203")
        self.horizontalLayout_75 = QHBoxLayout(self.page_203)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.page_203)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_46)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_74.addWidget(self.label_7)


        self.horizontalLayout_75.addWidget(self.frame_46)

        self.mainbody_stackedWidget.addWidget(self.page_203)
        self.page_301 = QWidget()
        self.page_301.setObjectName(u"page_301")
        self.page_301.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.page_301)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 9, 9, 9)
        self.NeuronGenerator_widget = QWidget(self.page_301)
        self.NeuronGenerator_widget.setObjectName(u"NeuronGenerator_widget")
        self.NeuronGenerator_widget.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.NeuronGenerator_widget)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subwidget1 = QWidget(self.NeuronGenerator_widget)
        self.NeuronGenerator_subwidget1.setObjectName(u"NeuronGenerator_subwidget1")
        self.verticalLayout_12 = QVBoxLayout(self.NeuronGenerator_subwidget1)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_top_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_top_frame.setObjectName(u"NeuronGenerator_subframe1_top_frame")
        self.NeuronGenerator_subframe1_top_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.NeuronGenerator_subframe1_top_frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_title_frame = QFrame(self.NeuronGenerator_subframe1_top_frame)
        self.NeuronGenerator_subframe1_title_frame.setObjectName(u"NeuronGenerator_subframe1_title_frame")
        self.NeuronGenerator_subframe1_title_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.NeuronGenerator_subframe1_title_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.NeuronGenerator_subframe1_title_label = QLabel(self.NeuronGenerator_subframe1_title_frame)
        self.NeuronGenerator_subframe1_title_label.setObjectName(u"NeuronGenerator_subframe1_title_label")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_title_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_title_label.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_title_label.setMaximumSize(QSize(16777215, 30))
        self.NeuronGenerator_subframe1_title_label.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.NeuronGenerator_subframe1_title_label, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.NeuronGenerator_subframe1_title_frame, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Izhik_frame = QFrame(self.NeuronGenerator_subframe1_top_frame)
        self.NeuronGenerator_subframe1_Izhik_frame.setObjectName(u"NeuronGenerator_subframe1_Izhik_frame")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_frame.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_Izhik_frame.setMaximumSize(QSize(16777215, 240))
        self.NeuronGenerator_subframe1_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_frame)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_subframe1 = QFrame(self.NeuronGenerator_subframe1_Izhik_frame)
        self.NeuronGenerator_subframe1_Izhik_subframe1.setObjectName(u"NeuronGenerator_subframe1_Izhik_subframe1")
        self.NeuronGenerator_subframe1_Izhik_subframe1.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_subframe1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_subframe1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_textbrowser = QTextBrowser(self.NeuronGenerator_subframe1_Izhik_subframe1)
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setObjectName(u"NeuronGenerator_subframe1_Izhik_textbrowser")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_textbrowser.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setSizePolicy(sizePolicy8)
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setMinimumSize(QSize(0, 240))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setMaximumSize(QSize(16777215, 200))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.NeuronGenerator_subframe1_Izhik_textbrowser, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_subframe1, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Izhik_subframe2 = QFrame(self.NeuronGenerator_subframe1_Izhik_frame)
        self.NeuronGenerator_subframe1_Izhik_subframe2.setObjectName(u"NeuronGenerator_subframe1_Izhik_subframe2")
        self.NeuronGenerator_subframe1_Izhik_subframe2.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_Izhik_subframe2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.NeuronGenerator_subframe1_Izhik_subframe2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_subframe2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.NeuronGenerator_subframe1_Izhik_frame, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_top_frame, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_middle_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_middle_frame.setObjectName(u"NeuronGenerator_subframe1_middle_frame")
        self.NeuronGenerator_subframe1_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.NeuronGenerator_subframe1_middle_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_Oscilloscope_widget = PlotWidget(self.NeuronGenerator_subframe1_middle_frame)
        self.NeuronGenerator_Oscilloscope_widget.setObjectName(u"NeuronGenerator_Oscilloscope_widget")
        sizePolicy5.setHeightForWidth(self.NeuronGenerator_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_Oscilloscope_widget.setSizePolicy(sizePolicy5)
        self.NeuronGenerator_Oscilloscope_widget.setStyleSheet(u"")
        self.verticalLayout_115 = QVBoxLayout(self.NeuronGenerator_Oscilloscope_widget)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.NeuronGenerator_Oscilloscope_widget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_186.setSpacing(150)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(5, 5, 5, 0)
        self.frame_15 = QFrame(self.frame_17)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(150, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_184 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_184.setSpacing(0)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox = QCheckBox(self.frame_15)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setObjectName(u"NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setEnabled(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setAutoFillBackground(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setStyleSheet(u"color: rgb(220, 50, 47);")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setChecked(True)

        self.horizontalLayout_184.addWidget(self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox = QCheckBox(self.frame_15)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setObjectName(u"NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setEnabled(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setAutoFillBackground(False)
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setChecked(True)

        self.horizontalLayout_184.addWidget(self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox, 0, Qt.AlignTop)


        self.horizontalLayout_186.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(200, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_185 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_185.setSpacing(0)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.StimInt_label = QLabel(self.frame_16)
        self.StimInt_label.setObjectName(u"StimInt_label")
        self.StimInt_label.setStyleSheet(u"color: rgb(38, 139, 210);")

        self.horizontalLayout_185.addWidget(self.StimInt_label, 0, Qt.AlignTop)

        self.StimInt_value = QLineEdit(self.frame_16)
        self.StimInt_value.setObjectName(u"StimInt_value")
        self.StimInt_value.setMaximumSize(QSize(50, 16777215))
        self.StimInt_value.setFont(font5)
        self.StimInt_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_185.addWidget(self.StimInt_value, 0, Qt.AlignTop)


        self.horizontalLayout_186.addWidget(self.frame_16)


        self.verticalLayout_115.addWidget(self.frame_17)


        self.horizontalLayout_12.addWidget(self.NeuronGenerator_Oscilloscope_widget)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_middle_frame)

        self.NeuronGenerator_subframe1_bottom_frame = QFrame(self.NeuronGenerator_subwidget1)
        self.NeuronGenerator_subframe1_bottom_frame.setObjectName(u"NeuronGenerator_subframe1_bottom_frame")
        sizePolicy1.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_frame.setSizePolicy(sizePolicy1)
        self.NeuronGenerator_subframe1_bottom_frame.setMinimumSize(QSize(0, 35))
        self.NeuronGenerator_subframe1_bottom_frame.setMaximumSize(QSize(16777215, 35))
        self.NeuronGenerator_subframe1_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe1_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.NeuronGenerator_subframe1_bottom_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_bottom_label = QLabel(self.NeuronGenerator_subframe1_bottom_frame)
        self.NeuronGenerator_subframe1_bottom_label.setObjectName(u"NeuronGenerator_subframe1_bottom_label")
        sizePolicy4.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_label.setSizePolicy(sizePolicy4)
        self.NeuronGenerator_subframe1_bottom_label.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.NeuronGenerator_subframe1_bottom_label, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.NeuronGenerator_subframe1_bottom_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_10.addWidget(self.NeuronGenerator_subwidget1)

        self.NeuronGenerator_subgroupBox2 = QGroupBox(self.NeuronGenerator_widget)
        self.NeuronGenerator_subgroupBox2.setObjectName(u"NeuronGenerator_subgroupBox2")
        self.NeuronGenerator_subgroupBox2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.NeuronGenerator_subgroupBox2.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subgroupBox2.setSizePolicy(sizePolicy)
        self.NeuronGenerator_subgroupBox2.setMinimumSize(QSize(400, 0))
        self.NeuronGenerator_subgroupBox2.setMaximumSize(QSize(400, 16777215))
        self.NeuronGenerator_subgroupBox2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.NeuronGenerator_subgroupBox2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe2 = QFrame(self.NeuronGenerator_subgroupBox2)
        self.NeuronGenerator_subframe2.setObjectName(u"NeuronGenerator_subframe2")
        self.NeuronGenerator_subframe2.setEnabled(True)
        self.NeuronGenerator_subframe2.setFrameShape(QFrame.StyledPanel)
        self.NeuronGenerator_subframe2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.NeuronGenerator_subframe2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.izhik_image = QFrame(self.NeuronGenerator_subframe2)
        self.izhik_image.setObjectName(u"izhik_image")
        sizePolicy1.setHeightForWidth(self.izhik_image.sizePolicy().hasHeightForWidth())
        self.izhik_image.setSizePolicy(sizePolicy1)
        self.izhik_image.setMinimumSize(QSize(0, 150))
        self.izhik_image.setMaximumSize(QSize(16777215, 200))
        self.izhik_image.setFrameShape(QFrame.StyledPanel)
        self.izhik_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.izhik_image)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.NeuronGenerator_subframe1_Izhik_image = QLabel(self.izhik_image)
        self.NeuronGenerator_subframe1_Izhik_image.setObjectName(u"NeuronGenerator_subframe1_Izhik_image")
        sizePolicy4.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_image.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_image.setSizePolicy(sizePolicy4)
        self.NeuronGenerator_subframe1_Izhik_image.setMinimumSize(QSize(225, 150))
        self.NeuronGenerator_subframe1_Izhik_image.setMaximumSize(QSize(225, 140))
        self.NeuronGenerator_subframe1_Izhik_image.setPixmap(QPixmap(u":/resources/resources/izhik.png"))
        self.NeuronGenerator_subframe1_Izhik_image.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.NeuronGenerator_subframe1_Izhik_image, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.izhik_image)

        self.line = QFrame(self.NeuronGenerator_subframe2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.a_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.a_Izhik_frame.setObjectName(u"a_Izhik_frame")
        self.a_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.a_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.a_Izhik_frame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.a_value_frame = QFrame(self.a_Izhik_frame)
        self.a_value_frame.setObjectName(u"a_value_frame")
        self.a_value_frame.setFrameShape(QFrame.StyledPanel)
        self.a_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.a_value_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.a_value = QLineEdit(self.a_value_frame)
        self.a_value.setObjectName(u"a_value")
        sizePolicy6.setHeightForWidth(self.a_value.sizePolicy().hasHeightForWidth())
        self.a_value.setSizePolicy(sizePolicy6)
        self.a_value.setMinimumSize(QSize(75, 0))
        self.a_value.setMaximumSize(QSize(50, 16777215))
        self.a_value.setFont(font5)
        self.a_value.setStyleSheet(u"")
        self.a_value.setFrame(True)
        self.a_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.a_value)


        self.horizontalLayout_18.addWidget(self.a_value_frame, 0, Qt.AlignLeft)

        self.a_text_frame = QFrame(self.a_Izhik_frame)
        self.a_text_frame.setObjectName(u"a_text_frame")
        self.a_text_frame.setFrameShape(QFrame.StyledPanel)
        self.a_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.a_text_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.a_text = QLabel(self.a_text_frame)
        self.a_text.setObjectName(u"a_text")
        sizePolicy4.setHeightForWidth(self.a_text.sizePolicy().hasHeightForWidth())
        self.a_text.setSizePolicy(sizePolicy4)
        self.a_text.setScaledContents(False)
        self.a_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.a_text.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.a_text)


        self.horizontalLayout_18.addWidget(self.a_text_frame)


        self.verticalLayout_14.addWidget(self.a_Izhik_frame)

        self.line_2 = QFrame(self.NeuronGenerator_subframe2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_2)

        self.b_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.b_Izhik_frame.setObjectName(u"b_Izhik_frame")
        self.b_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.b_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.b_Izhik_frame)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.b_value_frame = QFrame(self.b_Izhik_frame)
        self.b_value_frame.setObjectName(u"b_value_frame")
        self.b_value_frame.setFrameShape(QFrame.StyledPanel)
        self.b_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.b_value_frame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.b_value = QLineEdit(self.b_value_frame)
        self.b_value.setObjectName(u"b_value")
        sizePolicy6.setHeightForWidth(self.b_value.sizePolicy().hasHeightForWidth())
        self.b_value.setSizePolicy(sizePolicy6)
        self.b_value.setMinimumSize(QSize(75, 0))
        self.b_value.setMaximumSize(QSize(75, 16777215))
        self.b_value.setFont(font5)
        self.b_value.setStyleSheet(u"")
        self.b_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.b_value)


        self.horizontalLayout_21.addWidget(self.b_value_frame, 0, Qt.AlignLeft)

        self.b_text_frame = QFrame(self.b_Izhik_frame)
        self.b_text_frame.setObjectName(u"b_text_frame")
        sizePolicy4.setHeightForWidth(self.b_text_frame.sizePolicy().hasHeightForWidth())
        self.b_text_frame.setSizePolicy(sizePolicy4)
        self.b_text_frame.setFrameShape(QFrame.StyledPanel)
        self.b_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.b_text_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.b_text = QLabel(self.b_text_frame)
        self.b_text.setObjectName(u"b_text")
        self.b_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.b_text.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.b_text)


        self.horizontalLayout_21.addWidget(self.b_text_frame)


        self.verticalLayout_14.addWidget(self.b_Izhik_frame)

        self.line_3 = QFrame(self.NeuronGenerator_subframe2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_3)

        self.c_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.c_Izhik_frame.setObjectName(u"c_Izhik_frame")
        self.c_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.c_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.c_Izhik_frame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.c_value_frame = QFrame(self.c_Izhik_frame)
        self.c_value_frame.setObjectName(u"c_value_frame")
        self.c_value_frame.setFrameShape(QFrame.StyledPanel)
        self.c_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.c_value_frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.c_value = QLineEdit(self.c_value_frame)
        self.c_value.setObjectName(u"c_value")
        sizePolicy6.setHeightForWidth(self.c_value.sizePolicy().hasHeightForWidth())
        self.c_value.setSizePolicy(sizePolicy6)
        self.c_value.setMinimumSize(QSize(75, 0))
        self.c_value.setMaximumSize(QSize(75, 16777215))
        self.c_value.setFont(font5)
        self.c_value.setStyleSheet(u"")
        self.c_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.c_value)


        self.horizontalLayout_24.addWidget(self.c_value_frame)

        self.c_text_frame = QFrame(self.c_Izhik_frame)
        self.c_text_frame.setObjectName(u"c_text_frame")
        sizePolicy4.setHeightForWidth(self.c_text_frame.sizePolicy().hasHeightForWidth())
        self.c_text_frame.setSizePolicy(sizePolicy4)
        self.c_text_frame.setFrameShape(QFrame.StyledPanel)
        self.c_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.c_text_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.c_text = QLabel(self.c_text_frame)
        self.c_text.setObjectName(u"c_text")
        self.c_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.c_text.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.c_text)


        self.horizontalLayout_24.addWidget(self.c_text_frame)


        self.verticalLayout_14.addWidget(self.c_Izhik_frame)

        self.line_4 = QFrame(self.NeuronGenerator_subframe2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_4)

        self.d_Izhik_frame = QFrame(self.NeuronGenerator_subframe2)
        self.d_Izhik_frame.setObjectName(u"d_Izhik_frame")
        self.d_Izhik_frame.setFrameShape(QFrame.StyledPanel)
        self.d_Izhik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.d_Izhik_frame)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.d_value_frame = QFrame(self.d_Izhik_frame)
        self.d_value_frame.setObjectName(u"d_value_frame")
        self.d_value_frame.setFrameShape(QFrame.StyledPanel)
        self.d_value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.d_value_frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.d_value = QLineEdit(self.d_value_frame)
        self.d_value.setObjectName(u"d_value")
        sizePolicy6.setHeightForWidth(self.d_value.sizePolicy().hasHeightForWidth())
        self.d_value.setSizePolicy(sizePolicy6)
        self.d_value.setMinimumSize(QSize(75, 0))
        self.d_value.setMaximumSize(QSize(75, 16777215))
        self.d_value.setFont(font5)
        self.d_value.setStyleSheet(u"")
        self.d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.d_value)


        self.horizontalLayout_27.addWidget(self.d_value_frame, 0, Qt.AlignLeft)

        self.d_text_frame = QFrame(self.d_Izhik_frame)
        self.d_text_frame.setObjectName(u"d_text_frame")
        self.d_text_frame.setFrameShape(QFrame.StyledPanel)
        self.d_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.d_text_frame)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.d_text = QLabel(self.d_text_frame)
        self.d_text.setObjectName(u"d_text")
        sizePolicy4.setHeightForWidth(self.d_text.sizePolicy().hasHeightForWidth())
        self.d_text.setSizePolicy(sizePolicy4)
        self.d_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.d_text.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.d_text)


        self.horizontalLayout_27.addWidget(self.d_text_frame)


        self.verticalLayout_14.addWidget(self.d_Izhik_frame)

        self.line_5 = QFrame(self.NeuronGenerator_subframe2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_5)

        self.Izhik_button_frame = QFrame(self.NeuronGenerator_subframe2)
        self.Izhik_button_frame.setObjectName(u"Izhik_button_frame")
        self.Izhik_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Izhik_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.Izhik_button_frame)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.DisplayNeuron_frame = QFrame(self.Izhik_button_frame)
        self.DisplayNeuron_frame.setObjectName(u"DisplayNeuron_frame")
        self.DisplayNeuron_frame.setFrameShape(QFrame.StyledPanel)
        self.DisplayNeuron_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.DisplayNeuron_frame)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.DisplayNeuronPushButton = QPushButton(self.DisplayNeuron_frame)
        self.DisplayNeuronPushButton.setObjectName(u"DisplayNeuronPushButton")
        self.DisplayNeuronPushButton.setEnabled(True)
        self.DisplayNeuronPushButton.setFont(font4)
        self.DisplayNeuronPushButton.setMouseTracking(True)
        self.DisplayNeuronPushButton.setFocusPolicy(Qt.NoFocus)
        self.DisplayNeuronPushButton.setAutoFillBackground(False)
        self.DisplayNeuronPushButton.setStyleSheet(u"color: rgb(147, 161, 161);")
        self.DisplayNeuronPushButton.setCheckable(False)
        self.DisplayNeuronPushButton.setAutoRepeat(False)

        self.horizontalLayout_31.addWidget(self.DisplayNeuronPushButton)


        self.horizontalLayout_30.addWidget(self.DisplayNeuron_frame)

        self.SaveNeuron_frame = QFrame(self.Izhik_button_frame)
        self.SaveNeuron_frame.setObjectName(u"SaveNeuron_frame")
        self.SaveNeuron_frame.setFrameShape(QFrame.StyledPanel)
        self.SaveNeuron_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.SaveNeuron_frame)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.SaveNeuronPushButton = QPushButton(self.SaveNeuron_frame)
        self.SaveNeuronPushButton.setObjectName(u"SaveNeuronPushButton")
        self.SaveNeuronPushButton.setEnabled(True)
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setStrikeOut(False)
        self.SaveNeuronPushButton.setFont(font7)
        self.SaveNeuronPushButton.setStyleSheet(u"color: rgb(147, 161, 161);")
        self.SaveNeuronPushButton.setCheckable(False)

        self.horizontalLayout_32.addWidget(self.SaveNeuronPushButton)


        self.horizontalLayout_30.addWidget(self.SaveNeuron_frame)

        self.LoadNeuron_frame = QFrame(self.Izhik_button_frame)
        self.LoadNeuron_frame.setObjectName(u"LoadNeuron_frame")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        self.LoadNeuron_frame.setFont(font8)
        self.LoadNeuron_frame.setFrameShape(QFrame.StyledPanel)
        self.LoadNeuron_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_187 = QHBoxLayout(self.LoadNeuron_frame)
        self.horizontalLayout_187.setSpacing(0)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.LoadNeuron_comboBox = QComboBox(self.LoadNeuron_frame)
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.addItem("")
        self.LoadNeuron_comboBox.setObjectName(u"LoadNeuron_comboBox")
        self.LoadNeuron_comboBox.setFont(font4)

        self.horizontalLayout_187.addWidget(self.LoadNeuron_comboBox)


        self.horizontalLayout_30.addWidget(self.LoadNeuron_frame)


        self.verticalLayout_14.addWidget(self.Izhik_button_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.NeuronGenerator_subframe2)


        self.horizontalLayout_10.addWidget(self.NeuronGenerator_subgroupBox2)


        self.horizontalLayout_9.addWidget(self.NeuronGenerator_widget)

        self.mainbody_stackedWidget.addWidget(self.page_301)
        self.page_401 = QWidget()
        self.page_401.setObjectName(u"page_401")
        self.verticalLayout_110 = QVBoxLayout(self.page_401)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Container = QFrame(self.page_401)
        self.StimulusGenerator_Container.setObjectName(u"StimulusGenerator_Container")
        self.StimulusGenerator_Container.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_203 = QHBoxLayout(self.StimulusGenerator_Container)
        self.horizontalLayout_203.setSpacing(0)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_TopContainer = QFrame(self.StimulusGenerator_Container)
        self.StimulusGenerator_TopContainer.setObjectName(u"StimulusGenerator_TopContainer")
        self.StimulusGenerator_TopContainer.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_TopContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_201 = QHBoxLayout(self.StimulusGenerator_TopContainer)
        self.horizontalLayout_201.setSpacing(0)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.StimuluGenerator_LeftContainer = QFrame(self.StimulusGenerator_TopContainer)
        self.StimuluGenerator_LeftContainer.setObjectName(u"StimuluGenerator_LeftContainer")
        self.StimuluGenerator_LeftContainer.setFrameShape(QFrame.StyledPanel)
        self.StimuluGenerator_LeftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.StimuluGenerator_LeftContainer)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Selection_frame = QFrame(self.StimuluGenerator_LeftContainer)
        self.StimulusGenerator_Selection_frame.setObjectName(u"StimulusGenerator_Selection_frame")
        self.StimulusGenerator_Selection_frame.setMinimumSize(QSize(0, 100))
        self.StimulusGenerator_Selection_frame.setMaximumSize(QSize(16777215, 100))
        self.StimulusGenerator_Selection_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Selection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_200 = QHBoxLayout(self.StimulusGenerator_Selection_frame)
        self.horizontalLayout_200.setSpacing(0)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Selection_Label_frame = QFrame(self.StimulusGenerator_Selection_frame)
        self.StimulusGenerator_Selection_Label_frame.setObjectName(u"StimulusGenerator_Selection_Label_frame")
        self.StimulusGenerator_Selection_Label_frame.setMinimumSize(QSize(250, 0))
        self.StimulusGenerator_Selection_Label_frame.setMaximumSize(QSize(250, 16777215))
        self.StimulusGenerator_Selection_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Selection_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_204 = QHBoxLayout(self.StimulusGenerator_Selection_Label_frame)
        self.horizontalLayout_204.setSpacing(0)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Selection_Label = QLabel(self.StimulusGenerator_Selection_Label_frame)
        self.StimulusGenerator_Selection_Label.setObjectName(u"StimulusGenerator_Selection_Label")
        self.StimulusGenerator_Selection_Label.setFont(font1)
        self.StimulusGenerator_Selection_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_204.addWidget(self.StimulusGenerator_Selection_Label)


        self.horizontalLayout_200.addWidget(self.StimulusGenerator_Selection_Label_frame)

        self.StimulusGenerator_Selection_comboBox_frame = QFrame(self.StimulusGenerator_Selection_frame)
        self.StimulusGenerator_Selection_comboBox_frame.setObjectName(u"StimulusGenerator_Selection_comboBox_frame")
        self.StimulusGenerator_Selection_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Selection_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_206 = QHBoxLayout(self.StimulusGenerator_Selection_comboBox_frame)
        self.horizontalLayout_206.setSpacing(0)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Selection_comboBox = QComboBox(self.StimulusGenerator_Selection_comboBox_frame)
        self.StimulusGenerator_Selection_comboBox.addItem("")
        self.StimulusGenerator_Selection_comboBox.addItem("")
        self.StimulusGenerator_Selection_comboBox.addItem("")
        self.StimulusGenerator_Selection_comboBox.addItem("")
        self.StimulusGenerator_Selection_comboBox.addItem("")
        self.StimulusGenerator_Selection_comboBox.setObjectName(u"StimulusGenerator_Selection_comboBox")
        self.StimulusGenerator_Selection_comboBox.setMinimumSize(QSize(400, 0))
        self.StimulusGenerator_Selection_comboBox.setMaximumSize(QSize(400, 16777215))
        self.StimulusGenerator_Selection_comboBox.setFont(font1)

        self.horizontalLayout_206.addWidget(self.StimulusGenerator_Selection_comboBox)


        self.horizontalLayout_200.addWidget(self.StimulusGenerator_Selection_comboBox_frame, 0, Qt.AlignLeft)


        self.verticalLayout_127.addWidget(self.StimulusGenerator_Selection_frame)

        self.StimulusGenerator_Oscilloscope_frame = QFrame(self.StimuluGenerator_LeftContainer)
        self.StimulusGenerator_Oscilloscope_frame.setObjectName(u"StimulusGenerator_Oscilloscope_frame")
        self.StimulusGenerator_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.StimulusGenerator_Oscilloscope_frame)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Oscilloscope_widget = PlotWidget(self.StimulusGenerator_Oscilloscope_frame)
        self.StimulusGenerator_Oscilloscope_widget.setObjectName(u"StimulusGenerator_Oscilloscope_widget")
        self.verticalLayout_128 = QVBoxLayout(self.StimulusGenerator_Oscilloscope_widget)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame = QFrame(self.StimulusGenerator_Oscilloscope_widget)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame.setObjectName(u"StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame")
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame.setMaximumSize(QSize(16777215, 16777215))
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_216 = QHBoxLayout(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame)
        self.horizontalLayout_216.setSpacing(0)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(50, 5, 0, 0)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox = QCheckBox(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setObjectName(u"StimulusGenerator_Oscilloscope_widget_Stim_checkbox")
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setEnabled(False)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setAutoFillBackground(False)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setStyleSheet(u"color: rgb(38,139,210);")
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setChecked(True)

        self.horizontalLayout_216.addWidget(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox, 0, Qt.AlignTop)


        self.verticalLayout_128.addWidget(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame)


        self.verticalLayout_125.addWidget(self.StimulusGenerator_Oscilloscope_widget)


        self.verticalLayout_127.addWidget(self.StimulusGenerator_Oscilloscope_frame)


        self.horizontalLayout_201.addWidget(self.StimuluGenerator_LeftContainer)

        self.line_42 = QFrame(self.StimulusGenerator_TopContainer)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.VLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_201.addWidget(self.line_42)

        self.line_44 = QFrame(self.StimulusGenerator_TopContainer)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.VLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_201.addWidget(self.line_44)

        self.StimulusGenerator_Parameter_frame = QFrame(self.StimulusGenerator_TopContainer)
        self.StimulusGenerator_Parameter_frame.setObjectName(u"StimulusGenerator_Parameter_frame")
        self.StimulusGenerator_Parameter_frame.setMaximumSize(QSize(300, 16777215))
        self.StimulusGenerator_Parameter_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Parameter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_205 = QHBoxLayout(self.StimulusGenerator_Parameter_frame)
        self.horizontalLayout_205.setSpacing(0)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Parameter_stackedWidget = QStackedWidget(self.StimulusGenerator_Parameter_frame)
        self.StimulusGenerator_Parameter_stackedWidget.setObjectName(u"StimulusGenerator_Parameter_stackedWidget")
        self.page_IntensitySteps = QWidget()
        self.page_IntensitySteps.setObjectName(u"page_IntensitySteps")
        self.StimulusGenerator_Parameter_stackedWidget.addWidget(self.page_IntensitySteps)
        self.page_SineWave = QWidget()
        self.page_SineWave.setObjectName(u"page_SineWave")
        self.verticalLayout_126 = QVBoxLayout(self.page_SineWave)
        self.verticalLayout_126.setSpacing(20)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 5)
        self.SineWave_Amplitude_frame = QFrame(self.page_SineWave)
        self.SineWave_Amplitude_frame.setObjectName(u"SineWave_Amplitude_frame")
        self.SineWave_Amplitude_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Amplitude_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_208 = QHBoxLayout(self.SineWave_Amplitude_frame)
        self.horizontalLayout_208.setSpacing(0)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Amplitude_Label_frame = QFrame(self.SineWave_Amplitude_frame)
        self.SineWave_Amplitude_Label_frame.setObjectName(u"SineWave_Amplitude_Label_frame")
        self.SineWave_Amplitude_Label_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Amplitude_Label_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Amplitude_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Amplitude_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_209 = QHBoxLayout(self.SineWave_Amplitude_Label_frame)
        self.horizontalLayout_209.setSpacing(0)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Amplitude_Label = QLabel(self.SineWave_Amplitude_Label_frame)
        self.SineWave_Amplitude_Label.setObjectName(u"SineWave_Amplitude_Label")
        self.SineWave_Amplitude_Label.setFont(font1)
        self.SineWave_Amplitude_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_209.addWidget(self.SineWave_Amplitude_Label)


        self.horizontalLayout_208.addWidget(self.SineWave_Amplitude_Label_frame)

        self.SineWave_Amplitude_Value_frame = QFrame(self.SineWave_Amplitude_frame)
        self.SineWave_Amplitude_Value_frame.setObjectName(u"SineWave_Amplitude_Value_frame")
        self.SineWave_Amplitude_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Amplitude_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Amplitude_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Amplitude_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_212 = QHBoxLayout(self.SineWave_Amplitude_Value_frame)
        self.horizontalLayout_212.setSpacing(0)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Amplitude_Value = QLineEdit(self.SineWave_Amplitude_Value_frame)
        self.SineWave_Amplitude_Value.setObjectName(u"SineWave_Amplitude_Value")
        self.SineWave_Amplitude_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_Amplitude_Value.setFont(font5)
        self.SineWave_Amplitude_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_212.addWidget(self.SineWave_Amplitude_Value)


        self.horizontalLayout_208.addWidget(self.SineWave_Amplitude_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_Amplitude_frame)

        self.SineWave_Frequency_frame = QFrame(self.page_SineWave)
        self.SineWave_Frequency_frame.setObjectName(u"SineWave_Frequency_frame")
        self.SineWave_Frequency_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Frequency_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_207 = QHBoxLayout(self.SineWave_Frequency_frame)
        self.horizontalLayout_207.setSpacing(0)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_207.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Frequency_Label_frame = QFrame(self.SineWave_Frequency_frame)
        self.SineWave_Frequency_Label_frame.setObjectName(u"SineWave_Frequency_Label_frame")
        self.SineWave_Frequency_Label_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Frequency_Label_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Frequency_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Frequency_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_210 = QHBoxLayout(self.SineWave_Frequency_Label_frame)
        self.horizontalLayout_210.setSpacing(0)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Frequency_Label = QLabel(self.SineWave_Frequency_Label_frame)
        self.SineWave_Frequency_Label.setObjectName(u"SineWave_Frequency_Label")
        self.SineWave_Frequency_Label.setMinimumSize(QSize(150, 0))
        self.SineWave_Frequency_Label.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Frequency_Label.setFont(font1)
        self.SineWave_Frequency_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_210.addWidget(self.SineWave_Frequency_Label)


        self.horizontalLayout_207.addWidget(self.SineWave_Frequency_Label_frame)

        self.SineWave_Frequency_Value_frame = QFrame(self.SineWave_Frequency_frame)
        self.SineWave_Frequency_Value_frame.setObjectName(u"SineWave_Frequency_Value_frame")
        self.SineWave_Frequency_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Frequency_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Frequency_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Frequency_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_211 = QHBoxLayout(self.SineWave_Frequency_Value_frame)
        self.horizontalLayout_211.setSpacing(0)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Frequency_Value = QLineEdit(self.SineWave_Frequency_Value_frame)
        self.SineWave_Frequency_Value.setObjectName(u"SineWave_Frequency_Value")
        self.SineWave_Frequency_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_Frequency_Value.setFont(font5)
        self.SineWave_Frequency_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_211.addWidget(self.SineWave_Frequency_Value)


        self.horizontalLayout_207.addWidget(self.SineWave_Frequency_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_Frequency_frame)

        self.SineWave_Mean_frame = QFrame(self.page_SineWave)
        self.SineWave_Mean_frame.setObjectName(u"SineWave_Mean_frame")
        self.SineWave_Mean_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Mean_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_213 = QHBoxLayout(self.SineWave_Mean_frame)
        self.horizontalLayout_213.setSpacing(0)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Mean_Label_frame = QFrame(self.SineWave_Mean_frame)
        self.SineWave_Mean_Label_frame.setObjectName(u"SineWave_Mean_Label_frame")
        self.SineWave_Mean_Label_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Mean_Label_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Mean_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Mean_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_214 = QHBoxLayout(self.SineWave_Mean_Label_frame)
        self.horizontalLayout_214.setSpacing(0)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Mean_Label = QLabel(self.SineWave_Mean_Label_frame)
        self.SineWave_Mean_Label.setObjectName(u"SineWave_Mean_Label")
        self.SineWave_Mean_Label.setMinimumSize(QSize(150, 0))
        self.SineWave_Mean_Label.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Mean_Label.setFont(font1)
        self.SineWave_Mean_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_214.addWidget(self.SineWave_Mean_Label)


        self.horizontalLayout_213.addWidget(self.SineWave_Mean_Label_frame)

        self.SineWave_Mean_Value_frame = QFrame(self.SineWave_Mean_frame)
        self.SineWave_Mean_Value_frame.setObjectName(u"SineWave_Mean_Value_frame")
        self.SineWave_Mean_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_Mean_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_Mean_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_Mean_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_215 = QHBoxLayout(self.SineWave_Mean_Value_frame)
        self.horizontalLayout_215.setSpacing(0)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.SineWave_Mean_Value = QLineEdit(self.SineWave_Mean_Value_frame)
        self.SineWave_Mean_Value.setObjectName(u"SineWave_Mean_Value")
        self.SineWave_Mean_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_Mean_Value.setFont(font5)
        self.SineWave_Mean_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_215.addWidget(self.SineWave_Mean_Value)


        self.horizontalLayout_213.addWidget(self.SineWave_Mean_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_Mean_frame)

        self.SineWave_StimOn_frame = QFrame(self.page_SineWave)
        self.SineWave_StimOn_frame.setObjectName(u"SineWave_StimOn_frame")
        self.SineWave_StimOn_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_220 = QHBoxLayout(self.SineWave_StimOn_frame)
        self.horizontalLayout_220.setSpacing(0)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.horizontalLayout_220.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOn_Label_frame = QFrame(self.SineWave_StimOn_frame)
        self.SineWave_StimOn_Label_frame.setObjectName(u"SineWave_StimOn_Label_frame")
        self.SineWave_StimOn_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOn_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_219 = QHBoxLayout(self.SineWave_StimOn_Label_frame)
        self.horizontalLayout_219.setSpacing(0)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOn_Label = QLabel(self.SineWave_StimOn_Label_frame)
        self.SineWave_StimOn_Label.setObjectName(u"SineWave_StimOn_Label")
        self.SineWave_StimOn_Label.setFont(font1)
        self.SineWave_StimOn_Label.setAlignment(Qt.AlignCenter)
        self.SineWave_StimOn_Label.setWordWrap(True)

        self.horizontalLayout_219.addWidget(self.SineWave_StimOn_Label)


        self.horizontalLayout_220.addWidget(self.SineWave_StimOn_Label_frame)

        self.SineWave_StimOn_Value_frame = QFrame(self.SineWave_StimOn_frame)
        self.SineWave_StimOn_Value_frame.setObjectName(u"SineWave_StimOn_Value_frame")
        self.SineWave_StimOn_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_StimOn_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_StimOn_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOn_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_217 = QHBoxLayout(self.SineWave_StimOn_Value_frame)
        self.horizontalLayout_217.setSpacing(0)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.horizontalLayout_217.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOn_Value = QLineEdit(self.SineWave_StimOn_Value_frame)
        self.SineWave_StimOn_Value.setObjectName(u"SineWave_StimOn_Value")
        self.SineWave_StimOn_Value.setMinimumSize(QSize(100, 0))
        self.SineWave_StimOn_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_StimOn_Value.setFont(font5)
        self.SineWave_StimOn_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_217.addWidget(self.SineWave_StimOn_Value)


        self.horizontalLayout_220.addWidget(self.SineWave_StimOn_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_StimOn_frame)

        self.SineWave_IntOff_frame = QFrame(self.page_SineWave)
        self.SineWave_IntOff_frame.setObjectName(u"SineWave_IntOff_frame")
        self.SineWave_IntOff_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_IntOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_225 = QHBoxLayout(self.SineWave_IntOff_frame)
        self.horizontalLayout_225.setSpacing(0)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.horizontalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.SineWave_IntOff_Label_frame = QFrame(self.SineWave_IntOff_frame)
        self.SineWave_IntOff_Label_frame.setObjectName(u"SineWave_IntOff_Label_frame")
        self.SineWave_IntOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_IntOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_224 = QHBoxLayout(self.SineWave_IntOff_Label_frame)
        self.horizontalLayout_224.setSpacing(0)
        self.horizontalLayout_224.setObjectName(u"horizontalLayout_224")
        self.horizontalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.SineWave_IntOff_Label = QLabel(self.SineWave_IntOff_Label_frame)
        self.SineWave_IntOff_Label.setObjectName(u"SineWave_IntOff_Label")
        self.SineWave_IntOff_Label.setFont(font1)
        self.SineWave_IntOff_Label.setAlignment(Qt.AlignCenter)
        self.SineWave_IntOff_Label.setWordWrap(True)

        self.horizontalLayout_224.addWidget(self.SineWave_IntOff_Label)


        self.horizontalLayout_225.addWidget(self.SineWave_IntOff_Label_frame)

        self.SineWave_IntOff_Value_frame = QFrame(self.SineWave_IntOff_frame)
        self.SineWave_IntOff_Value_frame.setObjectName(u"SineWave_IntOff_Value_frame")
        self.SineWave_IntOff_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_IntOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_IntOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_IntOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_223 = QHBoxLayout(self.SineWave_IntOff_Value_frame)
        self.horizontalLayout_223.setSpacing(0)
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.horizontalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.SineWave_IntOff_Value = QLineEdit(self.SineWave_IntOff_Value_frame)
        self.SineWave_IntOff_Value.setObjectName(u"SineWave_IntOff_Value")
        self.SineWave_IntOff_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_IntOff_Value.setFont(font5)
        self.SineWave_IntOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_223.addWidget(self.SineWave_IntOff_Value)


        self.horizontalLayout_225.addWidget(self.SineWave_IntOff_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_IntOff_frame)

        self.SineWave_StimOff_frame = QFrame(self.page_SineWave)
        self.SineWave_StimOff_frame.setObjectName(u"SineWave_StimOff_frame")
        self.SineWave_StimOff_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_221 = QHBoxLayout(self.SineWave_StimOff_frame)
        self.horizontalLayout_221.setSpacing(0)
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.horizontalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOff_Label_frame = QFrame(self.SineWave_StimOff_frame)
        self.SineWave_StimOff_Label_frame.setObjectName(u"SineWave_StimOff_Label_frame")
        self.SineWave_StimOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_218 = QHBoxLayout(self.SineWave_StimOff_Label_frame)
        self.horizontalLayout_218.setSpacing(0)
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.horizontalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOff_Label = QLabel(self.SineWave_StimOff_Label_frame)
        self.SineWave_StimOff_Label.setObjectName(u"SineWave_StimOff_Label")
        self.SineWave_StimOff_Label.setFont(font1)
        self.SineWave_StimOff_Label.setAlignment(Qt.AlignCenter)
        self.SineWave_StimOff_Label.setWordWrap(True)

        self.horizontalLayout_218.addWidget(self.SineWave_StimOff_Label)


        self.horizontalLayout_221.addWidget(self.SineWave_StimOff_Label_frame)

        self.SineWave_StimOff_Value_frame = QFrame(self.SineWave_StimOff_frame)
        self.SineWave_StimOff_Value_frame.setObjectName(u"SineWave_StimOff_Value_frame")
        self.SineWave_StimOff_Value_frame.setMinimumSize(QSize(150, 0))
        self.SineWave_StimOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.SineWave_StimOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.SineWave_StimOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_222 = QHBoxLayout(self.SineWave_StimOff_Value_frame)
        self.horizontalLayout_222.setSpacing(0)
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.horizontalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.SineWave_StimOff_Value = QLineEdit(self.SineWave_StimOff_Value_frame)
        self.SineWave_StimOff_Value.setObjectName(u"SineWave_StimOff_Value")
        self.SineWave_StimOff_Value.setMinimumSize(QSize(100, 0))
        self.SineWave_StimOff_Value.setMaximumSize(QSize(100, 16777215))
        self.SineWave_StimOff_Value.setFont(font5)
        self.SineWave_StimOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_222.addWidget(self.SineWave_StimOff_Value)


        self.horizontalLayout_221.addWidget(self.SineWave_StimOff_Value_frame)


        self.verticalLayout_126.addWidget(self.SineWave_StimOff_frame)

        self.StimulusGenerator_Parameter_stackedWidget.addWidget(self.page_SineWave)

        self.horizontalLayout_205.addWidget(self.StimulusGenerator_Parameter_stackedWidget)


        self.horizontalLayout_201.addWidget(self.StimulusGenerator_Parameter_frame)


        self.horizontalLayout_203.addWidget(self.StimulusGenerator_TopContainer)


        self.verticalLayout_110.addWidget(self.StimulusGenerator_Container)

        self.StimulusGenerator_SubContainer = QFrame(self.page_401)
        self.StimulusGenerator_SubContainer.setObjectName(u"StimulusGenerator_SubContainer")
        self.StimulusGenerator_SubContainer.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_SubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_202 = QHBoxLayout(self.StimulusGenerator_SubContainer)
        self.horizontalLayout_202.setSpacing(100)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(75, 0, 75, 5)
        self.StimulusGenerator_Display_pushButton = QPushButton(self.StimulusGenerator_SubContainer)
        self.StimulusGenerator_Display_pushButton.setObjectName(u"StimulusGenerator_Display_pushButton")
        self.StimulusGenerator_Display_pushButton.setMinimumSize(QSize(200, 0))
        self.StimulusGenerator_Display_pushButton.setMaximumSize(QSize(200, 16777215))
        self.StimulusGenerator_Display_pushButton.setFont(font1)

        self.horizontalLayout_202.addWidget(self.StimulusGenerator_Display_pushButton)

        self.StimulusGenerator_Save_pushButton = QPushButton(self.StimulusGenerator_SubContainer)
        self.StimulusGenerator_Save_pushButton.setObjectName(u"StimulusGenerator_Save_pushButton")
        self.StimulusGenerator_Save_pushButton.setMinimumSize(QSize(200, 0))
        self.StimulusGenerator_Save_pushButton.setMaximumSize(QSize(200, 16777215))
        self.StimulusGenerator_Save_pushButton.setFont(font1)

        self.horizontalLayout_202.addWidget(self.StimulusGenerator_Save_pushButton)

        self.frame_5 = QFrame(self.StimulusGenerator_SubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_202.addWidget(self.frame_5)


        self.verticalLayout_110.addWidget(self.StimulusGenerator_SubContainer)

        self.mainbody_stackedWidget.addWidget(self.page_401)
        self.page_501 = QWidget()
        self.page_501.setObjectName(u"page_501")
        self.horizontalLayout_192 = QHBoxLayout(self.page_501)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.Exercises_Main_frame = QFrame(self.page_501)
        self.Exercises_Main_frame.setObjectName(u"Exercises_Main_frame")
        self.Exercises_Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercises_Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.Exercises_Main_frame)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.Exercises_StackedWideget_frame = QFrame(self.Exercises_Main_frame)
        self.Exercises_StackedWideget_frame.setObjectName(u"Exercises_StackedWideget_frame")
        self.Exercises_StackedWideget_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercises_StackedWideget_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.Exercises_StackedWideget_frame)
        self.horizontalLayout_159.setSpacing(0)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.Exercises_stackedWidget = QStackedWidget(self.Exercises_StackedWideget_frame)
        self.Exercises_stackedWidget.setObjectName(u"Exercises_stackedWidget")
        self.page501_01_01 = QWidget()
        self.page501_01_01.setObjectName(u"page501_01_01")
        self.verticalLayout_119 = QVBoxLayout(self.page501_01_01)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.Vm_Intro_frame = QFrame(self.page501_01_01)
        self.Vm_Intro_frame.setObjectName(u"Vm_Intro_frame")
        self.Vm_Intro_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Intro_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.Vm_Intro_frame)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.Vm_IntroTitle_frame = QFrame(self.Vm_Intro_frame)
        self.Vm_IntroTitle_frame.setObjectName(u"Vm_IntroTitle_frame")
        self.Vm_IntroTitle_frame.setMaximumSize(QSize(16777215, 50))
        self.Vm_IntroTitle_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_IntroTitle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_193 = QHBoxLayout(self.Vm_IntroTitle_frame)
        self.horizontalLayout_193.setSpacing(0)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.Vm_IntroTitle = QLabel(self.Vm_IntroTitle_frame)
        self.Vm_IntroTitle.setObjectName(u"Vm_IntroTitle")
        self.Vm_IntroTitle.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setPointSize(18)
        self.Vm_IntroTitle.setFont(font9)
        self.Vm_IntroTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_193.addWidget(self.Vm_IntroTitle)


        self.verticalLayout_117.addWidget(self.Vm_IntroTitle_frame)

        self.Vm_IntroText_frame = QFrame(self.Vm_Intro_frame)
        self.Vm_IntroText_frame.setObjectName(u"Vm_IntroText_frame")
        self.Vm_IntroText_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_IntroText_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_195 = QHBoxLayout(self.Vm_IntroText_frame)
        self.horizontalLayout_195.setSpacing(0)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.Vm_IntroText = QLabel(self.Vm_IntroText_frame)
        self.Vm_IntroText.setObjectName(u"Vm_IntroText")
        self.Vm_IntroText.setWordWrap(True)

        self.horizontalLayout_195.addWidget(self.Vm_IntroText)


        self.verticalLayout_117.addWidget(self.Vm_IntroText_frame)


        self.verticalLayout_119.addWidget(self.Vm_Intro_frame)

        self.Exercises_stackedWidget.addWidget(self.page501_01_01)
        self.page501_01_02 = QWidget()
        self.page501_01_02.setObjectName(u"page501_01_02")
        self.verticalLayout_118 = QVBoxLayout(self.page501_01_02)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task01_frame = QFrame(self.page501_01_02)
        self.Vm_Task01_frame.setObjectName(u"Vm_Task01_frame")
        self.Vm_Task01_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task01_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.Vm_Task01_frame)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task01_Title_frame = QFrame(self.Vm_Task01_frame)
        self.Vm_Task01_Title_frame.setObjectName(u"Vm_Task01_Title_frame")
        sizePolicy3.setHeightForWidth(self.Vm_Task01_Title_frame.sizePolicy().hasHeightForWidth())
        self.Vm_Task01_Title_frame.setSizePolicy(sizePolicy3)
        self.Vm_Task01_Title_frame.setMaximumSize(QSize(16777215, 50))
        font10 = QFont()
        font10.setPointSize(14)
        self.Vm_Task01_Title_frame.setFont(font10)
        self.Vm_Task01_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task01_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_194 = QHBoxLayout(self.Vm_Task01_Title_frame)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task01_Title = QLabel(self.Vm_Task01_Title_frame)
        self.Vm_Task01_Title.setObjectName(u"Vm_Task01_Title")
        self.Vm_Task01_Title.setMaximumSize(QSize(16777215, 50))
        self.Vm_Task01_Title.setFont(font9)
        self.Vm_Task01_Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_194.addWidget(self.Vm_Task01_Title)


        self.verticalLayout_120.addWidget(self.Vm_Task01_Title_frame)

        self.Vm_Task01_Text_frame = QFrame(self.Vm_Task01_frame)
        self.Vm_Task01_Text_frame.setObjectName(u"Vm_Task01_Text_frame")
        self.Vm_Task01_Text_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task01_Text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_188 = QHBoxLayout(self.Vm_Task01_Text_frame)
        self.horizontalLayout_188.setSpacing(0)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task01_Text = QLabel(self.Vm_Task01_Text_frame)
        self.Vm_Task01_Text.setObjectName(u"Vm_Task01_Text")
        self.Vm_Task01_Text.setTextFormat(Qt.AutoText)
        self.Vm_Task01_Text.setWordWrap(True)

        self.horizontalLayout_188.addWidget(self.Vm_Task01_Text)


        self.verticalLayout_120.addWidget(self.Vm_Task01_Text_frame)


        self.verticalLayout_118.addWidget(self.Vm_Task01_frame)

        self.Exercises_stackedWidget.addWidget(self.page501_01_02)
        self.page501_01_03 = QWidget()
        self.page501_01_03.setObjectName(u"page501_01_03")
        self.verticalLayout_122 = QVBoxLayout(self.page501_01_03)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task02_frame = QFrame(self.page501_01_03)
        self.Vm_Task02_frame.setObjectName(u"Vm_Task02_frame")
        self.Vm_Task02_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task02_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.Vm_Task02_frame)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task02_Text_frame = QFrame(self.Vm_Task02_frame)
        self.Vm_Task02_Text_frame.setObjectName(u"Vm_Task02_Text_frame")
        self.Vm_Task02_Text_frame.setMaximumSize(QSize(16777215, 50))
        self.Vm_Task02_Text_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task02_Text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_196 = QHBoxLayout(self.Vm_Task02_Text_frame)
        self.horizontalLayout_196.setSpacing(0)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task02_Text = QLabel(self.Vm_Task02_Text_frame)
        self.Vm_Task02_Text.setObjectName(u"Vm_Task02_Text")
        self.Vm_Task02_Text.setFont(font9)
        self.Vm_Task02_Text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_196.addWidget(self.Vm_Task02_Text)


        self.verticalLayout_121.addWidget(self.Vm_Task02_Text_frame)

        self.Vm_Task02_Title_frame = QFrame(self.Vm_Task02_frame)
        self.Vm_Task02_Title_frame.setObjectName(u"Vm_Task02_Title_frame")
        self.Vm_Task02_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task02_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_197 = QHBoxLayout(self.Vm_Task02_Title_frame)
        self.horizontalLayout_197.setSpacing(0)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task02_Title = QLabel(self.Vm_Task02_Title_frame)
        self.Vm_Task02_Title.setObjectName(u"Vm_Task02_Title")
        self.Vm_Task02_Title.setWordWrap(True)

        self.horizontalLayout_197.addWidget(self.Vm_Task02_Title)


        self.verticalLayout_121.addWidget(self.Vm_Task02_Title_frame)


        self.verticalLayout_122.addWidget(self.Vm_Task02_frame)

        self.Exercises_stackedWidget.addWidget(self.page501_01_03)
        self.page501_01_04 = QWidget()
        self.page501_01_04.setObjectName(u"page501_01_04")
        self.verticalLayout_124 = QVBoxLayout(self.page501_01_04)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task03_frame = QFrame(self.page501_01_04)
        self.Vm_Task03_frame.setObjectName(u"Vm_Task03_frame")
        self.Vm_Task03_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task03_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.Vm_Task03_frame)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task03_Title_frame = QFrame(self.Vm_Task03_frame)
        self.Vm_Task03_Title_frame.setObjectName(u"Vm_Task03_Title_frame")
        self.Vm_Task03_Title_frame.setMaximumSize(QSize(16777215, 50))
        self.Vm_Task03_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task03_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_198 = QHBoxLayout(self.Vm_Task03_Title_frame)
        self.horizontalLayout_198.setSpacing(0)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task03_Title = QLabel(self.Vm_Task03_Title_frame)
        self.Vm_Task03_Title.setObjectName(u"Vm_Task03_Title")
        self.Vm_Task03_Title.setMaximumSize(QSize(16777215, 50))
        self.Vm_Task03_Title.setFont(font9)
        self.Vm_Task03_Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_198.addWidget(self.Vm_Task03_Title)


        self.verticalLayout_123.addWidget(self.Vm_Task03_Title_frame)

        self.Vm_Task03_Text_frame = QFrame(self.Vm_Task03_frame)
        self.Vm_Task03_Text_frame.setObjectName(u"Vm_Task03_Text_frame")
        self.Vm_Task03_Text_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task03_Text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_199 = QHBoxLayout(self.Vm_Task03_Text_frame)
        self.horizontalLayout_199.setSpacing(0)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task03_Text = QLabel(self.Vm_Task03_Text_frame)
        self.Vm_Task03_Text.setObjectName(u"Vm_Task03_Text")
        self.Vm_Task03_Text.setWordWrap(True)

        self.horizontalLayout_199.addWidget(self.Vm_Task03_Text)


        self.verticalLayout_123.addWidget(self.Vm_Task03_Text_frame)


        self.verticalLayout_124.addWidget(self.Vm_Task03_frame)

        self.Exercises_stackedWidget.addWidget(self.page501_01_04)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Exercises_stackedWidget.addWidget(self.page)

        self.horizontalLayout_159.addWidget(self.Exercises_stackedWidget)


        self.verticalLayout_116.addWidget(self.Exercises_StackedWideget_frame)

        self.Exercises_Button_frame = QFrame(self.Exercises_Main_frame)
        self.Exercises_Button_frame.setObjectName(u"Exercises_Button_frame")
        self.Exercises_Button_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercises_Button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_191 = QHBoxLayout(self.Exercises_Button_frame)
        self.horizontalLayout_191.setSpacing(0)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.Exercises_PreviousButton_frame = QFrame(self.Exercises_Button_frame)
        self.Exercises_PreviousButton_frame.setObjectName(u"Exercises_PreviousButton_frame")
        self.Exercises_PreviousButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercises_PreviousButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_190 = QHBoxLayout(self.Exercises_PreviousButton_frame)
        self.horizontalLayout_190.setSpacing(0)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.Exercises_PreviousButton_pushButton = QPushButton(self.Exercises_PreviousButton_frame)
        self.Exercises_PreviousButton_pushButton.setObjectName(u"Exercises_PreviousButton_pushButton")

        self.horizontalLayout_190.addWidget(self.Exercises_PreviousButton_pushButton)


        self.horizontalLayout_191.addWidget(self.Exercises_PreviousButton_frame)

        self.Exercises_AfterButton_frame = QFrame(self.Exercises_Button_frame)
        self.Exercises_AfterButton_frame.setObjectName(u"Exercises_AfterButton_frame")
        self.Exercises_AfterButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercises_AfterButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.Exercises_AfterButton_frame)
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(0, 0, 0, 0)
        self.Exercises_AfterButton_pushButton = QPushButton(self.Exercises_AfterButton_frame)
        self.Exercises_AfterButton_pushButton.setObjectName(u"Exercises_AfterButton_pushButton")

        self.horizontalLayout_189.addWidget(self.Exercises_AfterButton_pushButton)


        self.horizontalLayout_191.addWidget(self.Exercises_AfterButton_frame)


        self.verticalLayout_116.addWidget(self.Exercises_Button_frame)


        self.horizontalLayout_192.addWidget(self.Exercises_Main_frame)

        self.mainbody_stackedWidget.addWidget(self.page_501)
        self.page_502 = QWidget()
        self.page_502.setObjectName(u"page_502")
        self.frame_10 = QFrame(self.page_502)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(80, 20, 860, 613))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_10)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))

        self.verticalLayout_113.addWidget(self.label_19)

        self.mainbody_stackedWidget.addWidget(self.page_502)
        self.page_601 = QWidget()
        self.page_601.setObjectName(u"page_601")
        self.frame_11 = QFrame(self.page_601)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(70, 30, 860, 613))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))

        self.horizontalLayout_160.addWidget(self.label_20)

        self.mainbody_stackedWidget.addWidget(self.page_601)
        self.page_701 = QWidget()
        self.page_701.setObjectName(u"page_701")
        self.frame_12 = QFrame(self.page_701)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(60, 30, 860, 613))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_12)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))

        self.verticalLayout_114.addWidget(self.label_21)

        self.mainbody_stackedWidget.addWidget(self.page_701)
        self.page_801 = QWidget()
        self.page_801.setObjectName(u"page_801")
        self.frame_13 = QFrame(self.page_801)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(70, 30, 860, 613))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))

        self.horizontalLayout_161.addWidget(self.label_22)

        self.mainbody_stackedWidget.addWidget(self.page_801)
        self.page_901 = QWidget()
        self.page_901.setObjectName(u"page_901")
        self.frame_14 = QFrame(self.page_901)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(70, 30, 860, 613))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/resources/resources/under_construction.svg"))

        self.horizontalLayout_162.addWidget(self.label_23)

        self.mainbody_stackedWidget.addWidget(self.page_901)

        self.horizontalLayout_7.addWidget(self.mainbody_stackedWidget)


        self.verticalLayout_2.addWidget(self.mainbodyContainer)


        self.horizontalLayout_112.addWidget(self.mainWindowContainer)


        self.verticalLayout_75.addWidget(self.CenterMainFrame)

        self.BottomMainFrame = QFrame(self.centralwidget)
        self.BottomMainFrame.setObjectName(u"BottomMainFrame")
        self.BottomMainFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.BottomMainFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.footer_widget = QWidget(self.BottomMainFrame)
        self.footer_widget.setObjectName(u"footer_widget")
        self.footer_widget.setMinimumSize(QSize(0, 30))
        self.footer_widget.setMaximumSize(QSize(16777215, 50))
        self.footer_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.footer_widget)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.license_frame = QFrame(self.footer_widget)
        self.license_frame.setObjectName(u"license_frame")
        self.license_frame.setFrameShape(QFrame.StyledPanel)
        self.license_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.license_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.license_frame)
        self.line_6.setObjectName(u"line_6")
        sizePolicy8.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy8)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.license_label = QLabel(self.license_frame)
        self.license_label.setObjectName(u"license_label")

        self.verticalLayout_3.addWidget(self.license_label)


        self.horizontalLayout_3.addWidget(self.license_frame)

        self.logo_frame = QFrame(self.footer_widget)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_8 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.badenlab_logo = QLabel(self.logo_frame)
        self.badenlab_logo.setObjectName(u"badenlab_logo")
        self.badenlab_logo.setMinimumSize(QSize(0, 0))
        self.badenlab_logo.setMaximumSize(QSize(100, 20))
        self.badenlab_logo.setPixmap(QPixmap(u":/resources/resources/Baden-Logo.png"))
        self.badenlab_logo.setScaledContents(True)
        self.badenlab_logo.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.badenlab_logo)

        self.ON_logo = QLabel(self.logo_frame)
        self.ON_logo.setObjectName(u"ON_logo")
        sizePolicy3.setHeightForWidth(self.ON_logo.sizePolicy().hasHeightForWidth())
        self.ON_logo.setSizePolicy(sizePolicy3)
        self.ON_logo.setMaximumSize(QSize(135, 15))
        self.ON_logo.setPixmap(QPixmap(u":/resources/resources/ON-Logo.png"))
        self.ON_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.ON_logo)

        self.sussex_logo = QLabel(self.logo_frame)
        self.sussex_logo.setObjectName(u"sussex_logo")
        self.sussex_logo.setMaximumSize(QSize(65, 20))
        self.sussex_logo.setPixmap(QPixmap(u":/resources/resources/SN-Logo.png"))
        self.sussex_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.sussex_logo)

        self.trend_logo = QLabel(self.logo_frame)
        self.trend_logo.setObjectName(u"trend_logo")
        sizePolicy3.setHeightForWidth(self.trend_logo.sizePolicy().hasHeightForWidth())
        self.trend_logo.setSizePolicy(sizePolicy3)
        self.trend_logo.setMaximumSize(QSize(30, 20))
        self.trend_logo.setPixmap(QPixmap(u":/resources/resources/TReND-Logo.png"))
        self.trend_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.trend_logo)


        self.horizontalLayout_3.addWidget(self.logo_frame, 0, Qt.AlignRight)

        self.sizegrip = QFrame(self.footer_widget)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setMinimumSize(QSize(20, 20))
        self.sizegrip.setMaximumSize(QSize(20, 20))
        self.sizegrip.setFrameShape(QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sizegrip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.sizegrip)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/resources/resources/SizeGrip.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.sizegrip)


        self.horizontalLayout.addWidget(self.footer_widget)


        self.verticalLayout_75.addWidget(self.BottomMainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuSubContainer_menu_stackedwidget.setCurrentIndex(4)
        self.mainbody_stackedWidget.setCurrentIndex(9)
        self.Spikeling_parameter_stackedwidget.setCurrentIndex(0)
        self.DataAnalysis_Display_StackedWidget.setCurrentIndex(6)
        self.Imaging_parameter_stackedWidget.setCurrentIndex(1)
        self.StimulusGenerator_Parameter_stackedWidget.setCurrentIndex(1)
        self.Exercises_stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appTitle_pushButton.setText(QCoreApplication.translate("MainWindow", u"Spikeling v2.2", None))
        self.reduce_pushButton.setText("")
        self.expand_pushButton.setText("")
        self.exit_pushButton.setText("")
        self.menu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Menus", None))
        self.SpikelingMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Spikeling", None))
        self.ImagingMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging", None))
        self.NeuronGeneratorMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Generator", None))
        self.StimuluGeneratorMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimulus Generator", None))
        self.ExercisesMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Exercises", None))
        self.SettingsMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.AboutMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.HelpMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.GitHubMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.centerMenuSubContainer_exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Sub-Menus   ", None))
        self.Spikeling_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron Interface", None))
        self.Neuron_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Interface", None))
        self.NeuronTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.NeuronDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.Imaging_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Spikeling Imaging Stimulation", None))
        self.ImagingStimulation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging Stimulation", None))
        self.ImagingTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.ImagingDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Stimulus Generator", None))
        self.Exercices_SubMenu_label.setText(QCoreApplication.translate("MainWindow", u"Suggested Exercices", None))
        self.Exercice101_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.1 Introduction to Spikeling", None))
        self.Exercice102_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.2 Spikes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Color theme", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Information about the project, sussex, TReND etc", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.mainbody_header_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#eee8d5;\">Spikeling</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">A hardware implementation of a spiking neuron for neursocience teaching and outreach</span></p><p align=\"right\"><span style=\" font-size:8pt; font-weight:700;\">Conceived and developed by M.J.Y. Zimmermann, A.M. Chagas, T. Baden</span><span style=\" font-size:8pt;\"/></p></body></html>", None))
        self.mainbody_content_text.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Spikeling</span><span style=\" font-size:12pt;\"> is an educational tool for neuroscience students and enthusiasts!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">It is an artificial neuron that can receive different inputs, integrate them and outputs its computation, just like a spiking neuron would!</span></p>\n"
"<p align=\"ju"
                        "stify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Technically, it consists on a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#268bd2;\">This project is licensed under the </span><span style=\" font-size:10pt; font-weight:700; color:#268bd2;\">GNU General Public License v3.0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color"
                        ":#268bd2;\">The hardware is licensed under the </span><span style=\" font-size:10pt; font-weight:700; color:#268bd2;\">CERN OHL v1.2</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700; color:#268bd2;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#268bd2;\">https://github.com/OpenSourceNeuro/Spikeling-V2</span></p></body></html>", None))
        self.mainbody_content_SpikelingGif.setText("")
        self.mainbody_footer_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Understanding how neurons encode and compute information is fundamental to our study of the brain, but opportunities for hands-on experience with neurophysiological techniques on live neurons are scarce in science education.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">Originally developped in the Baden Lab at the University of Sussex, Spikeling is an </span><span style=\" font-size:8pt; font-style:italic;\">in-silico</span><span style=\" font-size:8pt;\"> neuron that mimics a wide range of neuronal behaviours for classroom education and public neuroscience outreach. The current version is the result of a collective work from on-field teaching experience, both in the UK and on the African continent and from users and students feedback.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">The GUI presented here proposed a full and didactic interaction with the neuronal model. It also contains various exercices wh"
                        "ich can be linked to classical neuroscience teachings from early to advanced degree students. Futhermore it offers the opportunity to teachers to prepare practical on: programming, data analysis scipting, methodology and protocol design. All very important skills for modern neuroscience academics but which is unfortunately widely lacking from neuroscience degrees education.</span></p></body></html>", None))
        self.Spikeling_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.Spikeling_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.Spikeling_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.LED_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED On   ", None))
        self.Sound_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buzzer On   ", None))
        self.Spikeling_NeuronModeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Neuron Mode: </span></p></body></html>", None))
        self.Spikeling_NeuronModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Neuron Mode", None))
        self.Spikeling_NeuronModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tonic Spiking", None))
        self.Spikeling_NeuronModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Phasic Spiking", None))
        self.Spikeling_NeuronModeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Tonic Bursting", None))
        self.Spikeling_NeuronModeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Phasic Bursting", None))
        self.Spikeling_NeuronModeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Mixed Mode", None))
        self.Spikeling_NeuronModeComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Spike Frequency Adaptation", None))
        self.Spikeling_NeuronModeComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 1 Excitable", None))
        self.Spikeling_NeuronModeComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 2 Excitable", None))
        self.Spikeling_NeuronModeComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Spike Latency", None))
        self.Spikeling_NeuronModeComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Subthreshold Oscillations", None))
        self.Spikeling_NeuronModeComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Resonator", None))
        self.Spikeling_NeuronModeComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Integrator", None))

        self.Spikeling_NeuronBrowsePushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.Spikeling_NeuronMode_pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Spikeling_VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.Spikeling_InputCurrentCheckbox.setText(QCoreApplication.translate("MainWindow", u"Input Current", None))
        self.Spikeling_StimulusCheckbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.Spikeling_Syn1VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Vm", None))
        self.Spikeling_Syn1InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Input", None))
        self.Spikeling_Syn2VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Vm", None))
        self.Spikeling_Syn2InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Input", None))
        self.Spikeling_DataRecording_box.setTitle(QCoreApplication.translate("MainWindow", u"Data Recording", None))
        self.Spikeling_DataRecording_ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Live ", None))
        self.Spikeling_DataRecording_ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Loop", None))

        self.Spikeling_DataRecording_NumberOfLoops_abel.setText(QCoreApplication.translate("MainWindow", u"Number of loops :", None))
        self.Spikeling_DataRecording_NumberOfLoops_value.setText("")
        self.Spikeling_DataRecording_SelectRecordFolder_label.setText(QCoreApplication.translate("MainWindow", u"Data Logging: Filename", None))
        self.Spikeling_DataRecording_RecordFolder_value.setText("")
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dir.", None))
        self.Spikeling_SelectedFolderLabel.setText("")
        self.Spikeling_DataRecording_Record_pushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.Spikeling_parameter_exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Hide Parameters", None))
        self.StimulusLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Stimulus</span></p></body></html>", None))
        self.Spikeling_StimFre_Label.setText(QCoreApplication.translate("MainWindow", u"Stimulus Frequency (Hz)", None))
        self.Spikeling_StimFre_readings.setText("")
        self.Spikeling_StimFre_values_min.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Spikeling_StimFre_values_0.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.Spikeling_StimFre_values_max.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Spikeling_StimFre_image.setText("")
        self.Spikeling_StimStr_Label.setText(QCoreApplication.translate("MainWindow", u"Stimulus Strength (%)", None))
        self.Spikeling_StimStr_readings.setText("")
        self.Spikeling_StimStr_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_StimStr_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_StimStr_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_StimStr_image.setText("")
        self.Spikeling_CustomStimulus_Label.setText(QCoreApplication.translate("MainWindow", u"Custom Stimulus", None))
        self.Spikeling_PR_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Photo-Receptor</span></p></body></html>", None))
        self.Spikeling_PR_Label.setText(QCoreApplication.translate("MainWindow", u"Photo-Gain (%)", None))
        self.Spikeling_PR_Photogain_readings.setText("")
        self.Spikeling_PR_PhotoGain_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_PR_PhotoGain_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_PR_PhotoGain_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_PRDecay_Label.setText(QCoreApplication.translate("MainWindow", u"Photo Decay: \u03bb (ms\u05bf \u00b9)", None))
        self.Spikeling_PR_Decay_readings.setText("")
        self.Spikeling_PR_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Spikeling_PR_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.SpikelingPRRecovery_Label.setText(QCoreApplication.translate("MainWindow", u"Photo Recovery: \u03bb (ms\u05bf \u00b9)", None))
        self.Spikeling_PR_Recovery_readings.setText("")
        self.Spikeling_PR_Recovery_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Spikeling_PR_Recovery_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Spikeling_PatchClamp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Patch Clamp</span></p></body></html>", None))
        self.Spikeling_PatchClamp_Label.setText(QCoreApplication.translate("MainWindow", u"Injected Current (a.u.)", None))
        self.Spikeling_PatchClamp_reading.setText("")
        self.Spikeling_PatchClamp_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_PatchClamp_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_PatchClamp_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Noise_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Noise</span></p></body></html>", None))
        self.Spikeling_Noise_Label.setText(QCoreApplication.translate("MainWindow", u"Noise Level (%)", None))
        self.Spikeling_Noise_readings.setText("")
        self.Spikeling_Noise_0_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Noise_max_value.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.Spikeling_Synapse1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 1</span></p></body></html>", None))
        self.Spikeling_Synapse1_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Spikeling_Synapse1_readings.setText("")
        self.Spikeling_Synapse1_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_Synapse1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Synapse1_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Synapse1_Decay_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Decay: \u03bb (ms\u05bf \u00b9) ", None))
        self.Spikeling_Synapse1_Decay_readings.setText("")
        self.Spikeling_Synapse1_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Spikeling_Synapse1_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Spikeling_Synapse2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 2</span></p></body></html>", None))
        self.Spikeling_Synapse2_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Spikeling_Synapse2_readings.setText("")
        self.Spikeling_Synapse2_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_Synapse2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Synapse2_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Synapse2_Decay_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Decay: \u03bb (ms\u05bf \u00b9) ", None))
        self.Spikeling_Synapse2_Decay_readings.setText("")
        self.Spikeling_Synapse2_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Spikeling_Synapse2_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Spikeling_rightMenuSubContainer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Parameters", None))
        self.Spikeling_StimulusParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimulus Parameters", None))
        self.Spikeling_NeuronParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Parameters", None))
        self.label_2.setText("")
        self.DataAnalysis_Neuron0Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton10.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton11.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton12.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton20.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton21.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton22.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton30.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton31.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_Neuron0Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton32.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
        self.DataAnalysis_LoadData_label.setText("")
        self.DataAnalysis_LoadData_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Load Data   ", None))
        self.DataAnalysis_LoadData_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Raw Data", None))
        self.DataAnalysis_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Spike_label.setText(QCoreApplication.translate("MainWindow", u"Find Spikes along the Vm trace(s)", None))
        self.DataAnalysis_Spike_threshold_label.setText(QCoreApplication.translate("MainWindow", u"Spike Threshold: ", None))
        self.DataAnalysis_Spike_lineEdit.setText(QCoreApplication.translate("MainWindow", u"-20", None))
        self.DataAnalysis_Spike_mV_label.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.DataAnalysis_Spike_result_label.setText("")
        self.DataAnalysis_Spike_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Spike events", None))
        self.DataAnalysis_Spike_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Spike_Export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.DataAnalysis_Average_result_label.setText(QCoreApplication.translate("MainWindow", u"Average traces based on stimulus cycles", None))
        self.DataAnalysis_Average_label.setText("")
        self.DataAnalysis_Average_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Average traces", None))
        self.DataAnalysis_Average_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.DataAnalysis_Average_Save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export .csv", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GECI", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"GCaMP2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GCaMP6", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"jRGECO", None))

        self.Imaging_InputCurrentCheckbox.setText(QCoreApplication.translate("MainWindow", u"Input Current", None))
        self.Imaging_VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.Imaging_StimulusCheckbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.Imaging_Syn1VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Vm", None))
        self.Imaging_Syn1InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 1 Input", None))
        self.Imaging_Syn2VmCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Vm", None))
        self.Imaging_Syn2InputCheckbox.setText(QCoreApplication.translate("MainWindow", u"Synapse 2 Input", None))
        self.Imaging_parameter_exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Hide Parameters", None))
        self.Imaging_Stimulus_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Stimulus</span></p></body></html>", None))
        self.Imaging_StimFre_checkBox.setText(QCoreApplication.translate("MainWindow", u"Stimulus Frequency (Hz)", None))
        self.Imaging_StimFre_readings.setText("")
        self.Imaging_StimFre_values_min.setText(QCoreApplication.translate("MainWindow", u"2.5", None))
        self.Imaging_StimFre_values.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Imaging_StimFre_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_StimFre_image.setText("")
        self.Imaging_StimStr_checkBox.setText(QCoreApplication.translate("MainWindow", u"Stimulus Strenght (%)", None))
        self.Imaging_StimStr_readings.setText("")
        self.Imaging_StimStr_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Imaging_StimStr_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_StimStr_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_StimStr_image.setText("")
        self.Imaging_PR_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Photo-Receptor</span></p></body></html>", None))
        self.Imaging_PR_PhotoGain_checkBox.setText(QCoreApplication.translate("MainWindow", u"Photo-Gain (%)", None))
        self.Imaging_PR_Photogain_readings.setText("")
        self.Imaging_PR_PhotoGain_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Imaging_PR_PhotoGain_values.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_PR_PhotoGain_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_PR_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay: \u03bb (ms\u05bf \u00b9)", None))
        self.Imaging_PR_Decay_readings.setText("")
        self.Imaging_PR_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Imaging_PR_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Imaging_PR_Recovery_checkBox.setText(QCoreApplication.translate("MainWindow", u"Recovery: \u03bb (ms\u05bf \u00b9)", None))
        self.Imaging_PR_Recovery_readings.setText("")
        self.Imaging_PR_Recovery_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Imaging_PR_Recovery_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Imaging_PatchClamp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Patch Clamp</span></p></body></html>", None))
        self.Imaging_PatchClamp_checkBox.setText(QCoreApplication.translate("MainWindow", u"Injected Current (a.u.)", None))
        self.Imaging_PatchClamp_reading.setText("")
        self.Imaging_PatchClamp_values_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Imaging_PatchClamp_values_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_PatchClamp_values_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_Noise_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Noise</span></p></body></html>", None))
        self.Imaging_Noise_checkBox.setText(QCoreApplication.translate("MainWindow", u"Noise Level", None))
        self.Imaging_Noise_readings.setText("")
        self.Imaging_Noise_0_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_Noise_max_value.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.Imaging_Synapse1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 1</span></p></body></html>", None))
        self.Imaging_Synapse1_checkBox.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Imaging_Synapse1_readings.setText("")
        self.Imaging_Synapse1_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Imaging_Synapse1_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_Synapse1_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_Synapse1_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay: \u03bb (ms\u05bf \u00b9)", None))
        self.Imaging_Synapse1_Decay_readings.setText("")
        self.Imaging_Synapse1_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Imaging_Synapse1_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Imaging_Synapse2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 2</span></p></body></html>", None))
        self.Imaging_Synapse2_checkBox.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Imaging_Synapse2_readings.setText("")
        self.Imaging_Synapse2_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Imaging_Synapse2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Imaging_Synapse2_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Imaging_Synapse2_Decay_checkBox.setText(QCoreApplication.translate("MainWindow", u"Decay: \u03bb (ms\u05bf \u00b9)", None))
        self.Imaging_Synapse2_Decay_readings.setText("")
        self.Imaging_Synapse2_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Imaging_Synapse2_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Imaging_rightMenuSubContainer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Parameters", None))
        self.Imaging_StimulusParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimulus Parameters", None))
        self.Imaging_NeuronParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Parameters", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.NeuronGenerator_subframe1_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Spikeling is built on the Izhikevich model</span></p></body></html>", None))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Bifurcation methodologies enable us to reduce many biophysically accurate Hodgkin\u2013Huxley-type neuronal models to a two-dimensional (2-D) system of ordinary differential equations of the form:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:696;\">v' = 0.04v</span><span style=\" font-size:11pt; font-weight:696; vertical-align:super;\">"
                        "2</span><span style=\" font-size:11pt; font-weight:696;\"> + 5v + 140 - u + I                    </span><span style=\" font-size:11pt;\">&amp;</span><span style=\" font-size:11pt; font-weight:696;\">                    u' = a(bv - u)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">with the auxiliary after-spike resetting:   if </span><span style=\" font-size:11pt; font-weight:696;\">v &gt;= 30 mV</span><span style=\" font-size:10pt;\">, then </span><span style=\" font-size:11pt; font-weight:696;\">v = c</span><span style=\" font-size:10pt;\"> and</span><span style=\" font-size:11pt;\"> </span><span style=\" font-size:11pt; font-weight:696;\">u = u + d</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:696;\"><br /></p>"
                        "\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here, </span><span style=\" font-size:11pt; font-weight:696;\">v</span><span style=\" font-size:10pt;\"> and </span><span style=\" font-size:11pt; font-weight:696;\">u</span><span style=\" font-size:10pt;\"> are dimensionless variables, and </span><span style=\" font-size:11pt; font-weight:696;\">a</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:696;\">b</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:696;\">c</span><span style=\" font-size:10pt;\">, and </span><span style=\" font-size:11pt; font-weight:696;\">d</span><span style=\" font-size:10pt;\"> are dimensionless parameters, and </span><span style=\" font-size:11pt; font-weight:696;\">'= d/dt</span><span style=\" font-size:10pt;\">, where </span><span style=\" font-size:11pt; font-weight:696;\""
                        ">t</span><span style=\" font-size:10pt;\"> is the time. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The variable v represents the membrane potential of the neuron and </span><span style=\" font-size:11pt; font-weight:696;\">u</span><span style=\" font-size:10pt;\"> represents a membrane recovery variable, which accounts for the activation of K+ ionic currents and inactivation of Na+ ionic currents, and it provides negative feedback to </span><span style=\" font-size:11pt; font-weight:696;\">v</span><span style=\" font-size:10pt;\">. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">After the spike reaches its apex (+30 mV), the membrane voltage and the recovery variable are reset. </span></p>\n"
"<p align=\"justify\" style=\" mar"
                        "gin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Synaptic currents or injected DC-currents are delivered via the variable</span><span style=\" font-size:10pt; font-weight:696;\"> </span><span style=\" font-size:11pt; font-weight:696;\">I</span><span style=\" font-size:10pt;\">.</span></p></body></html>", None))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_Vm_checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.NeuronGenerator_subframe1_Oscilloscope_widget_stimulus_checkbox.setText(QCoreApplication.translate("MainWindow", u"Current Input", None))
        self.StimInt_label.setText(QCoreApplication.translate("MainWindow", u"Stimulus intensity (a.u.): ", None))
        self.StimInt_value.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.NeuronGenerator_subframe1_bottom_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>As most real neurons, the model does not have a fixed threshold: Depending on the history of the membrane potential prior to the spike, the threshold potential can be as low as -55 mV or as high as -40mV</p></body></html>", None))
        self.NeuronGenerator_subframe1_Izhik_image.setText("")
        self.a_value.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.a_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter </span><span style=\" font-size:12pt; font-weight:600;\">a</span><span style=\" font-size:9pt;\"> describes the time scale of the recovery variable </span><span style=\" font-size:9pt; font-weight:600;\">u</span><span style=\" font-size:9pt;\">. Smaller values result in slower recovery. </span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">a</span><span style=\" font-size:9pt; text-decoration: underline;\"> = 0.02.</span></p></body></html>", None))
        self.b_value.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.b_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The parameter <span style=\" font-size:12pt; font-weight:600;\">b</span> describes the sensitivity of the recovery variable <span style=\" font-weight:600;\">u </span>to the subthreshold fluctuations of the membrane potential v. Greater values couple<span style=\" font-weight:600;\"> v</span> and<span style=\" font-weight:600;\"> u</span> more strongly resulting in possible sub-threshold oscillations and low-threshold spiking dynamics. </p><p><span style=\" text-decoration: underline;\">A typical value is </span><span style=\" font-weight:600; text-decoration: underline;\">b </span><span style=\" text-decoration: underline;\">= 0.2</span>. </p><p>The case <span style=\" font-weight:600;\">b</span> &lt; <span style=\" font-weight:600;\">a</span>(<span style=\" font-weight:600;\">b</span> &gt; <span style=\" font-weight:600;\">a</span>) corresponds to saddle-node (Andronov\u2013Hopf) bifurcation of the resting state.</p></body></html>", None))
        self.c_value.setText(QCoreApplication.translate("MainWindow", u"-65", None))
        self.c_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter</span><span style=\" font-size:12pt; font-weight:600;\"> c</span><span style=\" font-size:9pt;\"> describes the after-spike reset value of the membrane potential v caused by the fast high-threshold K+ conductances. </span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">c</span><span style=\" font-size:9pt; text-decoration: underline;\"> = -65 (mV)</span><span style=\" font-size:9pt;\">.</span></p></body></html>", None))
        self.d_value.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.d_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">The parameter </span><span style=\" font-size:12pt; font-weight:600;\">d</span><span style=\" font-size:9pt;\"> describes after-spike reset of the recovery variable </span><span style=\" font-size:9pt; font-weight:600;\">u</span><span style=\" font-size:9pt;\"> caused by slow high-threshold Na+ and K+ conductances.</span></p><p><span style=\" font-size:9pt; text-decoration: underline;\">A typical value is </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">d</span><span style=\" font-size:9pt; text-decoration: underline;\"> = 2</span><span style=\" font-size:9pt;\">.</span></p></body></html>", None))
        self.DisplayNeuronPushButton.setText(QCoreApplication.translate("MainWindow", u"Display Neuron", None))
        self.SaveNeuronPushButton.setText(QCoreApplication.translate("MainWindow", u"Save Neuron", None))
        self.LoadNeuron_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Load Neuron", None))
        self.LoadNeuron_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tonic Spiking", None))
        self.LoadNeuron_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Phasic Spiking", None))
        self.LoadNeuron_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Tonic Bursting", None))
        self.LoadNeuron_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Phasic Bursting", None))
        self.LoadNeuron_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Mixed Mode", None))
        self.LoadNeuron_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Spike Frequency Adaptation", None))
        self.LoadNeuron_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Class1 Excitable", None))
        self.LoadNeuron_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Class2 Excitable", None))
        self.LoadNeuron_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Spike Latency", None))
        self.LoadNeuron_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Sub-threshold Oscillations", None))
        self.LoadNeuron_comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Resonator", None))
        self.LoadNeuron_comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Integrator", None))

        self.StimulusGenerator_Selection_Label.setText(QCoreApplication.translate("MainWindow", u"Select stimulus type", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Intensity steps", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sine wave", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Linear sine wave", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Chirp", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Binary noise", None))

        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.SineWave_Amplitude_Label.setText(QCoreApplication.translate("MainWindow", u"Amplitude (a.u.)", None))
        self.SineWave_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.SineWave_Frequency_Label.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.SineWave_Frequency_Value.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.SineWave_Mean_Label.setText(QCoreApplication.translate("MainWindow", u"Mean (a.u.)", None))
        self.SineWave_Mean_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SineWave_StimOn_Label.setText(QCoreApplication.translate("MainWindow", u"Stimulus Time (ms)", None))
        self.SineWave_StimOn_Value.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.SineWave_IntOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus Intensity (a.u.)", None))
        self.SineWave_IntOff_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SineWave_StimOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus Time (ms)", None))
        self.SineWave_StimOff_Value.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.StimulusGenerator_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Stimulus", None))
        self.StimulusGenerator_Save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Stimulus", None))
        self.Vm_IntroTitle.setText(QCoreApplication.translate("MainWindow", u"Resting membrane potential", None))
        self.Vm_IntroText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">In the absence of a stimulus, the Spikeling neuron rests at -70 mV and should only spike sporadically.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">The resting membrane voltage (Vm) can be adjust indirectly by the virtual stimulating electrode located at the bottom left of the unit. The dial sitting on the electrode drawing sets a constant input current increasing or decreasing the polarised state of the neuron. </span></p><p align=\"justify\"><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">In this session we are only  interested in the membrane potential trace (the red one on the oscilloscope) and the input current trace (the green one). </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">The red LED on the unit also tracks the Vm, and flashes with each spike which should also be accompanied by an audible \u201cclick\u201d. As human auditory frequency discrimination ( is higher than the visu"
                        "al flicker fusion frequency (50-90Hz), electrophysiologists often connect a speaker to their recording of membrane voltage to get a direct audio feedback of what the neuron might respond to.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.Vm_Task01_Title.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Vm_Task01_Title.setText(QCoreApplication.translate("MainWindow", u"What happens when you increase or decrease the static input current?", None))
        self.Vm_Task01_Text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">You should observe that increasing the static input current drives Vm towards and beyond spike threshold. </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">As you keep driving Vm upwards, you will elicit progressively higher spike rates. This is the simplest of all </span><span style=\" font-size:12pt; font-weight:700;\">neuronal codes</span><span style=\" font-size:12pt;\">: The intensity of a stimulus (here, simply the increased input current) is </span><span style=\" font-size:12pt; font-weight:700;\">encoded</span><span style=\" font-size:12pt;\"> in the frequency of spikes. Imagine you are the postsynaptic neuron and all you see is this spike pattern; you could easily infer from seeing more spikes in close succession that the input to the presynaptic neuron has probably increased. Most spiking neurons use this </span><span style=\" font-size:12pt; font-weight:700;\">rate code </span><span style=\" font-size:12pt;\">to "
                        "signal input intensity.</span><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">On the screen, note that each spike is preceded by a shallow rise in Vm and followed by a brief dip below starting levels. This dip is the refractory period of the neuron. During this time, generating another spike is particularly difficult.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">At the extreme low point of Vm it is impossible to generate a spike, which in a biological neurons is because the sodium channels are blocked (not just closed). This absolute refractory time, together with the duration of the spike itself (1-2 ms) sets a limit on the maximum spike rate possible. In an average neuron, the </span><span style=\" font-size:12pt; font-weight:700;\">absolute refractory period</span><span style=\" font-size:12pt;\"> is a few milliseconds, and thus the maximal spike rate of most neurons is ~100-200 Hz. </span><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">Some specialised neuro"
                        "ns can go a bit higher, but kHz range is out of question. This means that, by using a single spiking neuron, it is impossible to faithfully encode a time-varying stimulus above this frequency. However, there are a few tricks around this problem that the nervous system can use. We will pick up on this point later.</span></p></body></html>", None))
        self.Vm_Task02_Text.setText(QCoreApplication.translate("MainWindow", u"What happens when you dial current up and then wait a few seconds? ", None))
        self.Vm_Task02_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">If you drive up input current and leave it there for a few seconds, you should observe that spike rate first increases, but then will taper off to some new basal rate of activity which will be higher than the original rate (rate code), but lower than the peak rate. </span></p><p align=\"justify\"><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">This is an example of </span><span style=\" font-size:12pt; font-weight:700;\">adaptation</span><span style=\" font-size:12pt;\">. Neurons respond to a change in the input not only by firing more or fewer spikes, but in addition by adjusting their sensitivity to further changes based on recent stimulus history. </span></p><p align=\"justify\"><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">This is a fundamental property of neurons that allows them to extend their operating range, and to stay responsive to further changes in subsequent inputs. </span></p></body></html>", None))
        self.Vm_Task03_Title.setText(QCoreApplication.translate("MainWindow", u"Does a rapid and a slow current increase generate the same voltage response?", None))
        self.Vm_Task03_Text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">As you increase input current slowly or rapidly, you should observe that you can reach different peak spike rates. </span></p><p><br/></p><p><span style=\" font-size:12pt;\">A rapid increase in input current is a much more effective way to trigger multiple spikes in close succession. This is again because of </span><span style=\" font-size:12pt; font-weight:700;\">adaptation</span><span style=\" font-size:12pt;\">. </span><br/></p><p><span style=\" font-size:12pt;\">If you change input current fast enough, the neuron does not have time to adapt and therefore fires vigorously at first.</span></p><p><span style=\" font-size:12pt;\">If you change input current slowly enough, you should be able to drive it quite high without eliciting many extra spikes as it adapts while you slowly ramp up the current. This means that not only the absolute level of a stimulus can be encoded by a neuron, by also the rate of change. </span></p><p><br/><span style=\" font-size:12"
                        "pt;\">Note that this creates ambiguity in the code, which is one important reason for the need of </span><span style=\" font-size:12pt; font-weight:700;\">parallelisation</span><span style=\" font-size:12pt;\">. This means that if you want to read both absolute levels of a stimulus and its rate of change, you may need two neurons with different properties. </span></p><p><br/></p><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic;\">NB: The fact that the speed of change in the input is encoded in a neuron\u2019s firing also means that that spike thresholds are not fixed. Depending how quickly you stimulate a neuron, it can start firing at different Vm values!</span></p></body></html>", None))
        self.Exercises_PreviousButton_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.Exercises_AfterButton_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.license_label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.badenlab_logo.setText("")
        self.ON_logo.setText("")
        self.sussex_logo.setText("")
        self.trend_logo.setText("")
        self.label.setText("")
    # retranslateUi

