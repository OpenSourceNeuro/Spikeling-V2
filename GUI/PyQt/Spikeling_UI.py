# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Spikeling_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTextBrowser, QToolBox,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 759)
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
"centerMenuSubContainer_menu_stackedwidget{\n"
"}\n"
"#centerMenuSubContainer_menu_stackedwidget QPushButton{\n"
"	text-align: center;\n"
"	padding: 10"
                        "px 0px;\n"
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
"#Connection_frame QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
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
"#StimulusParameter_page QComboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(0, 30, 38);\n"
"	padding: 2px;\n"
"}\n"
"#Spikeling_CustomStimulus_Selection_frame QPushButton{\n"
"	padding: 4px 0px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"#Spikeling_DataRecord"
                        "ing_box{\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#Spikeling_DataRecording_box QLineEdit{\n"
"	border: 2px solid rgb(147,161,161);\n"
"    background-color: rgb(7, 54, 66);\n"
"}\n"
"#Spikeling_DataRecording_box QComboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"#Spikeling_bottom_subframe QPushButton{\n"
"	padding: 5px 5px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
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
""
                        "	background-color: rgb(7, 54, 66)\n"
"}\n"
"#Spikeling_parameter_exit_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#Imaging_rightMenuSubContainer{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Imaging_parameter_stackedWidget{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Imaging_rightMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
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
"#Imaging_pushButton_frame QPushButton{\n"
""
                        "	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
"}\n"
"#Imaging_GECI_comboBox_frame QComboBox{\n"
"	background-color: rgb(7, 54, 66);\n"
"	padding: 2px 2px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#MultipleImaging_rightMenuSubContainer{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#MultipleImaging_parameter_stackedWidget{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#MultipleImaging_rightMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 20px 0px;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#MultipleImaging_rightMenuSubContainer QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#MultipleImaging_rightMenuSubContainer_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#MultipleImaging_rightMenuSubContainer_frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#MultipleImaging_Cente"
                        "rMenuContainer{\n"
"	background-color: rgb(7, 54, 66)\n"
"}\n"
"#MultipleImaging_parameter_exit_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#MultipleImaging_pushButton_frame QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
"}\n"
"#MultipleImaging_GECI_comboBox_frame QComboBox{\n"
"	background-color: rgb(7, 54, 66);\n"
"	padding: 2px 2px;\n"
"}\n"
"\n"
"\n"
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
"	border-radius: 10px;\n"
"	padding: 5px 5px;\n"
"}\n"
"#NeuronGenerator_subframe2 QComboBox{\n"
"	background-color: rgb(7, 54, 66);\n"
"	border: 2p"
                        "x solid rgb(147,161,161);\n"
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
"\n"
"#DataAnalysis_stackedWidget{\n"
"	background-color: rgb(7,54,66);\n"
"    border: 2px solid rgb(147,161,161);\n"
"}\n"
"#DataAnalysis_stackedWidget QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"#DataAnalysis_stackedWidget QLineEdit{\n"
"    border: 2px solid rgb(147,161,161);\n"
"}\n"
"#DataAnalysis_stackedWidget Line{\n"
"    border: 1px solid rgb(147,161,161);\n"
"}\n"
"\n"
"#DataAnalysis_Display_frame QPushButton{\n"
"	background-color: rgb(7,54,66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#DataAnalysis_RightMenu_Container{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Data"
                        "Analysis_RightMenu_Container QPushButton{\n"
"	text-align: left;\n"
"	padding: 20px 0px;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#DataAnalysis_RightMenu_Container QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#DataAnalysis_RightMenu_Frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#DataAnalysis_RightMenu_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#Imaging_DataRecording_box{\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#Imaging_DataRecording_box QLineEdit{\n"
"	border: 2px solid rgb(147,161,161);\n"
"    background-color: rgb(7, 54, 66);\n"
"}\n"
"#Imaging_DataRecording_box QComboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"#Imaging_DataRecording_box QPushButton{\n"
"	padding: 5px 5px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"\n"
"\n"
"\n"
"#MultipleIm"
                        "aging_DataRecording_box{\n"
"	border: 2px solid rgb(147,161,161);\n"
"}\n"
"#MultipleImaging_DataRecording_box QLineEdit{\n"
"	border: 2px solid rgb(147,161,161);\n"
"    background-color: rgb(7, 54, 66);\n"
"}\n"
"#MultipleImaging_DataRecording_box QComboBox{\n"
"	border: 2px solid rgb(147,161,161);\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"#MultipleImaging_DataRecording_box QPushButton{\n"
"	padding: 5px 5px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(7, 54, 66);\n"
"}\n"
"\n"
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
"}\n"
"\n"
"\n"
"\n"
"\n"
"#Exercise101"
                        "_Button_frame QPushButton{\n"
"	background-color: rgb(7,54,66);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
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
        icon.addFile(u":/resources/resources/Spiky_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u":/resources/resources/Artboard 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reduce_pushButton.setIcon(icon1)
        self.reduce_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.reduce_pushButton)

        self.expand_pushButton = QPushButton(self.app_frame)
        self.expand_pushButton.setObjectName(u"expand_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expand_pushButton.setIcon(icon2)
        self.expand_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.expand_pushButton)

        self.exit_pushButton = QPushButton(self.app_frame)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/Exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
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
        icon4.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_pushButton.setIcon(icon4)
        self.menu_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_64.addWidget(self.menu_pushButton)


        self.verticalLayout_4.addWidget(self.menu_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        icon5.addFile(u":/resources/resources/Neuron.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SpikelingMenu_pushButton.setIcon(icon5)
        self.SpikelingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.SpikelingMenu_pushButton)

        self.ImagingMenu_pushButton = QPushButton(self.menus_frame)
        self.ImagingMenu_pushButton.setObjectName(u"ImagingMenu_pushButton")
        self.ImagingMenu_pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/Imaging.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ImagingMenu_pushButton.setIcon(icon6)
        self.ImagingMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.ImagingMenu_pushButton)

        self.NeuronGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.NeuronGeneratorMenu_pushButton.setObjectName(u"NeuronGeneratorMenu_pushButton")
        self.NeuronGeneratorMenu_pushButton.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/StimGen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NeuronGeneratorMenu_pushButton.setIcon(icon7)
        self.NeuronGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.NeuronGeneratorMenu_pushButton)

        self.StimuluGeneratorMenu_pushButton = QPushButton(self.menus_frame)
        self.StimuluGeneratorMenu_pushButton.setObjectName(u"StimuluGeneratorMenu_pushButton")
        self.StimuluGeneratorMenu_pushButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/Stimulus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StimuluGeneratorMenu_pushButton.setIcon(icon8)
        self.StimuluGeneratorMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_37.addWidget(self.StimuluGeneratorMenu_pushButton)

        self.ExercisesMenu_pushButton = QPushButton(self.menus_frame)
        self.ExercisesMenu_pushButton.setObjectName(u"ExercisesMenu_pushButton")
        self.ExercisesMenu_pushButton.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/resources/resources/Exercices.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.SettingsMenu_pushButton = QPushButton(self.options_frame)
        self.SettingsMenu_pushButton.setObjectName(u"SettingsMenu_pushButton")
        self.SettingsMenu_pushButton.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/resources/resources/Tutorial.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsMenu_pushButton.setIcon(icon10)
        self.SettingsMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.SettingsMenu_pushButton)

        self.AboutMenu_pushButton = QPushButton(self.options_frame)
        self.AboutMenu_pushButton.setObjectName(u"AboutMenu_pushButton")
        self.AboutMenu_pushButton.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/resources/resources/About.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AboutMenu_pushButton.setIcon(icon11)
        self.AboutMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AboutMenu_pushButton)

        self.HelpMenu_pushButton = QPushButton(self.options_frame)
        self.HelpMenu_pushButton.setObjectName(u"HelpMenu_pushButton")
        self.HelpMenu_pushButton.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HelpMenu_pushButton.setIcon(icon12)
        self.HelpMenu_pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.HelpMenu_pushButton)

        self.GitHubMenu_pushButton = QPushButton(self.options_frame)
        self.GitHubMenu_pushButton.setObjectName(u"GitHubMenu_pushButton")
        self.GitHubMenu_pushButton.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon14.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.Spikeling_SubMenu_button_frame = QFrame(self.Spikeling_SubMenu_page)
        self.Spikeling_SubMenu_button_frame.setObjectName(u"Spikeling_SubMenu_button_frame")
        self.Spikeling_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Spikeling_SubMenu_button_frame)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_5)

        self.Neuron_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.Neuron_pushButton.setObjectName(u"Neuron_pushButton")
        self.Neuron_pushButton.setFont(font1)
        self.Neuron_pushButton.setIcon(icon5)
        self.Neuron_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.Neuron_pushButton)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)

        self.NeuronSimulation_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronSimulation_pushButton.setObjectName(u"NeuronSimulation_pushButton")
        self.NeuronSimulation_pushButton.setFont(font1)
        self.NeuronSimulation_pushButton.setIcon(icon5)
        self.NeuronSimulation_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronSimulation_pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.NeuronDataAnalysis_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronDataAnalysis_pushButton.setObjectName(u"NeuronDataAnalysis_pushButton")
        self.NeuronDataAnalysis_pushButton.setFont(font1)
        icon15 = QIcon()
        icon15.addFile(u":/resources/resources/DataAnalysis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NeuronDataAnalysis_pushButton.setIcon(icon15)
        self.NeuronDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronDataAnalysis_pushButton)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.NeuronTutorial_pushButton = QPushButton(self.Spikeling_SubMenu_button_frame)
        self.NeuronTutorial_pushButton.setObjectName(u"NeuronTutorial_pushButton")
        self.NeuronTutorial_pushButton.setFont(font1)
        self.NeuronTutorial_pushButton.setIcon(icon10)
        self.NeuronTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_19.addWidget(self.NeuronTutorial_pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addWidget(self.Spikeling_SubMenu_button_frame)

        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.Spikeling_SubMenu_page)
        self.Imaging_SubMenu_page = QWidget()
        self.Imaging_SubMenu_page.setObjectName(u"Imaging_SubMenu_page")
        self.verticalLayout_10 = QVBoxLayout(self.Imaging_SubMenu_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SubMenu_button_frame = QFrame(self.Imaging_SubMenu_page)
        self.Imaging_SubMenu_button_frame.setObjectName(u"Imaging_SubMenu_button_frame")
        self.Imaging_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.Imaging_SubMenu_button_frame)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_9)

        self.ImagingStimulation_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingStimulation_pushButton.setObjectName(u"ImagingStimulation_pushButton")
        self.ImagingStimulation_pushButton.setFont(font1)
        self.ImagingStimulation_pushButton.setIcon(icon6)
        self.ImagingStimulation_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingStimulation_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_3)

        self.MultipleImagingStimulation_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.MultipleImagingStimulation_pushButton.setObjectName(u"MultipleImagingStimulation_pushButton")
        self.MultipleImagingStimulation_pushButton.setFont(font1)
        self.MultipleImagingStimulation_pushButton.setIcon(icon6)
        self.MultipleImagingStimulation_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.MultipleImagingStimulation_pushButton)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_10)

        self.ImagingTutorial_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingTutorial_pushButton.setObjectName(u"ImagingTutorial_pushButton")
        self.ImagingTutorial_pushButton.setFont(font1)
        self.ImagingTutorial_pushButton.setIcon(icon10)
        self.ImagingTutorial_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingTutorial_pushButton)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_11)

        self.ImagingDataAnalysis_pushButton = QPushButton(self.Imaging_SubMenu_button_frame)
        self.ImagingDataAnalysis_pushButton.setObjectName(u"ImagingDataAnalysis_pushButton")
        self.ImagingDataAnalysis_pushButton.setFont(font1)
        self.ImagingDataAnalysis_pushButton.setIcon(icon15)
        self.ImagingDataAnalysis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_59.addWidget(self.ImagingDataAnalysis_pushButton)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.centerMenuSubContainer_menu_stackedwidget.addWidget(self.StimulusGenerator_SubMenu_page)
        self.Exercises_SubMenu_page = QWidget()
        self.Exercises_SubMenu_page.setObjectName(u"Exercises_SubMenu_page")
        self.verticalLayout_16 = QVBoxLayout(self.Exercises_SubMenu_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Exercices_SubMenu_button_frame = QFrame(self.Exercises_SubMenu_page)
        self.Exercices_SubMenu_button_frame.setObjectName(u"Exercices_SubMenu_button_frame")
        self.Exercices_SubMenu_button_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercices_SubMenu_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.Exercices_SubMenu_button_frame)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_13)

        self.toolBox = QToolBox(self.Exercices_SubMenu_button_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 163, 111))
        self.verticalLayout_98 = QVBoxLayout(self.page_3)
        self.verticalLayout_98.setSpacing(5)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.Exercice101_pushButton = QPushButton(self.page_3)
        self.Exercice101_pushButton.setObjectName(u"Exercice101_pushButton")
        font2 = QFont()
        font2.setPointSize(9)
        self.Exercice101_pushButton.setFont(font2)

        self.verticalLayout_98.addWidget(self.Exercice101_pushButton)

        self.Exercice102_pushButton = QPushButton(self.page_3)
        self.Exercice102_pushButton.setObjectName(u"Exercice102_pushButton")
        self.Exercice102_pushButton.setFont(font2)

        self.verticalLayout_98.addWidget(self.Exercice102_pushButton)

        self.pushButton = QPushButton(self.page_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_98.addWidget(self.pushButton)

        self.toolBox.addItem(self.page_3, u"1 - Introduction to Spikeling")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 83, 71))
        self.verticalLayout_99 = QVBoxLayout(self.page_4)
        self.verticalLayout_99.setSpacing(5)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.page_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_99.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.page_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_99.addWidget(self.pushButton_2)

        self.toolBox.addItem(self.page_4, u"2 - Electrophysiology")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 65, 16))
        self.toolBox.addItem(self.page_6, u"3 - Photo-stimulation")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_7, u"4 - Synapses")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_8, u"5 - Neuronal network")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_5, u"6- Fluorescence Imaging")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_9, u"7 - Spike Inference")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_10, u"8 - Methodology")

        self.verticalLayout_61.addWidget(self.toolBox)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.label_15 = QLabel(self.Settings_SubMenu_page)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_38.addWidget(self.label_15)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbodyContainer.sizePolicy().hasHeightForWidth())
        self.mainbodyContainer.setSizePolicy(sizePolicy1)
        self.mainbodyContainer.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.mainbodyContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainbody_stackedWidget = QStackedWidget(self.mainbodyContainer)
        self.mainbody_stackedWidget.setObjectName(u"mainbody_stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainbody_stackedWidget.sizePolicy().hasHeightForWidth())
        self.mainbody_stackedWidget.setSizePolicy(sizePolicy2)
        self.mainbody_stackedWidget.setMinimumSize(QSize(600, 600))
        self.mainbody_stackedWidget.setStyleSheet(u"")
        self.page_000 = QWidget()
        self.page_000.setObjectName(u"page_000")
        self.verticalLayout_30 = QVBoxLayout(self.page_000)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 5, 0)
        self.mainbody_header_frame = QFrame(self.page_000)
        self.mainbody_header_frame.setObjectName(u"mainbody_header_frame")
        self.mainbody_header_frame.setMaximumSize(QSize(16777215, 16777215))
        self.mainbody_header_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.mainbody_header_frame)
        self.horizontalLayout_115.setSpacing(0)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.mainbody_header_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(197, 125))
        self.label_8.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_115.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.mainbody_header_text = QLabel(self.mainbody_header_frame)
        self.mainbody_header_text.setObjectName(u"mainbody_header_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainbody_header_text.sizePolicy().hasHeightForWidth())
        self.mainbody_header_text.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setBold(False)
        self.mainbody_header_text.setFont(font3)
        self.mainbody_header_text.setStyleSheet(u"")

        self.horizontalLayout_115.addWidget(self.mainbody_header_text)


        self.verticalLayout_30.addWidget(self.mainbody_header_frame)

        self.mainbody_content_frame = QFrame(self.page_000)
        self.mainbody_content_frame.setObjectName(u"mainbody_content_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainbody_content_frame.sizePolicy().hasHeightForWidth())
        self.mainbody_content_frame.setSizePolicy(sizePolicy4)
        self.mainbody_content_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.mainbody_content_frame)
        self.horizontalLayout_76.setSpacing(5)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 10)
        self.mainbody_content_text_frame = QFrame(self.mainbody_content_frame)
        self.mainbody_content_text_frame.setObjectName(u"mainbody_content_text_frame")
        self.mainbody_content_text_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_content_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_251 = QHBoxLayout(self.mainbody_content_text_frame)
        self.horizontalLayout_251.setSpacing(0)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.horizontalLayout_251.setContentsMargins(0, 10, 0, 0)
        self.mainbody_content_text = QLabel(self.mainbody_content_text_frame)
        self.mainbody_content_text.setObjectName(u"mainbody_content_text")
        sizePolicy4.setHeightForWidth(self.mainbody_content_text.sizePolicy().hasHeightForWidth())
        self.mainbody_content_text.setSizePolicy(sizePolicy4)
        self.mainbody_content_text.setAlignment(Qt.AlignCenter)
        self.mainbody_content_text.setWordWrap(True)

        self.horizontalLayout_251.addWidget(self.mainbody_content_text)


        self.horizontalLayout_76.addWidget(self.mainbody_content_text_frame)


        self.verticalLayout_30.addWidget(self.mainbody_content_frame)

        self.frame_22 = QFrame(self.page_000)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_22)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_22)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(442, 300))
        self.label_98.setPixmap(QPixmap(u":/resources/resources/SpikelingLayout.png"))
        self.label_98.setScaledContents(True)
        self.label_98.setAlignment(Qt.AlignCenter)
        self.label_98.setWordWrap(True)

        self.verticalLayout_104.addWidget(self.label_98, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.frame_22)

        self.mainbody_footer_frame = QFrame(self.page_000)
        self.mainbody_footer_frame.setObjectName(u"mainbody_footer_frame")
        self.mainbody_footer_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbody_footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_419 = QHBoxLayout(self.mainbody_footer_frame)
        self.horizontalLayout_419.setSpacing(0)
        self.horizontalLayout_419.setObjectName(u"horizontalLayout_419")
        self.horizontalLayout_419.setContentsMargins(5, 10, 5, 10)
        self.frame_21 = QFrame(self.mainbody_footer_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_420 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_420.setSpacing(0)
        self.horizontalLayout_420.setObjectName(u"horizontalLayout_420")
        self.horizontalLayout_420.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.frame_21)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_420.addWidget(self.label_97, 0, Qt.AlignBottom)


        self.horizontalLayout_419.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.mainbody_footer_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_421 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_421.setSpacing(0)
        self.horizontalLayout_421.setObjectName(u"horizontalLayout_421")
        self.horizontalLayout_421.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_421.addWidget(self.label_9)


        self.horizontalLayout_419.addWidget(self.frame_20, 0, Qt.AlignBottom)


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
        sizePolicy3.setHeightForWidth(self.Spikeling_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_widget.setSizePolicy(sizePolicy3)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Spikeling_top_subframe1.sizePolicy().hasHeightForWidth())
        self.Spikeling_top_subframe1.setSizePolicy(sizePolicy5)
        self.Spikeling_top_subframe1.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_top_subframe1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.Spikeling_top_subframe1)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 0, 5, 0)
        self.Spikeling_connection_frame = QFrame(self.Spikeling_top_subframe1)
        self.Spikeling_connection_frame.setObjectName(u"Spikeling_connection_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_connection_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_connection_frame.setSizePolicy(sizePolicy2)
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

        self.Spikeling_ConnectButton = QPushButton(self.Connection_frame)
        self.Spikeling_ConnectButton.setObjectName(u"Spikeling_ConnectButton")
        self.Spikeling_ConnectButton.setEnabled(True)
        self.Spikeling_ConnectButton.setFont(font1)
        self.Spikeling_ConnectButton.setCheckable(True)

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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
        icon16.addFile(u":/resources/resources/LEDON.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon17.addFile(u":/resources/resources/SoundON.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        sizePolicy4.setHeightForWidth(self.Spikeling_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.Spikeling_Oscilloscope_widget.setSizePolicy(sizePolicy4)
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
        sizePolicy5.setHeightForWidth(self.Spikeling_DataRecording_box.sizePolicy().hasHeightForWidth())
        self.Spikeling_DataRecording_box.setSizePolicy(sizePolicy5)
        self.Spikeling_DataRecording_box.setMinimumSize(QSize(0, 100))
        self.Spikeling_DataRecording_box.setMaximumSize(QSize(16777215, 100))
        self.Spikeling_DataRecording_box.setStyleSheet(u"")
        self.horizontalLayout_52 = QHBoxLayout(self.Spikeling_DataRecording_box)
        self.horizontalLayout_52.setSpacing(0)
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

        self.verticalLayout_27.addWidget(self.Spikeling_DataRecording_recordingMode_frame)


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
        self.horizontalLayout_56.setSpacing(10)
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
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
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
        sizePolicy3.setHeightForWidth(self.Spikeling_SelectedFolderLabel.sizePolicy().hasHeightForWidth())
        self.Spikeling_SelectedFolderLabel.setSizePolicy(sizePolicy3)
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
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

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
        icon18.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        sizePolicy1.setHeightForWidth(self.Spikeling_StimFre_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_frame.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.Spikeling_StimFre_toggle_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimFre_toggle_frame.setSizePolicy(sizePolicy2)
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
        self.Spikeling_parameter_top_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_parameter_top_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_top_line)

        self.Spikeling_StimStr_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_StimStr_frame.setObjectName(u"Spikeling_StimStr_frame")
        sizePolicy1.setHeightForWidth(self.Spikeling_StimStr_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_frame.setSizePolicy(sizePolicy1)
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
        sizePolicy5.setHeightForWidth(self.Spikeling_StimStr_image.sizePolicy().hasHeightForWidth())
        self.Spikeling_StimStr_image.setSizePolicy(sizePolicy5)
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
        self.Spikeling_parameter_middle_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_parameter_middle_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_middle_line)

        self.Spikeling_CustomStimulus_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_CustomStimulus_frame.setObjectName(u"Spikeling_CustomStimulus_frame")
        sizePolicy1.setHeightForWidth(self.Spikeling_CustomStimulus_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_frame.setSizePolicy(sizePolicy1)
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

        self.Spikeling_CustomStimulus_Selection_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_Selection_frame.setObjectName(u"Spikeling_CustomStimulus_Selection_frame")
        self.Spikeling_CustomStimulus_Selection_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_Selection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.Spikeling_CustomStimulus_Selection_frame)
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 5, 0)
        self.Spikeling_CustomStimulus_StimLabel_frame = QFrame(self.Spikeling_CustomStimulus_Selection_frame)
        self.Spikeling_CustomStimulus_StimLabel_frame.setObjectName(u"Spikeling_CustomStimulus_StimLabel_frame")
        self.Spikeling_CustomStimulus_StimLabel_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_StimLabel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_253 = QHBoxLayout(self.Spikeling_CustomStimulus_StimLabel_frame)
        self.horizontalLayout_253.setSpacing(0)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.horizontalLayout_253.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_StimLabel = QLabel(self.Spikeling_CustomStimulus_StimLabel_frame)
        self.Spikeling_CustomStimulus_StimLabel.setObjectName(u"Spikeling_CustomStimulus_StimLabel")
        self.Spikeling_CustomStimulus_StimLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_253.addWidget(self.Spikeling_CustomStimulus_StimLabel)


        self.horizontalLayout_45.addWidget(self.Spikeling_CustomStimulus_StimLabel_frame)

        self.Spikeling_CustomStimulus_Load_frame = QFrame(self.Spikeling_CustomStimulus_Selection_frame)
        self.Spikeling_CustomStimulus_Load_frame.setObjectName(u"Spikeling_CustomStimulus_Load_frame")
        sizePolicy2.setHeightForWidth(self.Spikeling_CustomStimulus_Load_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_Load_frame.setSizePolicy(sizePolicy2)
        self.Spikeling_CustomStimulus_Load_frame.setMinimumSize(QSize(50, 0))
        self.Spikeling_CustomStimulus_Load_frame.setMaximumSize(QSize(50, 16777215))
        self.Spikeling_CustomStimulus_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_Load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_252 = QHBoxLayout(self.Spikeling_CustomStimulus_Load_frame)
        self.horizontalLayout_252.setSpacing(0)
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.horizontalLayout_252.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_Load_pushButton = QPushButton(self.Spikeling_CustomStimulus_Load_frame)
        self.Spikeling_CustomStimulus_Load_pushButton.setObjectName(u"Spikeling_CustomStimulus_Load_pushButton")
        self.Spikeling_CustomStimulus_Load_pushButton.setMinimumSize(QSize(50, 0))
        self.Spikeling_CustomStimulus_Load_pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_252.addWidget(self.Spikeling_CustomStimulus_Load_pushButton)


        self.horizontalLayout_45.addWidget(self.Spikeling_CustomStimulus_Load_frame)


        self.verticalLayout_24.addWidget(self.Spikeling_CustomStimulus_Selection_frame)

        self.Spikeling_CustomStimulus_display_frame = QFrame(self.Spikeling_CustomStimulus_frame)
        self.Spikeling_CustomStimulus_display_frame.setObjectName(u"Spikeling_CustomStimulus_display_frame")
        self.Spikeling_CustomStimulus_display_frame.setFrameShape(QFrame.StyledPanel)
        self.Spikeling_CustomStimulus_display_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.Spikeling_CustomStimulus_display_frame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.Spikeling_CustomStimulus_display = PlotWidget(self.Spikeling_CustomStimulus_display_frame)
        self.Spikeling_CustomStimulus_display.setObjectName(u"Spikeling_CustomStimulus_display")
        self.Spikeling_CustomStimulus_display.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.Spikeling_CustomStimulus_display.sizePolicy().hasHeightForWidth())
        self.Spikeling_CustomStimulus_display.setSizePolicy(sizePolicy5)
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
        self.Spikeling_parameter_bottom_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_parameter_bottom_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_58.addWidget(self.Spikeling_parameter_bottom_line)

        self.Spikeling_PR_frame = QFrame(self.StimulusParameter_page)
        self.Spikeling_PR_frame.setObjectName(u"Spikeling_PR_frame")
        sizePolicy1.setHeightForWidth(self.Spikeling_PR_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_PR_frame.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.Spikeling_NeuronParameter_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_NeuronParameter_frame.setSizePolicy(sizePolicy2)
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
        self.Spikeling_neuronparameters_top_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_neuronparameters_top_line.setFrameShadow(QFrame.Shadow.Sunken)

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
        self.Spikeling_neuronparameters_middle_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_neuronparameters_middle_line.setFrameShadow(QFrame.Shadow.Sunken)

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
        self.Spikeling_neuronparameters_bottom_line.setFrameShape(QFrame.Shape.HLine)
        self.Spikeling_neuronparameters_bottom_line.setFrameShadow(QFrame.Shadow.Sunken)

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
        self.Spikeling_Synapse2_Decay_toggle_frame.setMaximumSize(QSize(50, 16777215))
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
        sizePolicy3.setHeightForWidth(self.Spikeling_Synapse2_Decay_frame.sizePolicy().hasHeightForWidth())
        self.Spikeling_Synapse2_Decay_frame.setSizePolicy(sizePolicy3)
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
        icon19.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_0)

        self.line_7 = QFrame(self.page_103_1_0)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_7)

        self.DataAnalysis_Oscilloscope_widget1_0_1 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_1)

        self.line_31 = QFrame(self.page_103_1_0)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.HLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_31)

        self.DataAnalysis_Oscilloscope_widget1_0_2 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_2")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_2.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget1_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_2)

        self.line_8 = QFrame(self.page_103_1_0)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_8)

        self.DataAnalysis_Oscilloscope_widget1_0_3 = PlotWidget(self.page_103_1_0)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget1_0_3")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_0_3.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_39.addWidget(self.DataAnalysis_Oscilloscope_widget1_0_3)

        self.line_32 = QFrame(self.page_103_1_0)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_32)

        self.DataAnalysis_Neurons_pushButton10_frame = QFrame(self.page_103_1_0)
        self.DataAnalysis_Neurons_pushButton10_frame.setObjectName(u"DataAnalysis_Neurons_pushButton10_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton10_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton10_frame.setSizePolicy(sizePolicy2)
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
        font6 = QFont()
        font6.setPointSize(10)
        self.DataAnalysis_Neuron0Vm_pushButton10.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton10.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron0Vm_pushButton10)

        self.DataAnalysis_Neuron1Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron1Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton10")
        self.DataAnalysis_Neuron1Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton10.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton10.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_80.addWidget(self.DataAnalysis_Neuron1Vm_pushButton10)

        self.DataAnalysis_Neuron2Vm_pushButton10 = QPushButton(self.DataAnalysis_Neurons_pushButton10_frame)
        self.DataAnalysis_Neuron2Vm_pushButton10.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(25)
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton10.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton10.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton10.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton10.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_0)

        self.line_10 = QFrame(self.page_103_1_1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_48.addWidget(self.line_10)

        self.DataAnalysis_Oscilloscope_widget1_1_1 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_1)

        self.line_9 = QFrame(self.page_103_1_1)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_48.addWidget(self.line_9)

        self.DataAnalysis_Oscilloscope_widget1_1_2 = PlotWidget(self.page_103_1_1)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_1_2")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_1_2.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setMaximumSize(QSize(16777215, 150))
        self.DataAnalysis_Oscilloscope_widget1_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_48.addWidget(self.DataAnalysis_Oscilloscope_widget1_1_2)

        self.line_33 = QFrame(self.page_103_1_1)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_48.addWidget(self.line_33)

        self.DataAnalysis_Neurons_pushButton11_frame = QFrame(self.page_103_1_1)
        self.DataAnalysis_Neurons_pushButton11_frame.setObjectName(u"DataAnalysis_Neurons_pushButton11_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton11_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton11_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton11.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton11.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron0Vm_pushButton11)

        self.DataAnalysis_Neuron1Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron1Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton11")
        self.DataAnalysis_Neuron1Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton11.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton11.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_101.addWidget(self.DataAnalysis_Neuron1Vm_pushButton11)

        self.DataAnalysis_Neuron2Vm_pushButton11 = QPushButton(self.DataAnalysis_Neurons_pushButton11_frame)
        self.DataAnalysis_Neuron2Vm_pushButton11.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton11")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton11.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton11.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton11.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton11.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_0)

        self.line_30 = QFrame(self.page_103_1_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.HLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_49.addWidget(self.line_30)

        self.DataAnalysis_Oscilloscope_widget1_2_1 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMinimumSize(QSize(0, 0))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setMaximumSize(QSize(16777215, 16777215))
        self.DataAnalysis_Oscilloscope_widget1_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_1)

        self.line_29 = QFrame(self.page_103_1_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.HLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_49.addWidget(self.line_29)

        self.DataAnalysis_Oscilloscope_widget1_2_2 = PlotWidget(self.page_103_1_2)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget1_2_2")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget1_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget1_2_2.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMinimumSize(QSize(0, 150))
        self.DataAnalysis_Oscilloscope_widget1_2_2.setMaximumSize(QSize(16777215, 150))
        font7 = QFont()
        font7.setPointSize(11)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setFont(font7)
        self.DataAnalysis_Oscilloscope_widget1_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_49.addWidget(self.DataAnalysis_Oscilloscope_widget1_2_2)

        self.line_34 = QFrame(self.page_103_1_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.HLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_49.addWidget(self.line_34)

        self.DataAnalysis_Neurons_pushButton12_frame = QFrame(self.page_103_1_2)
        self.DataAnalysis_Neurons_pushButton12_frame.setObjectName(u"DataAnalysis_Neurons_pushButton12_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton12_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton12_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton12.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton12.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron0Vm_pushButton12)

        self.DataAnalysis_Neuron1Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron1Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton12")
        self.DataAnalysis_Neuron1Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton12.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton12.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_103.addWidget(self.DataAnalysis_Neuron1Vm_pushButton12)

        self.DataAnalysis_Neuron2Vm_pushButton12 = QPushButton(self.DataAnalysis_Neurons_pushButton12_frame)
        self.DataAnalysis_Neuron2Vm_pushButton12.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton12")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton12.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton12.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton12.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton12.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_0)

        self.line_14 = QFrame(self.page_103_2_0)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_42.addWidget(self.line_14)

        self.DataAnalysis_Oscilloscope_widget2_0_1 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_1)

        self.line_13 = QFrame(self.page_103_2_0)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_42.addWidget(self.line_13)

        self.DataAnalysis_Oscilloscope_widget2_0_2 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_2)

        self.line_11 = QFrame(self.page_103_2_0)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_42.addWidget(self.line_11)

        self.DataAnalysis_Oscilloscope_widget2_0_3 = PlotWidget(self.page_103_2_0)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_0_3")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_0_3.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_42.addWidget(self.DataAnalysis_Oscilloscope_widget2_0_3)

        self.line_35 = QFrame(self.page_103_2_0)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.HLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_42.addWidget(self.line_35)

        self.DataAnalysis_Neurons_pushButton20_frame = QFrame(self.page_103_2_0)
        self.DataAnalysis_Neurons_pushButton20_frame.setObjectName(u"DataAnalysis_Neurons_pushButton20_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton20_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton20_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton20.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton20.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron0Vm_pushButton20)

        self.DataAnalysis_Neuron1Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron1Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton20")
        self.DataAnalysis_Neuron1Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton20.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton20.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_105.addWidget(self.DataAnalysis_Neuron1Vm_pushButton20)

        self.DataAnalysis_Neuron2Vm_pushButton20 = QPushButton(self.DataAnalysis_Neurons_pushButton20_frame)
        self.DataAnalysis_Neuron2Vm_pushButton20.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton20")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton20.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton20.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton20.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton20.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_0)

        self.line_16 = QFrame(self.page_103_2_1)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.line_16)

        self.DataAnalysis_Oscilloscope_widget2_1_1 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_1)

        self.line_15 = QFrame(self.page_103_2_1)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.line_15)

        self.DataAnalysis_Oscilloscope_widget2_1_2 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_2)

        self.line_12 = QFrame(self.page_103_2_1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.line_12)

        self.DataAnalysis_Oscilloscope_widget2_1_3 = PlotWidget(self.page_103_2_1)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_1_3")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_1_3.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);\n"
"")

        self.verticalLayout_43.addWidget(self.DataAnalysis_Oscilloscope_widget2_1_3)

        self.line_36 = QFrame(self.page_103_2_1)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.HLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.line_36)

        self.DataAnalysis_Neurons_pushButton21_frame = QFrame(self.page_103_2_1)
        self.DataAnalysis_Neurons_pushButton21_frame.setObjectName(u"DataAnalysis_Neurons_pushButton21_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton21_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton21_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton21.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton21.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron0Vm_pushButton21)

        self.DataAnalysis_Neuron1Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron1Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton21")
        self.DataAnalysis_Neuron1Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton21.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton21.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_107.addWidget(self.DataAnalysis_Neuron1Vm_pushButton21)

        self.DataAnalysis_Neuron2Vm_pushButton21 = QPushButton(self.DataAnalysis_Neurons_pushButton21_frame)
        self.DataAnalysis_Neuron2Vm_pushButton21.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton21")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton21.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton21.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton21.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton21.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_0)

        self.line_18 = QFrame(self.page_103_2_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_44.addWidget(self.line_18)

        self.DataAnalysis_Oscilloscope_widget2_2_1 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_1)

        self.line_17 = QFrame(self.page_103_2_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_44.addWidget(self.line_17)

        self.DataAnalysis_Oscilloscope_widget2_2_2 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget2_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_2)

        self.line_19 = QFrame(self.page_103_2_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_44.addWidget(self.line_19)

        self.DataAnalysis_Oscilloscope_widget2_2_3 = PlotWidget(self.page_103_2_2)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget2_2_3")
        sizePolicy5.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget2_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget2_2_3.setSizePolicy(sizePolicy5)
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMinimumSize(QSize(0, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setMaximumSize(QSize(16777215, 100))
        self.DataAnalysis_Oscilloscope_widget2_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_44.addWidget(self.DataAnalysis_Oscilloscope_widget2_2_3)

        self.line_37 = QFrame(self.page_103_2_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.HLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_44.addWidget(self.line_37)

        self.DataAnalysis_Neurons_pushButton22_frame = QFrame(self.page_103_2_2)
        self.DataAnalysis_Neurons_pushButton22_frame.setObjectName(u"DataAnalysis_Neurons_pushButton22_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton22_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton22_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton22.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton22.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron0Vm_pushButton22)

        self.DataAnalysis_Neuron1Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron1Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton22")
        self.DataAnalysis_Neuron1Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton22.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton22.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_108.addWidget(self.DataAnalysis_Neuron1Vm_pushButton22)

        self.DataAnalysis_Neuron2Vm_pushButton22 = QPushButton(self.DataAnalysis_Neurons_pushButton22_frame)
        self.DataAnalysis_Neuron2Vm_pushButton22.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton22")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton22.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton22.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton22.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton22.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_0)

        self.line_20 = QFrame(self.page_103_3_0)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_45.addWidget(self.line_20)

        self.DataAnalysis_Oscilloscope_widget3_0_1 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_1")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_1.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Oscilloscope_widget3_0_1.setMinimumSize(QSize(0, 50))
        self.DataAnalysis_Oscilloscope_widget3_0_1.setMaximumSize(QSize(16777215, 75))
        self.DataAnalysis_Oscilloscope_widget3_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_1)

        self.line_22 = QFrame(self.page_103_3_0)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_45.addWidget(self.line_22)

        self.DataAnalysis_Oscilloscope_widget3_0_2 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_2)

        self.line_21 = QFrame(self.page_103_3_0)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_45.addWidget(self.line_21)

        self.DataAnalysis_Oscilloscope_widget3_0_3 = PlotWidget(self.page_103_3_0)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_0_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_0_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_0_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_45.addWidget(self.DataAnalysis_Oscilloscope_widget3_0_3)

        self.line_38 = QFrame(self.page_103_3_0)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.HLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_45.addWidget(self.line_38)

        self.DataAnalysis_Neurons_pushButton30_frame = QFrame(self.page_103_3_0)
        self.DataAnalysis_Neurons_pushButton30_frame.setObjectName(u"DataAnalysis_Neurons_pushButton30_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton30_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton30_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton30.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton30.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron0Vm_pushButton30)

        self.DataAnalysis_Neuron1Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron1Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton30")
        self.DataAnalysis_Neuron1Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton30.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton30.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_109.addWidget(self.DataAnalysis_Neuron1Vm_pushButton30)

        self.DataAnalysis_Neuron2Vm_pushButton30 = QPushButton(self.DataAnalysis_Neurons_pushButton30_frame)
        self.DataAnalysis_Neuron2Vm_pushButton30.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton30")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton30.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton30.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton30.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton30.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_1_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_0)

        self.line_23 = QFrame(self.page_103_3_1)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_46.addWidget(self.line_23)

        self.DataAnalysis_Oscilloscope_widget3_1_1 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_1_1.setMinimumSize(QSize(0, 50))
        self.DataAnalysis_Oscilloscope_widget3_1_1.setMaximumSize(QSize(16777215, 75))
        self.DataAnalysis_Oscilloscope_widget3_1_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_1)

        self.line_25 = QFrame(self.page_103_3_1)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_46.addWidget(self.line_25)

        self.DataAnalysis_Oscilloscope_widget3_1_2 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_1_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_2)

        self.line_24 = QFrame(self.page_103_3_1)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_46.addWidget(self.line_24)

        self.DataAnalysis_Oscilloscope_widget3_1_3 = PlotWidget(self.page_103_3_1)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_1_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_1_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_1_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_1_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_46.addWidget(self.DataAnalysis_Oscilloscope_widget3_1_3)

        self.line_39 = QFrame(self.page_103_3_1)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.HLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_46.addWidget(self.line_39)

        self.DataAnalysis_Neurons_pushButton31_frame = QFrame(self.page_103_3_1)
        self.DataAnalysis_Neurons_pushButton31_frame.setObjectName(u"DataAnalysis_Neurons_pushButton31_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton31_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton31_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton31.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton31.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron0Vm_pushButton31)

        self.DataAnalysis_Neuron1Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron1Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton31")
        self.DataAnalysis_Neuron1Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton31.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton31.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_110.addWidget(self.DataAnalysis_Neuron1Vm_pushButton31)

        self.DataAnalysis_Neuron2Vm_pushButton31 = QPushButton(self.DataAnalysis_Neurons_pushButton31_frame)
        self.DataAnalysis_Neuron2Vm_pushButton31.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton31")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton31.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton31.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton31.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton31.setFont(font6)
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
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_0.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_0.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_2_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_0)

        self.line_26 = QFrame(self.page_103_3_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_47.addWidget(self.line_26)

        self.DataAnalysis_Oscilloscope_widget3_2_1 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_1")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_1.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_1.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_2_1.setMinimumSize(QSize(0, 50))
        self.DataAnalysis_Oscilloscope_widget3_2_1.setMaximumSize(QSize(16777215, 75))
        self.DataAnalysis_Oscilloscope_widget3_2_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_1)

        self.line_28 = QFrame(self.page_103_3_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_47.addWidget(self.line_28)

        self.DataAnalysis_Oscilloscope_widget3_2_2 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_2")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_2.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_2.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_2_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_2)

        self.line_27 = QFrame(self.page_103_3_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_47.addWidget(self.line_27)

        self.DataAnalysis_Oscilloscope_widget3_2_3 = PlotWidget(self.page_103_3_2)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setObjectName(u"DataAnalysis_Oscilloscope_widget3_2_3")
        sizePolicy1.setHeightForWidth(self.DataAnalysis_Oscilloscope_widget3_2_3.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Oscilloscope_widget3_2_3.setSizePolicy(sizePolicy1)
        self.DataAnalysis_Oscilloscope_widget3_2_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_47.addWidget(self.DataAnalysis_Oscilloscope_widget3_2_3)

        self.line_40 = QFrame(self.page_103_3_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.HLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_47.addWidget(self.line_40)

        self.DataAnalysis_Neurons_pushButton32_frame = QFrame(self.page_103_3_2)
        self.DataAnalysis_Neurons_pushButton32_frame.setObjectName(u"DataAnalysis_Neurons_pushButton32_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton32_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton32_frame.setSizePolicy(sizePolicy2)
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
        self.DataAnalysis_Neuron0Vm_pushButton32.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton32.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron0Vm_pushButton32)

        self.DataAnalysis_Neuron1Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron1Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton32")
        self.DataAnalysis_Neuron1Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton32.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton32.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron1Vm_pushButton32)

        self.DataAnalysis_Neuron2Vm_pushButton32 = QPushButton(self.DataAnalysis_Neurons_pushButton32_frame)
        self.DataAnalysis_Neuron2Vm_pushButton32.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton32")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton32.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton32.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton32.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton32.setFont(font6)
        self.DataAnalysis_Neuron2Vm_pushButton32.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_111.addWidget(self.DataAnalysis_Neuron2Vm_pushButton32)


        self.verticalLayout_47.addWidget(self.DataAnalysis_Neurons_pushButton32_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_3_2)
        self.page_103_11_0 = QWidget()
        self.page_103_11_0.setObjectName(u"page_103_11_0")
        self.verticalLayout_20 = QVBoxLayout(self.page_103_11_0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_Oscilloscope_widget11_0_0 = PlotWidget(self.page_103_11_0)
        self.DataAnalysis_Oscilloscope_widget11_0_0.setObjectName(u"DataAnalysis_Oscilloscope_widget11_0_0")
        self.DataAnalysis_Oscilloscope_widget11_0_0.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_20.addWidget(self.DataAnalysis_Oscilloscope_widget11_0_0)

        self.line_6 = QFrame(self.page_103_11_0)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_6)

        self.DataAnalysis_Oscilloscope_widget11_0_1 = PlotWidget(self.page_103_11_0)
        self.DataAnalysis_Oscilloscope_widget11_0_1.setObjectName(u"DataAnalysis_Oscilloscope_widget11_0_1")
        self.DataAnalysis_Oscilloscope_widget11_0_1.setMinimumSize(QSize(0, 50))
        self.DataAnalysis_Oscilloscope_widget11_0_1.setMaximumSize(QSize(16777215, 75))
        self.DataAnalysis_Oscilloscope_widget11_0_1.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_20.addWidget(self.DataAnalysis_Oscilloscope_widget11_0_1)

        self.line_69 = QFrame(self.page_103_11_0)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.Shape.HLine)
        self.line_69.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_69)

        self.DataAnalysis_Oscilloscope_widget11_0_2 = PlotWidget(self.page_103_11_0)
        self.DataAnalysis_Oscilloscope_widget11_0_2.setObjectName(u"DataAnalysis_Oscilloscope_widget11_0_2")
        self.DataAnalysis_Oscilloscope_widget11_0_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_20.addWidget(self.DataAnalysis_Oscilloscope_widget11_0_2)

        self.line_70 = QFrame(self.page_103_11_0)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.Shape.HLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_70)

        self.DataAnalysis_Oscilloscope_widget11_0_3 = PlotWidget(self.page_103_11_0)
        self.DataAnalysis_Oscilloscope_widget11_0_3.setObjectName(u"DataAnalysis_Oscilloscope_widget11_0_3")
        self.DataAnalysis_Oscilloscope_widget11_0_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")

        self.verticalLayout_20.addWidget(self.DataAnalysis_Oscilloscope_widget11_0_3)

        self.line_71 = QFrame(self.page_103_11_0)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setFrameShape(QFrame.Shape.HLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_71)

        self.DataAnalysis_Neurons_pushButton110_frame = QFrame(self.page_103_11_0)
        self.DataAnalysis_Neurons_pushButton110_frame.setObjectName(u"DataAnalysis_Neurons_pushButton110_frame")
        sizePolicy2.setHeightForWidth(self.DataAnalysis_Neurons_pushButton110_frame.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neurons_pushButton110_frame.setSizePolicy(sizePolicy2)
        self.DataAnalysis_Neurons_pushButton110_frame.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neurons_pushButton110_frame.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neurons_pushButton110_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_Neurons_pushButton110_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_417 = QHBoxLayout(self.DataAnalysis_Neurons_pushButton110_frame)
        self.horizontalLayout_417.setSpacing(5)
        self.horizontalLayout_417.setObjectName(u"horizontalLayout_417")
        self.horizontalLayout_417.setContentsMargins(5, 0, 5, 0)
        self.DataAnalysis_Neuron0Vm_pushButton110 = QPushButton(self.DataAnalysis_Neurons_pushButton110_frame)
        self.DataAnalysis_Neuron0Vm_pushButton110.setObjectName(u"DataAnalysis_Neuron0Vm_pushButton110")
        self.DataAnalysis_Neuron0Vm_pushButton110.setMinimumSize(QSize(25, 0))
        self.DataAnalysis_Neuron0Vm_pushButton110.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron0Vm_pushButton110.setFont(font6)
        self.DataAnalysis_Neuron0Vm_pushButton110.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_417.addWidget(self.DataAnalysis_Neuron0Vm_pushButton110)

        self.DataAnalysis_Neuron1Vm_pushButton110 = QPushButton(self.DataAnalysis_Neurons_pushButton110_frame)
        self.DataAnalysis_Neuron1Vm_pushButton110.setObjectName(u"DataAnalysis_Neuron1Vm_pushButton110")
        self.DataAnalysis_Neuron1Vm_pushButton110.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron1Vm_pushButton110.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron1Vm_pushButton110.setFont(font6)
        self.DataAnalysis_Neuron1Vm_pushButton110.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.horizontalLayout_417.addWidget(self.DataAnalysis_Neuron1Vm_pushButton110)

        self.DataAnalysis_Neuron2Vm_pushButton110 = QPushButton(self.DataAnalysis_Neurons_pushButton110_frame)
        self.DataAnalysis_Neuron2Vm_pushButton110.setObjectName(u"DataAnalysis_Neuron2Vm_pushButton110")
        sizePolicy7.setHeightForWidth(self.DataAnalysis_Neuron2Vm_pushButton110.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Neuron2Vm_pushButton110.setSizePolicy(sizePolicy7)
        self.DataAnalysis_Neuron2Vm_pushButton110.setMinimumSize(QSize(0, 25))
        self.DataAnalysis_Neuron2Vm_pushButton110.setMaximumSize(QSize(16777215, 25))
        self.DataAnalysis_Neuron2Vm_pushButton110.setFont(font6)
        self.DataAnalysis_Neuron2Vm_pushButton110.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.horizontalLayout_417.addWidget(self.DataAnalysis_Neuron2Vm_pushButton110)


        self.verticalLayout_20.addWidget(self.DataAnalysis_Neurons_pushButton110_frame)

        self.DataAnalysis_Display_StackedWidget.addWidget(self.page_103_11_0)

        self.verticalLayout_35.addWidget(self.DataAnalysis_Display_StackedWidget)


        self.horizontalLayout_61.addWidget(self.DataAnalysis_Display_frame)

        self.DataAnalysis_stackedWidget = QStackedWidget(self.DataAnalysis_frame)
        self.DataAnalysis_stackedWidget.setObjectName(u"DataAnalysis_stackedWidget")
        sizePolicy.setHeightForWidth(self.DataAnalysis_stackedWidget.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_stackedWidget.setSizePolicy(sizePolicy)
        self.DataAnalysis_stackedWidget.setMinimumSize(QSize(250, 0))
        self.DataAnalysis_stackedWidget.setMaximumSize(QSize(250, 16777215))
        self.DataAnalysis_stackedWidget.setStyleSheet(u"")
        self.DataAnalysis_SquareStim = QWidget()
        self.DataAnalysis_SquareStim.setObjectName(u"DataAnalysis_SquareStim")
        self.verticalLayout_34 = QVBoxLayout(self.DataAnalysis_SquareStim)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 1)
        self.DataAnalysis_LoadData_frame = QFrame(self.DataAnalysis_SquareStim)
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
        sizePolicy3.setHeightForWidth(self.DataAnalysis_LoadData_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_LoadData_label.setSizePolicy(sizePolicy3)
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

        self.DataAnalysis_LoadData_line = QFrame(self.DataAnalysis_SquareStim)
        self.DataAnalysis_LoadData_line.setObjectName(u"DataAnalysis_LoadData_line")
        self.DataAnalysis_LoadData_line.setFrameShape(QFrame.Shape.HLine)
        self.DataAnalysis_LoadData_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.DataAnalysis_LoadData_line)

        self.DataAnalysis_Spike_frame = QFrame(self.DataAnalysis_SquareStim)
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
        sizePolicy3.setHeightForWidth(self.DataAnalysis_Spike_threshold_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_Spike_threshold_label.setSizePolicy(sizePolicy3)

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

        self.DataAnalysis_Spike_line = QFrame(self.DataAnalysis_SquareStim)
        self.DataAnalysis_Spike_line.setObjectName(u"DataAnalysis_Spike_line")
        self.DataAnalysis_Spike_line.setFrameShape(QFrame.Shape.HLine)
        self.DataAnalysis_Spike_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.DataAnalysis_Spike_line)

        self.DataAnalysis_Average_frame = QFrame(self.DataAnalysis_SquareStim)
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

        self.DataAnalysis_stackedWidget.addWidget(self.DataAnalysis_SquareStim)
        self.DataAnalysis_StepStim = QWidget()
        self.DataAnalysis_StepStim.setObjectName(u"DataAnalysis_StepStim")
        self.verticalLayout_18 = QVBoxLayout(self.DataAnalysis_StepStim)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_StepStim_LoadData_frame = QFrame(self.DataAnalysis_StepStim)
        self.DataAnalysis_StepStim_LoadData_frame.setObjectName(u"DataAnalysis_StepStim_LoadData_frame")
        self.DataAnalysis_StepStim_LoadData_frame.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_StepStim_LoadData_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.DataAnalysis_StepStim_LoadData_frame)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(15, -1, 15, -1)
        self.DataAnalysis_StepStim_LoadData_subframe = QFrame(self.DataAnalysis_StepStim_LoadData_frame)
        self.DataAnalysis_StepStim_LoadData_subframe.setObjectName(u"DataAnalysis_StepStim_LoadData_subframe")
        self.DataAnalysis_StepStim_LoadData_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_StepStim_LoadData_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_416 = QHBoxLayout(self.DataAnalysis_StepStim_LoadData_subframe)
        self.horizontalLayout_416.setSpacing(0)
        self.horizontalLayout_416.setObjectName(u"horizontalLayout_416")
        self.horizontalLayout_416.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_StepStim_LoadData_label = QLabel(self.DataAnalysis_StepStim_LoadData_subframe)
        self.DataAnalysis_StepStim_LoadData_label.setObjectName(u"DataAnalysis_StepStim_LoadData_label")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_StepStim_LoadData_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_StepStim_LoadData_label.setSizePolicy(sizePolicy3)
        self.DataAnalysis_StepStim_LoadData_label.setWordWrap(True)

        self.horizontalLayout_416.addWidget(self.DataAnalysis_StepStim_LoadData_label)

        self.DataAnalysis_StepStim_LoadData_pushButton = QPushButton(self.DataAnalysis_StepStim_LoadData_subframe)
        self.DataAnalysis_StepStim_LoadData_pushButton.setObjectName(u"DataAnalysis_StepStim_LoadData_pushButton")
        self.DataAnalysis_StepStim_LoadData_pushButton.setIconSize(QSize(14, 16))

        self.horizontalLayout_416.addWidget(self.DataAnalysis_StepStim_LoadData_pushButton)


        self.verticalLayout_60.addWidget(self.DataAnalysis_StepStim_LoadData_subframe)

        self.DataAnalysis_StepStim_LoadStim_subframe = QFrame(self.DataAnalysis_StepStim_LoadData_frame)
        self.DataAnalysis_StepStim_LoadStim_subframe.setObjectName(u"DataAnalysis_StepStim_LoadStim_subframe")
        self.DataAnalysis_StepStim_LoadStim_subframe.setFrameShape(QFrame.StyledPanel)
        self.DataAnalysis_StepStim_LoadStim_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_418 = QHBoxLayout(self.DataAnalysis_StepStim_LoadStim_subframe)
        self.horizontalLayout_418.setSpacing(0)
        self.horizontalLayout_418.setObjectName(u"horizontalLayout_418")
        self.horizontalLayout_418.setContentsMargins(0, 0, 0, 0)
        self.DataAnalysis_StepStim_LoadStim_label = QLabel(self.DataAnalysis_StepStim_LoadStim_subframe)
        self.DataAnalysis_StepStim_LoadStim_label.setObjectName(u"DataAnalysis_StepStim_LoadStim_label")
        sizePolicy3.setHeightForWidth(self.DataAnalysis_StepStim_LoadStim_label.sizePolicy().hasHeightForWidth())
        self.DataAnalysis_StepStim_LoadStim_label.setSizePolicy(sizePolicy3)
        self.DataAnalysis_StepStim_LoadStim_label.setWordWrap(True)

        self.horizontalLayout_418.addWidget(self.DataAnalysis_StepStim_LoadStim_label)

        self.DataAnalysis_LoadStim_pushButton = QPushButton(self.DataAnalysis_StepStim_LoadStim_subframe)
        self.DataAnalysis_LoadStim_pushButton.setObjectName(u"DataAnalysis_LoadStim_pushButton")
        self.DataAnalysis_LoadStim_pushButton.setIconSize(QSize(14, 16))

        self.horizontalLayout_418.addWidget(self.DataAnalysis_LoadStim_pushButton)


        self.verticalLayout_60.addWidget(self.DataAnalysis_StepStim_LoadStim_subframe)

        self.DataAnalysis_StepStim_LoadData_Display_pushButton = QPushButton(self.DataAnalysis_StepStim_LoadData_frame)
        self.DataAnalysis_StepStim_LoadData_Display_pushButton.setObjectName(u"DataAnalysis_StepStim_LoadData_Display_pushButton")

        self.verticalLayout_60.addWidget(self.DataAnalysis_StepStim_LoadData_Display_pushButton)

        self.DataAnalysis_StepStim_SaveImage_pushButton = QPushButton(self.DataAnalysis_StepStim_LoadData_frame)
        self.DataAnalysis_StepStim_SaveImage_pushButton.setObjectName(u"DataAnalysis_StepStim_SaveImage_pushButton")

        self.verticalLayout_60.addWidget(self.DataAnalysis_StepStim_SaveImage_pushButton)


        self.verticalLayout_18.addWidget(self.DataAnalysis_StepStim_LoadData_frame)

        self.frame_7 = QFrame(self.DataAnalysis_StepStim)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_18.addWidget(self.frame_7)

        self.DataAnalysis_stackedWidget.addWidget(self.DataAnalysis_StepStim)

        self.horizontalLayout_61.addWidget(self.DataAnalysis_stackedWidget)


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
        self.Imaging_header_frame = QFrame(self.Imaging_widget)
        self.Imaging_header_frame.setObjectName(u"Imaging_header_frame")
        self.Imaging_header_frame.setMinimumSize(QSize(0, 30))
        self.Imaging_header_frame.setMaximumSize(QSize(16777215, 25))
        self.Imaging_header_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.Imaging_header_frame)
        self.horizontalLayout_119.setSpacing(0)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 5)
        self.Imaging_pushButton_frame = QFrame(self.Imaging_header_frame)
        self.Imaging_pushButton_frame.setObjectName(u"Imaging_pushButton_frame")
        self.Imaging_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.Imaging_pushButton_frame)
        self.horizontalLayout_158.setSpacing(0)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(25, 0, 0, 0)
        self.Imaging_pushButton = QPushButton(self.Imaging_pushButton_frame)
        self.Imaging_pushButton.setObjectName(u"Imaging_pushButton")
        self.Imaging_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.Imaging_pushButton.setFont(font1)
        self.Imaging_pushButton.setCheckable(True)

        self.horizontalLayout_158.addWidget(self.Imaging_pushButton)

        self.frame_6 = QFrame(self.Imaging_pushButton_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")

        self.horizontalLayout_158.addWidget(self.frame_6)


        self.horizontalLayout_119.addWidget(self.Imaging_pushButton_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_109.addWidget(self.Imaging_header_frame)

        self.Imaging_Oscilloscope_frame = QFrame(self.Imaging_widget)
        self.Imaging_Oscilloscope_frame.setObjectName(u"Imaging_Oscilloscope_frame")
        self.Imaging_Oscilloscope_frame.setMaximumSize(QSize(16777215, 16777200))
        self.Imaging_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.Imaging_Oscilloscope_frame)
        self.horizontalLayout_157.setSpacing(0)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Oscilloscope_widget = PlotWidget(self.Imaging_Oscilloscope_frame)
        self.Imaging_Oscilloscope_widget.setObjectName(u"Imaging_Oscilloscope_widget")
        sizePolicy4.setHeightForWidth(self.Imaging_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.Imaging_Oscilloscope_widget.setSizePolicy(sizePolicy4)
        self.Imaging_Oscilloscope_widget.setAutoFillBackground(False)
        self.Imaging_Oscilloscope_widget.setStyleSheet(u"")
        self.horizontalLayout_178 = QHBoxLayout(self.Imaging_Oscilloscope_widget)
        self.horizontalLayout_178.setSpacing(0)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Oscilloscope_Traces_frame = QFrame(self.Imaging_Oscilloscope_widget)
        self.Imaging_Oscilloscope_Traces_frame.setObjectName(u"Imaging_Oscilloscope_Traces_frame")
        self.Imaging_Oscilloscope_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.Imaging_Oscilloscope_Traces_frame)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Oscilloscope_FirstTraces_frame = QFrame(self.Imaging_Oscilloscope_Traces_frame)
        self.Imaging_Oscilloscope_FirstTraces_frame.setObjectName(u"Imaging_Oscilloscope_FirstTraces_frame")
        self.Imaging_Oscilloscope_FirstTraces_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Oscilloscope_FirstTraces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Fluorescence_Checkbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_Fluorescence_Checkbox.setObjectName(u"Imaging_Fluorescence_Checkbox")
        self.Imaging_Fluorescence_Checkbox.setEnabled(True)
        self.Imaging_Fluorescence_Checkbox.setAutoFillBackground(False)
        self.Imaging_Fluorescence_Checkbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.Imaging_Fluorescence_Checkbox.setChecked(True)

        self.horizontalLayout_53.addWidget(self.Imaging_Fluorescence_Checkbox)

        self.Imaging_Calcium_Checkbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_Calcium_Checkbox.setObjectName(u"Imaging_Calcium_Checkbox")
        self.Imaging_Calcium_Checkbox.setEnabled(True)
        self.Imaging_Calcium_Checkbox.setAutoFillBackground(False)
        self.Imaging_Calcium_Checkbox.setStyleSheet(u"color: rgb(211, 54, 130);")
        self.Imaging_Calcium_Checkbox.setChecked(False)

        self.horizontalLayout_53.addWidget(self.Imaging_Calcium_Checkbox)

        self.Imaging_Vm_Checkbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_Vm_Checkbox.setObjectName(u"Imaging_Vm_Checkbox")
        self.Imaging_Vm_Checkbox.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.horizontalLayout_53.addWidget(self.Imaging_Vm_Checkbox)

        self.Imaging_Stimulus_Checkbox = QCheckBox(self.Imaging_Oscilloscope_FirstTraces_frame)
        self.Imaging_Stimulus_Checkbox.setObjectName(u"Imaging_Stimulus_Checkbox")
        self.Imaging_Stimulus_Checkbox.setEnabled(True)
        self.Imaging_Stimulus_Checkbox.setAutoFillBackground(False)
        self.Imaging_Stimulus_Checkbox.setStyleSheet(u"color: rgb(38, 139, 210);")
        self.Imaging_Stimulus_Checkbox.setChecked(True)

        self.horizontalLayout_53.addWidget(self.Imaging_Stimulus_Checkbox)


        self.verticalLayout_129.addWidget(self.Imaging_Oscilloscope_FirstTraces_frame, 0, Qt.AlignTop)


        self.horizontalLayout_178.addWidget(self.Imaging_Oscilloscope_Traces_frame)


        self.horizontalLayout_157.addWidget(self.Imaging_Oscilloscope_widget)


        self.verticalLayout_109.addWidget(self.Imaging_Oscilloscope_frame)

        self.Imaging_DataRecording_box = QGroupBox(self.Imaging_widget)
        self.Imaging_DataRecording_box.setObjectName(u"Imaging_DataRecording_box")
        sizePolicy5.setHeightForWidth(self.Imaging_DataRecording_box.sizePolicy().hasHeightForWidth())
        self.Imaging_DataRecording_box.setSizePolicy(sizePolicy5)
        self.Imaging_DataRecording_box.setMinimumSize(QSize(0, 100))
        self.Imaging_DataRecording_box.setMaximumSize(QSize(16777215, 100))
        self.Imaging_DataRecording_box.setStyleSheet(u"")
        self.horizontalLayout_114 = QHBoxLayout(self.Imaging_DataRecording_box)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(5, 5, 5, 5)
        self.Imaging_DataRecording_left_frame = QFrame(self.Imaging_DataRecording_box)
        self.Imaging_DataRecording_left_frame.setObjectName(u"Imaging_DataRecording_left_frame")
        self.Imaging_DataRecording_left_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_DataRecording_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.Imaging_DataRecording_left_frame)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.Imaging_DataRecording_recordingMode_frame = QFrame(self.Imaging_DataRecording_left_frame)
        self.Imaging_DataRecording_recordingMode_frame.setObjectName(u"Imaging_DataRecording_recordingMode_frame")
        self.Imaging_DataRecording_recordingMode_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_DataRecording_recordingMode_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_422 = QHBoxLayout(self.Imaging_DataRecording_recordingMode_frame)
        self.horizontalLayout_422.setSpacing(0)
        self.horizontalLayout_422.setObjectName(u"horizontalLayout_422")
        self.horizontalLayout_422.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_105.addWidget(self.Imaging_DataRecording_recordingMode_frame)


        self.horizontalLayout_114.addWidget(self.Imaging_DataRecording_left_frame)

        self.Imaging_DataRecording_right_frame = QFrame(self.Imaging_DataRecording_box)
        self.Imaging_DataRecording_right_frame.setObjectName(u"Imaging_DataRecording_right_frame")
        self.Imaging_DataRecording_right_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_DataRecording_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.Imaging_DataRecording_right_frame)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.Imaging_DataRecording_directory_frame = QFrame(self.Imaging_DataRecording_right_frame)
        self.Imaging_DataRecording_directory_frame.setObjectName(u"Imaging_DataRecording_directory_frame")
        self.Imaging_DataRecording_directory_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_DataRecording_directory_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_423 = QHBoxLayout(self.Imaging_DataRecording_directory_frame)
        self.horizontalLayout_423.setSpacing(10)
        self.horizontalLayout_423.setObjectName(u"horizontalLayout_423")
        self.horizontalLayout_423.setContentsMargins(0, 0, 0, 0)
        self.Imaging_DataRecording_SelectRecordFolder_label_ = QLabel(self.Imaging_DataRecording_directory_frame)
        self.Imaging_DataRecording_SelectRecordFolder_label_.setObjectName(u"Imaging_DataRecording_SelectRecordFolder_label_")

        self.horizontalLayout_423.addWidget(self.Imaging_DataRecording_SelectRecordFolder_label_)

        self.Imaging_DataRecording_RecordFolder_value = QLineEdit(self.Imaging_DataRecording_directory_frame)
        self.Imaging_DataRecording_RecordFolder_value.setObjectName(u"Imaging_DataRecording_RecordFolder_value")
        self.Imaging_DataRecording_RecordFolder_value.setEnabled(False)

        self.horizontalLayout_423.addWidget(self.Imaging_DataRecording_RecordFolder_value)

        self.Imaging_DataRecording_RecordFolderDir_pushButton = QPushButton(self.Imaging_DataRecording_directory_frame)
        self.Imaging_DataRecording_RecordFolderDir_pushButton.setObjectName(u"Imaging_DataRecording_RecordFolderDir_pushButton")
        self.Imaging_DataRecording_RecordFolderDir_pushButton.setMinimumSize(QSize(150, 0))
        self.Imaging_DataRecording_RecordFolderDir_pushButton.setFont(font4)

        self.horizontalLayout_423.addWidget(self.Imaging_DataRecording_RecordFolderDir_pushButton)


        self.verticalLayout_106.addWidget(self.Imaging_DataRecording_directory_frame)

        self.Imaging_DataRecording_record_frame = QFrame(self.Imaging_DataRecording_right_frame)
        self.Imaging_DataRecording_record_frame.setObjectName(u"Imaging_DataRecording_record_frame")
        self.Imaging_DataRecording_record_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_DataRecording_record_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_424 = QHBoxLayout(self.Imaging_DataRecording_record_frame)
        self.horizontalLayout_424.setSpacing(0)
        self.horizontalLayout_424.setObjectName(u"horizontalLayout_424")
        self.horizontalLayout_424.setContentsMargins(0, 0, 0, 0)
        self.Imaging_SelectedFolderLabel = QLabel(self.Imaging_DataRecording_record_frame)
        self.Imaging_SelectedFolderLabel.setObjectName(u"Imaging_SelectedFolderLabel")
        sizePolicy3.setHeightForWidth(self.Imaging_SelectedFolderLabel.sizePolicy().hasHeightForWidth())
        self.Imaging_SelectedFolderLabel.setSizePolicy(sizePolicy3)
        self.Imaging_SelectedFolderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_424.addWidget(self.Imaging_SelectedFolderLabel)

        self.Imaging_DataRecording_Record_pushButton = QPushButton(self.Imaging_DataRecording_record_frame)
        self.Imaging_DataRecording_Record_pushButton.setObjectName(u"Imaging_DataRecording_Record_pushButton")
        sizePolicy6.setHeightForWidth(self.Imaging_DataRecording_Record_pushButton.sizePolicy().hasHeightForWidth())
        self.Imaging_DataRecording_Record_pushButton.setSizePolicy(sizePolicy6)
        self.Imaging_DataRecording_Record_pushButton.setMinimumSize(QSize(150, 0))
        self.Imaging_DataRecording_Record_pushButton.setFont(font5)
        self.Imaging_DataRecording_Record_pushButton.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"background-color: rgb(220, 50, 47);")

        self.horizontalLayout_424.addWidget(self.Imaging_DataRecording_Record_pushButton)


        self.verticalLayout_106.addWidget(self.Imaging_DataRecording_record_frame)


        self.horizontalLayout_114.addWidget(self.Imaging_DataRecording_right_frame)


        self.verticalLayout_109.addWidget(self.Imaging_DataRecording_box)


        self.horizontalLayout_70.addWidget(self.Imaging_widget)

        self.line_43 = QFrame(self.page_201)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

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
        self.Imaging_ImagingParameter_page = QWidget()
        self.Imaging_ImagingParameter_page.setObjectName(u"Imaging_ImagingParameter_page")
        self.verticalLayout_131 = QVBoxLayout(self.Imaging_ImagingParameter_page)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_frame = QFrame(self.Imaging_ImagingParameter_page)
        self.Imaging_GECI_frame.setObjectName(u"Imaging_GECI_frame")
        self.Imaging_GECI_frame.setMaximumSize(QSize(16777215, 16777215))
        self.Imaging_GECI_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.Imaging_GECI_frame)
        self.verticalLayout_82.setSpacing(10)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(5, 10, 5, 10)
        self.Imaging_GECI_Label_frame = QFrame(self.Imaging_GECI_frame)
        self.Imaging_GECI_Label_frame.setObjectName(u"Imaging_GECI_Label_frame")
        self.Imaging_GECI_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.Imaging_GECI_Label_frame)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_Label = QLabel(self.Imaging_GECI_Label_frame)
        self.Imaging_GECI_Label.setObjectName(u"Imaging_GECI_Label")
        self.Imaging_GECI_Label.setFont(font1)
        self.Imaging_GECI_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.Imaging_GECI_Label)


        self.verticalLayout_82.addWidget(self.Imaging_GECI_Label_frame)

        self.Imaging_GECI_comboBox_frame = QFrame(self.Imaging_GECI_frame)
        self.Imaging_GECI_comboBox_frame.setObjectName(u"Imaging_GECI_comboBox_frame")
        self.Imaging_GECI_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.Imaging_GECI_comboBox_frame)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_comboBox = QComboBox(self.Imaging_GECI_comboBox_frame)
        self.Imaging_GECI_comboBox.addItem("")
        self.Imaging_GECI_comboBox.addItem("")
        self.Imaging_GECI_comboBox.addItem("")
        self.Imaging_GECI_comboBox.addItem("")
        self.Imaging_GECI_comboBox.setObjectName(u"Imaging_GECI_comboBox")

        self.horizontalLayout_123.addWidget(self.Imaging_GECI_comboBox)


        self.verticalLayout_82.addWidget(self.Imaging_GECI_comboBox_frame)

        self.Imaging_GECI_Readings_frame = QFrame(self.Imaging_GECI_frame)
        self.Imaging_GECI_Readings_frame.setObjectName(u"Imaging_GECI_Readings_frame")
        self.Imaging_GECI_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_Readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.Imaging_GECI_Readings_frame)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_ReadingsAffinity_frame = QFrame(self.Imaging_GECI_Readings_frame)
        self.Imaging_GECI_ReadingsAffinity_frame.setObjectName(u"Imaging_GECI_ReadingsAffinity_frame")
        self.Imaging_GECI_ReadingsAffinity_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_ReadingsAffinity_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.Imaging_GECI_ReadingsAffinity_frame)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_ReadingsAffinity_Label = QLabel(self.Imaging_GECI_ReadingsAffinity_frame)
        self.Imaging_GECI_ReadingsAffinity_Label.setObjectName(u"Imaging_GECI_ReadingsAffinity_Label")
        font8 = QFont()
        font8.setPointSize(8)
        self.Imaging_GECI_ReadingsAffinity_Label.setFont(font8)

        self.horizontalLayout_121.addWidget(self.Imaging_GECI_ReadingsAffinity_Label)

        self.Imaging_GECI_ReadingsAffinity_Value = QLabel(self.Imaging_GECI_ReadingsAffinity_frame)
        self.Imaging_GECI_ReadingsAffinity_Value.setObjectName(u"Imaging_GECI_ReadingsAffinity_Value")
        self.Imaging_GECI_ReadingsAffinity_Value.setFont(font8)
        self.Imaging_GECI_ReadingsAffinity_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_121.addWidget(self.Imaging_GECI_ReadingsAffinity_Value)


        self.verticalLayout_83.addWidget(self.Imaging_GECI_ReadingsAffinity_frame)

        self.Imaging_GECI_ReadingsKd_frame = QFrame(self.Imaging_GECI_Readings_frame)
        self.Imaging_GECI_ReadingsKd_frame.setObjectName(u"Imaging_GECI_ReadingsKd_frame")
        self.Imaging_GECI_ReadingsKd_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_ReadingsKd_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.Imaging_GECI_ReadingsKd_frame)
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_ReadingsKd_Label = QLabel(self.Imaging_GECI_ReadingsKd_frame)
        self.Imaging_GECI_ReadingsKd_Label.setObjectName(u"Imaging_GECI_ReadingsKd_Label")
        self.Imaging_GECI_ReadingsKd_Label.setFont(font8)

        self.horizontalLayout_144.addWidget(self.Imaging_GECI_ReadingsKd_Label)

        self.Imaging_GECI_ReadingsKd_Value = QLabel(self.Imaging_GECI_ReadingsKd_frame)
        self.Imaging_GECI_ReadingsKd_Value.setObjectName(u"Imaging_GECI_ReadingsKd_Value")
        self.Imaging_GECI_ReadingsKd_Value.setFont(font8)
        self.Imaging_GECI_ReadingsKd_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_144.addWidget(self.Imaging_GECI_ReadingsKd_Value)


        self.verticalLayout_83.addWidget(self.Imaging_GECI_ReadingsKd_frame)

        self.Imaging_GECI_ReadingsBrightness_frame = QFrame(self.Imaging_GECI_Readings_frame)
        self.Imaging_GECI_ReadingsBrightness_frame.setObjectName(u"Imaging_GECI_ReadingsBrightness_frame")
        self.Imaging_GECI_ReadingsBrightness_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_GECI_ReadingsBrightness_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.Imaging_GECI_ReadingsBrightness_frame)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.Imaging_GECI_ReadingsBrightness_Label = QLabel(self.Imaging_GECI_ReadingsBrightness_frame)
        self.Imaging_GECI_ReadingsBrightness_Label.setObjectName(u"Imaging_GECI_ReadingsBrightness_Label")
        self.Imaging_GECI_ReadingsBrightness_Label.setFont(font8)

        self.horizontalLayout_140.addWidget(self.Imaging_GECI_ReadingsBrightness_Label)

        self.Imaging_GECI_ReadingsBrightness_Value = QLabel(self.Imaging_GECI_ReadingsBrightness_frame)
        self.Imaging_GECI_ReadingsBrightness_Value.setObjectName(u"Imaging_GECI_ReadingsBrightness_Value")
        self.Imaging_GECI_ReadingsBrightness_Value.setFont(font8)
        self.Imaging_GECI_ReadingsBrightness_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_140.addWidget(self.Imaging_GECI_ReadingsBrightness_Value)


        self.verticalLayout_83.addWidget(self.Imaging_GECI_ReadingsBrightness_frame)


        self.verticalLayout_82.addWidget(self.Imaging_GECI_Readings_frame)


        self.verticalLayout_131.addWidget(self.Imaging_GECI_frame)

        self.line_49 = QFrame(self.Imaging_ImagingParameter_page)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_49.setFrameShape(QFrame.Shape.HLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_49)

        self.Imaging_FrameRate_frame = QFrame(self.Imaging_ImagingParameter_page)
        self.Imaging_FrameRate_frame.setObjectName(u"Imaging_FrameRate_frame")
        self.Imaging_FrameRate_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.Imaging_FrameRate_frame)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(5, 0, 5, 0)
        self.Imaging_FrameRate_Title_frame = QFrame(self.Imaging_FrameRate_frame)
        self.Imaging_FrameRate_Title_frame.setObjectName(u"Imaging_FrameRate_Title_frame")
        self.Imaging_FrameRate_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.Imaging_FrameRate_Title_frame)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FrameRate_Toggle_frame = QFrame(self.Imaging_FrameRate_Title_frame)
        self.Imaging_FrameRate_Toggle_frame.setObjectName(u"Imaging_FrameRate_Toggle_frame")
        self.Imaging_FrameRate_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.Imaging_FrameRate_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_FrameRate_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FrameRate_Toggle_layout = QHBoxLayout(self.Imaging_FrameRate_Toggle_frame)
        self.Imaging_FrameRate_Toggle_layout.setSpacing(0)
        self.Imaging_FrameRate_Toggle_layout.setObjectName(u"Imaging_FrameRate_Toggle_layout")
        self.Imaging_FrameRate_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_128.addWidget(self.Imaging_FrameRate_Toggle_frame)

        self.Imaging_FrameRate_Label_frame = QFrame(self.Imaging_FrameRate_Title_frame)
        self.Imaging_FrameRate_Label_frame.setObjectName(u"Imaging_FrameRate_Label_frame")
        self.Imaging_FrameRate_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.Imaging_FrameRate_Label_frame)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FrameRate_Label = QLabel(self.Imaging_FrameRate_Label_frame)
        self.Imaging_FrameRate_Label.setObjectName(u"Imaging_FrameRate_Label")
        self.Imaging_FrameRate_Label.setWordWrap(True)

        self.horizontalLayout_129.addWidget(self.Imaging_FrameRate_Label)


        self.horizontalLayout_128.addWidget(self.Imaging_FrameRate_Label_frame)


        self.verticalLayout_130.addWidget(self.Imaging_FrameRate_Title_frame)

        self.Imaging_FrameRate_Readings_frame = QFrame(self.Imaging_FrameRate_frame)
        self.Imaging_FrameRate_Readings_frame.setObjectName(u"Imaging_FrameRate_Readings_frame")
        self.Imaging_FrameRate_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.Imaging_FrameRate_Readings_frame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FrameRate_Readings = QLabel(self.Imaging_FrameRate_Readings_frame)
        self.Imaging_FrameRate_Readings.setObjectName(u"Imaging_FrameRate_Readings")
        self.Imaging_FrameRate_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.Imaging_FrameRate_Readings)


        self.verticalLayout_130.addWidget(self.Imaging_FrameRate_Readings_frame)

        self.Imaging_FrameRate_Slider_frame = QFrame(self.Imaging_FrameRate_frame)
        self.Imaging_FrameRate_Slider_frame.setObjectName(u"Imaging_FrameRate_Slider_frame")
        self.Imaging_FrameRate_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Slider_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FrameRate_toggle_layout = QHBoxLayout(self.Imaging_FrameRate_Slider_frame)
        self.Imaging_FrameRate_toggle_layout.setSpacing(0)
        self.Imaging_FrameRate_toggle_layout.setObjectName(u"Imaging_FrameRate_toggle_layout")
        self.Imaging_FrameRate_toggle_layout.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FrameRate_Slider = QSlider(self.Imaging_FrameRate_Slider_frame)
        self.Imaging_FrameRate_Slider.setObjectName(u"Imaging_FrameRate_Slider")
        self.Imaging_FrameRate_Slider.setEnabled(False)
        self.Imaging_FrameRate_Slider.setMinimum(1)
        self.Imaging_FrameRate_Slider.setMaximum(1000)
        self.Imaging_FrameRate_Slider.setSingleStep(10)
        self.Imaging_FrameRate_Slider.setValue(250)
        self.Imaging_FrameRate_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_FrameRate_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_FrameRate_Slider.setTickInterval(100)

        self.Imaging_FrameRate_toggle_layout.addWidget(self.Imaging_FrameRate_Slider)


        self.verticalLayout_130.addWidget(self.Imaging_FrameRate_Slider_frame)

        self.Imaging_FrameRate_Values_frame = QFrame(self.Imaging_FrameRate_frame)
        self.Imaging_FrameRate_Values_frame.setObjectName(u"Imaging_FrameRate_Values_frame")
        self.Imaging_FrameRate_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FrameRate_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.Imaging_FrameRate_Values_frame)
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.Imaging_FrameRate_Values_frame)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_145.addWidget(self.label_39)

        self.label_34 = QLabel(self.Imaging_FrameRate_Values_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.label_34)

        self.label_35 = QLabel(self.Imaging_FrameRate_Values_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_145.addWidget(self.label_35)


        self.verticalLayout_130.addWidget(self.Imaging_FrameRate_Values_frame)


        self.verticalLayout_131.addWidget(self.Imaging_FrameRate_frame)

        self.line_50 = QFrame(self.Imaging_ImagingParameter_page)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_50.setFrameShape(QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_50)

        self.Imaging_PMT_frame = QFrame(self.Imaging_ImagingParameter_page)
        self.Imaging_PMT_frame.setObjectName(u"Imaging_PMT_frame")
        self.Imaging_PMT_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.Imaging_PMT_frame)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(5, 0, 5, 0)
        self.Imaging_PMT_Title_frame = QFrame(self.Imaging_PMT_frame)
        self.Imaging_PMT_Title_frame.setObjectName(u"Imaging_PMT_Title_frame")
        self.Imaging_PMT_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.Imaging_PMT_Title_frame)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PMT_Toggle_frame = QFrame(self.Imaging_PMT_Title_frame)
        self.Imaging_PMT_Toggle_frame.setObjectName(u"Imaging_PMT_Toggle_frame")
        self.Imaging_PMT_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.Imaging_PMT_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_PMT_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_PMT_Toggle_layout = QHBoxLayout(self.Imaging_PMT_Toggle_frame)
        self.Imaging_PMT_Toggle_layout.setSpacing(0)
        self.Imaging_PMT_Toggle_layout.setObjectName(u"Imaging_PMT_Toggle_layout")
        self.Imaging_PMT_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_55.addWidget(self.Imaging_PMT_Toggle_frame)

        self.Imaging_PMT_Label_frame = QFrame(self.Imaging_PMT_Title_frame)
        self.Imaging_PMT_Label_frame.setObjectName(u"Imaging_PMT_Label_frame")
        self.Imaging_PMT_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.Imaging_PMT_Label_frame)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PMT_Label = QLabel(self.Imaging_PMT_Label_frame)
        self.Imaging_PMT_Label.setObjectName(u"Imaging_PMT_Label")
        self.Imaging_PMT_Label.setWordWrap(True)

        self.horizontalLayout_131.addWidget(self.Imaging_PMT_Label)


        self.horizontalLayout_55.addWidget(self.Imaging_PMT_Label_frame)


        self.verticalLayout_132.addWidget(self.Imaging_PMT_Title_frame)

        self.Imaging_PMT_Readings_frame = QFrame(self.Imaging_PMT_frame)
        self.Imaging_PMT_Readings_frame.setObjectName(u"Imaging_PMT_Readings_frame")
        self.Imaging_PMT_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_175 = QHBoxLayout(self.Imaging_PMT_Readings_frame)
        self.horizontalLayout_175.setSpacing(0)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PMT_Readings = QLabel(self.Imaging_PMT_Readings_frame)
        self.Imaging_PMT_Readings.setObjectName(u"Imaging_PMT_Readings")
        self.Imaging_PMT_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_175.addWidget(self.Imaging_PMT_Readings)


        self.verticalLayout_132.addWidget(self.Imaging_PMT_Readings_frame)

        self.Imaging_PMT_Slider_frame = QFrame(self.Imaging_PMT_frame)
        self.Imaging_PMT_Slider_frame.setObjectName(u"Imaging_PMT_Slider_frame")
        self.Imaging_PMT_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.Imaging_PMT_Slider_frame)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PMT_Slider = QSlider(self.Imaging_PMT_Slider_frame)
        self.Imaging_PMT_Slider.setObjectName(u"Imaging_PMT_Slider")
        self.Imaging_PMT_Slider.setEnabled(False)
        self.Imaging_PMT_Slider.setMaximum(200)
        self.Imaging_PMT_Slider.setValue(100)
        self.Imaging_PMT_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_PMT_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PMT_Slider.setTickInterval(20)

        self.horizontalLayout_116.addWidget(self.Imaging_PMT_Slider)


        self.verticalLayout_132.addWidget(self.Imaging_PMT_Slider_frame)

        self.Imaging_PMT_Values_frame = QFrame(self.Imaging_PMT_frame)
        self.Imaging_PMT_Values_frame.setObjectName(u"Imaging_PMT_Values_frame")
        self.Imaging_PMT_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PMT_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.Imaging_PMT_Values_frame)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.Imaging_PMT_Values_frame)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_146.addWidget(self.label_40)

        self.label_41 = QLabel(self.Imaging_PMT_Values_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_146.addWidget(self.label_41)

        self.label_42 = QLabel(self.Imaging_PMT_Values_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_146.addWidget(self.label_42)


        self.verticalLayout_132.addWidget(self.Imaging_PMT_Values_frame)


        self.verticalLayout_131.addWidget(self.Imaging_PMT_frame)

        self.line_51 = QFrame(self.Imaging_ImagingParameter_page)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_51)

        self.Imaging_Laser_frame = QFrame(self.Imaging_ImagingParameter_page)
        self.Imaging_Laser_frame.setObjectName(u"Imaging_Laser_frame")
        self.Imaging_Laser_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.Imaging_Laser_frame)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(5, 0, 5, 0)
        self.Imaging_Laser_Title_frame = QFrame(self.Imaging_Laser_frame)
        self.Imaging_Laser_Title_frame.setObjectName(u"Imaging_Laser_Title_frame")
        self.Imaging_Laser_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_272 = QHBoxLayout(self.Imaging_Laser_Title_frame)
        self.horizontalLayout_272.setSpacing(0)
        self.horizontalLayout_272.setObjectName(u"horizontalLayout_272")
        self.horizontalLayout_272.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Laser_Toggle_frame = QFrame(self.Imaging_Laser_Title_frame)
        self.Imaging_Laser_Toggle_frame.setObjectName(u"Imaging_Laser_Toggle_frame")
        self.Imaging_Laser_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.Imaging_Laser_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_Laser_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_Laser_Toggle_layout = QHBoxLayout(self.Imaging_Laser_Toggle_frame)
        self.Imaging_Laser_Toggle_layout.setSpacing(0)
        self.Imaging_Laser_Toggle_layout.setObjectName(u"Imaging_Laser_Toggle_layout")
        self.Imaging_Laser_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_272.addWidget(self.Imaging_Laser_Toggle_frame)

        self.Imaging_Laser_Label_frame = QFrame(self.Imaging_Laser_Title_frame)
        self.Imaging_Laser_Label_frame.setObjectName(u"Imaging_Laser_Label_frame")
        self.Imaging_Laser_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.Imaging_Laser_Label_frame)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Laser_Label = QLabel(self.Imaging_Laser_Label_frame)
        self.Imaging_Laser_Label.setObjectName(u"Imaging_Laser_Label")
        self.Imaging_Laser_Label.setWordWrap(True)

        self.horizontalLayout_135.addWidget(self.Imaging_Laser_Label)


        self.horizontalLayout_272.addWidget(self.Imaging_Laser_Label_frame)


        self.verticalLayout_133.addWidget(self.Imaging_Laser_Title_frame)

        self.Imaging_Laser_Readings_frame = QFrame(self.Imaging_Laser_frame)
        self.Imaging_Laser_Readings_frame.setObjectName(u"Imaging_Laser_Readings_frame")
        self.Imaging_Laser_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.Imaging_Laser_Readings_frame)
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Laser_Readings = QLabel(self.Imaging_Laser_Readings_frame)
        self.Imaging_Laser_Readings.setObjectName(u"Imaging_Laser_Readings")
        self.Imaging_Laser_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_177.addWidget(self.Imaging_Laser_Readings)


        self.verticalLayout_133.addWidget(self.Imaging_Laser_Readings_frame)

        self.Imaging_Laser_Slider_frame = QFrame(self.Imaging_Laser_frame)
        self.Imaging_Laser_Slider_frame.setObjectName(u"Imaging_Laser_Slider_frame")
        self.Imaging_Laser_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Laser_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.Imaging_Laser_Slider_frame)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Laser_Slider = QSlider(self.Imaging_Laser_Slider_frame)
        self.Imaging_Laser_Slider.setObjectName(u"Imaging_Laser_Slider")
        self.Imaging_Laser_Slider.setEnabled(False)
        self.Imaging_Laser_Slider.setMaximum(200)
        self.Imaging_Laser_Slider.setValue(100)
        self.Imaging_Laser_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_Laser_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Laser_Slider.setTickInterval(20)

        self.horizontalLayout_176.addWidget(self.Imaging_Laser_Slider)


        self.verticalLayout_133.addWidget(self.Imaging_Laser_Slider_frame)

        self.frame_3 = QFrame(self.Imaging_Laser_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_3)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_147.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_147.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_147.addWidget(self.label_45)


        self.verticalLayout_133.addWidget(self.frame_3)


        self.verticalLayout_131.addWidget(self.Imaging_Laser_frame)

        self.Imaging_parameter_stackedWidget.addWidget(self.Imaging_ImagingParameter_page)
        self.Imaging_CalciumParameter_page = QWidget()
        self.Imaging_CalciumParameter_page.setObjectName(u"Imaging_CalciumParameter_page")
        self.verticalLayout_137 = QVBoxLayout(self.Imaging_CalciumParameter_page)
        self.verticalLayout_137.setSpacing(5)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 5, 0, 5)
        self.Imaging_CalciumDecay_frame = QFrame(self.Imaging_CalciumParameter_page)
        self.Imaging_CalciumDecay_frame.setObjectName(u"Imaging_CalciumDecay_frame")
        self.Imaging_CalciumDecay_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.Imaging_CalciumDecay_frame)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(5, 0, 5, 0)
        self.Imaging_CalciumDecay_Title_frame = QFrame(self.Imaging_CalciumDecay_frame)
        self.Imaging_CalciumDecay_Title_frame.setObjectName(u"Imaging_CalciumDecay_Title_frame")
        self.Imaging_CalciumDecay_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_278 = QHBoxLayout(self.Imaging_CalciumDecay_Title_frame)
        self.horizontalLayout_278.setSpacing(0)
        self.horizontalLayout_278.setObjectName(u"horizontalLayout_278")
        self.horizontalLayout_278.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumDecay_Toggle_frame = QFrame(self.Imaging_CalciumDecay_Title_frame)
        self.Imaging_CalciumDecay_Toggle_frame.setObjectName(u"Imaging_CalciumDecay_Toggle_frame")
        self.Imaging_CalciumDecay_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_CalciumDecay_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_CalciumDecay_Toggle_layout = QHBoxLayout(self.Imaging_CalciumDecay_Toggle_frame)
        self.Imaging_CalciumDecay_Toggle_layout.setSpacing(0)
        self.Imaging_CalciumDecay_Toggle_layout.setObjectName(u"Imaging_CalciumDecay_Toggle_layout")
        self.Imaging_CalciumDecay_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_278.addWidget(self.Imaging_CalciumDecay_Toggle_frame)

        self.Imaging_CalciumDecay_Label_frame = QFrame(self.Imaging_CalciumDecay_Title_frame)
        self.Imaging_CalciumDecay_Label_frame.setObjectName(u"Imaging_CalciumDecay_Label_frame")
        self.Imaging_CalciumDecay_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.Imaging_CalciumDecay_Label_frame)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumDecay_Label = QLabel(self.Imaging_CalciumDecay_Label_frame)
        self.Imaging_CalciumDecay_Label.setObjectName(u"Imaging_CalciumDecay_Label")
        self.Imaging_CalciumDecay_Label.setWordWrap(True)

        self.horizontalLayout_71.addWidget(self.Imaging_CalciumDecay_Label)


        self.horizontalLayout_278.addWidget(self.Imaging_CalciumDecay_Label_frame)


        self.verticalLayout_135.addWidget(self.Imaging_CalciumDecay_Title_frame)

        self.Imaging_CalciumDecay_Readings_frame = QFrame(self.Imaging_CalciumDecay_frame)
        self.Imaging_CalciumDecay_Readings_frame.setObjectName(u"Imaging_CalciumDecay_Readings_frame")
        self.Imaging_CalciumDecay_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_277 = QHBoxLayout(self.Imaging_CalciumDecay_Readings_frame)
        self.horizontalLayout_277.setSpacing(0)
        self.horizontalLayout_277.setObjectName(u"horizontalLayout_277")
        self.horizontalLayout_277.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumDecay_Readings = QLabel(self.Imaging_CalciumDecay_Readings_frame)
        self.Imaging_CalciumDecay_Readings.setObjectName(u"Imaging_CalciumDecay_Readings")
        self.Imaging_CalciumDecay_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_277.addWidget(self.Imaging_CalciumDecay_Readings)


        self.verticalLayout_135.addWidget(self.Imaging_CalciumDecay_Readings_frame)

        self.Imaging_CalciumDecay_Slider_frame = QFrame(self.Imaging_CalciumDecay_frame)
        self.Imaging_CalciumDecay_Slider_frame.setObjectName(u"Imaging_CalciumDecay_Slider_frame")
        self.Imaging_CalciumDecay_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumDecay_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_276 = QHBoxLayout(self.Imaging_CalciumDecay_Slider_frame)
        self.horizontalLayout_276.setSpacing(0)
        self.horizontalLayout_276.setObjectName(u"horizontalLayout_276")
        self.horizontalLayout_276.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumDecay_Slider = QSlider(self.Imaging_CalciumDecay_Slider_frame)
        self.Imaging_CalciumDecay_Slider.setObjectName(u"Imaging_CalciumDecay_Slider")
        self.Imaging_CalciumDecay_Slider.setEnabled(False)
        self.Imaging_CalciumDecay_Slider.setMinimum(1)
        self.Imaging_CalciumDecay_Slider.setMaximum(200)
        self.Imaging_CalciumDecay_Slider.setValue(50)
        self.Imaging_CalciumDecay_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_CalciumDecay_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_CalciumDecay_Slider.setTickInterval(20)

        self.horizontalLayout_276.addWidget(self.Imaging_CalciumDecay_Slider)


        self.verticalLayout_135.addWidget(self.Imaging_CalciumDecay_Slider_frame)

        self.frame_4 = QFrame(self.Imaging_CalciumDecay_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.label_55 = QLabel(self.frame_4)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_151.addWidget(self.label_55)

        self.label_56 = QLabel(self.frame_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_151.addWidget(self.label_56)

        self.label_57 = QLabel(self.frame_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_151.addWidget(self.label_57)


        self.verticalLayout_135.addWidget(self.frame_4)


        self.verticalLayout_137.addWidget(self.Imaging_CalciumDecay_frame)

        self.line_52 = QFrame(self.Imaging_CalciumParameter_page)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_52.setFrameShape(QFrame.Shape.HLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_137.addWidget(self.line_52)

        self.Imaging_CalciumJump_frame = QFrame(self.Imaging_CalciumParameter_page)
        self.Imaging_CalciumJump_frame.setObjectName(u"Imaging_CalciumJump_frame")
        self.Imaging_CalciumJump_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.Imaging_CalciumJump_frame)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(5, 0, 5, 0)
        self.Imaging_CalciumJump_Title_frame = QFrame(self.Imaging_CalciumJump_frame)
        self.Imaging_CalciumJump_Title_frame.setObjectName(u"Imaging_CalciumJump_Title_frame")
        self.Imaging_CalciumJump_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_281 = QHBoxLayout(self.Imaging_CalciumJump_Title_frame)
        self.horizontalLayout_281.setSpacing(0)
        self.horizontalLayout_281.setObjectName(u"horizontalLayout_281")
        self.horizontalLayout_281.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumJump_Toggle_frame = QFrame(self.Imaging_CalciumJump_Title_frame)
        self.Imaging_CalciumJump_Toggle_frame.setObjectName(u"Imaging_CalciumJump_Toggle_frame")
        self.Imaging_CalciumJump_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_CalciumJump_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_CalciumJump_Toggle_layout = QHBoxLayout(self.Imaging_CalciumJump_Toggle_frame)
        self.Imaging_CalciumJump_Toggle_layout.setSpacing(0)
        self.Imaging_CalciumJump_Toggle_layout.setObjectName(u"Imaging_CalciumJump_Toggle_layout")
        self.Imaging_CalciumJump_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_281.addWidget(self.Imaging_CalciumJump_Toggle_frame)

        self.Imaging_CalciumJump_Label_frame = QFrame(self.Imaging_CalciumJump_Title_frame)
        self.Imaging_CalciumJump_Label_frame.setObjectName(u"Imaging_CalciumJump_Label_frame")
        self.Imaging_CalciumJump_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.Imaging_CalciumJump_Label_frame)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumJump_Label = QLabel(self.Imaging_CalciumJump_Label_frame)
        self.Imaging_CalciumJump_Label.setObjectName(u"Imaging_CalciumJump_Label")
        self.Imaging_CalciumJump_Label.setWordWrap(True)

        self.horizontalLayout_122.addWidget(self.Imaging_CalciumJump_Label)


        self.horizontalLayout_281.addWidget(self.Imaging_CalciumJump_Label_frame)


        self.verticalLayout_136.addWidget(self.Imaging_CalciumJump_Title_frame)

        self.Imaging_CalciumJump_Readings_frame = QFrame(self.Imaging_CalciumJump_frame)
        self.Imaging_CalciumJump_Readings_frame.setObjectName(u"Imaging_CalciumJump_Readings_frame")
        self.Imaging_CalciumJump_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_280 = QHBoxLayout(self.Imaging_CalciumJump_Readings_frame)
        self.horizontalLayout_280.setSpacing(0)
        self.horizontalLayout_280.setObjectName(u"horizontalLayout_280")
        self.horizontalLayout_280.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumJump_Readings = QLabel(self.Imaging_CalciumJump_Readings_frame)
        self.Imaging_CalciumJump_Readings.setObjectName(u"Imaging_CalciumJump_Readings")
        self.Imaging_CalciumJump_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_280.addWidget(self.Imaging_CalciumJump_Readings)


        self.verticalLayout_136.addWidget(self.Imaging_CalciumJump_Readings_frame)

        self.Imaging_CalciumJump_Slider_frame = QFrame(self.Imaging_CalciumJump_frame)
        self.Imaging_CalciumJump_Slider_frame.setObjectName(u"Imaging_CalciumJump_Slider_frame")
        self.Imaging_CalciumJump_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_279 = QHBoxLayout(self.Imaging_CalciumJump_Slider_frame)
        self.horizontalLayout_279.setSpacing(0)
        self.horizontalLayout_279.setObjectName(u"horizontalLayout_279")
        self.horizontalLayout_279.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumJump_Slider = QSlider(self.Imaging_CalciumJump_Slider_frame)
        self.Imaging_CalciumJump_Slider.setObjectName(u"Imaging_CalciumJump_Slider")
        self.Imaging_CalciumJump_Slider.setEnabled(False)
        self.Imaging_CalciumJump_Slider.setMinimum(1)
        self.Imaging_CalciumJump_Slider.setMaximum(50)
        self.Imaging_CalciumJump_Slider.setValue(5)
        self.Imaging_CalciumJump_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_CalciumJump_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_CalciumJump_Slider.setTickInterval(5)

        self.horizontalLayout_279.addWidget(self.Imaging_CalciumJump_Slider)


        self.verticalLayout_136.addWidget(self.Imaging_CalciumJump_Slider_frame)

        self.Imaging_CalciumJump_Values_frame = QFrame(self.Imaging_CalciumJump_frame)
        self.Imaging_CalciumJump_Values_frame.setObjectName(u"Imaging_CalciumJump_Values_frame")
        self.Imaging_CalciumJump_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumJump_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.Imaging_CalciumJump_Values_frame)
        self.horizontalLayout_150.setSpacing(0)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.Imaging_CalciumJump_Values_frame)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_150.addWidget(self.label_52)

        self.label_53 = QLabel(self.Imaging_CalciumJump_Values_frame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_150.addWidget(self.label_53)

        self.label_54 = QLabel(self.Imaging_CalciumJump_Values_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_150.addWidget(self.label_54)


        self.verticalLayout_136.addWidget(self.Imaging_CalciumJump_Values_frame)


        self.verticalLayout_137.addWidget(self.Imaging_CalciumJump_frame)

        self.line_53 = QFrame(self.Imaging_CalciumParameter_page)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_53.setFrameShape(QFrame.Shape.HLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_137.addWidget(self.line_53)

        self.Imaging_CalciumNoise_frame = QFrame(self.Imaging_CalciumParameter_page)
        self.Imaging_CalciumNoise_frame.setObjectName(u"Imaging_CalciumNoise_frame")
        self.Imaging_CalciumNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.Imaging_CalciumNoise_frame)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(5, 0, 5, 0)
        self.Imaging_CalciumNoise_Title_frame = QFrame(self.Imaging_CalciumNoise_frame)
        self.Imaging_CalciumNoise_Title_frame.setObjectName(u"Imaging_CalciumNoise_Title_frame")
        self.Imaging_CalciumNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_275 = QHBoxLayout(self.Imaging_CalciumNoise_Title_frame)
        self.horizontalLayout_275.setSpacing(0)
        self.horizontalLayout_275.setObjectName(u"horizontalLayout_275")
        self.horizontalLayout_275.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumNoise_Toggle_frame = QFrame(self.Imaging_CalciumNoise_Title_frame)
        self.Imaging_CalciumNoise_Toggle_frame.setObjectName(u"Imaging_CalciumNoise_Toggle_frame")
        self.Imaging_CalciumNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_CalciumNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_CalciumNoise_Toggle_layout = QHBoxLayout(self.Imaging_CalciumNoise_Toggle_frame)
        self.Imaging_CalciumNoise_Toggle_layout.setSpacing(0)
        self.Imaging_CalciumNoise_Toggle_layout.setObjectName(u"Imaging_CalciumNoise_Toggle_layout")
        self.Imaging_CalciumNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_275.addWidget(self.Imaging_CalciumNoise_Toggle_frame)

        self.Imaging_CalciumNoise_Label_frame = QFrame(self.Imaging_CalciumNoise_Title_frame)
        self.Imaging_CalciumNoise_Label_frame.setObjectName(u"Imaging_CalciumNoise_Label_frame")
        self.Imaging_CalciumNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.Imaging_CalciumNoise_Label_frame)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumNoise_Label = QLabel(self.Imaging_CalciumNoise_Label_frame)
        self.Imaging_CalciumNoise_Label.setObjectName(u"Imaging_CalciumNoise_Label")

        self.horizontalLayout_124.addWidget(self.Imaging_CalciumNoise_Label)


        self.horizontalLayout_275.addWidget(self.Imaging_CalciumNoise_Label_frame)


        self.verticalLayout_134.addWidget(self.Imaging_CalciumNoise_Title_frame)

        self.Imaging_CalciumNoise_Readings_frame = QFrame(self.Imaging_CalciumNoise_frame)
        self.Imaging_CalciumNoise_Readings_frame.setObjectName(u"Imaging_CalciumNoise_Readings_frame")
        self.Imaging_CalciumNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_274 = QHBoxLayout(self.Imaging_CalciumNoise_Readings_frame)
        self.horizontalLayout_274.setSpacing(0)
        self.horizontalLayout_274.setObjectName(u"horizontalLayout_274")
        self.horizontalLayout_274.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumNoise_Readings = QLabel(self.Imaging_CalciumNoise_Readings_frame)
        self.Imaging_CalciumNoise_Readings.setObjectName(u"Imaging_CalciumNoise_Readings")
        self.Imaging_CalciumNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_274.addWidget(self.Imaging_CalciumNoise_Readings)


        self.verticalLayout_134.addWidget(self.Imaging_CalciumNoise_Readings_frame)

        self.Imaging_CalciumNoise_Slider_frame = QFrame(self.Imaging_CalciumNoise_frame)
        self.Imaging_CalciumNoise_Slider_frame.setObjectName(u"Imaging_CalciumNoise_Slider_frame")
        self.Imaging_CalciumNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_273 = QHBoxLayout(self.Imaging_CalciumNoise_Slider_frame)
        self.horizontalLayout_273.setSpacing(0)
        self.horizontalLayout_273.setObjectName(u"horizontalLayout_273")
        self.horizontalLayout_273.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumNoise_Slider = QSlider(self.Imaging_CalciumNoise_Slider_frame)
        self.Imaging_CalciumNoise_Slider.setObjectName(u"Imaging_CalciumNoise_Slider")
        self.Imaging_CalciumNoise_Slider.setEnabled(False)
        self.Imaging_CalciumNoise_Slider.setMaximum(100)
        self.Imaging_CalciumNoise_Slider.setPageStep(10)
        self.Imaging_CalciumNoise_Slider.setValue(10)
        self.Imaging_CalciumNoise_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_CalciumNoise_Slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_273.addWidget(self.Imaging_CalciumNoise_Slider)


        self.verticalLayout_134.addWidget(self.Imaging_CalciumNoise_Slider_frame)

        self.Imaging_CalciumNoise_Values_frame = QFrame(self.Imaging_CalciumNoise_frame)
        self.Imaging_CalciumNoise_Values_frame.setObjectName(u"Imaging_CalciumNoise_Values_frame")
        self.Imaging_CalciumNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.Imaging_CalciumNoise_Values_frame)
        self.horizontalLayout_149.setSpacing(0)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.Imaging_CalciumNoise_Values_frame)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_149.addWidget(self.label_49)

        self.label_50 = QLabel(self.Imaging_CalciumNoise_Values_frame)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_149.addWidget(self.label_50)

        self.label_51 = QLabel(self.Imaging_CalciumNoise_Values_frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_149.addWidget(self.label_51)


        self.verticalLayout_134.addWidget(self.Imaging_CalciumNoise_Values_frame)


        self.verticalLayout_137.addWidget(self.Imaging_CalciumNoise_frame)

        self.line_54 = QFrame(self.Imaging_CalciumParameter_page)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_54.setFrameShape(QFrame.Shape.HLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_137.addWidget(self.line_54)

        self.Imaging_CalciumBaseline_frame = QFrame(self.Imaging_CalciumParameter_page)
        self.Imaging_CalciumBaseline_frame.setObjectName(u"Imaging_CalciumBaseline_frame")
        self.Imaging_CalciumBaseline_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.Imaging_CalciumBaseline_frame)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(5, 0, 5, 0)
        self.Imaging_CalciumBaseline_Title_frame = QFrame(self.Imaging_CalciumBaseline_frame)
        self.Imaging_CalciumBaseline_Title_frame.setObjectName(u"Imaging_CalciumBaseline_Title_frame")
        self.Imaging_CalciumBaseline_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_282 = QHBoxLayout(self.Imaging_CalciumBaseline_Title_frame)
        self.horizontalLayout_282.setSpacing(0)
        self.horizontalLayout_282.setObjectName(u"horizontalLayout_282")
        self.horizontalLayout_282.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumBaseline_Toggle_frame = QFrame(self.Imaging_CalciumBaseline_Title_frame)
        self.Imaging_CalciumBaseline_Toggle_frame.setObjectName(u"Imaging_CalciumBaseline_Toggle_frame")
        self.Imaging_CalciumBaseline_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_CalciumBaseline_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_CalciumBaseline_Toggle_layout = QHBoxLayout(self.Imaging_CalciumBaseline_Toggle_frame)
        self.Imaging_CalciumBaseline_Toggle_layout.setSpacing(0)
        self.Imaging_CalciumBaseline_Toggle_layout.setObjectName(u"Imaging_CalciumBaseline_Toggle_layout")
        self.Imaging_CalciumBaseline_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_282.addWidget(self.Imaging_CalciumBaseline_Toggle_frame)

        self.Imaging_CalciumBaseline_Label_frame = QFrame(self.Imaging_CalciumBaseline_Title_frame)
        self.Imaging_CalciumBaseline_Label_frame.setObjectName(u"Imaging_CalciumBaseline_Label_frame")
        self.Imaging_CalciumBaseline_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.Imaging_CalciumBaseline_Label_frame)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumBaseline_Label = QLabel(self.Imaging_CalciumBaseline_Label_frame)
        self.Imaging_CalciumBaseline_Label.setObjectName(u"Imaging_CalciumBaseline_Label")
        self.Imaging_CalciumBaseline_Label.setWordWrap(True)

        self.horizontalLayout_127.addWidget(self.Imaging_CalciumBaseline_Label)


        self.horizontalLayout_282.addWidget(self.Imaging_CalciumBaseline_Label_frame)


        self.verticalLayout_138.addWidget(self.Imaging_CalciumBaseline_Title_frame)

        self.Imaging_CalciumBaseline_Readings_frame = QFrame(self.Imaging_CalciumBaseline_frame)
        self.Imaging_CalciumBaseline_Readings_frame.setObjectName(u"Imaging_CalciumBaseline_Readings_frame")
        self.Imaging_CalciumBaseline_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_283 = QHBoxLayout(self.Imaging_CalciumBaseline_Readings_frame)
        self.horizontalLayout_283.setSpacing(0)
        self.horizontalLayout_283.setObjectName(u"horizontalLayout_283")
        self.horizontalLayout_283.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumBaseline_Readings = QLabel(self.Imaging_CalciumBaseline_Readings_frame)
        self.Imaging_CalciumBaseline_Readings.setObjectName(u"Imaging_CalciumBaseline_Readings")
        self.Imaging_CalciumBaseline_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_283.addWidget(self.Imaging_CalciumBaseline_Readings)


        self.verticalLayout_138.addWidget(self.Imaging_CalciumBaseline_Readings_frame)

        self.Imaging_CalciumBaseline_Slider_frame = QFrame(self.Imaging_CalciumBaseline_frame)
        self.Imaging_CalciumBaseline_Slider_frame.setObjectName(u"Imaging_CalciumBaseline_Slider_frame")
        self.Imaging_CalciumBaseline_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_284 = QHBoxLayout(self.Imaging_CalciumBaseline_Slider_frame)
        self.horizontalLayout_284.setSpacing(0)
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.horizontalLayout_284.setContentsMargins(0, 0, 0, 0)
        self.Imaging_CalciumBaseline_Slider = QSlider(self.Imaging_CalciumBaseline_Slider_frame)
        self.Imaging_CalciumBaseline_Slider.setObjectName(u"Imaging_CalciumBaseline_Slider")
        self.Imaging_CalciumBaseline_Slider.setEnabled(False)
        self.Imaging_CalciumBaseline_Slider.setMinimum(1)
        self.Imaging_CalciumBaseline_Slider.setMaximum(50)
        self.Imaging_CalciumBaseline_Slider.setValue(10)
        self.Imaging_CalciumBaseline_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_CalciumBaseline_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_CalciumBaseline_Slider.setTickInterval(10)

        self.horizontalLayout_284.addWidget(self.Imaging_CalciumBaseline_Slider)


        self.verticalLayout_138.addWidget(self.Imaging_CalciumBaseline_Slider_frame)

        self.Imaging_CalciumBaseline_Values_frame = QFrame(self.Imaging_CalciumBaseline_frame)
        self.Imaging_CalciumBaseline_Values_frame.setObjectName(u"Imaging_CalciumBaseline_Values_frame")
        self.Imaging_CalciumBaseline_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_CalciumBaseline_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.Imaging_CalciumBaseline_Values_frame)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.Imaging_CalciumBaseline_Values_frame)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_148.addWidget(self.label_46)

        self.label_47 = QLabel(self.Imaging_CalciumBaseline_Values_frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_148.addWidget(self.label_47)

        self.label_48 = QLabel(self.Imaging_CalciumBaseline_Values_frame)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_148.addWidget(self.label_48)


        self.verticalLayout_138.addWidget(self.Imaging_CalciumBaseline_Values_frame)


        self.verticalLayout_137.addWidget(self.Imaging_CalciumBaseline_frame)

        self.Imaging_parameter_stackedWidget.addWidget(self.Imaging_CalciumParameter_page)
        self.Imaging_FluoParameter_page = QWidget()
        self.Imaging_FluoParameter_page.setObjectName(u"Imaging_FluoParameter_page")
        self.verticalLayout_145 = QVBoxLayout(self.Imaging_FluoParameter_page)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoScale_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_FluoScale_frame.setObjectName(u"Imaging_FluoScale_frame")
        self.Imaging_FluoScale_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.Imaging_FluoScale_frame)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(5, 0, 5, 0)
        self.Imaging_FluoScale_Title_frame = QFrame(self.Imaging_FluoScale_frame)
        self.Imaging_FluoScale_Title_frame.setObjectName(u"Imaging_FluoScale_Title_frame")
        self.Imaging_FluoScale_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_294 = QHBoxLayout(self.Imaging_FluoScale_Title_frame)
        self.horizontalLayout_294.setSpacing(0)
        self.horizontalLayout_294.setObjectName(u"horizontalLayout_294")
        self.horizontalLayout_294.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoScale_Toggle_frame = QFrame(self.Imaging_FluoScale_Title_frame)
        self.Imaging_FluoScale_Toggle_frame.setObjectName(u"Imaging_FluoScale_Toggle_frame")
        self.Imaging_FluoScale_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_FluoScale_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FluoScale_Toggle_layout = QHBoxLayout(self.Imaging_FluoScale_Toggle_frame)
        self.Imaging_FluoScale_Toggle_layout.setSpacing(0)
        self.Imaging_FluoScale_Toggle_layout.setObjectName(u"Imaging_FluoScale_Toggle_layout")
        self.Imaging_FluoScale_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_294.addWidget(self.Imaging_FluoScale_Toggle_frame)

        self.Imaging_FluoScale_Label_frame = QFrame(self.Imaging_FluoScale_Title_frame)
        self.Imaging_FluoScale_Label_frame.setObjectName(u"Imaging_FluoScale_Label_frame")
        self.Imaging_FluoScale_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_308 = QHBoxLayout(self.Imaging_FluoScale_Label_frame)
        self.horizontalLayout_308.setSpacing(0)
        self.horizontalLayout_308.setObjectName(u"horizontalLayout_308")
        self.horizontalLayout_308.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoScale_Label = QLabel(self.Imaging_FluoScale_Label_frame)
        self.Imaging_FluoScale_Label.setObjectName(u"Imaging_FluoScale_Label")
        self.Imaging_FluoScale_Label.setWordWrap(True)

        self.horizontalLayout_308.addWidget(self.Imaging_FluoScale_Label)


        self.horizontalLayout_294.addWidget(self.Imaging_FluoScale_Label_frame)


        self.verticalLayout_142.addWidget(self.Imaging_FluoScale_Title_frame)

        self.Imaging_FluoScale_Readings_frame = QFrame(self.Imaging_FluoScale_frame)
        self.Imaging_FluoScale_Readings_frame.setObjectName(u"Imaging_FluoScale_Readings_frame")
        self.Imaging_FluoScale_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_295 = QHBoxLayout(self.Imaging_FluoScale_Readings_frame)
        self.horizontalLayout_295.setSpacing(0)
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.horizontalLayout_295.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoScale_Readings = QLabel(self.Imaging_FluoScale_Readings_frame)
        self.Imaging_FluoScale_Readings.setObjectName(u"Imaging_FluoScale_Readings")
        self.Imaging_FluoScale_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_295.addWidget(self.Imaging_FluoScale_Readings)


        self.verticalLayout_142.addWidget(self.Imaging_FluoScale_Readings_frame)

        self.Imaging_FluoScale_Slider_frame = QFrame(self.Imaging_FluoScale_frame)
        self.Imaging_FluoScale_Slider_frame.setObjectName(u"Imaging_FluoScale_Slider_frame")
        self.Imaging_FluoScale_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_296 = QHBoxLayout(self.Imaging_FluoScale_Slider_frame)
        self.horizontalLayout_296.setSpacing(0)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoScale_Slider = QSlider(self.Imaging_FluoScale_Slider_frame)
        self.Imaging_FluoScale_Slider.setObjectName(u"Imaging_FluoScale_Slider")
        self.Imaging_FluoScale_Slider.setEnabled(False)
        self.Imaging_FluoScale_Slider.setMinimum(0)
        self.Imaging_FluoScale_Slider.setMaximum(100)
        self.Imaging_FluoScale_Slider.setValue(10)
        self.Imaging_FluoScale_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_FluoScale_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_FluoScale_Slider.setTickInterval(10)

        self.horizontalLayout_296.addWidget(self.Imaging_FluoScale_Slider)


        self.verticalLayout_142.addWidget(self.Imaging_FluoScale_Slider_frame)

        self.Imaging_FluoScale_Values_frame = QFrame(self.Imaging_FluoScale_frame)
        self.Imaging_FluoScale_Values_frame.setObjectName(u"Imaging_FluoScale_Values_frame")
        self.Imaging_FluoScale_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoScale_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.Imaging_FluoScale_Values_frame)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.Imaging_FluoScale_Values_frame)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_126.addWidget(self.label_16)

        self.label_17 = QLabel(self.Imaging_FluoScale_Values_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_126.addWidget(self.label_17)

        self.label_4 = QLabel(self.Imaging_FluoScale_Values_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_126.addWidget(self.label_4)


        self.verticalLayout_142.addWidget(self.Imaging_FluoScale_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_FluoScale_frame)

        self.line_45 = QFrame(self.Imaging_FluoParameter_page)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_45.setFrameShape(QFrame.Shape.HLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.line_45)

        self.Imaging_FluoOffset_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_FluoOffset_frame.setObjectName(u"Imaging_FluoOffset_frame")
        self.Imaging_FluoOffset_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.Imaging_FluoOffset_frame)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(5, 0, 5, 0)
        self.Imaging_FluoOffset_Title_frame = QFrame(self.Imaging_FluoOffset_frame)
        self.Imaging_FluoOffset_Title_frame.setObjectName(u"Imaging_FluoOffset_Title_frame")
        self.Imaging_FluoOffset_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_297 = QHBoxLayout(self.Imaging_FluoOffset_Title_frame)
        self.horizontalLayout_297.setSpacing(0)
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_297.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoOffset_Toggle_frame = QFrame(self.Imaging_FluoOffset_Title_frame)
        self.Imaging_FluoOffset_Toggle_frame.setObjectName(u"Imaging_FluoOffset_Toggle_frame")
        self.Imaging_FluoOffset_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_FluoOffset_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FluoOffset_Toggle_layout = QHBoxLayout(self.Imaging_FluoOffset_Toggle_frame)
        self.Imaging_FluoOffset_Toggle_layout.setSpacing(0)
        self.Imaging_FluoOffset_Toggle_layout.setObjectName(u"Imaging_FluoOffset_Toggle_layout")
        self.Imaging_FluoOffset_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_297.addWidget(self.Imaging_FluoOffset_Toggle_frame)

        self.Imaging_FluoOffset_Label_frame = QFrame(self.Imaging_FluoOffset_Title_frame)
        self.Imaging_FluoOffset_Label_frame.setObjectName(u"Imaging_FluoOffset_Label_frame")
        self.Imaging_FluoOffset_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_311 = QHBoxLayout(self.Imaging_FluoOffset_Label_frame)
        self.horizontalLayout_311.setSpacing(0)
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.horizontalLayout_311.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoOffset_Label = QLabel(self.Imaging_FluoOffset_Label_frame)
        self.Imaging_FluoOffset_Label.setObjectName(u"Imaging_FluoOffset_Label")
        self.Imaging_FluoOffset_Label.setWordWrap(True)

        self.horizontalLayout_311.addWidget(self.Imaging_FluoOffset_Label)


        self.horizontalLayout_297.addWidget(self.Imaging_FluoOffset_Label_frame)


        self.verticalLayout_143.addWidget(self.Imaging_FluoOffset_Title_frame)

        self.Imaging_FluoOffset_Readings_frame = QFrame(self.Imaging_FluoOffset_frame)
        self.Imaging_FluoOffset_Readings_frame.setObjectName(u"Imaging_FluoOffset_Readings_frame")
        self.Imaging_FluoOffset_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_298 = QHBoxLayout(self.Imaging_FluoOffset_Readings_frame)
        self.horizontalLayout_298.setSpacing(0)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.horizontalLayout_298.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoOffset_Readings = QLabel(self.Imaging_FluoOffset_Readings_frame)
        self.Imaging_FluoOffset_Readings.setObjectName(u"Imaging_FluoOffset_Readings")
        self.Imaging_FluoOffset_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_298.addWidget(self.Imaging_FluoOffset_Readings)


        self.verticalLayout_143.addWidget(self.Imaging_FluoOffset_Readings_frame)

        self.Imaging_FluoOffset_Slider_frame = QFrame(self.Imaging_FluoOffset_frame)
        self.Imaging_FluoOffset_Slider_frame.setObjectName(u"Imaging_FluoOffset_Slider_frame")
        self.Imaging_FluoOffset_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_299 = QHBoxLayout(self.Imaging_FluoOffset_Slider_frame)
        self.horizontalLayout_299.setSpacing(0)
        self.horizontalLayout_299.setObjectName(u"horizontalLayout_299")
        self.horizontalLayout_299.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoOffset_Slider = QSlider(self.Imaging_FluoOffset_Slider_frame)
        self.Imaging_FluoOffset_Slider.setObjectName(u"Imaging_FluoOffset_Slider")
        self.Imaging_FluoOffset_Slider.setEnabled(False)
        self.Imaging_FluoOffset_Slider.setMaximum(20)
        self.Imaging_FluoOffset_Slider.setValue(5)
        self.Imaging_FluoOffset_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_FluoOffset_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_FluoOffset_Slider.setTickInterval(2)

        self.horizontalLayout_299.addWidget(self.Imaging_FluoOffset_Slider)


        self.verticalLayout_143.addWidget(self.Imaging_FluoOffset_Slider_frame)

        self.Imaging_FluoOffset_Values_frame = QFrame(self.Imaging_FluoOffset_frame)
        self.Imaging_FluoOffset_Values_frame.setObjectName(u"Imaging_FluoOffset_Values_frame")
        self.Imaging_FluoOffset_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoOffset_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.Imaging_FluoOffset_Values_frame)
        self.horizontalLayout_130.setSpacing(0)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.Imaging_FluoOffset_Values_frame)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_130.addWidget(self.label_24)

        self.label_18 = QLabel(self.Imaging_FluoOffset_Values_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_130.addWidget(self.label_18)

        self.label_21 = QLabel(self.Imaging_FluoOffset_Values_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_130.addWidget(self.label_21)


        self.verticalLayout_143.addWidget(self.Imaging_FluoOffset_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_FluoOffset_frame)

        self.line_46 = QFrame(self.Imaging_FluoParameter_page)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_46.setFrameShape(QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.line_46)

        self.Imaging_FluoNoise_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_FluoNoise_frame.setObjectName(u"Imaging_FluoNoise_frame")
        self.Imaging_FluoNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.Imaging_FluoNoise_frame)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(5, 0, 5, 0)
        self.Imaging_FluoNoise_Title_frame = QFrame(self.Imaging_FluoNoise_frame)
        self.Imaging_FluoNoise_Title_frame.setObjectName(u"Imaging_FluoNoise_Title_frame")
        self.Imaging_FluoNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_291 = QHBoxLayout(self.Imaging_FluoNoise_Title_frame)
        self.horizontalLayout_291.setSpacing(0)
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.horizontalLayout_291.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoNoise_Toggle_frame = QFrame(self.Imaging_FluoNoise_Title_frame)
        self.Imaging_FluoNoise_Toggle_frame.setObjectName(u"Imaging_FluoNoise_Toggle_frame")
        self.Imaging_FluoNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_FluoNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FluoNoise_Toggle_layout = QHBoxLayout(self.Imaging_FluoNoise_Toggle_frame)
        self.Imaging_FluoNoise_Toggle_layout.setSpacing(0)
        self.Imaging_FluoNoise_Toggle_layout.setObjectName(u"Imaging_FluoNoise_Toggle_layout")
        self.Imaging_FluoNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_291.addWidget(self.Imaging_FluoNoise_Toggle_frame)

        self.Imaging_FluoNoise_Label_frame = QFrame(self.Imaging_FluoNoise_Title_frame)
        self.Imaging_FluoNoise_Label_frame.setObjectName(u"Imaging_FluoNoise_Label_frame")
        self.Imaging_FluoNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_307 = QHBoxLayout(self.Imaging_FluoNoise_Label_frame)
        self.horizontalLayout_307.setSpacing(0)
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.horizontalLayout_307.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoNoise_Label = QLabel(self.Imaging_FluoNoise_Label_frame)
        self.Imaging_FluoNoise_Label.setObjectName(u"Imaging_FluoNoise_Label")

        self.horizontalLayout_307.addWidget(self.Imaging_FluoNoise_Label)


        self.horizontalLayout_291.addWidget(self.Imaging_FluoNoise_Label_frame)


        self.verticalLayout_141.addWidget(self.Imaging_FluoNoise_Title_frame)

        self.Imaging_FluoNoise_Readings_frame = QFrame(self.Imaging_FluoNoise_frame)
        self.Imaging_FluoNoise_Readings_frame.setObjectName(u"Imaging_FluoNoise_Readings_frame")
        self.Imaging_FluoNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_292 = QHBoxLayout(self.Imaging_FluoNoise_Readings_frame)
        self.horizontalLayout_292.setSpacing(0)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalLayout_292.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoNoise_Readings = QLabel(self.Imaging_FluoNoise_Readings_frame)
        self.Imaging_FluoNoise_Readings.setObjectName(u"Imaging_FluoNoise_Readings")
        self.Imaging_FluoNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_292.addWidget(self.Imaging_FluoNoise_Readings)


        self.verticalLayout_141.addWidget(self.Imaging_FluoNoise_Readings_frame)

        self.Imaging_FluoNoise_Slider_frame = QFrame(self.Imaging_FluoNoise_frame)
        self.Imaging_FluoNoise_Slider_frame.setObjectName(u"Imaging_FluoNoise_Slider_frame")
        self.Imaging_FluoNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_293 = QHBoxLayout(self.Imaging_FluoNoise_Slider_frame)
        self.horizontalLayout_293.setSpacing(0)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.horizontalLayout_293.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoNoise_Slider = QSlider(self.Imaging_FluoNoise_Slider_frame)
        self.Imaging_FluoNoise_Slider.setObjectName(u"Imaging_FluoNoise_Slider")
        self.Imaging_FluoNoise_Slider.setEnabled(False)
        self.Imaging_FluoNoise_Slider.setMinimum(0)
        self.Imaging_FluoNoise_Slider.setMaximum(100)
        self.Imaging_FluoNoise_Slider.setValue(10)
        self.Imaging_FluoNoise_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_FluoNoise_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_FluoNoise_Slider.setTickInterval(10)

        self.horizontalLayout_293.addWidget(self.Imaging_FluoNoise_Slider)


        self.verticalLayout_141.addWidget(self.Imaging_FluoNoise_Slider_frame)

        self.Imaging_FluoNoise_Values_frame = QFrame(self.Imaging_FluoNoise_frame)
        self.Imaging_FluoNoise_Values_frame.setObjectName(u"Imaging_FluoNoise_Values_frame")
        self.Imaging_FluoNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.Imaging_FluoNoise_Values_frame)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.Imaging_FluoNoise_Values_frame)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_132.addWidget(self.label_27)

        self.label_25 = QLabel(self.Imaging_FluoNoise_Values_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_132.addWidget(self.label_25)

        self.label_26 = QLabel(self.Imaging_FluoNoise_Values_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_132.addWidget(self.label_26)


        self.verticalLayout_141.addWidget(self.Imaging_FluoNoise_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_FluoNoise_frame)

        self.line_47 = QFrame(self.Imaging_FluoParameter_page)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_47.setFrameShape(QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.line_47)

        self.Imaging_FluoSat_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_FluoSat_frame.setObjectName(u"Imaging_FluoSat_frame")
        self.Imaging_FluoSat_frame.setMaximumSize(QSize(16777215, 25))
        self.Imaging_FluoSat_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoSat_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.Imaging_FluoSat_frame)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(5, 0, 5, 0)
        self.Imaging_FluoSat_Title_frame = QFrame(self.Imaging_FluoSat_frame)
        self.Imaging_FluoSat_Title_frame.setObjectName(u"Imaging_FluoSat_Title_frame")
        self.Imaging_FluoSat_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoSat_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_300 = QHBoxLayout(self.Imaging_FluoSat_Title_frame)
        self.horizontalLayout_300.setSpacing(0)
        self.horizontalLayout_300.setObjectName(u"horizontalLayout_300")
        self.horizontalLayout_300.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoSat_Toggle_frame = QFrame(self.Imaging_FluoSat_Title_frame)
        self.Imaging_FluoSat_Toggle_frame.setObjectName(u"Imaging_FluoSat_Toggle_frame")
        self.Imaging_FluoSat_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_FluoSat_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoSat_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_Saturation_Toggle_layout = QHBoxLayout(self.Imaging_FluoSat_Toggle_frame)
        self.Imaging_Saturation_Toggle_layout.setSpacing(0)
        self.Imaging_Saturation_Toggle_layout.setObjectName(u"Imaging_Saturation_Toggle_layout")
        self.Imaging_Saturation_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_300.addWidget(self.Imaging_FluoSat_Toggle_frame)

        self.Imaging_FluoSat_Label_frame = QFrame(self.Imaging_FluoSat_Title_frame)
        self.Imaging_FluoSat_Label_frame.setObjectName(u"Imaging_FluoSat_Label_frame")
        self.Imaging_FluoSat_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_FluoSat_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.Imaging_FluoSat_Label_frame)
        self.horizontalLayout_120.setSpacing(0)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoSat_Label = QLabel(self.Imaging_FluoSat_Label_frame)
        self.Imaging_FluoSat_Label.setObjectName(u"Imaging_FluoSat_Label")
        self.Imaging_FluoSat_Label.setFont(font4)
        self.Imaging_FluoSat_Label.setWordWrap(True)

        self.horizontalLayout_120.addWidget(self.Imaging_FluoSat_Label)


        self.horizontalLayout_300.addWidget(self.Imaging_FluoSat_Label_frame)


        self.verticalLayout_144.addWidget(self.Imaging_FluoSat_Title_frame)


        self.verticalLayout_145.addWidget(self.Imaging_FluoSat_frame)

        self.line_48 = QFrame(self.Imaging_FluoParameter_page)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_48.setFrameShape(QFrame.Shape.HLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.line_48)

        self.Imaging_kd_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_kd_frame.setObjectName(u"Imaging_kd_frame")
        self.Imaging_kd_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.Imaging_kd_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.Imaging_kd_frame)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(5, 0, 5, 0)
        self.Imaging_kd_Title_frame = QFrame(self.Imaging_kd_frame)
        self.Imaging_kd_Title_frame.setObjectName(u"Imaging_kd_Title_frame")
        self.Imaging_kd_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_287 = QHBoxLayout(self.Imaging_kd_Title_frame)
        self.horizontalLayout_287.setSpacing(0)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.horizontalLayout_287.setContentsMargins(0, 0, 0, 0)
        self.Imaging_kd_Toggle_frame = QFrame(self.Imaging_kd_Title_frame)
        self.Imaging_kd_Toggle_frame.setObjectName(u"Imaging_kd_Toggle_frame")
        self.Imaging_kd_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_kd_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_kd_Toggle_layout = QHBoxLayout(self.Imaging_kd_Toggle_frame)
        self.Imaging_kd_Toggle_layout.setSpacing(0)
        self.Imaging_kd_Toggle_layout.setObjectName(u"Imaging_kd_Toggle_layout")
        self.Imaging_kd_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_287.addWidget(self.Imaging_kd_Toggle_frame)

        self.Imaging_kd_Label_frame = QFrame(self.Imaging_kd_Title_frame)
        self.Imaging_kd_Label_frame.setObjectName(u"Imaging_kd_Label_frame")
        self.Imaging_kd_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_302 = QHBoxLayout(self.Imaging_kd_Label_frame)
        self.horizontalLayout_302.setSpacing(0)
        self.horizontalLayout_302.setObjectName(u"horizontalLayout_302")
        self.horizontalLayout_302.setContentsMargins(0, 0, 0, 0)
        self.Imaging_kd_Label = QLabel(self.Imaging_kd_Label_frame)
        self.Imaging_kd_Label.setObjectName(u"Imaging_kd_Label")
        self.Imaging_kd_Label.setWordWrap(True)

        self.horizontalLayout_302.addWidget(self.Imaging_kd_Label)


        self.horizontalLayout_287.addWidget(self.Imaging_kd_Label_frame)


        self.verticalLayout_139.addWidget(self.Imaging_kd_Title_frame)

        self.Imaging_kd_Readings_frame = QFrame(self.Imaging_kd_frame)
        self.Imaging_kd_Readings_frame.setObjectName(u"Imaging_kd_Readings_frame")
        self.Imaging_kd_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_286 = QHBoxLayout(self.Imaging_kd_Readings_frame)
        self.horizontalLayout_286.setSpacing(0)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.horizontalLayout_286.setContentsMargins(0, 0, 0, 0)
        self.Imaging_kd_Readings = QLabel(self.Imaging_kd_Readings_frame)
        self.Imaging_kd_Readings.setObjectName(u"Imaging_kd_Readings")
        self.Imaging_kd_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_286.addWidget(self.Imaging_kd_Readings)


        self.verticalLayout_139.addWidget(self.Imaging_kd_Readings_frame)

        self.Imaging_kd_Slider_frame = QFrame(self.Imaging_kd_frame)
        self.Imaging_kd_Slider_frame.setObjectName(u"Imaging_kd_Slider_frame")
        self.Imaging_kd_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_285 = QHBoxLayout(self.Imaging_kd_Slider_frame)
        self.horizontalLayout_285.setSpacing(0)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_285.setContentsMargins(0, 0, 0, 0)
        self.Imaging_kd_Slider = QSlider(self.Imaging_kd_Slider_frame)
        self.Imaging_kd_Slider.setObjectName(u"Imaging_kd_Slider")
        self.Imaging_kd_Slider.setEnabled(False)
        self.Imaging_kd_Slider.setMinimum(1)
        self.Imaging_kd_Slider.setMaximum(100)
        self.Imaging_kd_Slider.setValue(25)
        self.Imaging_kd_Slider.setSliderPosition(25)
        self.Imaging_kd_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_kd_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_kd_Slider.setTickInterval(10)

        self.horizontalLayout_285.addWidget(self.Imaging_kd_Slider)


        self.verticalLayout_139.addWidget(self.Imaging_kd_Slider_frame)

        self.Imaging_kd_Values_frame = QFrame(self.Imaging_kd_frame)
        self.Imaging_kd_Values_frame.setObjectName(u"Imaging_kd_Values_frame")
        self.Imaging_kd_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_kd_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.Imaging_kd_Values_frame)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.Imaging_kd_Values_frame)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_133.addWidget(self.label_30)

        self.label_28 = QLabel(self.Imaging_kd_Values_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_133.addWidget(self.label_28)

        self.label_29 = QLabel(self.Imaging_kd_Values_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_133.addWidget(self.label_29)


        self.verticalLayout_139.addWidget(self.Imaging_kd_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_kd_frame)

        self.Imaging_Saturation_Line = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_Saturation_Line.setObjectName(u"Imaging_Saturation_Line")
        self.Imaging_Saturation_Line.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.Imaging_Saturation_Line.setFrameShape(QFrame.Shape.HLine)
        self.Imaging_Saturation_Line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.Imaging_Saturation_Line)

        self.Imaging_Hill_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_Hill_frame.setObjectName(u"Imaging_Hill_frame")
        self.Imaging_Hill_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.Imaging_Hill_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.Imaging_Hill_frame)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(5, 0, 5, 0)
        self.Imaging_Hill_Title_frame = QFrame(self.Imaging_Hill_frame)
        self.Imaging_Hill_Title_frame.setObjectName(u"Imaging_Hill_Title_frame")
        self.Imaging_Hill_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_290 = QHBoxLayout(self.Imaging_Hill_Title_frame)
        self.horizontalLayout_290.setSpacing(0)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.horizontalLayout_290.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Hill_Toggle_frame = QFrame(self.Imaging_Hill_Title_frame)
        self.Imaging_Hill_Toggle_frame.setObjectName(u"Imaging_Hill_Toggle_frame")
        self.Imaging_Hill_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_Hill_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_Hill_Toggle_layout = QHBoxLayout(self.Imaging_Hill_Toggle_frame)
        self.Imaging_Hill_Toggle_layout.setSpacing(0)
        self.Imaging_Hill_Toggle_layout.setObjectName(u"Imaging_Hill_Toggle_layout")
        self.Imaging_Hill_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_290.addWidget(self.Imaging_Hill_Toggle_frame)

        self.Imaging_Hill_Label_frame = QFrame(self.Imaging_Hill_Title_frame)
        self.Imaging_Hill_Label_frame.setObjectName(u"Imaging_Hill_Label_frame")
        self.Imaging_Hill_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_304 = QHBoxLayout(self.Imaging_Hill_Label_frame)
        self.horizontalLayout_304.setSpacing(0)
        self.horizontalLayout_304.setObjectName(u"horizontalLayout_304")
        self.horizontalLayout_304.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Hill_Label = QLabel(self.Imaging_Hill_Label_frame)
        self.Imaging_Hill_Label.setObjectName(u"Imaging_Hill_Label")

        self.horizontalLayout_304.addWidget(self.Imaging_Hill_Label)


        self.horizontalLayout_290.addWidget(self.Imaging_Hill_Label_frame)


        self.verticalLayout_140.addWidget(self.Imaging_Hill_Title_frame)

        self.Imaging_Hill_Readings_frame = QFrame(self.Imaging_Hill_frame)
        self.Imaging_Hill_Readings_frame.setObjectName(u"Imaging_Hill_Readings_frame")
        self.Imaging_Hill_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_289 = QHBoxLayout(self.Imaging_Hill_Readings_frame)
        self.horizontalLayout_289.setSpacing(0)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.horizontalLayout_289.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Hill_Readings = QLabel(self.Imaging_Hill_Readings_frame)
        self.Imaging_Hill_Readings.setObjectName(u"Imaging_Hill_Readings")
        self.Imaging_Hill_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_289.addWidget(self.Imaging_Hill_Readings)


        self.verticalLayout_140.addWidget(self.Imaging_Hill_Readings_frame)

        self.Imaging_Hill_Slider_frame = QFrame(self.Imaging_Hill_frame)
        self.Imaging_Hill_Slider_frame.setObjectName(u"Imaging_Hill_Slider_frame")
        self.Imaging_Hill_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_288 = QHBoxLayout(self.Imaging_Hill_Slider_frame)
        self.horizontalLayout_288.setSpacing(0)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_288.setContentsMargins(0, 0, 0, 0)
        self.Imaging_Hill_Slider = QSlider(self.Imaging_Hill_Slider_frame)
        self.Imaging_Hill_Slider.setObjectName(u"Imaging_Hill_Slider")
        self.Imaging_Hill_Slider.setEnabled(False)
        self.Imaging_Hill_Slider.setMinimum(50)
        self.Imaging_Hill_Slider.setMaximum(100)
        self.Imaging_Hill_Slider.setValue(100)
        self.Imaging_Hill_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_Hill_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_Hill_Slider.setTickInterval(5)

        self.horizontalLayout_288.addWidget(self.Imaging_Hill_Slider)


        self.verticalLayout_140.addWidget(self.Imaging_Hill_Slider_frame)

        self.Imaging_Hill_Values_frame = QFrame(self.Imaging_Hill_frame)
        self.Imaging_Hill_Values_frame.setObjectName(u"Imaging_Hill_Values_frame")
        self.Imaging_Hill_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_Hill_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.Imaging_Hill_Values_frame)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.Imaging_Hill_Values_frame)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_136.addWidget(self.label_31)

        self.label_32 = QLabel(self.Imaging_Hill_Values_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_32)

        self.label_33 = QLabel(self.Imaging_Hill_Values_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_136.addWidget(self.label_33)


        self.verticalLayout_140.addWidget(self.Imaging_Hill_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_Hill_frame)

        self.Imaging_Saturation_Line2 = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_Saturation_Line2.setObjectName(u"Imaging_Saturation_Line2")
        self.Imaging_Saturation_Line2.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.Imaging_Saturation_Line2.setFrameShape(QFrame.Shape.HLine)
        self.Imaging_Saturation_Line2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_145.addWidget(self.Imaging_Saturation_Line2)

        self.Imaging_PhotoShotNoise_frame = QFrame(self.Imaging_FluoParameter_page)
        self.Imaging_PhotoShotNoise_frame.setObjectName(u"Imaging_PhotoShotNoise_frame")
        self.Imaging_PhotoShotNoise_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.Imaging_PhotoShotNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.Imaging_PhotoShotNoise_frame)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(5, 0, 5, 0)
        self.Imaging_PhotoShotNoise_Title_frame = QFrame(self.Imaging_PhotoShotNoise_frame)
        self.Imaging_PhotoShotNoise_Title_frame.setObjectName(u"Imaging_PhotoShotNoise_Title_frame")
        self.Imaging_PhotoShotNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.Imaging_PhotoShotNoise_Title_frame)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PhotoShotNoise_Toggle_frame = QFrame(self.Imaging_PhotoShotNoise_Title_frame)
        self.Imaging_PhotoShotNoise_Toggle_frame.setObjectName(u"Imaging_PhotoShotNoise_Toggle_frame")
        self.Imaging_PhotoShotNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.Imaging_PhotoShotNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_PhotoShotNoise_Toggle_layout = QHBoxLayout(self.Imaging_PhotoShotNoise_Toggle_frame)
        self.Imaging_PhotoShotNoise_Toggle_layout.setSpacing(0)
        self.Imaging_PhotoShotNoise_Toggle_layout.setObjectName(u"Imaging_PhotoShotNoise_Toggle_layout")
        self.Imaging_PhotoShotNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_138.addWidget(self.Imaging_PhotoShotNoise_Toggle_frame)

        self.Imaging_PhotoShotNoise_Label_frame = QFrame(self.Imaging_PhotoShotNoise_Title_frame)
        self.Imaging_PhotoShotNoise_Label_frame.setObjectName(u"Imaging_PhotoShotNoise_Label_frame")
        self.Imaging_PhotoShotNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.Imaging_PhotoShotNoise_Label_frame)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PhotoShotNoise_Label = QLabel(self.Imaging_PhotoShotNoise_Label_frame)
        self.Imaging_PhotoShotNoise_Label.setObjectName(u"Imaging_PhotoShotNoise_Label")
        self.Imaging_PhotoShotNoise_Label.setWordWrap(True)

        self.horizontalLayout_139.addWidget(self.Imaging_PhotoShotNoise_Label)


        self.horizontalLayout_138.addWidget(self.Imaging_PhotoShotNoise_Label_frame)


        self.verticalLayout_79.addWidget(self.Imaging_PhotoShotNoise_Title_frame)

        self.Imaging_PhotoShotNoise_Readings_frame = QFrame(self.Imaging_PhotoShotNoise_frame)
        self.Imaging_PhotoShotNoise_Readings_frame.setObjectName(u"Imaging_PhotoShotNoise_Readings_frame")
        self.Imaging_PhotoShotNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.Imaging_PhotoShotNoise_Readings_frame)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PhotoShotNoise_Readings = QLabel(self.Imaging_PhotoShotNoise_Readings_frame)
        self.Imaging_PhotoShotNoise_Readings.setObjectName(u"Imaging_PhotoShotNoise_Readings")
        self.Imaging_PhotoShotNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_141.addWidget(self.Imaging_PhotoShotNoise_Readings)


        self.verticalLayout_79.addWidget(self.Imaging_PhotoShotNoise_Readings_frame)

        self.Imaging_PhotoShotNoise_Slider_frame = QFrame(self.Imaging_PhotoShotNoise_frame)
        self.Imaging_PhotoShotNoise_Slider_frame.setObjectName(u"Imaging_PhotoShotNoise_Slider_frame")
        self.Imaging_PhotoShotNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.Imaging_PhotoShotNoise_Slider_frame)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.Imaging_PhotoShotNoise_Slider = QSlider(self.Imaging_PhotoShotNoise_Slider_frame)
        self.Imaging_PhotoShotNoise_Slider.setObjectName(u"Imaging_PhotoShotNoise_Slider")
        self.Imaging_PhotoShotNoise_Slider.setEnabled(False)
        self.Imaging_PhotoShotNoise_Slider.setMinimum(1)
        self.Imaging_PhotoShotNoise_Slider.setMaximum(1000)
        self.Imaging_PhotoShotNoise_Slider.setPageStep(10)
        self.Imaging_PhotoShotNoise_Slider.setValue(400)
        self.Imaging_PhotoShotNoise_Slider.setOrientation(Qt.Horizontal)
        self.Imaging_PhotoShotNoise_Slider.setTickPosition(QSlider.TicksBelow)
        self.Imaging_PhotoShotNoise_Slider.setTickInterval(100)

        self.horizontalLayout_142.addWidget(self.Imaging_PhotoShotNoise_Slider)


        self.verticalLayout_79.addWidget(self.Imaging_PhotoShotNoise_Slider_frame)

        self.Imaging_PhotoShotNoise_Values_frame = QFrame(self.Imaging_PhotoShotNoise_frame)
        self.Imaging_PhotoShotNoise_Values_frame.setObjectName(u"Imaging_PhotoShotNoise_Values_frame")
        self.Imaging_PhotoShotNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.Imaging_PhotoShotNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.Imaging_PhotoShotNoise_Values_frame)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.Imaging_PhotoShotNoise_Values_frame)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_143.addWidget(self.label_36)

        self.label_37 = QLabel(self.Imaging_PhotoShotNoise_Values_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_143.addWidget(self.label_37)

        self.label_38 = QLabel(self.Imaging_PhotoShotNoise_Values_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_143.addWidget(self.label_38)


        self.verticalLayout_79.addWidget(self.Imaging_PhotoShotNoise_Values_frame)


        self.verticalLayout_145.addWidget(self.Imaging_PhotoShotNoise_frame)

        self.Imaging_parameter_stackedWidget.addWidget(self.Imaging_FluoParameter_page)

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
        self.verticalLayout_95.setSpacing(50)
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
        self.Imaging_ImagingParameter_pushButton = QPushButton(self.Imaging_rightMenuParameterContainer_frame)
        self.Imaging_ImagingParameter_pushButton.setObjectName(u"Imaging_ImagingParameter_pushButton")
        self.Imaging_ImagingParameter_pushButton.setFont(font1)
        self.Imaging_ImagingParameter_pushButton.setIcon(icon6)
        self.Imaging_ImagingParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_94.addWidget(self.Imaging_ImagingParameter_pushButton)

        self.Imaging_CalciumParameter_pushButton = QPushButton(self.Imaging_rightMenuParameterContainer_frame)
        self.Imaging_CalciumParameter_pushButton.setObjectName(u"Imaging_CalciumParameter_pushButton")
        self.Imaging_CalciumParameter_pushButton.setFont(font1)
        icon20 = QIcon()
        icon20.addFile(u":/resources/resources/Calcium.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Imaging_CalciumParameter_pushButton.setIcon(icon20)
        self.Imaging_CalciumParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_94.addWidget(self.Imaging_CalciumParameter_pushButton)

        self.Imaging_FluoParameter_pushButton = QPushButton(self.Imaging_rightMenuParameterContainer_frame)
        self.Imaging_FluoParameter_pushButton.setObjectName(u"Imaging_FluoParameter_pushButton")
        self.Imaging_FluoParameter_pushButton.setFont(font1)
        self.Imaging_FluoParameter_pushButton.setIcon(icon16)
        self.Imaging_FluoParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_94.addWidget(self.Imaging_FluoParameter_pushButton)


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
        self.horizontalLayout_380 = QHBoxLayout(self.page_202)
        self.horizontalLayout_380.setSpacing(0)
        self.horizontalLayout_380.setObjectName(u"horizontalLayout_380")
        self.horizontalLayout_380.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_widget = QFrame(self.page_202)
        self.MultipleImaging_widget.setObjectName(u"MultipleImaging_widget")
        self.MultipleImaging_widget.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.MultipleImaging_widget)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_header_frame = QFrame(self.MultipleImaging_widget)
        self.MultipleImaging_header_frame.setObjectName(u"MultipleImaging_header_frame")
        self.MultipleImaging_header_frame.setMinimumSize(QSize(0, 30))
        self.MultipleImaging_header_frame.setMaximumSize(QSize(16777215, 25))
        self.MultipleImaging_header_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.MultipleImaging_header_frame)
        self.horizontalLayout_152.setSpacing(0)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 5)
        self.MultipleImaging_pushButton_frame = QFrame(self.MultipleImaging_header_frame)
        self.MultipleImaging_pushButton_frame.setObjectName(u"MultipleImaging_pushButton_frame")
        self.MultipleImaging_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_301 = QHBoxLayout(self.MultipleImaging_pushButton_frame)
        self.horizontalLayout_301.setSpacing(0)
        self.horizontalLayout_301.setObjectName(u"horizontalLayout_301")
        self.horizontalLayout_301.setContentsMargins(25, 0, 0, 0)
        self.MultipleImaging_pushButton = QPushButton(self.MultipleImaging_pushButton_frame)
        self.MultipleImaging_pushButton.setObjectName(u"MultipleImaging_pushButton")
        self.MultipleImaging_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.MultipleImaging_pushButton.setFont(font1)
        self.MultipleImaging_pushButton.setCheckable(True)

        self.horizontalLayout_301.addWidget(self.MultipleImaging_pushButton)

        self.frame_8 = QFrame(self.MultipleImaging_pushButton_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")

        self.horizontalLayout_301.addWidget(self.frame_8)


        self.horizontalLayout_152.addWidget(self.MultipleImaging_pushButton_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_84.addWidget(self.MultipleImaging_header_frame)

        self.MultipleImaging_Oscilloscope_frame = QFrame(self.MultipleImaging_widget)
        self.MultipleImaging_Oscilloscope_frame.setObjectName(u"MultipleImaging_Oscilloscope_frame")
        self.MultipleImaging_Oscilloscope_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_303 = QHBoxLayout(self.MultipleImaging_Oscilloscope_frame)
        self.horizontalLayout_303.setSpacing(0)
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.horizontalLayout_303.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Oscilloscope_widget = PlotWidget(self.MultipleImaging_Oscilloscope_frame)
        self.MultipleImaging_Oscilloscope_widget.setObjectName(u"MultipleImaging_Oscilloscope_widget")
        sizePolicy4.setHeightForWidth(self.MultipleImaging_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.MultipleImaging_Oscilloscope_widget.setSizePolicy(sizePolicy4)
        self.MultipleImaging_Oscilloscope_widget.setAutoFillBackground(False)
        self.MultipleImaging_Oscilloscope_widget.setStyleSheet(u"")
        self.horizontalLayout_305 = QHBoxLayout(self.MultipleImaging_Oscilloscope_widget)
        self.horizontalLayout_305.setSpacing(0)
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.horizontalLayout_305.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Oscilloscope_Traces_frame = QFrame(self.MultipleImaging_Oscilloscope_widget)
        self.MultipleImaging_Oscilloscope_Traces_frame.setObjectName(u"MultipleImaging_Oscilloscope_Traces_frame")
        self.MultipleImaging_Oscilloscope_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.MultipleImaging_Oscilloscope_Traces_frame)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Oscilloscope_Traces_frame_2 = QFrame(self.MultipleImaging_Oscilloscope_Traces_frame)
        self.MultipleImaging_Oscilloscope_Traces_frame_2.setObjectName(u"MultipleImaging_Oscilloscope_Traces_frame_2")
        self.MultipleImaging_Oscilloscope_Traces_frame_2.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Traces_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.MultipleImaging_Oscilloscope_Traces_frame_2)
        self.horizontalLayout_154.setSpacing(0)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame = QFrame(self.MultipleImaging_Oscilloscope_Traces_frame_2)
        self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame.setObjectName(u"MultipleImaging_Oscilloscope_Fluorescence_Traces_frame")
        self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Fluorescence1_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame)
        self.MultipleImaging_Fluorescence1_Checkbox.setObjectName(u"MultipleImaging_Fluorescence1_Checkbox")
        self.MultipleImaging_Fluorescence1_Checkbox.setEnabled(True)
        self.MultipleImaging_Fluorescence1_Checkbox.setAutoFillBackground(False)
        self.MultipleImaging_Fluorescence1_Checkbox.setStyleSheet(u"color: rgb(133, 153, 0);")
        self.MultipleImaging_Fluorescence1_Checkbox.setChecked(True)

        self.verticalLayout_90.addWidget(self.MultipleImaging_Fluorescence1_Checkbox)

        self.MultipleImaging_Fluorescence2_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame)
        self.MultipleImaging_Fluorescence2_Checkbox.setObjectName(u"MultipleImaging_Fluorescence2_Checkbox")
        self.MultipleImaging_Fluorescence2_Checkbox.setStyleSheet(u"color: rgb(0, 255, 133);")

        self.verticalLayout_90.addWidget(self.MultipleImaging_Fluorescence2_Checkbox)

        self.MultipleImaging_Fluorescence3_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame)
        self.MultipleImaging_Fluorescence3_Checkbox.setObjectName(u"MultipleImaging_Fluorescence3_Checkbox")
        self.MultipleImaging_Fluorescence3_Checkbox.setStyleSheet(u"color: rgb(133, 255, 0);")

        self.verticalLayout_90.addWidget(self.MultipleImaging_Fluorescence3_Checkbox)


        self.horizontalLayout_154.addWidget(self.MultipleImaging_Oscilloscope_Fluorescence_Traces_frame)

        self.MultipleImaging_Oscilloscope_Calcium_Traces_frame = QFrame(self.MultipleImaging_Oscilloscope_Traces_frame_2)
        self.MultipleImaging_Oscilloscope_Calcium_Traces_frame.setObjectName(u"MultipleImaging_Oscilloscope_Calcium_Traces_frame")
        self.MultipleImaging_Oscilloscope_Calcium_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Calcium_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.MultipleImaging_Oscilloscope_Calcium_Traces_frame)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Calcium1_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Calcium_Traces_frame)
        self.MultipleImaging_Calcium1_Checkbox.setObjectName(u"MultipleImaging_Calcium1_Checkbox")
        self.MultipleImaging_Calcium1_Checkbox.setEnabled(True)
        self.MultipleImaging_Calcium1_Checkbox.setAutoFillBackground(False)
        self.MultipleImaging_Calcium1_Checkbox.setStyleSheet(u"color: rgb(211, 54, 130);")
        self.MultipleImaging_Calcium1_Checkbox.setChecked(False)

        self.verticalLayout_91.addWidget(self.MultipleImaging_Calcium1_Checkbox)

        self.MultipleImaging_Calcium2_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Calcium_Traces_frame)
        self.MultipleImaging_Calcium2_Checkbox.setObjectName(u"MultipleImaging_Calcium2_Checkbox")
        self.MultipleImaging_Calcium2_Checkbox.setStyleSheet(u"color: rgb(108, 113, 196);")

        self.verticalLayout_91.addWidget(self.MultipleImaging_Calcium2_Checkbox)

        self.MultipleImaging_Calcium3_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Calcium_Traces_frame)
        self.MultipleImaging_Calcium3_Checkbox.setObjectName(u"MultipleImaging_Calcium3_Checkbox")
        self.MultipleImaging_Calcium3_Checkbox.setStyleSheet(u"color: rgb(42, 161, 152);")

        self.verticalLayout_91.addWidget(self.MultipleImaging_Calcium3_Checkbox)


        self.horizontalLayout_154.addWidget(self.MultipleImaging_Oscilloscope_Calcium_Traces_frame)

        self.MultipleImaging_Oscilloscope_Vm_Traces_frame = QFrame(self.MultipleImaging_Oscilloscope_Traces_frame_2)
        self.MultipleImaging_Oscilloscope_Vm_Traces_frame.setObjectName(u"MultipleImaging_Oscilloscope_Vm_Traces_frame")
        self.MultipleImaging_Oscilloscope_Vm_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Vm_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.MultipleImaging_Oscilloscope_Vm_Traces_frame)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Vm1_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Vm_Traces_frame)
        self.MultipleImaging_Vm1_Checkbox.setObjectName(u"MultipleImaging_Vm1_Checkbox")
        self.MultipleImaging_Vm1_Checkbox.setStyleSheet(u"color: rgb(220, 50, 47);")

        self.verticalLayout_92.addWidget(self.MultipleImaging_Vm1_Checkbox)

        self.MultipleImaging_Vm3_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Vm_Traces_frame)
        self.MultipleImaging_Vm3_Checkbox.setObjectName(u"MultipleImaging_Vm3_Checkbox")
        self.MultipleImaging_Vm3_Checkbox.setStyleSheet(u"color: rgb(203, 75, 22);")

        self.verticalLayout_92.addWidget(self.MultipleImaging_Vm3_Checkbox)

        self.MultipleImaging_Vm2_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Vm_Traces_frame)
        self.MultipleImaging_Vm2_Checkbox.setObjectName(u"MultipleImaging_Vm2_Checkbox")
        self.MultipleImaging_Vm2_Checkbox.setStyleSheet(u"color: rgb(181, 137, 0);")

        self.verticalLayout_92.addWidget(self.MultipleImaging_Vm2_Checkbox)


        self.horizontalLayout_154.addWidget(self.MultipleImaging_Oscilloscope_Vm_Traces_frame)

        self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame = QFrame(self.MultipleImaging_Oscilloscope_Traces_frame_2)
        self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame.setObjectName(u"MultipleImaging_Oscilloscope_Stimulus_Traces_frame")
        self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.MultipleImaging_Stimulus_Checkbox = QCheckBox(self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame)
        self.MultipleImaging_Stimulus_Checkbox.setObjectName(u"MultipleImaging_Stimulus_Checkbox")
        self.MultipleImaging_Stimulus_Checkbox.setEnabled(True)
        self.MultipleImaging_Stimulus_Checkbox.setAutoFillBackground(False)
        self.MultipleImaging_Stimulus_Checkbox.setStyleSheet(u"color: rgb(38, 139, 210);")
        self.MultipleImaging_Stimulus_Checkbox.setChecked(True)

        self.verticalLayout_93.addWidget(self.MultipleImaging_Stimulus_Checkbox)


        self.horizontalLayout_154.addWidget(self.MultipleImaging_Oscilloscope_Stimulus_Traces_frame)


        self.verticalLayout_146.addWidget(self.MultipleImaging_Oscilloscope_Traces_frame_2, 0, Qt.AlignTop)


        self.horizontalLayout_305.addWidget(self.MultipleImaging_Oscilloscope_Traces_frame)


        self.horizontalLayout_303.addWidget(self.MultipleImaging_Oscilloscope_widget)


        self.verticalLayout_84.addWidget(self.MultipleImaging_Oscilloscope_frame)

        self.MultipleImaging_DataRecording_box = QGroupBox(self.MultipleImaging_widget)
        self.MultipleImaging_DataRecording_box.setObjectName(u"MultipleImaging_DataRecording_box")
        sizePolicy5.setHeightForWidth(self.MultipleImaging_DataRecording_box.sizePolicy().hasHeightForWidth())
        self.MultipleImaging_DataRecording_box.setSizePolicy(sizePolicy5)
        self.MultipleImaging_DataRecording_box.setMinimumSize(QSize(0, 100))
        self.MultipleImaging_DataRecording_box.setMaximumSize(QSize(16777215, 100))
        self.MultipleImaging_DataRecording_box.setStyleSheet(u"")
        self.horizontalLayout_415 = QHBoxLayout(self.MultipleImaging_DataRecording_box)
        self.horizontalLayout_415.setSpacing(0)
        self.horizontalLayout_415.setObjectName(u"horizontalLayout_415")
        self.horizontalLayout_415.setContentsMargins(5, 5, 5, 5)
        self.MultipleImaging_DataRecording_left_frame = QFrame(self.MultipleImaging_DataRecording_box)
        self.MultipleImaging_DataRecording_left_frame.setObjectName(u"MultipleImaging_DataRecording_left_frame")
        self.MultipleImaging_DataRecording_left_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_DataRecording_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.MultipleImaging_DataRecording_left_frame)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_DataRecording_recordingMode_frame = QFrame(self.MultipleImaging_DataRecording_left_frame)
        self.MultipleImaging_DataRecording_recordingMode_frame.setObjectName(u"MultipleImaging_DataRecording_recordingMode_frame")
        self.MultipleImaging_DataRecording_recordingMode_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_DataRecording_recordingMode_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_425 = QHBoxLayout(self.MultipleImaging_DataRecording_recordingMode_frame)
        self.horizontalLayout_425.setSpacing(0)
        self.horizontalLayout_425.setObjectName(u"horizontalLayout_425")
        self.horizontalLayout_425.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_107.addWidget(self.MultipleImaging_DataRecording_recordingMode_frame)


        self.horizontalLayout_415.addWidget(self.MultipleImaging_DataRecording_left_frame)

        self.MultipleImaging_DataRecording_right_frame = QFrame(self.MultipleImaging_DataRecording_box)
        self.MultipleImaging_DataRecording_right_frame.setObjectName(u"MultipleImaging_DataRecording_right_frame")
        self.MultipleImaging_DataRecording_right_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_DataRecording_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.MultipleImaging_DataRecording_right_frame)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_DataRecording_directory_frame = QFrame(self.MultipleImaging_DataRecording_right_frame)
        self.MultipleImaging_DataRecording_directory_frame.setObjectName(u"MultipleImaging_DataRecording_directory_frame")
        self.MultipleImaging_DataRecording_directory_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_DataRecording_directory_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_426 = QHBoxLayout(self.MultipleImaging_DataRecording_directory_frame)
        self.horizontalLayout_426.setSpacing(10)
        self.horizontalLayout_426.setObjectName(u"horizontalLayout_426")
        self.horizontalLayout_426.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_DataRecording_SelectRecordFolder_label = QLabel(self.MultipleImaging_DataRecording_directory_frame)
        self.MultipleImaging_DataRecording_SelectRecordFolder_label.setObjectName(u"MultipleImaging_DataRecording_SelectRecordFolder_label")

        self.horizontalLayout_426.addWidget(self.MultipleImaging_DataRecording_SelectRecordFolder_label)

        self.MultipleImaging_DataRecording_RecordFolder_value = QLineEdit(self.MultipleImaging_DataRecording_directory_frame)
        self.MultipleImaging_DataRecording_RecordFolder_value.setObjectName(u"MultipleImaging_DataRecording_RecordFolder_value")
        self.MultipleImaging_DataRecording_RecordFolder_value.setEnabled(False)

        self.horizontalLayout_426.addWidget(self.MultipleImaging_DataRecording_RecordFolder_value)

        self.MultipleImaging_DataRecording_RecordFolderDir_pushButton = QPushButton(self.MultipleImaging_DataRecording_directory_frame)
        self.MultipleImaging_DataRecording_RecordFolderDir_pushButton.setObjectName(u"MultipleImaging_DataRecording_RecordFolderDir_pushButton")
        self.MultipleImaging_DataRecording_RecordFolderDir_pushButton.setMinimumSize(QSize(150, 0))
        self.MultipleImaging_DataRecording_RecordFolderDir_pushButton.setFont(font4)

        self.horizontalLayout_426.addWidget(self.MultipleImaging_DataRecording_RecordFolderDir_pushButton)


        self.verticalLayout_108.addWidget(self.MultipleImaging_DataRecording_directory_frame)

        self.MultipleImaging_DataRecording_record_frame = QFrame(self.MultipleImaging_DataRecording_right_frame)
        self.MultipleImaging_DataRecording_record_frame.setObjectName(u"MultipleImaging_DataRecording_record_frame")
        self.MultipleImaging_DataRecording_record_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_DataRecording_record_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_427 = QHBoxLayout(self.MultipleImaging_DataRecording_record_frame)
        self.horizontalLayout_427.setSpacing(0)
        self.horizontalLayout_427.setObjectName(u"horizontalLayout_427")
        self.horizontalLayout_427.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_SelectedFolderLabel = QLabel(self.MultipleImaging_DataRecording_record_frame)
        self.MultipleImaging_SelectedFolderLabel.setObjectName(u"MultipleImaging_SelectedFolderLabel")
        sizePolicy3.setHeightForWidth(self.MultipleImaging_SelectedFolderLabel.sizePolicy().hasHeightForWidth())
        self.MultipleImaging_SelectedFolderLabel.setSizePolicy(sizePolicy3)
        self.MultipleImaging_SelectedFolderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_427.addWidget(self.MultipleImaging_SelectedFolderLabel)

        self.MultipleImaging_DataRecording_Record_pushButton = QPushButton(self.MultipleImaging_DataRecording_record_frame)
        self.MultipleImaging_DataRecording_Record_pushButton.setObjectName(u"MultipleImaging_DataRecording_Record_pushButton")
        sizePolicy6.setHeightForWidth(self.MultipleImaging_DataRecording_Record_pushButton.sizePolicy().hasHeightForWidth())
        self.MultipleImaging_DataRecording_Record_pushButton.setSizePolicy(sizePolicy6)
        self.MultipleImaging_DataRecording_Record_pushButton.setMinimumSize(QSize(150, 0))
        self.MultipleImaging_DataRecording_Record_pushButton.setFont(font5)
        self.MultipleImaging_DataRecording_Record_pushButton.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"background-color: rgb(220, 50, 47);")

        self.horizontalLayout_427.addWidget(self.MultipleImaging_DataRecording_Record_pushButton)


        self.verticalLayout_108.addWidget(self.MultipleImaging_DataRecording_record_frame)


        self.horizontalLayout_415.addWidget(self.MultipleImaging_DataRecording_right_frame)


        self.verticalLayout_84.addWidget(self.MultipleImaging_DataRecording_box)


        self.horizontalLayout_380.addWidget(self.MultipleImaging_widget)

        self.MultipleImaging_CenterMenuContainer = QFrame(self.page_202)
        self.MultipleImaging_CenterMenuContainer.setObjectName(u"MultipleImaging_CenterMenuContainer")
        self.MultipleImaging_CenterMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.MultipleImaging_CenterMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CenterMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.MultipleImaging_CenterMenuContainer)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_parameter_exit_frame = QFrame(self.MultipleImaging_CenterMenuContainer)
        self.MultipleImaging_parameter_exit_frame.setObjectName(u"MultipleImaging_parameter_exit_frame")
        self.MultipleImaging_parameter_exit_frame.setMinimumSize(QSize(200, 0))
        self.MultipleImaging_parameter_exit_frame.setMaximumSize(QSize(200, 16777215))
        self.MultipleImaging_parameter_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_parameter_exit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.MultipleImaging_parameter_exit_frame)
        self.horizontalLayout_156.setSpacing(0)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_parameter_exit_pushButton = QPushButton(self.MultipleImaging_parameter_exit_frame)
        self.MultipleImaging_parameter_exit_pushButton.setObjectName(u"MultipleImaging_parameter_exit_pushButton")
        self.MultipleImaging_parameter_exit_pushButton.setIcon(icon18)
        self.MultipleImaging_parameter_exit_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_156.addWidget(self.MultipleImaging_parameter_exit_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_86.addWidget(self.MultipleImaging_parameter_exit_frame)

        self.MultipleImaging_parameter_stackedWidget = QStackedWidget(self.MultipleImaging_CenterMenuContainer)
        self.MultipleImaging_parameter_stackedWidget.setObjectName(u"MultipleImaging_parameter_stackedWidget")
        self.MultipleImaging_parameter_stackedWidget.setMaximumSize(QSize(200, 16777215))
        self.MultipleImaging_ImagingParameter_page = QWidget()
        self.MultipleImaging_ImagingParameter_page.setObjectName(u"MultipleImaging_ImagingParameter_page")
        self.verticalLayout_147 = QVBoxLayout(self.MultipleImaging_ImagingParameter_page)
        self.verticalLayout_147.setSpacing(0)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_frame = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.MultipleImaging_GECI_frame.setObjectName(u"MultipleImaging_GECI_frame")
        self.MultipleImaging_GECI_frame.setMaximumSize(QSize(16777215, 16777215))
        self.MultipleImaging_GECI_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.MultipleImaging_GECI_frame)
        self.verticalLayout_87.setSpacing(10)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(5, 10, 5, 10)
        self.MultipleImaging_GECI_Label_frame = QFrame(self.MultipleImaging_GECI_frame)
        self.MultipleImaging_GECI_Label_frame.setObjectName(u"MultipleImaging_GECI_Label_frame")
        self.MultipleImaging_GECI_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_306 = QHBoxLayout(self.MultipleImaging_GECI_Label_frame)
        self.horizontalLayout_306.setSpacing(0)
        self.horizontalLayout_306.setObjectName(u"horizontalLayout_306")
        self.horizontalLayout_306.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_Label = QLabel(self.MultipleImaging_GECI_Label_frame)
        self.MultipleImaging_GECI_Label.setObjectName(u"MultipleImaging_GECI_Label")
        self.MultipleImaging_GECI_Label.setFont(font1)
        self.MultipleImaging_GECI_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_306.addWidget(self.MultipleImaging_GECI_Label)


        self.verticalLayout_87.addWidget(self.MultipleImaging_GECI_Label_frame)

        self.MultipleImaging_GECI_comboBox_frame = QFrame(self.MultipleImaging_GECI_frame)
        self.MultipleImaging_GECI_comboBox_frame.setObjectName(u"MultipleImaging_GECI_comboBox_frame")
        self.MultipleImaging_GECI_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_309 = QHBoxLayout(self.MultipleImaging_GECI_comboBox_frame)
        self.horizontalLayout_309.setSpacing(0)
        self.horizontalLayout_309.setObjectName(u"horizontalLayout_309")
        self.horizontalLayout_309.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_comboBox = QComboBox(self.MultipleImaging_GECI_comboBox_frame)
        self.MultipleImaging_GECI_comboBox.addItem("")
        self.MultipleImaging_GECI_comboBox.addItem("")
        self.MultipleImaging_GECI_comboBox.addItem("")
        self.MultipleImaging_GECI_comboBox.addItem("")
        self.MultipleImaging_GECI_comboBox.setObjectName(u"MultipleImaging_GECI_comboBox")

        self.horizontalLayout_309.addWidget(self.MultipleImaging_GECI_comboBox)


        self.verticalLayout_87.addWidget(self.MultipleImaging_GECI_comboBox_frame)

        self.MultipleImaging_GECI_Readings_frame = QFrame(self.MultipleImaging_GECI_frame)
        self.MultipleImaging_GECI_Readings_frame.setObjectName(u"MultipleImaging_GECI_Readings_frame")
        self.MultipleImaging_GECI_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_Readings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.MultipleImaging_GECI_Readings_frame)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_ReadingsAffinity_frame = QFrame(self.MultipleImaging_GECI_Readings_frame)
        self.MultipleImaging_GECI_ReadingsAffinity_frame.setObjectName(u"MultipleImaging_GECI_ReadingsAffinity_frame")
        self.MultipleImaging_GECI_ReadingsAffinity_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_ReadingsAffinity_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_310 = QHBoxLayout(self.MultipleImaging_GECI_ReadingsAffinity_frame)
        self.horizontalLayout_310.setSpacing(0)
        self.horizontalLayout_310.setObjectName(u"horizontalLayout_310")
        self.horizontalLayout_310.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_ReadingsAffinity_Label = QLabel(self.MultipleImaging_GECI_ReadingsAffinity_frame)
        self.MultipleImaging_GECI_ReadingsAffinity_Label.setObjectName(u"MultipleImaging_GECI_ReadingsAffinity_Label")
        self.MultipleImaging_GECI_ReadingsAffinity_Label.setFont(font8)

        self.horizontalLayout_310.addWidget(self.MultipleImaging_GECI_ReadingsAffinity_Label)

        self.MultipleImaging_GECI_ReadingsAffinity_Value = QLabel(self.MultipleImaging_GECI_ReadingsAffinity_frame)
        self.MultipleImaging_GECI_ReadingsAffinity_Value.setObjectName(u"MultipleImaging_GECI_ReadingsAffinity_Value")
        self.MultipleImaging_GECI_ReadingsAffinity_Value.setFont(font8)
        self.MultipleImaging_GECI_ReadingsAffinity_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_310.addWidget(self.MultipleImaging_GECI_ReadingsAffinity_Value)


        self.verticalLayout_88.addWidget(self.MultipleImaging_GECI_ReadingsAffinity_frame)

        self.MultipleImaging_GECI_ReadingsKd_frame = QFrame(self.MultipleImaging_GECI_Readings_frame)
        self.MultipleImaging_GECI_ReadingsKd_frame.setObjectName(u"MultipleImaging_GECI_ReadingsKd_frame")
        self.MultipleImaging_GECI_ReadingsKd_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_ReadingsKd_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_312 = QHBoxLayout(self.MultipleImaging_GECI_ReadingsKd_frame)
        self.horizontalLayout_312.setSpacing(0)
        self.horizontalLayout_312.setObjectName(u"horizontalLayout_312")
        self.horizontalLayout_312.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_ReadingsKd_Label = QLabel(self.MultipleImaging_GECI_ReadingsKd_frame)
        self.MultipleImaging_GECI_ReadingsKd_Label.setObjectName(u"MultipleImaging_GECI_ReadingsKd_Label")
        self.MultipleImaging_GECI_ReadingsKd_Label.setFont(font8)

        self.horizontalLayout_312.addWidget(self.MultipleImaging_GECI_ReadingsKd_Label)

        self.MultipleImaging_GECI_ReadingsKd_Value = QLabel(self.MultipleImaging_GECI_ReadingsKd_frame)
        self.MultipleImaging_GECI_ReadingsKd_Value.setObjectName(u"MultipleImaging_GECI_ReadingsKd_Value")
        self.MultipleImaging_GECI_ReadingsKd_Value.setFont(font8)
        self.MultipleImaging_GECI_ReadingsKd_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_312.addWidget(self.MultipleImaging_GECI_ReadingsKd_Value)


        self.verticalLayout_88.addWidget(self.MultipleImaging_GECI_ReadingsKd_frame)

        self.MultipleImaging_GECI_ReadingsBrightness_frame = QFrame(self.MultipleImaging_GECI_Readings_frame)
        self.MultipleImaging_GECI_ReadingsBrightness_frame.setObjectName(u"MultipleImaging_GECI_ReadingsBrightness_frame")
        self.MultipleImaging_GECI_ReadingsBrightness_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_GECI_ReadingsBrightness_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_313 = QHBoxLayout(self.MultipleImaging_GECI_ReadingsBrightness_frame)
        self.horizontalLayout_313.setSpacing(0)
        self.horizontalLayout_313.setObjectName(u"horizontalLayout_313")
        self.horizontalLayout_313.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_GECI_ReadingsBrightness_Label = QLabel(self.MultipleImaging_GECI_ReadingsBrightness_frame)
        self.MultipleImaging_GECI_ReadingsBrightness_Label.setObjectName(u"MultipleImaging_GECI_ReadingsBrightness_Label")
        self.MultipleImaging_GECI_ReadingsBrightness_Label.setFont(font8)

        self.horizontalLayout_313.addWidget(self.MultipleImaging_GECI_ReadingsBrightness_Label)

        self.MultipleImaging_GECI_ReadingsBrightness_Value = QLabel(self.MultipleImaging_GECI_ReadingsBrightness_frame)
        self.MultipleImaging_GECI_ReadingsBrightness_Value.setObjectName(u"MultipleImaging_GECI_ReadingsBrightness_Value")
        self.MultipleImaging_GECI_ReadingsBrightness_Value.setFont(font8)
        self.MultipleImaging_GECI_ReadingsBrightness_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_313.addWidget(self.MultipleImaging_GECI_ReadingsBrightness_Value)


        self.verticalLayout_88.addWidget(self.MultipleImaging_GECI_ReadingsBrightness_frame)


        self.verticalLayout_87.addWidget(self.MultipleImaging_GECI_Readings_frame)


        self.verticalLayout_147.addWidget(self.MultipleImaging_GECI_frame)

        self.line_55 = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_55.setFrameShape(QFrame.Shape.HLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_147.addWidget(self.line_55)

        self.MultipleImaging_FrameRate_frame = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.MultipleImaging_FrameRate_frame.setObjectName(u"MultipleImaging_FrameRate_frame")
        self.MultipleImaging_FrameRate_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.MultipleImaging_FrameRate_frame)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_FrameRate_Title_frame = QFrame(self.MultipleImaging_FrameRate_frame)
        self.MultipleImaging_FrameRate_Title_frame.setObjectName(u"MultipleImaging_FrameRate_Title_frame")
        self.MultipleImaging_FrameRate_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_314 = QHBoxLayout(self.MultipleImaging_FrameRate_Title_frame)
        self.horizontalLayout_314.setSpacing(0)
        self.horizontalLayout_314.setObjectName(u"horizontalLayout_314")
        self.horizontalLayout_314.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FrameRate_Toggle_frame = QFrame(self.MultipleImaging_FrameRate_Title_frame)
        self.MultipleImaging_FrameRate_Toggle_frame.setObjectName(u"MultipleImaging_FrameRate_Toggle_frame")
        self.MultipleImaging_FrameRate_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.MultipleImaging_FrameRate_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_FrameRate_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_FrameRate_Toggle_layout = QHBoxLayout(self.MultipleImaging_FrameRate_Toggle_frame)
        self.MultipleImaging_FrameRate_Toggle_layout.setSpacing(0)
        self.MultipleImaging_FrameRate_Toggle_layout.setObjectName(u"MultipleImaging_FrameRate_Toggle_layout")
        self.MultipleImaging_FrameRate_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_314.addWidget(self.MultipleImaging_FrameRate_Toggle_frame)

        self.MultipleImaging_FrameRate_Label_frame = QFrame(self.MultipleImaging_FrameRate_Title_frame)
        self.MultipleImaging_FrameRate_Label_frame.setObjectName(u"MultipleImaging_FrameRate_Label_frame")
        self.MultipleImaging_FrameRate_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_315 = QHBoxLayout(self.MultipleImaging_FrameRate_Label_frame)
        self.horizontalLayout_315.setSpacing(0)
        self.horizontalLayout_315.setObjectName(u"horizontalLayout_315")
        self.horizontalLayout_315.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FrameRate_Label = QLabel(self.MultipleImaging_FrameRate_Label_frame)
        self.MultipleImaging_FrameRate_Label.setObjectName(u"MultipleImaging_FrameRate_Label")
        self.MultipleImaging_FrameRate_Label.setWordWrap(True)

        self.horizontalLayout_315.addWidget(self.MultipleImaging_FrameRate_Label)


        self.horizontalLayout_314.addWidget(self.MultipleImaging_FrameRate_Label_frame)


        self.verticalLayout_148.addWidget(self.MultipleImaging_FrameRate_Title_frame)

        self.MultipleImaging_FrameRate_Readings_frame = QFrame(self.MultipleImaging_FrameRate_frame)
        self.MultipleImaging_FrameRate_Readings_frame.setObjectName(u"MultipleImaging_FrameRate_Readings_frame")
        self.MultipleImaging_FrameRate_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_316 = QHBoxLayout(self.MultipleImaging_FrameRate_Readings_frame)
        self.horizontalLayout_316.setSpacing(0)
        self.horizontalLayout_316.setObjectName(u"horizontalLayout_316")
        self.horizontalLayout_316.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FrameRate_Readings = QLabel(self.MultipleImaging_FrameRate_Readings_frame)
        self.MultipleImaging_FrameRate_Readings.setObjectName(u"MultipleImaging_FrameRate_Readings")
        self.MultipleImaging_FrameRate_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_316.addWidget(self.MultipleImaging_FrameRate_Readings)


        self.verticalLayout_148.addWidget(self.MultipleImaging_FrameRate_Readings_frame)

        self.MultipleImaging_FrameRate_Slider_frame = QFrame(self.MultipleImaging_FrameRate_frame)
        self.MultipleImaging_FrameRate_Slider_frame.setObjectName(u"MultipleImaging_FrameRate_Slider_frame")
        self.MultipleImaging_FrameRate_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Slider_frame.setFrameShadow(QFrame.Raised)
        self.Imaging_FrameRate_toggle_layout_2 = QHBoxLayout(self.MultipleImaging_FrameRate_Slider_frame)
        self.Imaging_FrameRate_toggle_layout_2.setSpacing(0)
        self.Imaging_FrameRate_toggle_layout_2.setObjectName(u"Imaging_FrameRate_toggle_layout_2")
        self.Imaging_FrameRate_toggle_layout_2.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FrameRate_Slider = QSlider(self.MultipleImaging_FrameRate_Slider_frame)
        self.MultipleImaging_FrameRate_Slider.setObjectName(u"MultipleImaging_FrameRate_Slider")
        self.MultipleImaging_FrameRate_Slider.setEnabled(False)
        self.MultipleImaging_FrameRate_Slider.setMinimum(1)
        self.MultipleImaging_FrameRate_Slider.setMaximum(1000)
        self.MultipleImaging_FrameRate_Slider.setSingleStep(10)
        self.MultipleImaging_FrameRate_Slider.setValue(250)
        self.MultipleImaging_FrameRate_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_FrameRate_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_FrameRate_Slider.setTickInterval(100)

        self.Imaging_FrameRate_toggle_layout_2.addWidget(self.MultipleImaging_FrameRate_Slider)


        self.verticalLayout_148.addWidget(self.MultipleImaging_FrameRate_Slider_frame)

        self.MultipleImaging_FrameRate_Values_frame = QFrame(self.MultipleImaging_FrameRate_frame)
        self.MultipleImaging_FrameRate_Values_frame.setObjectName(u"MultipleImaging_FrameRate_Values_frame")
        self.MultipleImaging_FrameRate_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FrameRate_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_317 = QHBoxLayout(self.MultipleImaging_FrameRate_Values_frame)
        self.horizontalLayout_317.setSpacing(0)
        self.horizontalLayout_317.setObjectName(u"horizontalLayout_317")
        self.horizontalLayout_317.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.MultipleImaging_FrameRate_Values_frame)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_317.addWidget(self.label_58)

        self.label_59 = QLabel(self.MultipleImaging_FrameRate_Values_frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_317.addWidget(self.label_59)

        self.label_60 = QLabel(self.MultipleImaging_FrameRate_Values_frame)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_317.addWidget(self.label_60)


        self.verticalLayout_148.addWidget(self.MultipleImaging_FrameRate_Values_frame)


        self.verticalLayout_147.addWidget(self.MultipleImaging_FrameRate_frame)

        self.line_56 = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_56.setFrameShape(QFrame.Shape.HLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_147.addWidget(self.line_56)

        self.MultipleImaging_PMT_frame = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.MultipleImaging_PMT_frame.setObjectName(u"MultipleImaging_PMT_frame")
        self.MultipleImaging_PMT_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.MultipleImaging_PMT_frame)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_PMT_Title_frame = QFrame(self.MultipleImaging_PMT_frame)
        self.MultipleImaging_PMT_Title_frame.setObjectName(u"MultipleImaging_PMT_Title_frame")
        self.MultipleImaging_PMT_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_318 = QHBoxLayout(self.MultipleImaging_PMT_Title_frame)
        self.horizontalLayout_318.setSpacing(0)
        self.horizontalLayout_318.setObjectName(u"horizontalLayout_318")
        self.horizontalLayout_318.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PMT_Toggle_frame = QFrame(self.MultipleImaging_PMT_Title_frame)
        self.MultipleImaging_PMT_Toggle_frame.setObjectName(u"MultipleImaging_PMT_Toggle_frame")
        self.MultipleImaging_PMT_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.MultipleImaging_PMT_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_PMT_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_PMT_Toggle_layout = QHBoxLayout(self.MultipleImaging_PMT_Toggle_frame)
        self.MultipleImaging_PMT_Toggle_layout.setSpacing(0)
        self.MultipleImaging_PMT_Toggle_layout.setObjectName(u"MultipleImaging_PMT_Toggle_layout")
        self.MultipleImaging_PMT_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_318.addWidget(self.MultipleImaging_PMT_Toggle_frame)

        self.MultipleImaging_PMT_Label_frame = QFrame(self.MultipleImaging_PMT_Title_frame)
        self.MultipleImaging_PMT_Label_frame.setObjectName(u"MultipleImaging_PMT_Label_frame")
        self.MultipleImaging_PMT_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_319 = QHBoxLayout(self.MultipleImaging_PMT_Label_frame)
        self.horizontalLayout_319.setSpacing(0)
        self.horizontalLayout_319.setObjectName(u"horizontalLayout_319")
        self.horizontalLayout_319.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PMT_Label = QLabel(self.MultipleImaging_PMT_Label_frame)
        self.MultipleImaging_PMT_Label.setObjectName(u"MultipleImaging_PMT_Label")
        self.MultipleImaging_PMT_Label.setWordWrap(True)

        self.horizontalLayout_319.addWidget(self.MultipleImaging_PMT_Label)


        self.horizontalLayout_318.addWidget(self.MultipleImaging_PMT_Label_frame)


        self.verticalLayout_149.addWidget(self.MultipleImaging_PMT_Title_frame)

        self.MultipleImaging_PMT_Readings_frame = QFrame(self.MultipleImaging_PMT_frame)
        self.MultipleImaging_PMT_Readings_frame.setObjectName(u"MultipleImaging_PMT_Readings_frame")
        self.MultipleImaging_PMT_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_320 = QHBoxLayout(self.MultipleImaging_PMT_Readings_frame)
        self.horizontalLayout_320.setSpacing(0)
        self.horizontalLayout_320.setObjectName(u"horizontalLayout_320")
        self.horizontalLayout_320.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PMT_Readings = QLabel(self.MultipleImaging_PMT_Readings_frame)
        self.MultipleImaging_PMT_Readings.setObjectName(u"MultipleImaging_PMT_Readings")
        self.MultipleImaging_PMT_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_320.addWidget(self.MultipleImaging_PMT_Readings)


        self.verticalLayout_149.addWidget(self.MultipleImaging_PMT_Readings_frame)

        self.MultipleImaging_PMT_Slider_frame = QFrame(self.MultipleImaging_PMT_frame)
        self.MultipleImaging_PMT_Slider_frame.setObjectName(u"MultipleImaging_PMT_Slider_frame")
        self.MultipleImaging_PMT_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_321 = QHBoxLayout(self.MultipleImaging_PMT_Slider_frame)
        self.horizontalLayout_321.setSpacing(0)
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.horizontalLayout_321.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PMT_Slider = QSlider(self.MultipleImaging_PMT_Slider_frame)
        self.MultipleImaging_PMT_Slider.setObjectName(u"MultipleImaging_PMT_Slider")
        self.MultipleImaging_PMT_Slider.setEnabled(False)
        self.MultipleImaging_PMT_Slider.setMaximum(200)
        self.MultipleImaging_PMT_Slider.setValue(100)
        self.MultipleImaging_PMT_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_PMT_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_PMT_Slider.setTickInterval(20)

        self.horizontalLayout_321.addWidget(self.MultipleImaging_PMT_Slider)


        self.verticalLayout_149.addWidget(self.MultipleImaging_PMT_Slider_frame)

        self.MultipleImaging_PMT_Values_frame = QFrame(self.MultipleImaging_PMT_frame)
        self.MultipleImaging_PMT_Values_frame.setObjectName(u"MultipleImaging_PMT_Values_frame")
        self.MultipleImaging_PMT_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PMT_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_322 = QHBoxLayout(self.MultipleImaging_PMT_Values_frame)
        self.horizontalLayout_322.setSpacing(0)
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.horizontalLayout_322.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.MultipleImaging_PMT_Values_frame)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_322.addWidget(self.label_61)

        self.label_62 = QLabel(self.MultipleImaging_PMT_Values_frame)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_322.addWidget(self.label_62)

        self.label_63 = QLabel(self.MultipleImaging_PMT_Values_frame)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_322.addWidget(self.label_63)


        self.verticalLayout_149.addWidget(self.MultipleImaging_PMT_Values_frame)


        self.verticalLayout_147.addWidget(self.MultipleImaging_PMT_frame)

        self.line_57 = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_57.setFrameShape(QFrame.Shape.HLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_147.addWidget(self.line_57)

        self.MultipleImaging_Laser_frame = QFrame(self.MultipleImaging_ImagingParameter_page)
        self.MultipleImaging_Laser_frame.setObjectName(u"MultipleImaging_Laser_frame")
        self.MultipleImaging_Laser_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.MultipleImaging_Laser_frame)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_Laser_Title_frame = QFrame(self.MultipleImaging_Laser_frame)
        self.MultipleImaging_Laser_Title_frame.setObjectName(u"MultipleImaging_Laser_Title_frame")
        self.MultipleImaging_Laser_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_323 = QHBoxLayout(self.MultipleImaging_Laser_Title_frame)
        self.horizontalLayout_323.setSpacing(0)
        self.horizontalLayout_323.setObjectName(u"horizontalLayout_323")
        self.horizontalLayout_323.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Laser_Toggle_frame = QFrame(self.MultipleImaging_Laser_Title_frame)
        self.MultipleImaging_Laser_Toggle_frame.setObjectName(u"MultipleImaging_Laser_Toggle_frame")
        self.MultipleImaging_Laser_Toggle_frame.setMinimumSize(QSize(50, 0))
        self.MultipleImaging_Laser_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_Laser_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_Laser_Toggle_layout = QHBoxLayout(self.MultipleImaging_Laser_Toggle_frame)
        self.MultipleImaging_Laser_Toggle_layout.setSpacing(0)
        self.MultipleImaging_Laser_Toggle_layout.setObjectName(u"MultipleImaging_Laser_Toggle_layout")
        self.MultipleImaging_Laser_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_323.addWidget(self.MultipleImaging_Laser_Toggle_frame)

        self.MultipleImaging_Laser_Label_frame = QFrame(self.MultipleImaging_Laser_Title_frame)
        self.MultipleImaging_Laser_Label_frame.setObjectName(u"MultipleImaging_Laser_Label_frame")
        self.MultipleImaging_Laser_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_324 = QHBoxLayout(self.MultipleImaging_Laser_Label_frame)
        self.horizontalLayout_324.setSpacing(0)
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.horizontalLayout_324.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Laser_Label = QLabel(self.MultipleImaging_Laser_Label_frame)
        self.MultipleImaging_Laser_Label.setObjectName(u"MultipleImaging_Laser_Label")
        self.MultipleImaging_Laser_Label.setWordWrap(True)

        self.horizontalLayout_324.addWidget(self.MultipleImaging_Laser_Label)


        self.horizontalLayout_323.addWidget(self.MultipleImaging_Laser_Label_frame)


        self.verticalLayout_150.addWidget(self.MultipleImaging_Laser_Title_frame)

        self.MultipleImaging_Laser_Readings_frame = QFrame(self.MultipleImaging_Laser_frame)
        self.MultipleImaging_Laser_Readings_frame.setObjectName(u"MultipleImaging_Laser_Readings_frame")
        self.MultipleImaging_Laser_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_325 = QHBoxLayout(self.MultipleImaging_Laser_Readings_frame)
        self.horizontalLayout_325.setSpacing(0)
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.horizontalLayout_325.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Laser_Readings = QLabel(self.MultipleImaging_Laser_Readings_frame)
        self.MultipleImaging_Laser_Readings.setObjectName(u"MultipleImaging_Laser_Readings")
        self.MultipleImaging_Laser_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_325.addWidget(self.MultipleImaging_Laser_Readings)


        self.verticalLayout_150.addWidget(self.MultipleImaging_Laser_Readings_frame)

        self.MultipleImaging_Laser_Slider_frame = QFrame(self.MultipleImaging_Laser_frame)
        self.MultipleImaging_Laser_Slider_frame.setObjectName(u"MultipleImaging_Laser_Slider_frame")
        self.MultipleImaging_Laser_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Laser_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_326 = QHBoxLayout(self.MultipleImaging_Laser_Slider_frame)
        self.horizontalLayout_326.setSpacing(0)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Laser_Slider = QSlider(self.MultipleImaging_Laser_Slider_frame)
        self.MultipleImaging_Laser_Slider.setObjectName(u"MultipleImaging_Laser_Slider")
        self.MultipleImaging_Laser_Slider.setEnabled(False)
        self.MultipleImaging_Laser_Slider.setMaximum(200)
        self.MultipleImaging_Laser_Slider.setValue(100)
        self.MultipleImaging_Laser_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_Laser_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_Laser_Slider.setTickInterval(20)

        self.horizontalLayout_326.addWidget(self.MultipleImaging_Laser_Slider)


        self.verticalLayout_150.addWidget(self.MultipleImaging_Laser_Slider_frame)

        self.frame_18 = QFrame(self.MultipleImaging_Laser_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_327 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_327.setSpacing(0)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_327.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_18)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_327.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_18)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_327.addWidget(self.label_65)

        self.label_66 = QLabel(self.frame_18)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_327.addWidget(self.label_66)


        self.verticalLayout_150.addWidget(self.frame_18)


        self.verticalLayout_147.addWidget(self.MultipleImaging_Laser_frame)

        self.MultipleImaging_parameter_stackedWidget.addWidget(self.MultipleImaging_ImagingParameter_page)
        self.MultipleImaging_CalciumParameter_page = QWidget()
        self.MultipleImaging_CalciumParameter_page.setObjectName(u"MultipleImaging_CalciumParameter_page")
        self.verticalLayout_151 = QVBoxLayout(self.MultipleImaging_CalciumParameter_page)
        self.verticalLayout_151.setSpacing(5)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 5, 0, 5)
        self.MultipleImaging_CalciumDecay_frame = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.MultipleImaging_CalciumDecay_frame.setObjectName(u"MultipleImaging_CalciumDecay_frame")
        self.MultipleImaging_CalciumDecay_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.MultipleImaging_CalciumDecay_frame)
        self.verticalLayout_152.setSpacing(0)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_CalciumDecay_Title_frame = QFrame(self.MultipleImaging_CalciumDecay_frame)
        self.MultipleImaging_CalciumDecay_Title_frame.setObjectName(u"MultipleImaging_CalciumDecay_Title_frame")
        self.MultipleImaging_CalciumDecay_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_328 = QHBoxLayout(self.MultipleImaging_CalciumDecay_Title_frame)
        self.horizontalLayout_328.setSpacing(0)
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.horizontalLayout_328.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumDecay_Toggle_frame = QFrame(self.MultipleImaging_CalciumDecay_Title_frame)
        self.MultipleImaging_CalciumDecay_Toggle_frame.setObjectName(u"MultipleImaging_CalciumDecay_Toggle_frame")
        self.MultipleImaging_CalciumDecay_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_CalciumDecay_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_CalciumDecay_Toggle_layout = QHBoxLayout(self.MultipleImaging_CalciumDecay_Toggle_frame)
        self.MultipleImaging_CalciumDecay_Toggle_layout.setSpacing(0)
        self.MultipleImaging_CalciumDecay_Toggle_layout.setObjectName(u"MultipleImaging_CalciumDecay_Toggle_layout")
        self.MultipleImaging_CalciumDecay_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_328.addWidget(self.MultipleImaging_CalciumDecay_Toggle_frame)

        self.MultipleImaging_CalciumDecay_Label_frame = QFrame(self.MultipleImaging_CalciumDecay_Title_frame)
        self.MultipleImaging_CalciumDecay_Label_frame.setObjectName(u"MultipleImaging_CalciumDecay_Label_frame")
        self.MultipleImaging_CalciumDecay_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_329 = QHBoxLayout(self.MultipleImaging_CalciumDecay_Label_frame)
        self.horizontalLayout_329.setSpacing(0)
        self.horizontalLayout_329.setObjectName(u"horizontalLayout_329")
        self.horizontalLayout_329.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumDecay_Label = QLabel(self.MultipleImaging_CalciumDecay_Label_frame)
        self.MultipleImaging_CalciumDecay_Label.setObjectName(u"MultipleImaging_CalciumDecay_Label")
        self.MultipleImaging_CalciumDecay_Label.setWordWrap(True)

        self.horizontalLayout_329.addWidget(self.MultipleImaging_CalciumDecay_Label)


        self.horizontalLayout_328.addWidget(self.MultipleImaging_CalciumDecay_Label_frame)


        self.verticalLayout_152.addWidget(self.MultipleImaging_CalciumDecay_Title_frame)

        self.MultipleImaging_CalciumDecay_Readings_frame = QFrame(self.MultipleImaging_CalciumDecay_frame)
        self.MultipleImaging_CalciumDecay_Readings_frame.setObjectName(u"MultipleImaging_CalciumDecay_Readings_frame")
        self.MultipleImaging_CalciumDecay_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_330 = QHBoxLayout(self.MultipleImaging_CalciumDecay_Readings_frame)
        self.horizontalLayout_330.setSpacing(0)
        self.horizontalLayout_330.setObjectName(u"horizontalLayout_330")
        self.horizontalLayout_330.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumDecay_Readings = QLabel(self.MultipleImaging_CalciumDecay_Readings_frame)
        self.MultipleImaging_CalciumDecay_Readings.setObjectName(u"MultipleImaging_CalciumDecay_Readings")
        self.MultipleImaging_CalciumDecay_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_330.addWidget(self.MultipleImaging_CalciumDecay_Readings)


        self.verticalLayout_152.addWidget(self.MultipleImaging_CalciumDecay_Readings_frame)

        self.MultipleImaging_CalciumDecay_Slider_frame = QFrame(self.MultipleImaging_CalciumDecay_frame)
        self.MultipleImaging_CalciumDecay_Slider_frame.setObjectName(u"MultipleImaging_CalciumDecay_Slider_frame")
        self.MultipleImaging_CalciumDecay_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumDecay_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_331 = QHBoxLayout(self.MultipleImaging_CalciumDecay_Slider_frame)
        self.horizontalLayout_331.setSpacing(0)
        self.horizontalLayout_331.setObjectName(u"horizontalLayout_331")
        self.horizontalLayout_331.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumDecay_Slider = QSlider(self.MultipleImaging_CalciumDecay_Slider_frame)
        self.MultipleImaging_CalciumDecay_Slider.setObjectName(u"MultipleImaging_CalciumDecay_Slider")
        self.MultipleImaging_CalciumDecay_Slider.setEnabled(False)
        self.MultipleImaging_CalciumDecay_Slider.setMinimum(1)
        self.MultipleImaging_CalciumDecay_Slider.setMaximum(200)
        self.MultipleImaging_CalciumDecay_Slider.setValue(50)
        self.MultipleImaging_CalciumDecay_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_CalciumDecay_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_CalciumDecay_Slider.setTickInterval(20)

        self.horizontalLayout_331.addWidget(self.MultipleImaging_CalciumDecay_Slider)


        self.verticalLayout_152.addWidget(self.MultipleImaging_CalciumDecay_Slider_frame)

        self.frame_19 = QFrame(self.MultipleImaging_CalciumDecay_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_332 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_332.setObjectName(u"horizontalLayout_332")
        self.label_67 = QLabel(self.frame_19)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_332.addWidget(self.label_67)

        self.label_68 = QLabel(self.frame_19)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_332.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_19)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_332.addWidget(self.label_69)


        self.verticalLayout_152.addWidget(self.frame_19)


        self.verticalLayout_151.addWidget(self.MultipleImaging_CalciumDecay_frame)

        self.line_58 = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_58.setFrameShape(QFrame.Shape.HLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_151.addWidget(self.line_58)

        self.MultipleImaging_CalciumJump_frame = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.MultipleImaging_CalciumJump_frame.setObjectName(u"MultipleImaging_CalciumJump_frame")
        self.MultipleImaging_CalciumJump_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.MultipleImaging_CalciumJump_frame)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_CalciumJump_Title_frame = QFrame(self.MultipleImaging_CalciumJump_frame)
        self.MultipleImaging_CalciumJump_Title_frame.setObjectName(u"MultipleImaging_CalciumJump_Title_frame")
        self.MultipleImaging_CalciumJump_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_333 = QHBoxLayout(self.MultipleImaging_CalciumJump_Title_frame)
        self.horizontalLayout_333.setSpacing(0)
        self.horizontalLayout_333.setObjectName(u"horizontalLayout_333")
        self.horizontalLayout_333.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumJump_Toggle_frame = QFrame(self.MultipleImaging_CalciumJump_Title_frame)
        self.MultipleImaging_CalciumJump_Toggle_frame.setObjectName(u"MultipleImaging_CalciumJump_Toggle_frame")
        self.MultipleImaging_CalciumJump_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_CalciumJump_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_CalciumJump_Toggle_layout = QHBoxLayout(self.MultipleImaging_CalciumJump_Toggle_frame)
        self.MultipleImaging_CalciumJump_Toggle_layout.setSpacing(0)
        self.MultipleImaging_CalciumJump_Toggle_layout.setObjectName(u"MultipleImaging_CalciumJump_Toggle_layout")
        self.MultipleImaging_CalciumJump_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_333.addWidget(self.MultipleImaging_CalciumJump_Toggle_frame)

        self.MultipleImaging_CalciumJump_Label_frame = QFrame(self.MultipleImaging_CalciumJump_Title_frame)
        self.MultipleImaging_CalciumJump_Label_frame.setObjectName(u"MultipleImaging_CalciumJump_Label_frame")
        self.MultipleImaging_CalciumJump_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_334 = QHBoxLayout(self.MultipleImaging_CalciumJump_Label_frame)
        self.horizontalLayout_334.setSpacing(0)
        self.horizontalLayout_334.setObjectName(u"horizontalLayout_334")
        self.horizontalLayout_334.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumJump_Label = QLabel(self.MultipleImaging_CalciumJump_Label_frame)
        self.MultipleImaging_CalciumJump_Label.setObjectName(u"MultipleImaging_CalciumJump_Label")
        self.MultipleImaging_CalciumJump_Label.setWordWrap(True)

        self.horizontalLayout_334.addWidget(self.MultipleImaging_CalciumJump_Label)


        self.horizontalLayout_333.addWidget(self.MultipleImaging_CalciumJump_Label_frame)


        self.verticalLayout_153.addWidget(self.MultipleImaging_CalciumJump_Title_frame)

        self.MultipleImaging_CalciumJump_Readings_frame = QFrame(self.MultipleImaging_CalciumJump_frame)
        self.MultipleImaging_CalciumJump_Readings_frame.setObjectName(u"MultipleImaging_CalciumJump_Readings_frame")
        self.MultipleImaging_CalciumJump_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_335 = QHBoxLayout(self.MultipleImaging_CalciumJump_Readings_frame)
        self.horizontalLayout_335.setSpacing(0)
        self.horizontalLayout_335.setObjectName(u"horizontalLayout_335")
        self.horizontalLayout_335.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumJump_Readings = QLabel(self.MultipleImaging_CalciumJump_Readings_frame)
        self.MultipleImaging_CalciumJump_Readings.setObjectName(u"MultipleImaging_CalciumJump_Readings")
        self.MultipleImaging_CalciumJump_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_335.addWidget(self.MultipleImaging_CalciumJump_Readings)


        self.verticalLayout_153.addWidget(self.MultipleImaging_CalciumJump_Readings_frame)

        self.MultipleImaging_CalciumJump_Slider_frame = QFrame(self.MultipleImaging_CalciumJump_frame)
        self.MultipleImaging_CalciumJump_Slider_frame.setObjectName(u"MultipleImaging_CalciumJump_Slider_frame")
        self.MultipleImaging_CalciumJump_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_336 = QHBoxLayout(self.MultipleImaging_CalciumJump_Slider_frame)
        self.horizontalLayout_336.setSpacing(0)
        self.horizontalLayout_336.setObjectName(u"horizontalLayout_336")
        self.horizontalLayout_336.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumJump_Slider = QSlider(self.MultipleImaging_CalciumJump_Slider_frame)
        self.MultipleImaging_CalciumJump_Slider.setObjectName(u"MultipleImaging_CalciumJump_Slider")
        self.MultipleImaging_CalciumJump_Slider.setEnabled(False)
        self.MultipleImaging_CalciumJump_Slider.setMinimum(1)
        self.MultipleImaging_CalciumJump_Slider.setMaximum(50)
        self.MultipleImaging_CalciumJump_Slider.setValue(5)
        self.MultipleImaging_CalciumJump_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_CalciumJump_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_CalciumJump_Slider.setTickInterval(5)

        self.horizontalLayout_336.addWidget(self.MultipleImaging_CalciumJump_Slider)


        self.verticalLayout_153.addWidget(self.MultipleImaging_CalciumJump_Slider_frame)

        self.MultipleImaging_CalciumJump_Values_frame = QFrame(self.MultipleImaging_CalciumJump_frame)
        self.MultipleImaging_CalciumJump_Values_frame.setObjectName(u"MultipleImaging_CalciumJump_Values_frame")
        self.MultipleImaging_CalciumJump_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumJump_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_337 = QHBoxLayout(self.MultipleImaging_CalciumJump_Values_frame)
        self.horizontalLayout_337.setSpacing(0)
        self.horizontalLayout_337.setObjectName(u"horizontalLayout_337")
        self.horizontalLayout_337.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.MultipleImaging_CalciumJump_Values_frame)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_337.addWidget(self.label_70)

        self.label_71 = QLabel(self.MultipleImaging_CalciumJump_Values_frame)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_337.addWidget(self.label_71)

        self.label_72 = QLabel(self.MultipleImaging_CalciumJump_Values_frame)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_337.addWidget(self.label_72)


        self.verticalLayout_153.addWidget(self.MultipleImaging_CalciumJump_Values_frame)


        self.verticalLayout_151.addWidget(self.MultipleImaging_CalciumJump_frame)

        self.line_59 = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_59.setFrameShape(QFrame.Shape.HLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_151.addWidget(self.line_59)

        self.MultipleImaging_CalciumNoise_frame = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.MultipleImaging_CalciumNoise_frame.setObjectName(u"MultipleImaging_CalciumNoise_frame")
        self.MultipleImaging_CalciumNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.MultipleImaging_CalciumNoise_frame)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_CalciumNoise_Title_frame = QFrame(self.MultipleImaging_CalciumNoise_frame)
        self.MultipleImaging_CalciumNoise_Title_frame.setObjectName(u"MultipleImaging_CalciumNoise_Title_frame")
        self.MultipleImaging_CalciumNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_338 = QHBoxLayout(self.MultipleImaging_CalciumNoise_Title_frame)
        self.horizontalLayout_338.setSpacing(0)
        self.horizontalLayout_338.setObjectName(u"horizontalLayout_338")
        self.horizontalLayout_338.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumNoise_Toggle_frame = QFrame(self.MultipleImaging_CalciumNoise_Title_frame)
        self.MultipleImaging_CalciumNoise_Toggle_frame.setObjectName(u"MultipleImaging_CalciumNoise_Toggle_frame")
        self.MultipleImaging_CalciumNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_CalciumNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_CalciumNoise_Toggle_layout = QHBoxLayout(self.MultipleImaging_CalciumNoise_Toggle_frame)
        self.MultipleImaging_CalciumNoise_Toggle_layout.setSpacing(0)
        self.MultipleImaging_CalciumNoise_Toggle_layout.setObjectName(u"MultipleImaging_CalciumNoise_Toggle_layout")
        self.MultipleImaging_CalciumNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_338.addWidget(self.MultipleImaging_CalciumNoise_Toggle_frame)

        self.MultipleImaging_CalciumNoise_Label_frame = QFrame(self.MultipleImaging_CalciumNoise_Title_frame)
        self.MultipleImaging_CalciumNoise_Label_frame.setObjectName(u"MultipleImaging_CalciumNoise_Label_frame")
        self.MultipleImaging_CalciumNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_339 = QHBoxLayout(self.MultipleImaging_CalciumNoise_Label_frame)
        self.horizontalLayout_339.setSpacing(0)
        self.horizontalLayout_339.setObjectName(u"horizontalLayout_339")
        self.horizontalLayout_339.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumNoise_Label = QLabel(self.MultipleImaging_CalciumNoise_Label_frame)
        self.MultipleImaging_CalciumNoise_Label.setObjectName(u"MultipleImaging_CalciumNoise_Label")

        self.horizontalLayout_339.addWidget(self.MultipleImaging_CalciumNoise_Label)


        self.horizontalLayout_338.addWidget(self.MultipleImaging_CalciumNoise_Label_frame)


        self.verticalLayout_154.addWidget(self.MultipleImaging_CalciumNoise_Title_frame)

        self.MultipleImaging_CalciumNoise_Readings_frame = QFrame(self.MultipleImaging_CalciumNoise_frame)
        self.MultipleImaging_CalciumNoise_Readings_frame.setObjectName(u"MultipleImaging_CalciumNoise_Readings_frame")
        self.MultipleImaging_CalciumNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_340 = QHBoxLayout(self.MultipleImaging_CalciumNoise_Readings_frame)
        self.horizontalLayout_340.setSpacing(0)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.horizontalLayout_340.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumNoise_Readings = QLabel(self.MultipleImaging_CalciumNoise_Readings_frame)
        self.MultipleImaging_CalciumNoise_Readings.setObjectName(u"MultipleImaging_CalciumNoise_Readings")
        self.MultipleImaging_CalciumNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_340.addWidget(self.MultipleImaging_CalciumNoise_Readings)


        self.verticalLayout_154.addWidget(self.MultipleImaging_CalciumNoise_Readings_frame)

        self.MultipleImaging_CalciumNoise_Slider_frame = QFrame(self.MultipleImaging_CalciumNoise_frame)
        self.MultipleImaging_CalciumNoise_Slider_frame.setObjectName(u"MultipleImaging_CalciumNoise_Slider_frame")
        self.MultipleImaging_CalciumNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_341 = QHBoxLayout(self.MultipleImaging_CalciumNoise_Slider_frame)
        self.horizontalLayout_341.setSpacing(0)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.horizontalLayout_341.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumNoise_Slider = QSlider(self.MultipleImaging_CalciumNoise_Slider_frame)
        self.MultipleImaging_CalciumNoise_Slider.setObjectName(u"MultipleImaging_CalciumNoise_Slider")
        self.MultipleImaging_CalciumNoise_Slider.setEnabled(False)
        self.MultipleImaging_CalciumNoise_Slider.setMaximum(100)
        self.MultipleImaging_CalciumNoise_Slider.setPageStep(10)
        self.MultipleImaging_CalciumNoise_Slider.setValue(10)
        self.MultipleImaging_CalciumNoise_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_CalciumNoise_Slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_341.addWidget(self.MultipleImaging_CalciumNoise_Slider)


        self.verticalLayout_154.addWidget(self.MultipleImaging_CalciumNoise_Slider_frame)

        self.MultipleImaging_CalciumNoise_Values_frame = QFrame(self.MultipleImaging_CalciumNoise_frame)
        self.MultipleImaging_CalciumNoise_Values_frame.setObjectName(u"MultipleImaging_CalciumNoise_Values_frame")
        self.MultipleImaging_CalciumNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_342 = QHBoxLayout(self.MultipleImaging_CalciumNoise_Values_frame)
        self.horizontalLayout_342.setSpacing(0)
        self.horizontalLayout_342.setObjectName(u"horizontalLayout_342")
        self.horizontalLayout_342.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.MultipleImaging_CalciumNoise_Values_frame)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_342.addWidget(self.label_73)

        self.label_74 = QLabel(self.MultipleImaging_CalciumNoise_Values_frame)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_342.addWidget(self.label_74)

        self.label_75 = QLabel(self.MultipleImaging_CalciumNoise_Values_frame)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_342.addWidget(self.label_75)


        self.verticalLayout_154.addWidget(self.MultipleImaging_CalciumNoise_Values_frame)


        self.verticalLayout_151.addWidget(self.MultipleImaging_CalciumNoise_frame)

        self.line_60 = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_151.addWidget(self.line_60)

        self.MultipleImaging_CalciumBaseline_frame = QFrame(self.MultipleImaging_CalciumParameter_page)
        self.MultipleImaging_CalciumBaseline_frame.setObjectName(u"MultipleImaging_CalciumBaseline_frame")
        self.MultipleImaging_CalciumBaseline_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.MultipleImaging_CalciumBaseline_frame)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_CalciumBaseline_Title_frame = QFrame(self.MultipleImaging_CalciumBaseline_frame)
        self.MultipleImaging_CalciumBaseline_Title_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Title_frame")
        self.MultipleImaging_CalciumBaseline_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_343 = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Title_frame)
        self.horizontalLayout_343.setSpacing(0)
        self.horizontalLayout_343.setObjectName(u"horizontalLayout_343")
        self.horizontalLayout_343.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumBaseline_Toggle_frame = QFrame(self.MultipleImaging_CalciumBaseline_Title_frame)
        self.MultipleImaging_CalciumBaseline_Toggle_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Toggle_frame")
        self.MultipleImaging_CalciumBaseline_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_CalciumBaseline_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_CalciumBaseline_Toggle_layout = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Toggle_frame)
        self.MultipleImaging_CalciumBaseline_Toggle_layout.setSpacing(0)
        self.MultipleImaging_CalciumBaseline_Toggle_layout.setObjectName(u"MultipleImaging_CalciumBaseline_Toggle_layout")
        self.MultipleImaging_CalciumBaseline_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_343.addWidget(self.MultipleImaging_CalciumBaseline_Toggle_frame)

        self.MultipleImaging_CalciumBaseline_Label_frame = QFrame(self.MultipleImaging_CalciumBaseline_Title_frame)
        self.MultipleImaging_CalciumBaseline_Label_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Label_frame")
        self.MultipleImaging_CalciumBaseline_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_344 = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Label_frame)
        self.horizontalLayout_344.setSpacing(0)
        self.horizontalLayout_344.setObjectName(u"horizontalLayout_344")
        self.horizontalLayout_344.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumBaseline_Label = QLabel(self.MultipleImaging_CalciumBaseline_Label_frame)
        self.MultipleImaging_CalciumBaseline_Label.setObjectName(u"MultipleImaging_CalciumBaseline_Label")
        self.MultipleImaging_CalciumBaseline_Label.setWordWrap(True)

        self.horizontalLayout_344.addWidget(self.MultipleImaging_CalciumBaseline_Label)


        self.horizontalLayout_343.addWidget(self.MultipleImaging_CalciumBaseline_Label_frame)


        self.verticalLayout_155.addWidget(self.MultipleImaging_CalciumBaseline_Title_frame)

        self.MultipleImaging_CalciumBaseline_Readings_frame = QFrame(self.MultipleImaging_CalciumBaseline_frame)
        self.MultipleImaging_CalciumBaseline_Readings_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Readings_frame")
        self.MultipleImaging_CalciumBaseline_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_345 = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Readings_frame)
        self.horizontalLayout_345.setSpacing(0)
        self.horizontalLayout_345.setObjectName(u"horizontalLayout_345")
        self.horizontalLayout_345.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumBaseline_Readings = QLabel(self.MultipleImaging_CalciumBaseline_Readings_frame)
        self.MultipleImaging_CalciumBaseline_Readings.setObjectName(u"MultipleImaging_CalciumBaseline_Readings")
        self.MultipleImaging_CalciumBaseline_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_345.addWidget(self.MultipleImaging_CalciumBaseline_Readings)


        self.verticalLayout_155.addWidget(self.MultipleImaging_CalciumBaseline_Readings_frame)

        self.MultipleImaging_CalciumBaseline_Slider_frame = QFrame(self.MultipleImaging_CalciumBaseline_frame)
        self.MultipleImaging_CalciumBaseline_Slider_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Slider_frame")
        self.MultipleImaging_CalciumBaseline_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_346 = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Slider_frame)
        self.horizontalLayout_346.setSpacing(0)
        self.horizontalLayout_346.setObjectName(u"horizontalLayout_346")
        self.horizontalLayout_346.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_CalciumBaseline_Slider = QSlider(self.MultipleImaging_CalciumBaseline_Slider_frame)
        self.MultipleImaging_CalciumBaseline_Slider.setObjectName(u"MultipleImaging_CalciumBaseline_Slider")
        self.MultipleImaging_CalciumBaseline_Slider.setEnabled(False)
        self.MultipleImaging_CalciumBaseline_Slider.setMinimum(1)
        self.MultipleImaging_CalciumBaseline_Slider.setMaximum(50)
        self.MultipleImaging_CalciumBaseline_Slider.setValue(10)
        self.MultipleImaging_CalciumBaseline_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_CalciumBaseline_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_CalciumBaseline_Slider.setTickInterval(10)

        self.horizontalLayout_346.addWidget(self.MultipleImaging_CalciumBaseline_Slider)


        self.verticalLayout_155.addWidget(self.MultipleImaging_CalciumBaseline_Slider_frame)

        self.MultipleImaging_CalciumBaseline_Values_frame = QFrame(self.MultipleImaging_CalciumBaseline_frame)
        self.MultipleImaging_CalciumBaseline_Values_frame.setObjectName(u"MultipleImaging_CalciumBaseline_Values_frame")
        self.MultipleImaging_CalciumBaseline_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_CalciumBaseline_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_347 = QHBoxLayout(self.MultipleImaging_CalciumBaseline_Values_frame)
        self.horizontalLayout_347.setSpacing(0)
        self.horizontalLayout_347.setObjectName(u"horizontalLayout_347")
        self.horizontalLayout_347.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.MultipleImaging_CalciumBaseline_Values_frame)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_347.addWidget(self.label_76)

        self.label_77 = QLabel(self.MultipleImaging_CalciumBaseline_Values_frame)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_347.addWidget(self.label_77)

        self.label_78 = QLabel(self.MultipleImaging_CalciumBaseline_Values_frame)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_347.addWidget(self.label_78)


        self.verticalLayout_155.addWidget(self.MultipleImaging_CalciumBaseline_Values_frame)


        self.verticalLayout_151.addWidget(self.MultipleImaging_CalciumBaseline_frame)

        self.MultipleImaging_parameter_stackedWidget.addWidget(self.MultipleImaging_CalciumParameter_page)
        self.MultipleImaging_FluoParameter_page = QWidget()
        self.MultipleImaging_FluoParameter_page.setObjectName(u"MultipleImaging_FluoParameter_page")
        self.verticalLayout_156 = QVBoxLayout(self.MultipleImaging_FluoParameter_page)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoScale_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_FluoScale_frame.setObjectName(u"MultipleImaging_FluoScale_frame")
        self.MultipleImaging_FluoScale_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.MultipleImaging_FluoScale_frame)
        self.verticalLayout_157.setSpacing(0)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_FluoScale_Title_frame = QFrame(self.MultipleImaging_FluoScale_frame)
        self.MultipleImaging_FluoScale_Title_frame.setObjectName(u"MultipleImaging_FluoScale_Title_frame")
        self.MultipleImaging_FluoScale_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_348 = QHBoxLayout(self.MultipleImaging_FluoScale_Title_frame)
        self.horizontalLayout_348.setSpacing(0)
        self.horizontalLayout_348.setObjectName(u"horizontalLayout_348")
        self.horizontalLayout_348.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoScale_Toggle_frame = QFrame(self.MultipleImaging_FluoScale_Title_frame)
        self.MultipleImaging_FluoScale_Toggle_frame.setObjectName(u"MultipleImaging_FluoScale_Toggle_frame")
        self.MultipleImaging_FluoScale_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_FluoScale_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_FluoScale_Toggle_layout = QHBoxLayout(self.MultipleImaging_FluoScale_Toggle_frame)
        self.MultipleImaging_FluoScale_Toggle_layout.setSpacing(0)
        self.MultipleImaging_FluoScale_Toggle_layout.setObjectName(u"MultipleImaging_FluoScale_Toggle_layout")
        self.MultipleImaging_FluoScale_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_348.addWidget(self.MultipleImaging_FluoScale_Toggle_frame)

        self.MultipleImaging_FluoScale_Label_frame = QFrame(self.MultipleImaging_FluoScale_Title_frame)
        self.MultipleImaging_FluoScale_Label_frame.setObjectName(u"MultipleImaging_FluoScale_Label_frame")
        self.MultipleImaging_FluoScale_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_349 = QHBoxLayout(self.MultipleImaging_FluoScale_Label_frame)
        self.horizontalLayout_349.setSpacing(0)
        self.horizontalLayout_349.setObjectName(u"horizontalLayout_349")
        self.horizontalLayout_349.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoScale_Label = QLabel(self.MultipleImaging_FluoScale_Label_frame)
        self.MultipleImaging_FluoScale_Label.setObjectName(u"MultipleImaging_FluoScale_Label")
        self.MultipleImaging_FluoScale_Label.setWordWrap(True)

        self.horizontalLayout_349.addWidget(self.MultipleImaging_FluoScale_Label)


        self.horizontalLayout_348.addWidget(self.MultipleImaging_FluoScale_Label_frame)


        self.verticalLayout_157.addWidget(self.MultipleImaging_FluoScale_Title_frame)

        self.MultipleImaging_FluoScale_Readings_frame = QFrame(self.MultipleImaging_FluoScale_frame)
        self.MultipleImaging_FluoScale_Readings_frame.setObjectName(u"MultipleImaging_FluoScale_Readings_frame")
        self.MultipleImaging_FluoScale_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_350 = QHBoxLayout(self.MultipleImaging_FluoScale_Readings_frame)
        self.horizontalLayout_350.setSpacing(0)
        self.horizontalLayout_350.setObjectName(u"horizontalLayout_350")
        self.horizontalLayout_350.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoScale_Readings = QLabel(self.MultipleImaging_FluoScale_Readings_frame)
        self.MultipleImaging_FluoScale_Readings.setObjectName(u"MultipleImaging_FluoScale_Readings")
        self.MultipleImaging_FluoScale_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_350.addWidget(self.MultipleImaging_FluoScale_Readings)


        self.verticalLayout_157.addWidget(self.MultipleImaging_FluoScale_Readings_frame)

        self.MultipleImaging_FluoScale_Slider_frame = QFrame(self.MultipleImaging_FluoScale_frame)
        self.MultipleImaging_FluoScale_Slider_frame.setObjectName(u"MultipleImaging_FluoScale_Slider_frame")
        self.MultipleImaging_FluoScale_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_351 = QHBoxLayout(self.MultipleImaging_FluoScale_Slider_frame)
        self.horizontalLayout_351.setSpacing(0)
        self.horizontalLayout_351.setObjectName(u"horizontalLayout_351")
        self.horizontalLayout_351.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoScale_Slider = QSlider(self.MultipleImaging_FluoScale_Slider_frame)
        self.MultipleImaging_FluoScale_Slider.setObjectName(u"MultipleImaging_FluoScale_Slider")
        self.MultipleImaging_FluoScale_Slider.setEnabled(False)
        self.MultipleImaging_FluoScale_Slider.setMinimum(0)
        self.MultipleImaging_FluoScale_Slider.setMaximum(100)
        self.MultipleImaging_FluoScale_Slider.setValue(10)
        self.MultipleImaging_FluoScale_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_FluoScale_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_FluoScale_Slider.setTickInterval(10)

        self.horizontalLayout_351.addWidget(self.MultipleImaging_FluoScale_Slider)


        self.verticalLayout_157.addWidget(self.MultipleImaging_FluoScale_Slider_frame)

        self.MultipleImaging_FluoScale_Values_frame = QFrame(self.MultipleImaging_FluoScale_frame)
        self.MultipleImaging_FluoScale_Values_frame.setObjectName(u"MultipleImaging_FluoScale_Values_frame")
        self.MultipleImaging_FluoScale_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoScale_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_352 = QHBoxLayout(self.MultipleImaging_FluoScale_Values_frame)
        self.horizontalLayout_352.setSpacing(0)
        self.horizontalLayout_352.setObjectName(u"horizontalLayout_352")
        self.horizontalLayout_352.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.MultipleImaging_FluoScale_Values_frame)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_352.addWidget(self.label_79)

        self.label_80 = QLabel(self.MultipleImaging_FluoScale_Values_frame)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_352.addWidget(self.label_80)

        self.label_81 = QLabel(self.MultipleImaging_FluoScale_Values_frame)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_352.addWidget(self.label_81)


        self.verticalLayout_157.addWidget(self.MultipleImaging_FluoScale_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_FluoScale_frame)

        self.line_61 = QFrame(self.MultipleImaging_FluoParameter_page)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_61.setFrameShape(QFrame.Shape.HLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.line_61)

        self.MultipleImaging_FluoOffset_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_FluoOffset_frame.setObjectName(u"MultipleImaging_FluoOffset_frame")
        self.MultipleImaging_FluoOffset_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.MultipleImaging_FluoOffset_frame)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_FluoOffset_Title_frame = QFrame(self.MultipleImaging_FluoOffset_frame)
        self.MultipleImaging_FluoOffset_Title_frame.setObjectName(u"MultipleImaging_FluoOffset_Title_frame")
        self.MultipleImaging_FluoOffset_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_353 = QHBoxLayout(self.MultipleImaging_FluoOffset_Title_frame)
        self.horizontalLayout_353.setSpacing(0)
        self.horizontalLayout_353.setObjectName(u"horizontalLayout_353")
        self.horizontalLayout_353.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoOffset_Toggle_frame = QFrame(self.MultipleImaging_FluoOffset_Title_frame)
        self.MultipleImaging_FluoOffset_Toggle_frame.setObjectName(u"MultipleImaging_FluoOffset_Toggle_frame")
        self.MultipleImaging_FluoOffset_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_FluoOffset_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_FluoOffset_Toggle_layout = QHBoxLayout(self.MultipleImaging_FluoOffset_Toggle_frame)
        self.MultipleImaging_FluoOffset_Toggle_layout.setSpacing(0)
        self.MultipleImaging_FluoOffset_Toggle_layout.setObjectName(u"MultipleImaging_FluoOffset_Toggle_layout")
        self.MultipleImaging_FluoOffset_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_353.addWidget(self.MultipleImaging_FluoOffset_Toggle_frame)

        self.MultipleImaging_FluoOffset_Label_frame = QFrame(self.MultipleImaging_FluoOffset_Title_frame)
        self.MultipleImaging_FluoOffset_Label_frame.setObjectName(u"MultipleImaging_FluoOffset_Label_frame")
        self.MultipleImaging_FluoOffset_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_354 = QHBoxLayout(self.MultipleImaging_FluoOffset_Label_frame)
        self.horizontalLayout_354.setSpacing(0)
        self.horizontalLayout_354.setObjectName(u"horizontalLayout_354")
        self.horizontalLayout_354.setContentsMargins(0, 0, 0, 0)
        self.Imaging_FluoOffset_Label_2 = QLabel(self.MultipleImaging_FluoOffset_Label_frame)
        self.Imaging_FluoOffset_Label_2.setObjectName(u"Imaging_FluoOffset_Label_2")
        self.Imaging_FluoOffset_Label_2.setWordWrap(True)

        self.horizontalLayout_354.addWidget(self.Imaging_FluoOffset_Label_2)


        self.horizontalLayout_353.addWidget(self.MultipleImaging_FluoOffset_Label_frame)


        self.verticalLayout_158.addWidget(self.MultipleImaging_FluoOffset_Title_frame)

        self.MultipleImaging_FluoOffset_Readings_frame = QFrame(self.MultipleImaging_FluoOffset_frame)
        self.MultipleImaging_FluoOffset_Readings_frame.setObjectName(u"MultipleImaging_FluoOffset_Readings_frame")
        self.MultipleImaging_FluoOffset_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_355 = QHBoxLayout(self.MultipleImaging_FluoOffset_Readings_frame)
        self.horizontalLayout_355.setSpacing(0)
        self.horizontalLayout_355.setObjectName(u"horizontalLayout_355")
        self.horizontalLayout_355.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoOffset_Readings = QLabel(self.MultipleImaging_FluoOffset_Readings_frame)
        self.MultipleImaging_FluoOffset_Readings.setObjectName(u"MultipleImaging_FluoOffset_Readings")
        self.MultipleImaging_FluoOffset_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_355.addWidget(self.MultipleImaging_FluoOffset_Readings)


        self.verticalLayout_158.addWidget(self.MultipleImaging_FluoOffset_Readings_frame)

        self.MultipleImaging_FluoOffset_Slider_frame = QFrame(self.MultipleImaging_FluoOffset_frame)
        self.MultipleImaging_FluoOffset_Slider_frame.setObjectName(u"MultipleImaging_FluoOffset_Slider_frame")
        self.MultipleImaging_FluoOffset_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_356 = QHBoxLayout(self.MultipleImaging_FluoOffset_Slider_frame)
        self.horizontalLayout_356.setSpacing(0)
        self.horizontalLayout_356.setObjectName(u"horizontalLayout_356")
        self.horizontalLayout_356.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoOffset_Slider = QSlider(self.MultipleImaging_FluoOffset_Slider_frame)
        self.MultipleImaging_FluoOffset_Slider.setObjectName(u"MultipleImaging_FluoOffset_Slider")
        self.MultipleImaging_FluoOffset_Slider.setEnabled(False)
        self.MultipleImaging_FluoOffset_Slider.setMaximum(20)
        self.MultipleImaging_FluoOffset_Slider.setValue(5)
        self.MultipleImaging_FluoOffset_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_FluoOffset_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_FluoOffset_Slider.setTickInterval(2)

        self.horizontalLayout_356.addWidget(self.MultipleImaging_FluoOffset_Slider)


        self.verticalLayout_158.addWidget(self.MultipleImaging_FluoOffset_Slider_frame)

        self.MultipleImaging_FluoOffset_Values_frame = QFrame(self.MultipleImaging_FluoOffset_frame)
        self.MultipleImaging_FluoOffset_Values_frame.setObjectName(u"MultipleImaging_FluoOffset_Values_frame")
        self.MultipleImaging_FluoOffset_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoOffset_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_357 = QHBoxLayout(self.MultipleImaging_FluoOffset_Values_frame)
        self.horizontalLayout_357.setSpacing(0)
        self.horizontalLayout_357.setObjectName(u"horizontalLayout_357")
        self.horizontalLayout_357.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.MultipleImaging_FluoOffset_Values_frame)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_357.addWidget(self.label_82)

        self.label_83 = QLabel(self.MultipleImaging_FluoOffset_Values_frame)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_357.addWidget(self.label_83)

        self.label_84 = QLabel(self.MultipleImaging_FluoOffset_Values_frame)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_357.addWidget(self.label_84)


        self.verticalLayout_158.addWidget(self.MultipleImaging_FluoOffset_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_FluoOffset_frame)

        self.line_62 = QFrame(self.MultipleImaging_FluoParameter_page)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_62.setFrameShape(QFrame.Shape.HLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.line_62)

        self.MultipleImaging_FluoNoise_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_FluoNoise_frame.setObjectName(u"MultipleImaging_FluoNoise_frame")
        self.MultipleImaging_FluoNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.MultipleImaging_FluoNoise_frame)
        self.verticalLayout_159.setSpacing(0)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_FluoNoise_Title_frame = QFrame(self.MultipleImaging_FluoNoise_frame)
        self.MultipleImaging_FluoNoise_Title_frame.setObjectName(u"MultipleImaging_FluoNoise_Title_frame")
        self.MultipleImaging_FluoNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_358 = QHBoxLayout(self.MultipleImaging_FluoNoise_Title_frame)
        self.horizontalLayout_358.setSpacing(0)
        self.horizontalLayout_358.setObjectName(u"horizontalLayout_358")
        self.horizontalLayout_358.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoNoise_Toggle_frame = QFrame(self.MultipleImaging_FluoNoise_Title_frame)
        self.MultipleImaging_FluoNoise_Toggle_frame.setObjectName(u"MultipleImaging_FluoNoise_Toggle_frame")
        self.MultipleImaging_FluoNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_FluoNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_FluoNoise_Toggle_layout = QHBoxLayout(self.MultipleImaging_FluoNoise_Toggle_frame)
        self.MultipleImaging_FluoNoise_Toggle_layout.setSpacing(0)
        self.MultipleImaging_FluoNoise_Toggle_layout.setObjectName(u"MultipleImaging_FluoNoise_Toggle_layout")
        self.MultipleImaging_FluoNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_358.addWidget(self.MultipleImaging_FluoNoise_Toggle_frame)

        self.MultipleImaging_FluoNoise_Label_frame = QFrame(self.MultipleImaging_FluoNoise_Title_frame)
        self.MultipleImaging_FluoNoise_Label_frame.setObjectName(u"MultipleImaging_FluoNoise_Label_frame")
        self.MultipleImaging_FluoNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_359 = QHBoxLayout(self.MultipleImaging_FluoNoise_Label_frame)
        self.horizontalLayout_359.setSpacing(0)
        self.horizontalLayout_359.setObjectName(u"horizontalLayout_359")
        self.horizontalLayout_359.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoNoise_Label = QLabel(self.MultipleImaging_FluoNoise_Label_frame)
        self.MultipleImaging_FluoNoise_Label.setObjectName(u"MultipleImaging_FluoNoise_Label")

        self.horizontalLayout_359.addWidget(self.MultipleImaging_FluoNoise_Label)


        self.horizontalLayout_358.addWidget(self.MultipleImaging_FluoNoise_Label_frame)


        self.verticalLayout_159.addWidget(self.MultipleImaging_FluoNoise_Title_frame)

        self.MultipleImaging_FluoNoise_Readings_frame = QFrame(self.MultipleImaging_FluoNoise_frame)
        self.MultipleImaging_FluoNoise_Readings_frame.setObjectName(u"MultipleImaging_FluoNoise_Readings_frame")
        self.MultipleImaging_FluoNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_360 = QHBoxLayout(self.MultipleImaging_FluoNoise_Readings_frame)
        self.horizontalLayout_360.setSpacing(0)
        self.horizontalLayout_360.setObjectName(u"horizontalLayout_360")
        self.horizontalLayout_360.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoNoise_Readings = QLabel(self.MultipleImaging_FluoNoise_Readings_frame)
        self.MultipleImaging_FluoNoise_Readings.setObjectName(u"MultipleImaging_FluoNoise_Readings")
        self.MultipleImaging_FluoNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_360.addWidget(self.MultipleImaging_FluoNoise_Readings)


        self.verticalLayout_159.addWidget(self.MultipleImaging_FluoNoise_Readings_frame)

        self.MultipleImaging_FluoNoise_Slider_frame = QFrame(self.MultipleImaging_FluoNoise_frame)
        self.MultipleImaging_FluoNoise_Slider_frame.setObjectName(u"MultipleImaging_FluoNoise_Slider_frame")
        self.MultipleImaging_FluoNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_361 = QHBoxLayout(self.MultipleImaging_FluoNoise_Slider_frame)
        self.horizontalLayout_361.setSpacing(0)
        self.horizontalLayout_361.setObjectName(u"horizontalLayout_361")
        self.horizontalLayout_361.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoNoise_Slider = QSlider(self.MultipleImaging_FluoNoise_Slider_frame)
        self.MultipleImaging_FluoNoise_Slider.setObjectName(u"MultipleImaging_FluoNoise_Slider")
        self.MultipleImaging_FluoNoise_Slider.setEnabled(False)
        self.MultipleImaging_FluoNoise_Slider.setMinimum(0)
        self.MultipleImaging_FluoNoise_Slider.setMaximum(100)
        self.MultipleImaging_FluoNoise_Slider.setValue(10)
        self.MultipleImaging_FluoNoise_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_FluoNoise_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_FluoNoise_Slider.setTickInterval(10)

        self.horizontalLayout_361.addWidget(self.MultipleImaging_FluoNoise_Slider)


        self.verticalLayout_159.addWidget(self.MultipleImaging_FluoNoise_Slider_frame)

        self.MultipleImaging_FluoNoise_Values_frame = QFrame(self.MultipleImaging_FluoNoise_frame)
        self.MultipleImaging_FluoNoise_Values_frame.setObjectName(u"MultipleImaging_FluoNoise_Values_frame")
        self.MultipleImaging_FluoNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_362 = QHBoxLayout(self.MultipleImaging_FluoNoise_Values_frame)
        self.horizontalLayout_362.setSpacing(0)
        self.horizontalLayout_362.setObjectName(u"horizontalLayout_362")
        self.horizontalLayout_362.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.MultipleImaging_FluoNoise_Values_frame)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_362.addWidget(self.label_85)

        self.label_86 = QLabel(self.MultipleImaging_FluoNoise_Values_frame)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_362.addWidget(self.label_86)

        self.label_87 = QLabel(self.MultipleImaging_FluoNoise_Values_frame)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_362.addWidget(self.label_87)


        self.verticalLayout_159.addWidget(self.MultipleImaging_FluoNoise_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_FluoNoise_frame)

        self.line_63 = QFrame(self.MultipleImaging_FluoParameter_page)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_63.setFrameShape(QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.line_63)

        self.MultipleImaging_FluoSat_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_FluoSat_frame.setObjectName(u"MultipleImaging_FluoSat_frame")
        self.MultipleImaging_FluoSat_frame.setMaximumSize(QSize(16777215, 25))
        self.MultipleImaging_FluoSat_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoSat_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.MultipleImaging_FluoSat_frame)
        self.verticalLayout_160.setSpacing(0)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_FluoSat_Title_frame = QFrame(self.MultipleImaging_FluoSat_frame)
        self.MultipleImaging_FluoSat_Title_frame.setObjectName(u"MultipleImaging_FluoSat_Title_frame")
        self.MultipleImaging_FluoSat_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoSat_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_363 = QHBoxLayout(self.MultipleImaging_FluoSat_Title_frame)
        self.horizontalLayout_363.setSpacing(0)
        self.horizontalLayout_363.setObjectName(u"horizontalLayout_363")
        self.horizontalLayout_363.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoSat_Toggle_frame = QFrame(self.MultipleImaging_FluoSat_Title_frame)
        self.MultipleImaging_FluoSat_Toggle_frame.setObjectName(u"MultipleImaging_FluoSat_Toggle_frame")
        self.MultipleImaging_FluoSat_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_FluoSat_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoSat_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_Saturation_Toggle_layout = QHBoxLayout(self.MultipleImaging_FluoSat_Toggle_frame)
        self.MultipleImaging_Saturation_Toggle_layout.setSpacing(0)
        self.MultipleImaging_Saturation_Toggle_layout.setObjectName(u"MultipleImaging_Saturation_Toggle_layout")
        self.MultipleImaging_Saturation_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_363.addWidget(self.MultipleImaging_FluoSat_Toggle_frame)

        self.MultipleImaging_FluoSat_Label_frame = QFrame(self.MultipleImaging_FluoSat_Title_frame)
        self.MultipleImaging_FluoSat_Label_frame.setObjectName(u"MultipleImaging_FluoSat_Label_frame")
        self.MultipleImaging_FluoSat_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_FluoSat_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_364 = QHBoxLayout(self.MultipleImaging_FluoSat_Label_frame)
        self.horizontalLayout_364.setSpacing(0)
        self.horizontalLayout_364.setObjectName(u"horizontalLayout_364")
        self.horizontalLayout_364.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_FluoSat_Label = QLabel(self.MultipleImaging_FluoSat_Label_frame)
        self.MultipleImaging_FluoSat_Label.setObjectName(u"MultipleImaging_FluoSat_Label")
        self.MultipleImaging_FluoSat_Label.setFont(font4)
        self.MultipleImaging_FluoSat_Label.setWordWrap(True)

        self.horizontalLayout_364.addWidget(self.MultipleImaging_FluoSat_Label)


        self.horizontalLayout_363.addWidget(self.MultipleImaging_FluoSat_Label_frame)


        self.verticalLayout_160.addWidget(self.MultipleImaging_FluoSat_Title_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_FluoSat_frame)

        self.line_64 = QFrame(self.MultipleImaging_FluoParameter_page)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_64.setFrameShape(QFrame.Shape.HLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.line_64)

        self.MultipleImaging_kd_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_kd_frame.setObjectName(u"MultipleImaging_kd_frame")
        self.MultipleImaging_kd_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.MultipleImaging_kd_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.MultipleImaging_kd_frame)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_kd_Title_frame = QFrame(self.MultipleImaging_kd_frame)
        self.MultipleImaging_kd_Title_frame.setObjectName(u"MultipleImaging_kd_Title_frame")
        self.MultipleImaging_kd_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_365 = QHBoxLayout(self.MultipleImaging_kd_Title_frame)
        self.horizontalLayout_365.setSpacing(0)
        self.horizontalLayout_365.setObjectName(u"horizontalLayout_365")
        self.horizontalLayout_365.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_kd_Toggle_frame = QFrame(self.MultipleImaging_kd_Title_frame)
        self.MultipleImaging_kd_Toggle_frame.setObjectName(u"MultipleImaging_kd_Toggle_frame")
        self.MultipleImaging_kd_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_kd_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_kd_Toggle_layout = QHBoxLayout(self.MultipleImaging_kd_Toggle_frame)
        self.MultipleImaging_kd_Toggle_layout.setSpacing(0)
        self.MultipleImaging_kd_Toggle_layout.setObjectName(u"MultipleImaging_kd_Toggle_layout")
        self.MultipleImaging_kd_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_365.addWidget(self.MultipleImaging_kd_Toggle_frame)

        self.MultipleImaging_kd_Label_frame = QFrame(self.MultipleImaging_kd_Title_frame)
        self.MultipleImaging_kd_Label_frame.setObjectName(u"MultipleImaging_kd_Label_frame")
        self.MultipleImaging_kd_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_366 = QHBoxLayout(self.MultipleImaging_kd_Label_frame)
        self.horizontalLayout_366.setSpacing(0)
        self.horizontalLayout_366.setObjectName(u"horizontalLayout_366")
        self.horizontalLayout_366.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_kd_Label = QLabel(self.MultipleImaging_kd_Label_frame)
        self.MultipleImaging_kd_Label.setObjectName(u"MultipleImaging_kd_Label")
        self.MultipleImaging_kd_Label.setWordWrap(True)

        self.horizontalLayout_366.addWidget(self.MultipleImaging_kd_Label)


        self.horizontalLayout_365.addWidget(self.MultipleImaging_kd_Label_frame)


        self.verticalLayout_161.addWidget(self.MultipleImaging_kd_Title_frame)

        self.MultipleImaging_kd_Readings_frame = QFrame(self.MultipleImaging_kd_frame)
        self.MultipleImaging_kd_Readings_frame.setObjectName(u"MultipleImaging_kd_Readings_frame")
        self.MultipleImaging_kd_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_367 = QHBoxLayout(self.MultipleImaging_kd_Readings_frame)
        self.horizontalLayout_367.setSpacing(0)
        self.horizontalLayout_367.setObjectName(u"horizontalLayout_367")
        self.horizontalLayout_367.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_kd_Readings = QLabel(self.MultipleImaging_kd_Readings_frame)
        self.MultipleImaging_kd_Readings.setObjectName(u"MultipleImaging_kd_Readings")
        self.MultipleImaging_kd_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_367.addWidget(self.MultipleImaging_kd_Readings)


        self.verticalLayout_161.addWidget(self.MultipleImaging_kd_Readings_frame)

        self.MultipleImaging_kd_Slider_frame = QFrame(self.MultipleImaging_kd_frame)
        self.MultipleImaging_kd_Slider_frame.setObjectName(u"MultipleImaging_kd_Slider_frame")
        self.MultipleImaging_kd_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_368 = QHBoxLayout(self.MultipleImaging_kd_Slider_frame)
        self.horizontalLayout_368.setSpacing(0)
        self.horizontalLayout_368.setObjectName(u"horizontalLayout_368")
        self.horizontalLayout_368.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_kd_Slider = QSlider(self.MultipleImaging_kd_Slider_frame)
        self.MultipleImaging_kd_Slider.setObjectName(u"MultipleImaging_kd_Slider")
        self.MultipleImaging_kd_Slider.setEnabled(False)
        self.MultipleImaging_kd_Slider.setMinimum(1)
        self.MultipleImaging_kd_Slider.setMaximum(100)
        self.MultipleImaging_kd_Slider.setValue(25)
        self.MultipleImaging_kd_Slider.setSliderPosition(25)
        self.MultipleImaging_kd_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_kd_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_kd_Slider.setTickInterval(10)

        self.horizontalLayout_368.addWidget(self.MultipleImaging_kd_Slider)


        self.verticalLayout_161.addWidget(self.MultipleImaging_kd_Slider_frame)

        self.MultipleImaging_kd_Values_frame = QFrame(self.MultipleImaging_kd_frame)
        self.MultipleImaging_kd_Values_frame.setObjectName(u"MultipleImaging_kd_Values_frame")
        self.MultipleImaging_kd_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_kd_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_369 = QHBoxLayout(self.MultipleImaging_kd_Values_frame)
        self.horizontalLayout_369.setSpacing(0)
        self.horizontalLayout_369.setObjectName(u"horizontalLayout_369")
        self.horizontalLayout_369.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.MultipleImaging_kd_Values_frame)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_369.addWidget(self.label_88)

        self.label_89 = QLabel(self.MultipleImaging_kd_Values_frame)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_369.addWidget(self.label_89)

        self.label_90 = QLabel(self.MultipleImaging_kd_Values_frame)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_369.addWidget(self.label_90)


        self.verticalLayout_161.addWidget(self.MultipleImaging_kd_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_kd_frame)

        self.MultipleImaging_Saturation_Line = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_Saturation_Line.setObjectName(u"MultipleImaging_Saturation_Line")
        self.MultipleImaging_Saturation_Line.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.MultipleImaging_Saturation_Line.setFrameShape(QFrame.Shape.HLine)
        self.MultipleImaging_Saturation_Line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.MultipleImaging_Saturation_Line)

        self.MultipleImaging_Hill_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_Hill_frame.setObjectName(u"MultipleImaging_Hill_frame")
        self.MultipleImaging_Hill_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.MultipleImaging_Hill_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.MultipleImaging_Hill_frame)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_Hill_Title_frame = QFrame(self.MultipleImaging_Hill_frame)
        self.MultipleImaging_Hill_Title_frame.setObjectName(u"MultipleImaging_Hill_Title_frame")
        self.MultipleImaging_Hill_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_370 = QHBoxLayout(self.MultipleImaging_Hill_Title_frame)
        self.horizontalLayout_370.setSpacing(0)
        self.horizontalLayout_370.setObjectName(u"horizontalLayout_370")
        self.horizontalLayout_370.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Hill_Toggle_frame = QFrame(self.MultipleImaging_Hill_Title_frame)
        self.MultipleImaging_Hill_Toggle_frame.setObjectName(u"MultipleImaging_Hill_Toggle_frame")
        self.MultipleImaging_Hill_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_Hill_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_Hill_Toggle_layout = QHBoxLayout(self.MultipleImaging_Hill_Toggle_frame)
        self.MultipleImaging_Hill_Toggle_layout.setSpacing(0)
        self.MultipleImaging_Hill_Toggle_layout.setObjectName(u"MultipleImaging_Hill_Toggle_layout")
        self.MultipleImaging_Hill_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_370.addWidget(self.MultipleImaging_Hill_Toggle_frame)

        self.MultipleImaging_Hill_Label_frame = QFrame(self.MultipleImaging_Hill_Title_frame)
        self.MultipleImaging_Hill_Label_frame.setObjectName(u"MultipleImaging_Hill_Label_frame")
        self.MultipleImaging_Hill_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_371 = QHBoxLayout(self.MultipleImaging_Hill_Label_frame)
        self.horizontalLayout_371.setSpacing(0)
        self.horizontalLayout_371.setObjectName(u"horizontalLayout_371")
        self.horizontalLayout_371.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Hill_Label = QLabel(self.MultipleImaging_Hill_Label_frame)
        self.MultipleImaging_Hill_Label.setObjectName(u"MultipleImaging_Hill_Label")

        self.horizontalLayout_371.addWidget(self.MultipleImaging_Hill_Label)


        self.horizontalLayout_370.addWidget(self.MultipleImaging_Hill_Label_frame)


        self.verticalLayout_162.addWidget(self.MultipleImaging_Hill_Title_frame)

        self.MultipleImaging_Hill_Readings_frame = QFrame(self.MultipleImaging_Hill_frame)
        self.MultipleImaging_Hill_Readings_frame.setObjectName(u"MultipleImaging_Hill_Readings_frame")
        self.MultipleImaging_Hill_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_372 = QHBoxLayout(self.MultipleImaging_Hill_Readings_frame)
        self.horizontalLayout_372.setSpacing(0)
        self.horizontalLayout_372.setObjectName(u"horizontalLayout_372")
        self.horizontalLayout_372.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Hill_Readings = QLabel(self.MultipleImaging_Hill_Readings_frame)
        self.MultipleImaging_Hill_Readings.setObjectName(u"MultipleImaging_Hill_Readings")
        self.MultipleImaging_Hill_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_372.addWidget(self.MultipleImaging_Hill_Readings)


        self.verticalLayout_162.addWidget(self.MultipleImaging_Hill_Readings_frame)

        self.MultipleImaging_Hill_Slider_frame = QFrame(self.MultipleImaging_Hill_frame)
        self.MultipleImaging_Hill_Slider_frame.setObjectName(u"MultipleImaging_Hill_Slider_frame")
        self.MultipleImaging_Hill_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_373 = QHBoxLayout(self.MultipleImaging_Hill_Slider_frame)
        self.horizontalLayout_373.setSpacing(0)
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.horizontalLayout_373.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_Hill_Slider = QSlider(self.MultipleImaging_Hill_Slider_frame)
        self.MultipleImaging_Hill_Slider.setObjectName(u"MultipleImaging_Hill_Slider")
        self.MultipleImaging_Hill_Slider.setEnabled(False)
        self.MultipleImaging_Hill_Slider.setMinimum(50)
        self.MultipleImaging_Hill_Slider.setMaximum(100)
        self.MultipleImaging_Hill_Slider.setValue(100)
        self.MultipleImaging_Hill_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_Hill_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_Hill_Slider.setTickInterval(5)

        self.horizontalLayout_373.addWidget(self.MultipleImaging_Hill_Slider)


        self.verticalLayout_162.addWidget(self.MultipleImaging_Hill_Slider_frame)

        self.MultipleImaging_Hill_Values_frame = QFrame(self.MultipleImaging_Hill_frame)
        self.MultipleImaging_Hill_Values_frame.setObjectName(u"MultipleImaging_Hill_Values_frame")
        self.MultipleImaging_Hill_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_Hill_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_374 = QHBoxLayout(self.MultipleImaging_Hill_Values_frame)
        self.horizontalLayout_374.setSpacing(0)
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.horizontalLayout_374.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.MultipleImaging_Hill_Values_frame)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_374.addWidget(self.label_91)

        self.label_92 = QLabel(self.MultipleImaging_Hill_Values_frame)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_374.addWidget(self.label_92)

        self.label_93 = QLabel(self.MultipleImaging_Hill_Values_frame)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_374.addWidget(self.label_93)


        self.verticalLayout_162.addWidget(self.MultipleImaging_Hill_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_Hill_frame)

        self.MultipleImaging_Saturation_Line2 = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_Saturation_Line2.setObjectName(u"MultipleImaging_Saturation_Line2")
        self.MultipleImaging_Saturation_Line2.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.MultipleImaging_Saturation_Line2.setFrameShape(QFrame.Shape.HLine)
        self.MultipleImaging_Saturation_Line2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_156.addWidget(self.MultipleImaging_Saturation_Line2)

        self.MultipleImaging_PhotoShotNoise_frame = QFrame(self.MultipleImaging_FluoParameter_page)
        self.MultipleImaging_PhotoShotNoise_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_frame")
        self.MultipleImaging_PhotoShotNoise_frame.setStyleSheet(u"background-color: rgb(80, 110, 117);")
        self.MultipleImaging_PhotoShotNoise_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.MultipleImaging_PhotoShotNoise_frame)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(5, 0, 5, 0)
        self.MultipleImaging_PhotoShotNoise_Title_frame = QFrame(self.MultipleImaging_PhotoShotNoise_frame)
        self.MultipleImaging_PhotoShotNoise_Title_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Title_frame")
        self.MultipleImaging_PhotoShotNoise_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_375 = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Title_frame)
        self.horizontalLayout_375.setSpacing(0)
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.horizontalLayout_375.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PhotoShotNoise_Toggle_frame = QFrame(self.MultipleImaging_PhotoShotNoise_Title_frame)
        self.MultipleImaging_PhotoShotNoise_Toggle_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Toggle_frame")
        self.MultipleImaging_PhotoShotNoise_Toggle_frame.setMaximumSize(QSize(50, 16777215))
        self.MultipleImaging_PhotoShotNoise_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.MultipleImaging_PhotoShotNoise_Toggle_layout = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Toggle_frame)
        self.MultipleImaging_PhotoShotNoise_Toggle_layout.setSpacing(0)
        self.MultipleImaging_PhotoShotNoise_Toggle_layout.setObjectName(u"MultipleImaging_PhotoShotNoise_Toggle_layout")
        self.MultipleImaging_PhotoShotNoise_Toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_375.addWidget(self.MultipleImaging_PhotoShotNoise_Toggle_frame)

        self.MultipleImaging_PhotoShotNoise_Label_frame = QFrame(self.MultipleImaging_PhotoShotNoise_Title_frame)
        self.MultipleImaging_PhotoShotNoise_Label_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Label_frame")
        self.MultipleImaging_PhotoShotNoise_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_376 = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Label_frame)
        self.horizontalLayout_376.setSpacing(0)
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.horizontalLayout_376.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PhotoShotNoise_Label = QLabel(self.MultipleImaging_PhotoShotNoise_Label_frame)
        self.MultipleImaging_PhotoShotNoise_Label.setObjectName(u"MultipleImaging_PhotoShotNoise_Label")
        self.MultipleImaging_PhotoShotNoise_Label.setWordWrap(True)

        self.horizontalLayout_376.addWidget(self.MultipleImaging_PhotoShotNoise_Label)


        self.horizontalLayout_375.addWidget(self.MultipleImaging_PhotoShotNoise_Label_frame)


        self.verticalLayout_89.addWidget(self.MultipleImaging_PhotoShotNoise_Title_frame)

        self.MultipleImaging_PhotoShotNoise_Readings_frame = QFrame(self.MultipleImaging_PhotoShotNoise_frame)
        self.MultipleImaging_PhotoShotNoise_Readings_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Readings_frame")
        self.MultipleImaging_PhotoShotNoise_Readings_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Readings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_377 = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Readings_frame)
        self.horizontalLayout_377.setSpacing(0)
        self.horizontalLayout_377.setObjectName(u"horizontalLayout_377")
        self.horizontalLayout_377.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PhotoShotNoise_Readings = QLabel(self.MultipleImaging_PhotoShotNoise_Readings_frame)
        self.MultipleImaging_PhotoShotNoise_Readings.setObjectName(u"MultipleImaging_PhotoShotNoise_Readings")
        self.MultipleImaging_PhotoShotNoise_Readings.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_377.addWidget(self.MultipleImaging_PhotoShotNoise_Readings)


        self.verticalLayout_89.addWidget(self.MultipleImaging_PhotoShotNoise_Readings_frame)

        self.MultipleImaging_PhotoShotNoise_Slider_frame = QFrame(self.MultipleImaging_PhotoShotNoise_frame)
        self.MultipleImaging_PhotoShotNoise_Slider_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Slider_frame")
        self.MultipleImaging_PhotoShotNoise_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_378 = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Slider_frame)
        self.horizontalLayout_378.setSpacing(0)
        self.horizontalLayout_378.setObjectName(u"horizontalLayout_378")
        self.horizontalLayout_378.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_PhotoShotNoise_Slider = QSlider(self.MultipleImaging_PhotoShotNoise_Slider_frame)
        self.MultipleImaging_PhotoShotNoise_Slider.setObjectName(u"MultipleImaging_PhotoShotNoise_Slider")
        self.MultipleImaging_PhotoShotNoise_Slider.setEnabled(False)
        self.MultipleImaging_PhotoShotNoise_Slider.setMinimum(1)
        self.MultipleImaging_PhotoShotNoise_Slider.setMaximum(1000)
        self.MultipleImaging_PhotoShotNoise_Slider.setPageStep(10)
        self.MultipleImaging_PhotoShotNoise_Slider.setValue(400)
        self.MultipleImaging_PhotoShotNoise_Slider.setOrientation(Qt.Horizontal)
        self.MultipleImaging_PhotoShotNoise_Slider.setTickPosition(QSlider.TicksBelow)
        self.MultipleImaging_PhotoShotNoise_Slider.setTickInterval(100)

        self.horizontalLayout_378.addWidget(self.MultipleImaging_PhotoShotNoise_Slider)


        self.verticalLayout_89.addWidget(self.MultipleImaging_PhotoShotNoise_Slider_frame)

        self.MultipleImaging_PhotoShotNoise_Values_frame = QFrame(self.MultipleImaging_PhotoShotNoise_frame)
        self.MultipleImaging_PhotoShotNoise_Values_frame.setObjectName(u"MultipleImaging_PhotoShotNoise_Values_frame")
        self.MultipleImaging_PhotoShotNoise_Values_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_PhotoShotNoise_Values_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_379 = QHBoxLayout(self.MultipleImaging_PhotoShotNoise_Values_frame)
        self.horizontalLayout_379.setSpacing(0)
        self.horizontalLayout_379.setObjectName(u"horizontalLayout_379")
        self.horizontalLayout_379.setContentsMargins(0, 0, 0, 0)
        self.label_94 = QLabel(self.MultipleImaging_PhotoShotNoise_Values_frame)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_379.addWidget(self.label_94)

        self.label_95 = QLabel(self.MultipleImaging_PhotoShotNoise_Values_frame)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_379.addWidget(self.label_95)

        self.label_96 = QLabel(self.MultipleImaging_PhotoShotNoise_Values_frame)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_379.addWidget(self.label_96)


        self.verticalLayout_89.addWidget(self.MultipleImaging_PhotoShotNoise_Values_frame)


        self.verticalLayout_156.addWidget(self.MultipleImaging_PhotoShotNoise_frame)

        self.MultipleImaging_parameter_stackedWidget.addWidget(self.MultipleImaging_FluoParameter_page)

        self.verticalLayout_86.addWidget(self.MultipleImaging_parameter_stackedWidget)


        self.horizontalLayout_380.addWidget(self.MultipleImaging_CenterMenuContainer)

        self.MultipleImaging_rightMenuContainer = QFrame(self.page_202)
        self.MultipleImaging_rightMenuContainer.setObjectName(u"MultipleImaging_rightMenuContainer")
        self.MultipleImaging_rightMenuContainer.setMaximumSize(QSize(40, 16777215))
        self.MultipleImaging_rightMenuContainer.setLayoutDirection(Qt.LeftToRight)
        self.MultipleImaging_rightMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_rightMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.MultipleImaging_rightMenuContainer)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_rightMenuSubContainer = QFrame(self.MultipleImaging_rightMenuContainer)
        self.MultipleImaging_rightMenuSubContainer.setObjectName(u"MultipleImaging_rightMenuSubContainer")
        self.MultipleImaging_rightMenuSubContainer.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_rightMenuSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.MultipleImaging_rightMenuSubContainer)
        self.verticalLayout_96.setSpacing(50)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 5, 0)
        self.MultipleImaging_rightMenuSubContainer_frame = QFrame(self.MultipleImaging_rightMenuSubContainer)
        self.MultipleImaging_rightMenuSubContainer_frame.setObjectName(u"MultipleImaging_rightMenuSubContainer_frame")
        self.MultipleImaging_rightMenuSubContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_rightMenuSubContainer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.MultipleImaging_rightMenuSubContainer_frame)
        self.horizontalLayout_155.setSpacing(0)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 20, 0, 0)
        self.MultipleImaging_rightMenuSubContainer_pushButton = QPushButton(self.MultipleImaging_rightMenuSubContainer_frame)
        self.MultipleImaging_rightMenuSubContainer_pushButton.setObjectName(u"MultipleImaging_rightMenuSubContainer_pushButton")
        self.MultipleImaging_rightMenuSubContainer_pushButton.setMinimumSize(QSize(0, 0))
        self.MultipleImaging_rightMenuSubContainer_pushButton.setFont(font1)
        self.MultipleImaging_rightMenuSubContainer_pushButton.setStyleSheet(u"")
        self.MultipleImaging_rightMenuSubContainer_pushButton.setIcon(icon19)
        self.MultipleImaging_rightMenuSubContainer_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_155.addWidget(self.MultipleImaging_rightMenuSubContainer_pushButton)


        self.verticalLayout_96.addWidget(self.MultipleImaging_rightMenuSubContainer_frame, 0, Qt.AlignTop)

        self.MultipleImaging_rightMenuParameterContainer_frame = QFrame(self.MultipleImaging_rightMenuSubContainer)
        self.MultipleImaging_rightMenuParameterContainer_frame.setObjectName(u"MultipleImaging_rightMenuParameterContainer_frame")
        self.MultipleImaging_rightMenuParameterContainer_frame.setLayoutDirection(Qt.LeftToRight)
        self.MultipleImaging_rightMenuParameterContainer_frame.setFrameShape(QFrame.StyledPanel)
        self.MultipleImaging_rightMenuParameterContainer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.MultipleImaging_rightMenuParameterContainer_frame)
        self.verticalLayout_97.setSpacing(50)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.MultipleImaging_ImagingParameter_pushButton = QPushButton(self.MultipleImaging_rightMenuParameterContainer_frame)
        self.MultipleImaging_ImagingParameter_pushButton.setObjectName(u"MultipleImaging_ImagingParameter_pushButton")
        self.MultipleImaging_ImagingParameter_pushButton.setFont(font1)
        self.MultipleImaging_ImagingParameter_pushButton.setIcon(icon6)
        self.MultipleImaging_ImagingParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_97.addWidget(self.MultipleImaging_ImagingParameter_pushButton)

        self.MultipleImaging_CalciumParameter_pushButton = QPushButton(self.MultipleImaging_rightMenuParameterContainer_frame)
        self.MultipleImaging_CalciumParameter_pushButton.setObjectName(u"MultipleImaging_CalciumParameter_pushButton")
        self.MultipleImaging_CalciumParameter_pushButton.setFont(font1)
        self.MultipleImaging_CalciumParameter_pushButton.setIcon(icon20)
        self.MultipleImaging_CalciumParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_97.addWidget(self.MultipleImaging_CalciumParameter_pushButton)

        self.MultipleImaging_FluoParameter_pushButton = QPushButton(self.MultipleImaging_rightMenuParameterContainer_frame)
        self.MultipleImaging_FluoParameter_pushButton.setObjectName(u"MultipleImaging_FluoParameter_pushButton")
        self.MultipleImaging_FluoParameter_pushButton.setFont(font1)
        self.MultipleImaging_FluoParameter_pushButton.setIcon(icon16)
        self.MultipleImaging_FluoParameter_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_97.addWidget(self.MultipleImaging_FluoParameter_pushButton)


        self.verticalLayout_96.addWidget(self.MultipleImaging_rightMenuParameterContainer_frame)

        self.frame_9 = QFrame(self.MultipleImaging_rightMenuSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_96.addWidget(self.frame_9)


        self.verticalLayout_85.addWidget(self.MultipleImaging_rightMenuSubContainer)


        self.horizontalLayout_380.addWidget(self.MultipleImaging_rightMenuContainer)

        self.mainbody_stackedWidget.addWidget(self.page_202)
        self.page_203 = QWidget()
        self.page_203.setObjectName(u"page_203")
        self.horizontalLayout_72 = QHBoxLayout(self.page_203)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.page_203)
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

        self.mainbody_stackedWidget.addWidget(self.page_203)
        self.page_204 = QWidget()
        self.page_204.setObjectName(u"page_204")
        self.horizontalLayout_75 = QHBoxLayout(self.page_204)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.page_204)
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

        self.mainbody_stackedWidget.addWidget(self.page_204)
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
        sizePolicy5.setHeightForWidth(self.NeuronGenerator_subframe1_title_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_title_label.setSizePolicy(sizePolicy5)
        self.NeuronGenerator_subframe1_title_label.setMaximumSize(QSize(16777215, 30))
        self.NeuronGenerator_subframe1_title_label.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.NeuronGenerator_subframe1_title_label, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.NeuronGenerator_subframe1_title_frame, 0, Qt.AlignTop)

        self.NeuronGenerator_subframe1_Izhik_frame = QFrame(self.NeuronGenerator_subframe1_top_frame)
        self.NeuronGenerator_subframe1_Izhik_frame.setObjectName(u"NeuronGenerator_subframe1_Izhik_frame")
        sizePolicy5.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_frame.setSizePolicy(sizePolicy5)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
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
        sizePolicy4.setHeightForWidth(self.NeuronGenerator_Oscilloscope_widget.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_Oscilloscope_widget.setSizePolicy(sizePolicy4)
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
        sizePolicy5.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_frame.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_frame.setSizePolicy(sizePolicy5)
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
        sizePolicy3.setHeightForWidth(self.NeuronGenerator_subframe1_bottom_label.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_bottom_label.setSizePolicy(sizePolicy3)
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
        sizePolicy5.setHeightForWidth(self.izhik_image.sizePolicy().hasHeightForWidth())
        self.izhik_image.setSizePolicy(sizePolicy5)
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
        sizePolicy3.setHeightForWidth(self.NeuronGenerator_subframe1_Izhik_image.sizePolicy().hasHeightForWidth())
        self.NeuronGenerator_subframe1_Izhik_image.setSizePolicy(sizePolicy3)
        self.NeuronGenerator_subframe1_Izhik_image.setMinimumSize(QSize(225, 150))
        self.NeuronGenerator_subframe1_Izhik_image.setMaximumSize(QSize(225, 140))
        self.NeuronGenerator_subframe1_Izhik_image.setPixmap(QPixmap(u":/resources/resources/izhik.png"))
        self.NeuronGenerator_subframe1_Izhik_image.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.NeuronGenerator_subframe1_Izhik_image, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.izhik_image)

        self.line = QFrame(self.NeuronGenerator_subframe2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

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
        sizePolicy3.setHeightForWidth(self.a_text.sizePolicy().hasHeightForWidth())
        self.a_text.setSizePolicy(sizePolicy3)
        self.a_text.setScaledContents(False)
        self.a_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.a_text.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.a_text)


        self.horizontalLayout_18.addWidget(self.a_text_frame)


        self.verticalLayout_14.addWidget(self.a_Izhik_frame)

        self.line_2 = QFrame(self.NeuronGenerator_subframe2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

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
        sizePolicy3.setHeightForWidth(self.b_text_frame.sizePolicy().hasHeightForWidth())
        self.b_text_frame.setSizePolicy(sizePolicy3)
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
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

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
        sizePolicy3.setHeightForWidth(self.c_text_frame.sizePolicy().hasHeightForWidth())
        self.c_text_frame.setSizePolicy(sizePolicy3)
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
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

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
        sizePolicy3.setHeightForWidth(self.d_text.sizePolicy().hasHeightForWidth())
        self.d_text.setSizePolicy(sizePolicy3)
        self.d_text.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.d_text.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.d_text)


        self.horizontalLayout_27.addWidget(self.d_text_frame)


        self.verticalLayout_14.addWidget(self.d_Izhik_frame)

        self.line_5 = QFrame(self.NeuronGenerator_subframe2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

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
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setStrikeOut(False)
        self.SaveNeuronPushButton.setFont(font9)
        self.SaveNeuronPushButton.setStyleSheet(u"color: rgb(147, 161, 161);")
        self.SaveNeuronPushButton.setCheckable(False)

        self.horizontalLayout_32.addWidget(self.SaveNeuronPushButton)


        self.horizontalLayout_30.addWidget(self.SaveNeuron_frame)

        self.LoadNeuron_frame = QFrame(self.Izhik_button_frame)
        self.LoadNeuron_frame.setObjectName(u"LoadNeuron_frame")
        font10 = QFont()
        font10.setPointSize(9)
        font10.setBold(True)
        self.LoadNeuron_frame.setFont(font10)
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
        self.StimulusGenerator_LeftContainer = QFrame(self.StimulusGenerator_TopContainer)
        self.StimulusGenerator_LeftContainer.setObjectName(u"StimulusGenerator_LeftContainer")
        self.StimulusGenerator_LeftContainer.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_LeftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.StimulusGenerator_LeftContainer)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.StimulusGenerator_Selection_frame = QFrame(self.StimulusGenerator_LeftContainer)
        self.StimulusGenerator_Selection_frame.setObjectName(u"StimulusGenerator_Selection_frame")
        self.StimulusGenerator_Selection_frame.setMinimumSize(QSize(0, 50))
        self.StimulusGenerator_Selection_frame.setMaximumSize(QSize(16777215, 50))
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

        self.StimulusGenerator_Oscilloscope_frame = QFrame(self.StimulusGenerator_LeftContainer)
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
        self.horizontalLayout_216.setContentsMargins(75, 5, 0, 0)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox = QCheckBox(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setObjectName(u"StimulusGenerator_Oscilloscope_widget_Stim_checkbox")
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setEnabled(False)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setAutoFillBackground(False)
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setStyleSheet(u"color: rgb(38,139,210);")
        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setChecked(True)

        self.horizontalLayout_216.addWidget(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox, 0, Qt.AlignTop)


        self.verticalLayout_128.addWidget(self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox_frame)


        self.verticalLayout_125.addWidget(self.StimulusGenerator_Oscilloscope_widget)

        self.StimulusGenerator_SubContainer = QFrame(self.StimulusGenerator_Oscilloscope_frame)
        self.StimulusGenerator_SubContainer.setObjectName(u"StimulusGenerator_SubContainer")
        self.StimulusGenerator_SubContainer.setMinimumSize(QSize(0, 40))
        self.StimulusGenerator_SubContainer.setMaximumSize(QSize(16777215, 40))
        self.StimulusGenerator_SubContainer.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_SubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_202 = QHBoxLayout(self.StimulusGenerator_SubContainer)
        self.horizontalLayout_202.setSpacing(100)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(100, 0, 100, 0)
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


        self.verticalLayout_125.addWidget(self.StimulusGenerator_SubContainer)


        self.verticalLayout_127.addWidget(self.StimulusGenerator_Oscilloscope_frame)


        self.horizontalLayout_201.addWidget(self.StimulusGenerator_LeftContainer)


        self.horizontalLayout_203.addWidget(self.StimulusGenerator_TopContainer)

        self.StimulusGenerator_Parameter_frame = QFrame(self.StimulusGenerator_Container)
        self.StimulusGenerator_Parameter_frame.setObjectName(u"StimulusGenerator_Parameter_frame")
        self.StimulusGenerator_Parameter_frame.setMaximumSize(QSize(300, 16777215))
        self.StimulusGenerator_Parameter_frame.setFrameShape(QFrame.StyledPanel)
        self.StimulusGenerator_Parameter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_205 = QHBoxLayout(self.StimulusGenerator_Parameter_frame)
        self.horizontalLayout_205.setSpacing(0)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.line_42 = QFrame(self.StimulusGenerator_Parameter_frame)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_205.addWidget(self.line_42)

        self.StimulusGenerator_Parameter_stackedWidget = QStackedWidget(self.StimulusGenerator_Parameter_frame)
        self.StimulusGenerator_Parameter_stackedWidget.setObjectName(u"StimulusGenerator_Parameter_stackedWidget")
        self.page_IntensitySteps = QWidget()
        self.page_IntensitySteps.setObjectName(u"page_IntensitySteps")
        self.verticalLayout_111 = QVBoxLayout(self.page_IntensitySteps)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(5, 0, 0, 0)
        self.Step_Number_frame = QFrame(self.page_IntensitySteps)
        self.Step_Number_frame.setObjectName(u"Step_Number_frame")
        self.Step_Number_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Number_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_226 = QHBoxLayout(self.Step_Number_frame)
        self.horizontalLayout_226.setSpacing(0)
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.horizontalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.Step_Number_Label_frame = QFrame(self.Step_Number_frame)
        self.Step_Number_Label_frame.setObjectName(u"Step_Number_Label_frame")
        self.Step_Number_Label_frame.setMinimumSize(QSize(150, 0))
        self.Step_Number_Label_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_Number_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Number_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_227 = QHBoxLayout(self.Step_Number_Label_frame)
        self.horizontalLayout_227.setSpacing(0)
        self.horizontalLayout_227.setObjectName(u"horizontalLayout_227")
        self.horizontalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.Step_Number_Label = QLabel(self.Step_Number_Label_frame)
        self.Step_Number_Label.setObjectName(u"Step_Number_Label")
        self.Step_Number_Label.setFont(font1)
        self.Step_Number_Label.setAlignment(Qt.AlignCenter)
        self.Step_Number_Label.setWordWrap(True)

        self.horizontalLayout_227.addWidget(self.Step_Number_Label)


        self.horizontalLayout_226.addWidget(self.Step_Number_Label_frame)

        self.Step_Number_Value_frame = QFrame(self.Step_Number_frame)
        self.Step_Number_Value_frame.setObjectName(u"Step_Number_Value_frame")
        self.Step_Number_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_Number_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Number_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_234 = QHBoxLayout(self.Step_Number_Value_frame)
        self.horizontalLayout_234.setSpacing(0)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.Step_Number_Value = QLineEdit(self.Step_Number_Value_frame)
        self.Step_Number_Value.setObjectName(u"Step_Number_Value")
        self.Step_Number_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_Number_Value.setFont(font5)
        self.Step_Number_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_234.addWidget(self.Step_Number_Value)


        self.horizontalLayout_226.addWidget(self.Step_Number_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_Number_frame)

        self.Step_Increment_frame = QFrame(self.page_IntensitySteps)
        self.Step_Increment_frame.setObjectName(u"Step_Increment_frame")
        self.Step_Increment_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Increment_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_231 = QHBoxLayout(self.Step_Increment_frame)
        self.horizontalLayout_231.setSpacing(0)
        self.horizontalLayout_231.setObjectName(u"horizontalLayout_231")
        self.horizontalLayout_231.setContentsMargins(0, 0, 0, 0)
        self.Step_Increment_Label_frame = QFrame(self.Step_Increment_frame)
        self.Step_Increment_Label_frame.setObjectName(u"Step_Increment_Label_frame")
        self.Step_Increment_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Increment_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_230 = QHBoxLayout(self.Step_Increment_Label_frame)
        self.horizontalLayout_230.setSpacing(0)
        self.horizontalLayout_230.setObjectName(u"horizontalLayout_230")
        self.horizontalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.Step_Increment_Label = QLabel(self.Step_Increment_Label_frame)
        self.Step_Increment_Label.setObjectName(u"Step_Increment_Label")
        self.Step_Increment_Label.setMinimumSize(QSize(150, 0))
        self.Step_Increment_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_Increment_Label.setFont(font1)
        self.Step_Increment_Label.setAlignment(Qt.AlignCenter)
        self.Step_Increment_Label.setWordWrap(True)

        self.horizontalLayout_230.addWidget(self.Step_Increment_Label)


        self.horizontalLayout_231.addWidget(self.Step_Increment_Label_frame)

        self.Step_Increment_Value_frame = QFrame(self.Step_Increment_frame)
        self.Step_Increment_Value_frame.setObjectName(u"Step_Increment_Value_frame")
        self.Step_Increment_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_Increment_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Increment_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_229 = QHBoxLayout(self.Step_Increment_Value_frame)
        self.horizontalLayout_229.setSpacing(0)
        self.horizontalLayout_229.setObjectName(u"horizontalLayout_229")
        self.horizontalLayout_229.setContentsMargins(0, 0, 0, 0)
        self.Step_Increment_Value = QLineEdit(self.Step_Increment_Value_frame)
        self.Step_Increment_Value.setObjectName(u"Step_Increment_Value")
        self.Step_Increment_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_Increment_Value.setFont(font5)
        self.Step_Increment_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_229.addWidget(self.Step_Increment_Value)


        self.horizontalLayout_231.addWidget(self.Step_Increment_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_Increment_frame)

        self.Step_First_frame = QFrame(self.page_IntensitySteps)
        self.Step_First_frame.setObjectName(u"Step_First_frame")
        self.Step_First_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_First_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_233 = QHBoxLayout(self.Step_First_frame)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.Step_First_Label_frame = QFrame(self.Step_First_frame)
        self.Step_First_Label_frame.setObjectName(u"Step_First_Label_frame")
        self.Step_First_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_First_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_232 = QHBoxLayout(self.Step_First_Label_frame)
        self.horizontalLayout_232.setSpacing(0)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.Step_First_Label = QLabel(self.Step_First_Label_frame)
        self.Step_First_Label.setObjectName(u"Step_First_Label")
        self.Step_First_Label.setMinimumSize(QSize(150, 0))
        self.Step_First_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_First_Label.setFont(font1)
        self.Step_First_Label.setAlignment(Qt.AlignCenter)
        self.Step_First_Label.setWordWrap(True)

        self.horizontalLayout_232.addWidget(self.Step_First_Label)


        self.horizontalLayout_233.addWidget(self.Step_First_Label_frame)

        self.Step_First_Value_frame = QFrame(self.Step_First_frame)
        self.Step_First_Value_frame.setObjectName(u"Step_First_Value_frame")
        self.Step_First_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_First_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_First_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_228 = QHBoxLayout(self.Step_First_Value_frame)
        self.horizontalLayout_228.setSpacing(0)
        self.horizontalLayout_228.setObjectName(u"horizontalLayout_228")
        self.horizontalLayout_228.setContentsMargins(0, 0, 0, 0)
        self.Step_First_Value = QLineEdit(self.Step_First_Value_frame)
        self.Step_First_Value.setObjectName(u"Step_First_Value")
        self.Step_First_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_First_Value.setFont(font5)
        self.Step_First_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_228.addWidget(self.Step_First_Value)


        self.horizontalLayout_233.addWidget(self.Step_First_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_First_frame)

        self.Step_On_frame = QFrame(self.page_IntensitySteps)
        self.Step_On_frame.setObjectName(u"Step_On_frame")
        self.Step_On_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_On_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_237 = QHBoxLayout(self.Step_On_frame)
        self.horizontalLayout_237.setSpacing(0)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.horizontalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.Step_On_Label_frame = QFrame(self.Step_On_frame)
        self.Step_On_Label_frame.setObjectName(u"Step_On_Label_frame")
        self.Step_On_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_On_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_236 = QHBoxLayout(self.Step_On_Label_frame)
        self.horizontalLayout_236.setSpacing(0)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalLayout_236.setContentsMargins(0, 0, 0, 0)
        self.Step_On_Label = QLabel(self.Step_On_Label_frame)
        self.Step_On_Label.setObjectName(u"Step_On_Label")
        self.Step_On_Label.setMinimumSize(QSize(150, 0))
        self.Step_On_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_On_Label.setFont(font1)
        self.Step_On_Label.setAlignment(Qt.AlignCenter)
        self.Step_On_Label.setWordWrap(True)

        self.horizontalLayout_236.addWidget(self.Step_On_Label)


        self.horizontalLayout_237.addWidget(self.Step_On_Label_frame)

        self.Step_On_Value_frame = QFrame(self.Step_On_frame)
        self.Step_On_Value_frame.setObjectName(u"Step_On_Value_frame")
        self.Step_On_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_On_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_On_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_235 = QHBoxLayout(self.Step_On_Value_frame)
        self.horizontalLayout_235.setSpacing(0)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.Step_On_Value = QLineEdit(self.Step_On_Value_frame)
        self.Step_On_Value.setObjectName(u"Step_On_Value")
        self.Step_On_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_On_Value.setFont(font5)
        self.Step_On_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_235.addWidget(self.Step_On_Value)


        self.horizontalLayout_237.addWidget(self.Step_On_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_On_frame)

        self.Step_Off_frame = QFrame(self.page_IntensitySteps)
        self.Step_Off_frame.setObjectName(u"Step_Off_frame")
        self.Step_Off_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Off_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_240 = QHBoxLayout(self.Step_Off_frame)
        self.horizontalLayout_240.setSpacing(0)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(0, 0, 0, 0)
        self.Step_Off_Label_frame = QFrame(self.Step_Off_frame)
        self.Step_Off_Label_frame.setObjectName(u"Step_Off_Label_frame")
        self.Step_Off_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Off_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_239 = QHBoxLayout(self.Step_Off_Label_frame)
        self.horizontalLayout_239.setSpacing(0)
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.horizontalLayout_239.setContentsMargins(0, 0, 0, 0)
        self.Step_Off_Label = QLabel(self.Step_Off_Label_frame)
        self.Step_Off_Label.setObjectName(u"Step_Off_Label")
        self.Step_Off_Label.setMinimumSize(QSize(150, 0))
        self.Step_Off_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_Off_Label.setFont(font1)
        self.Step_Off_Label.setAlignment(Qt.AlignCenter)
        self.Step_Off_Label.setWordWrap(True)

        self.horizontalLayout_239.addWidget(self.Step_Off_Label)


        self.horizontalLayout_240.addWidget(self.Step_Off_Label_frame)

        self.Step_Off_Value_frame = QFrame(self.Step_Off_frame)
        self.Step_Off_Value_frame.setObjectName(u"Step_Off_Value_frame")
        self.Step_Off_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_Off_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Off_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_238 = QHBoxLayout(self.Step_Off_Value_frame)
        self.horizontalLayout_238.setSpacing(0)
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.horizontalLayout_238.setContentsMargins(0, 0, 0, 0)
        self.Step_Off_Value = QLineEdit(self.Step_Off_Value_frame)
        self.Step_Off_Value.setObjectName(u"Step_Off_Value")
        self.Step_Off_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_Off_Value.setFont(font5)
        self.Step_Off_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_238.addWidget(self.Step_Off_Value)


        self.horizontalLayout_240.addWidget(self.Step_Off_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_Off_frame)

        self.Step_OffInt_frame = QFrame(self.page_IntensitySteps)
        self.Step_OffInt_frame.setObjectName(u"Step_OffInt_frame")
        self.Step_OffInt_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_OffInt_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_249 = QHBoxLayout(self.Step_OffInt_frame)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.Step_OffInt_Label_frame = QFrame(self.Step_OffInt_frame)
        self.Step_OffInt_Label_frame.setObjectName(u"Step_OffInt_Label_frame")
        self.Step_OffInt_Label_frame.setMinimumSize(QSize(150, 0))
        self.Step_OffInt_Label_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_OffInt_Label_frame.setFont(font1)
        self.Step_OffInt_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_OffInt_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_248 = QHBoxLayout(self.Step_OffInt_Label_frame)
        self.horizontalLayout_248.setSpacing(0)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.horizontalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.Step_OffInt_Label = QLabel(self.Step_OffInt_Label_frame)
        self.Step_OffInt_Label.setObjectName(u"Step_OffInt_Label")
        self.Step_OffInt_Label.setFont(font1)
        self.Step_OffInt_Label.setAlignment(Qt.AlignCenter)
        self.Step_OffInt_Label.setWordWrap(True)

        self.horizontalLayout_248.addWidget(self.Step_OffInt_Label)


        self.horizontalLayout_249.addWidget(self.Step_OffInt_Label_frame)

        self.Step_OffInt_Value_frame = QFrame(self.Step_OffInt_frame)
        self.Step_OffInt_Value_frame.setObjectName(u"Step_OffInt_Value_frame")
        self.Step_OffInt_Value_frame.setMinimumSize(QSize(150, 0))
        self.Step_OffInt_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_OffInt_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_OffInt_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_247 = QHBoxLayout(self.Step_OffInt_Value_frame)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.Step_OffInt_Value = QLineEdit(self.Step_OffInt_Value_frame)
        self.Step_OffInt_Value.setObjectName(u"Step_OffInt_Value")
        self.Step_OffInt_Value.setMinimumSize(QSize(100, 0))
        self.Step_OffInt_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_OffInt_Value.setFont(font5)
        self.Step_OffInt_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_247.addWidget(self.Step_OffInt_Value)


        self.horizontalLayout_249.addWidget(self.Step_OffInt_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_OffInt_frame)

        self.line_68 = QFrame(self.page_IntensitySteps)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_68.setFrameShape(QFrame.Shape.HLine)
        self.line_68.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_111.addWidget(self.line_68)

        self.Step_Inter_frame = QFrame(self.page_IntensitySteps)
        self.Step_Inter_frame.setObjectName(u"Step_Inter_frame")
        self.Step_Inter_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Inter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_243 = QHBoxLayout(self.Step_Inter_frame)
        self.horizontalLayout_243.setSpacing(0)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.Step_Inter_Label_frame = QFrame(self.Step_Inter_frame)
        self.Step_Inter_Label_frame.setObjectName(u"Step_Inter_Label_frame")
        self.Step_Inter_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Inter_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_242 = QHBoxLayout(self.Step_Inter_Label_frame)
        self.horizontalLayout_242.setSpacing(0)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.horizontalLayout_242.setContentsMargins(0, 0, 0, 0)
        self.Step_Inter_Label = QLabel(self.Step_Inter_Label_frame)
        self.Step_Inter_Label.setObjectName(u"Step_Inter_Label")
        self.Step_Inter_Label.setMinimumSize(QSize(150, 0))
        self.Step_Inter_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_Inter_Label.setFont(font1)
        self.Step_Inter_Label.setAlignment(Qt.AlignCenter)
        self.Step_Inter_Label.setWordWrap(True)

        self.horizontalLayout_242.addWidget(self.Step_Inter_Label)


        self.horizontalLayout_243.addWidget(self.Step_Inter_Label_frame)

        self.Step_Inter_Value_frame = QFrame(self.Step_Inter_frame)
        self.Step_Inter_Value_frame.setObjectName(u"Step_Inter_Value_frame")
        self.Step_Inter_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_Inter_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_Inter_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_241 = QHBoxLayout(self.Step_Inter_Value_frame)
        self.horizontalLayout_241.setSpacing(0)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.Step_Inter_Value = QLineEdit(self.Step_Inter_Value_frame)
        self.Step_Inter_Value.setObjectName(u"Step_Inter_Value")
        self.Step_Inter_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_Inter_Value.setFont(font5)
        self.Step_Inter_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_241.addWidget(self.Step_Inter_Value)


        self.horizontalLayout_243.addWidget(self.Step_Inter_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_Inter_frame)

        self.Step_InterInt_frame = QFrame(self.page_IntensitySteps)
        self.Step_InterInt_frame.setObjectName(u"Step_InterInt_frame")
        self.Step_InterInt_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_InterInt_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_246 = QHBoxLayout(self.Step_InterInt_frame)
        self.horizontalLayout_246.setSpacing(0)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(0, 0, 0, 0)
        self.Step_InterInt_Label_frame = QFrame(self.Step_InterInt_frame)
        self.Step_InterInt_Label_frame.setObjectName(u"Step_InterInt_Label_frame")
        self.Step_InterInt_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_InterInt_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_245 = QHBoxLayout(self.Step_InterInt_Label_frame)
        self.horizontalLayout_245.setSpacing(0)
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalLayout_245.setContentsMargins(0, 0, 0, 0)
        self.Step_InterInt_Label = QLabel(self.Step_InterInt_Label_frame)
        self.Step_InterInt_Label.setObjectName(u"Step_InterInt_Label")
        self.Step_InterInt_Label.setMinimumSize(QSize(150, 0))
        self.Step_InterInt_Label.setMaximumSize(QSize(150, 16777215))
        self.Step_InterInt_Label.setFont(font1)
        self.Step_InterInt_Label.setAlignment(Qt.AlignCenter)
        self.Step_InterInt_Label.setWordWrap(True)

        self.horizontalLayout_245.addWidget(self.Step_InterInt_Label)


        self.horizontalLayout_246.addWidget(self.Step_InterInt_Label_frame)

        self.Step_InterInt_Value_frame = QFrame(self.Step_InterInt_frame)
        self.Step_InterInt_Value_frame.setObjectName(u"Step_InterInt_Value_frame")
        self.Step_InterInt_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Step_InterInt_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Step_InterInt_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_244 = QHBoxLayout(self.Step_InterInt_Value_frame)
        self.horizontalLayout_244.setSpacing(0)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.Step_InterInt_Value = QLineEdit(self.Step_InterInt_Value_frame)
        self.Step_InterInt_Value.setObjectName(u"Step_InterInt_Value")
        self.Step_InterInt_Value.setMaximumSize(QSize(100, 16777215))
        self.Step_InterInt_Value.setFont(font5)
        self.Step_InterInt_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_244.addWidget(self.Step_InterInt_Value)


        self.horizontalLayout_246.addWidget(self.Step_InterInt_Value_frame)


        self.verticalLayout_111.addWidget(self.Step_InterInt_frame)

        self.StimulusGenerator_Parameter_stackedWidget.addWidget(self.page_IntensitySteps)
        self.page_SineWave = QWidget()
        self.page_SineWave.setObjectName(u"page_SineWave")
        self.verticalLayout_126 = QVBoxLayout(self.page_SineWave)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(5, 0, 0, 0)
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

        self.line_67 = QFrame(self.page_SineWave)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_67.setFrameShape(QFrame.Shape.HLine)
        self.line_67.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_126.addWidget(self.line_67)

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
        self.page_TriangularWave = QWidget()
        self.page_TriangularWave.setObjectName(u"page_TriangularWave")
        self.verticalLayout_112 = QVBoxLayout(self.page_TriangularWave)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(5, 0, 0, 0)
        self.TriangleWave_Amplitude = QFrame(self.page_TriangularWave)
        self.TriangleWave_Amplitude.setObjectName(u"TriangleWave_Amplitude")
        self.TriangleWave_Amplitude.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Amplitude.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_256 = QHBoxLayout(self.TriangleWave_Amplitude)
        self.horizontalLayout_256.setSpacing(0)
        self.horizontalLayout_256.setObjectName(u"horizontalLayout_256")
        self.horizontalLayout_256.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Amplitude_Label_frame = QFrame(self.TriangleWave_Amplitude)
        self.TriangleWave_Amplitude_Label_frame.setObjectName(u"TriangleWave_Amplitude_Label_frame")
        self.TriangleWave_Amplitude_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Amplitude_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_255 = QHBoxLayout(self.TriangleWave_Amplitude_Label_frame)
        self.horizontalLayout_255.setSpacing(0)
        self.horizontalLayout_255.setObjectName(u"horizontalLayout_255")
        self.horizontalLayout_255.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Amplitude_Label = QLabel(self.TriangleWave_Amplitude_Label_frame)
        self.TriangleWave_Amplitude_Label.setObjectName(u"TriangleWave_Amplitude_Label")
        self.TriangleWave_Amplitude_Label.setFont(font1)
        self.TriangleWave_Amplitude_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_Amplitude_Label.setWordWrap(True)

        self.horizontalLayout_255.addWidget(self.TriangleWave_Amplitude_Label)


        self.horizontalLayout_256.addWidget(self.TriangleWave_Amplitude_Label_frame)

        self.TriangleWave_Amplitude_Value_frame = QFrame(self.TriangleWave_Amplitude)
        self.TriangleWave_Amplitude_Value_frame.setObjectName(u"TriangleWave_Amplitude_Value_frame")
        self.TriangleWave_Amplitude_Value_frame.setMinimumSize(QSize(150, 0))
        self.TriangleWave_Amplitude_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_Amplitude_Value_frame.setFont(font5)
        self.TriangleWave_Amplitude_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Amplitude_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_254 = QHBoxLayout(self.TriangleWave_Amplitude_Value_frame)
        self.horizontalLayout_254.setSpacing(0)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.horizontalLayout_254.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Amplitude_Value = QLineEdit(self.TriangleWave_Amplitude_Value_frame)
        self.TriangleWave_Amplitude_Value.setObjectName(u"TriangleWave_Amplitude_Value")
        self.TriangleWave_Amplitude_Value.setMinimumSize(QSize(100, 0))
        self.TriangleWave_Amplitude_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_Amplitude_Value.setFont(font5)
        self.TriangleWave_Amplitude_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_254.addWidget(self.TriangleWave_Amplitude_Value)


        self.horizontalLayout_256.addWidget(self.TriangleWave_Amplitude_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_Amplitude)

        self.TriangleWave_Frequency_frame = QFrame(self.page_TriangularWave)
        self.TriangleWave_Frequency_frame.setObjectName(u"TriangleWave_Frequency_frame")
        self.TriangleWave_Frequency_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Frequency_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_259 = QHBoxLayout(self.TriangleWave_Frequency_frame)
        self.horizontalLayout_259.setSpacing(0)
        self.horizontalLayout_259.setObjectName(u"horizontalLayout_259")
        self.horizontalLayout_259.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Frequency_Label_frame = QFrame(self.TriangleWave_Frequency_frame)
        self.TriangleWave_Frequency_Label_frame.setObjectName(u"TriangleWave_Frequency_Label_frame")
        self.TriangleWave_Frequency_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Frequency_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_258 = QHBoxLayout(self.TriangleWave_Frequency_Label_frame)
        self.horizontalLayout_258.setSpacing(0)
        self.horizontalLayout_258.setObjectName(u"horizontalLayout_258")
        self.horizontalLayout_258.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Frequency_Label = QLabel(self.TriangleWave_Frequency_Label_frame)
        self.TriangleWave_Frequency_Label.setObjectName(u"TriangleWave_Frequency_Label")
        self.TriangleWave_Frequency_Label.setFont(font1)
        self.TriangleWave_Frequency_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_Frequency_Label.setWordWrap(True)

        self.horizontalLayout_258.addWidget(self.TriangleWave_Frequency_Label)


        self.horizontalLayout_259.addWidget(self.TriangleWave_Frequency_Label_frame)

        self.TriangleWave_Frequency_Value_frame = QFrame(self.TriangleWave_Frequency_frame)
        self.TriangleWave_Frequency_Value_frame.setObjectName(u"TriangleWave_Frequency_Value_frame")
        self.TriangleWave_Frequency_Value_frame.setMinimumSize(QSize(150, 0))
        self.TriangleWave_Frequency_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_Frequency_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Frequency_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_257 = QHBoxLayout(self.TriangleWave_Frequency_Value_frame)
        self.horizontalLayout_257.setSpacing(0)
        self.horizontalLayout_257.setObjectName(u"horizontalLayout_257")
        self.horizontalLayout_257.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Frequency_Value = QLineEdit(self.TriangleWave_Frequency_Value_frame)
        self.TriangleWave_Frequency_Value.setObjectName(u"TriangleWave_Frequency_Value")
        self.TriangleWave_Frequency_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_Frequency_Value.setFont(font5)
        self.TriangleWave_Frequency_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_257.addWidget(self.TriangleWave_Frequency_Value)


        self.horizontalLayout_259.addWidget(self.TriangleWave_Frequency_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_Frequency_frame)

        self.TriangleWave_Mean_frame = QFrame(self.page_TriangularWave)
        self.TriangleWave_Mean_frame.setObjectName(u"TriangleWave_Mean_frame")
        self.TriangleWave_Mean_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Mean_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_262 = QHBoxLayout(self.TriangleWave_Mean_frame)
        self.horizontalLayout_262.setSpacing(0)
        self.horizontalLayout_262.setObjectName(u"horizontalLayout_262")
        self.horizontalLayout_262.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Mean_Label_frame = QFrame(self.TriangleWave_Mean_frame)
        self.TriangleWave_Mean_Label_frame.setObjectName(u"TriangleWave_Mean_Label_frame")
        self.TriangleWave_Mean_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Mean_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_261 = QHBoxLayout(self.TriangleWave_Mean_Label_frame)
        self.horizontalLayout_261.setSpacing(0)
        self.horizontalLayout_261.setObjectName(u"horizontalLayout_261")
        self.horizontalLayout_261.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Mean_Label = QLabel(self.TriangleWave_Mean_Label_frame)
        self.TriangleWave_Mean_Label.setObjectName(u"TriangleWave_Mean_Label")
        self.TriangleWave_Mean_Label.setFont(font1)
        self.TriangleWave_Mean_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_Mean_Label.setWordWrap(True)

        self.horizontalLayout_261.addWidget(self.TriangleWave_Mean_Label)


        self.horizontalLayout_262.addWidget(self.TriangleWave_Mean_Label_frame)

        self.TriangleWave_Mean_Value_frame = QFrame(self.TriangleWave_Mean_frame)
        self.TriangleWave_Mean_Value_frame.setObjectName(u"TriangleWave_Mean_Value_frame")
        self.TriangleWave_Mean_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_Mean_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_Mean_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_260 = QHBoxLayout(self.TriangleWave_Mean_Value_frame)
        self.horizontalLayout_260.setSpacing(0)
        self.horizontalLayout_260.setObjectName(u"horizontalLayout_260")
        self.horizontalLayout_260.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_Mean_Value = QLineEdit(self.TriangleWave_Mean_Value_frame)
        self.TriangleWave_Mean_Value.setObjectName(u"TriangleWave_Mean_Value")
        self.TriangleWave_Mean_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_Mean_Value.setFont(font5)
        self.TriangleWave_Mean_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_260.addWidget(self.TriangleWave_Mean_Value)


        self.horizontalLayout_262.addWidget(self.TriangleWave_Mean_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_Mean_frame)

        self.TriangleWave_StimOn_frame = QFrame(self.page_TriangularWave)
        self.TriangleWave_StimOn_frame.setObjectName(u"TriangleWave_StimOn_frame")
        self.TriangleWave_StimOn_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_265 = QHBoxLayout(self.TriangleWave_StimOn_frame)
        self.horizontalLayout_265.setSpacing(0)
        self.horizontalLayout_265.setObjectName(u"horizontalLayout_265")
        self.horizontalLayout_265.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOn_Label_frame = QFrame(self.TriangleWave_StimOn_frame)
        self.TriangleWave_StimOn_Label_frame.setObjectName(u"TriangleWave_StimOn_Label_frame")
        self.TriangleWave_StimOn_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOn_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_264 = QHBoxLayout(self.TriangleWave_StimOn_Label_frame)
        self.horizontalLayout_264.setSpacing(0)
        self.horizontalLayout_264.setObjectName(u"horizontalLayout_264")
        self.horizontalLayout_264.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOn_Label = QLabel(self.TriangleWave_StimOn_Label_frame)
        self.TriangleWave_StimOn_Label.setObjectName(u"TriangleWave_StimOn_Label")
        self.TriangleWave_StimOn_Label.setFont(font1)
        self.TriangleWave_StimOn_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_StimOn_Label.setWordWrap(True)

        self.horizontalLayout_264.addWidget(self.TriangleWave_StimOn_Label)


        self.horizontalLayout_265.addWidget(self.TriangleWave_StimOn_Label_frame)

        self.TriangleWave_StimOn_Value_frame = QFrame(self.TriangleWave_StimOn_frame)
        self.TriangleWave_StimOn_Value_frame.setObjectName(u"TriangleWave_StimOn_Value_frame")
        self.TriangleWave_StimOn_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_StimOn_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOn_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_263 = QHBoxLayout(self.TriangleWave_StimOn_Value_frame)
        self.horizontalLayout_263.setSpacing(0)
        self.horizontalLayout_263.setObjectName(u"horizontalLayout_263")
        self.horizontalLayout_263.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOn_Value = QLineEdit(self.TriangleWave_StimOn_Value_frame)
        self.TriangleWave_StimOn_Value.setObjectName(u"TriangleWave_StimOn_Value")
        self.TriangleWave_StimOn_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_StimOn_Value.setFont(font5)
        self.TriangleWave_StimOn_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_263.addWidget(self.TriangleWave_StimOn_Value)


        self.horizontalLayout_265.addWidget(self.TriangleWave_StimOn_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_StimOn_frame)

        self.line_44 = QFrame(self.page_TriangularWave)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_44.setFrameShape(QFrame.Shape.HLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_112.addWidget(self.line_44)

        self.TriangleWave_IntOff_frame = QFrame(self.page_TriangularWave)
        self.TriangleWave_IntOff_frame.setObjectName(u"TriangleWave_IntOff_frame")
        self.TriangleWave_IntOff_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_IntOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_268 = QHBoxLayout(self.TriangleWave_IntOff_frame)
        self.horizontalLayout_268.setSpacing(0)
        self.horizontalLayout_268.setObjectName(u"horizontalLayout_268")
        self.horizontalLayout_268.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_IntOff_Label_frame = QFrame(self.TriangleWave_IntOff_frame)
        self.TriangleWave_IntOff_Label_frame.setObjectName(u"TriangleWave_IntOff_Label_frame")
        self.TriangleWave_IntOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_IntOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_267 = QHBoxLayout(self.TriangleWave_IntOff_Label_frame)
        self.horizontalLayout_267.setSpacing(0)
        self.horizontalLayout_267.setObjectName(u"horizontalLayout_267")
        self.horizontalLayout_267.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_IntOff_Label = QLabel(self.TriangleWave_IntOff_Label_frame)
        self.TriangleWave_IntOff_Label.setObjectName(u"TriangleWave_IntOff_Label")
        self.TriangleWave_IntOff_Label.setFont(font1)
        self.TriangleWave_IntOff_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_IntOff_Label.setWordWrap(True)

        self.horizontalLayout_267.addWidget(self.TriangleWave_IntOff_Label)


        self.horizontalLayout_268.addWidget(self.TriangleWave_IntOff_Label_frame)

        self.TriangleWave_IntOff_Value_frame = QFrame(self.TriangleWave_IntOff_frame)
        self.TriangleWave_IntOff_Value_frame.setObjectName(u"TriangleWave_IntOff_Value_frame")
        self.TriangleWave_IntOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_IntOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_IntOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_266 = QHBoxLayout(self.TriangleWave_IntOff_Value_frame)
        self.horizontalLayout_266.setSpacing(0)
        self.horizontalLayout_266.setObjectName(u"horizontalLayout_266")
        self.horizontalLayout_266.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_IntOff_Value = QLineEdit(self.TriangleWave_IntOff_Value_frame)
        self.TriangleWave_IntOff_Value.setObjectName(u"TriangleWave_IntOff_Value")
        self.TriangleWave_IntOff_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_IntOff_Value.setFont(font5)
        self.TriangleWave_IntOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_266.addWidget(self.TriangleWave_IntOff_Value)


        self.horizontalLayout_268.addWidget(self.TriangleWave_IntOff_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_IntOff_frame)

        self.TriangleWave_StimOff_frame = QFrame(self.page_TriangularWave)
        self.TriangleWave_StimOff_frame.setObjectName(u"TriangleWave_StimOff_frame")
        self.TriangleWave_StimOff_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_271 = QHBoxLayout(self.TriangleWave_StimOff_frame)
        self.horizontalLayout_271.setSpacing(0)
        self.horizontalLayout_271.setObjectName(u"horizontalLayout_271")
        self.horizontalLayout_271.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOff_Label_frame = QFrame(self.TriangleWave_StimOff_frame)
        self.TriangleWave_StimOff_Label_frame.setObjectName(u"TriangleWave_StimOff_Label_frame")
        self.TriangleWave_StimOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_270 = QHBoxLayout(self.TriangleWave_StimOff_Label_frame)
        self.horizontalLayout_270.setSpacing(0)
        self.horizontalLayout_270.setObjectName(u"horizontalLayout_270")
        self.horizontalLayout_270.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOff_Label = QLabel(self.TriangleWave_StimOff_Label_frame)
        self.TriangleWave_StimOff_Label.setObjectName(u"TriangleWave_StimOff_Label")
        self.TriangleWave_StimOff_Label.setFont(font1)
        self.TriangleWave_StimOff_Label.setAlignment(Qt.AlignCenter)
        self.TriangleWave_StimOff_Label.setWordWrap(True)

        self.horizontalLayout_270.addWidget(self.TriangleWave_StimOff_Label)


        self.horizontalLayout_271.addWidget(self.TriangleWave_StimOff_Label_frame)

        self.TriangleWave_StimOff_Value_frame = QFrame(self.TriangleWave_StimOff_frame)
        self.TriangleWave_StimOff_Value_frame.setObjectName(u"TriangleWave_StimOff_Value_frame")
        self.TriangleWave_StimOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.TriangleWave_StimOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.TriangleWave_StimOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_269 = QHBoxLayout(self.TriangleWave_StimOff_Value_frame)
        self.horizontalLayout_269.setSpacing(0)
        self.horizontalLayout_269.setObjectName(u"horizontalLayout_269")
        self.horizontalLayout_269.setContentsMargins(0, 0, 0, 0)
        self.TriangleWave_StimOff_Value = QLineEdit(self.TriangleWave_StimOff_Value_frame)
        self.TriangleWave_StimOff_Value.setObjectName(u"TriangleWave_StimOff_Value")
        self.TriangleWave_StimOff_Value.setMaximumSize(QSize(100, 16777215))
        self.TriangleWave_StimOff_Value.setFont(font5)
        self.TriangleWave_StimOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_269.addWidget(self.TriangleWave_StimOff_Value)


        self.horizontalLayout_271.addWidget(self.TriangleWave_StimOff_Value_frame)


        self.verticalLayout_112.addWidget(self.TriangleWave_StimOff_frame)

        self.StimulusGenerator_Parameter_stackedWidget.addWidget(self.page_TriangularWave)
        self.page_Chirp = QWidget()
        self.page_Chirp.setObjectName(u"page_Chirp")
        self.verticalLayout_100 = QVBoxLayout(self.page_Chirp)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(5, 0, 0, 0)
        self.Chirp_comboBox_frame = QFrame(self.page_Chirp)
        self.Chirp_comboBox_frame.setObjectName(u"Chirp_comboBox_frame")
        self.Chirp_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_402 = QHBoxLayout(self.Chirp_comboBox_frame)
        self.horizontalLayout_402.setSpacing(10)
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.horizontalLayout_402.setContentsMargins(5, 0, 5, 0)
        self.Chirp_comboBox = QComboBox(self.Chirp_comboBox_frame)
        self.Chirp_comboBox.addItem("")
        self.Chirp_comboBox.addItem("")
        self.Chirp_comboBox.addItem("")
        self.Chirp_comboBox.setObjectName(u"Chirp_comboBox")
        self.Chirp_comboBox.setFont(font1)

        self.horizontalLayout_402.addWidget(self.Chirp_comboBox)


        self.verticalLayout_100.addWidget(self.Chirp_comboBox_frame)

        self.Chirp_Amplitude = QFrame(self.page_Chirp)
        self.Chirp_Amplitude.setObjectName(u"Chirp_Amplitude")
        self.Chirp_Amplitude.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Amplitude.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_381 = QHBoxLayout(self.Chirp_Amplitude)
        self.horizontalLayout_381.setSpacing(0)
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.horizontalLayout_381.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Amplitude_Label_frame = QFrame(self.Chirp_Amplitude)
        self.Chirp_Amplitude_Label_frame.setObjectName(u"Chirp_Amplitude_Label_frame")
        self.Chirp_Amplitude_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_Amplitude_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Amplitude_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_382 = QHBoxLayout(self.Chirp_Amplitude_Label_frame)
        self.horizontalLayout_382.setSpacing(0)
        self.horizontalLayout_382.setObjectName(u"horizontalLayout_382")
        self.horizontalLayout_382.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Amplitude_Label = QLabel(self.Chirp_Amplitude_Label_frame)
        self.Chirp_Amplitude_Label.setObjectName(u"Chirp_Amplitude_Label")
        self.Chirp_Amplitude_Label.setMaximumSize(QSize(150, 16777215))
        self.Chirp_Amplitude_Label.setFont(font1)
        self.Chirp_Amplitude_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_Amplitude_Label.setWordWrap(True)

        self.horizontalLayout_382.addWidget(self.Chirp_Amplitude_Label)


        self.horizontalLayout_381.addWidget(self.Chirp_Amplitude_Label_frame)

        self.Chirp_Amplitude_Value_frame = QFrame(self.Chirp_Amplitude)
        self.Chirp_Amplitude_Value_frame.setObjectName(u"Chirp_Amplitude_Value_frame")
        self.Chirp_Amplitude_Value_frame.setMinimumSize(QSize(150, 0))
        self.Chirp_Amplitude_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_Amplitude_Value_frame.setFont(font5)
        self.Chirp_Amplitude_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Amplitude_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_383 = QHBoxLayout(self.Chirp_Amplitude_Value_frame)
        self.horizontalLayout_383.setSpacing(0)
        self.horizontalLayout_383.setObjectName(u"horizontalLayout_383")
        self.horizontalLayout_383.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Amplitude_Value = QLineEdit(self.Chirp_Amplitude_Value_frame)
        self.Chirp_Amplitude_Value.setObjectName(u"Chirp_Amplitude_Value")
        self.Chirp_Amplitude_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_Amplitude_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_Amplitude_Value.setFont(font5)
        self.Chirp_Amplitude_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_383.addWidget(self.Chirp_Amplitude_Value)


        self.horizontalLayout_381.addWidget(self.Chirp_Amplitude_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_Amplitude)

        self.Chirp_Frequency_frame = QFrame(self.page_Chirp)
        self.Chirp_Frequency_frame.setObjectName(u"Chirp_Frequency_frame")
        self.Chirp_Frequency_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Frequency_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_393 = QHBoxLayout(self.Chirp_Frequency_frame)
        self.horizontalLayout_393.setSpacing(0)
        self.horizontalLayout_393.setObjectName(u"horizontalLayout_393")
        self.horizontalLayout_393.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Frequency_Label_frame = QFrame(self.Chirp_Frequency_frame)
        self.Chirp_Frequency_Label_frame.setObjectName(u"Chirp_Frequency_Label_frame")
        self.Chirp_Frequency_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_Frequency_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Frequency_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_394 = QHBoxLayout(self.Chirp_Frequency_Label_frame)
        self.horizontalLayout_394.setSpacing(0)
        self.horizontalLayout_394.setObjectName(u"horizontalLayout_394")
        self.horizontalLayout_394.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Frequency_Label = QLabel(self.Chirp_Frequency_Label_frame)
        self.Chirp_Frequency_Label.setObjectName(u"Chirp_Frequency_Label")
        self.Chirp_Frequency_Label.setMaximumSize(QSize(150, 16777215))
        self.Chirp_Frequency_Label.setFont(font1)
        self.Chirp_Frequency_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_Frequency_Label.setWordWrap(True)

        self.horizontalLayout_394.addWidget(self.Chirp_Frequency_Label)


        self.horizontalLayout_393.addWidget(self.Chirp_Frequency_Label_frame)

        self.Chirp_Frequency_Value_frame = QFrame(self.Chirp_Frequency_frame)
        self.Chirp_Frequency_Value_frame.setObjectName(u"Chirp_Frequency_Value_frame")
        self.Chirp_Frequency_Value_frame.setMinimumSize(QSize(150, 0))
        self.Chirp_Frequency_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_Frequency_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Frequency_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_395 = QHBoxLayout(self.Chirp_Frequency_Value_frame)
        self.horizontalLayout_395.setSpacing(0)
        self.horizontalLayout_395.setObjectName(u"horizontalLayout_395")
        self.horizontalLayout_395.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Frequency_Value = QLineEdit(self.Chirp_Frequency_Value_frame)
        self.Chirp_Frequency_Value.setObjectName(u"Chirp_Frequency_Value")
        self.Chirp_Frequency_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_Frequency_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_Frequency_Value.setFont(font5)
        self.Chirp_Frequency_Value.setStyleSheet(u"background-color: rgb(80, 110, 117);\n"
"border : none;")
        self.Chirp_Frequency_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_395.addWidget(self.Chirp_Frequency_Value)


        self.horizontalLayout_393.addWidget(self.Chirp_Frequency_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_Frequency_frame)

        self.Chirp_StartFrequency_frame = QFrame(self.page_Chirp)
        self.Chirp_StartFrequency_frame.setObjectName(u"Chirp_StartFrequency_frame")
        self.Chirp_StartFrequency_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StartFrequency_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_396 = QHBoxLayout(self.Chirp_StartFrequency_frame)
        self.horizontalLayout_396.setSpacing(0)
        self.horizontalLayout_396.setObjectName(u"horizontalLayout_396")
        self.horizontalLayout_396.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StartFrequency_Label_frame = QFrame(self.Chirp_StartFrequency_frame)
        self.Chirp_StartFrequency_Label_frame.setObjectName(u"Chirp_StartFrequency_Label_frame")
        self.Chirp_StartFrequency_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_StartFrequency_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StartFrequency_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_397 = QHBoxLayout(self.Chirp_StartFrequency_Label_frame)
        self.horizontalLayout_397.setSpacing(0)
        self.horizontalLayout_397.setObjectName(u"horizontalLayout_397")
        self.horizontalLayout_397.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StartFrequency_Label = QLabel(self.Chirp_StartFrequency_Label_frame)
        self.Chirp_StartFrequency_Label.setObjectName(u"Chirp_StartFrequency_Label")
        self.Chirp_StartFrequency_Label.setMaximumSize(QSize(150, 16777215))
        self.Chirp_StartFrequency_Label.setFont(font1)
        self.Chirp_StartFrequency_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_StartFrequency_Label.setWordWrap(True)

        self.horizontalLayout_397.addWidget(self.Chirp_StartFrequency_Label)


        self.horizontalLayout_396.addWidget(self.Chirp_StartFrequency_Label_frame)

        self.Chirp_StartFrequency_Value_frame = QFrame(self.Chirp_StartFrequency_frame)
        self.Chirp_StartFrequency_Value_frame.setObjectName(u"Chirp_StartFrequency_Value_frame")
        self.Chirp_StartFrequency_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_StartFrequency_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StartFrequency_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_398 = QHBoxLayout(self.Chirp_StartFrequency_Value_frame)
        self.horizontalLayout_398.setSpacing(0)
        self.horizontalLayout_398.setObjectName(u"horizontalLayout_398")
        self.horizontalLayout_398.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StartFrequency_Value = QLineEdit(self.Chirp_StartFrequency_Value_frame)
        self.Chirp_StartFrequency_Value.setObjectName(u"Chirp_StartFrequency_Value")
        self.Chirp_StartFrequency_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_StartFrequency_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_StartFrequency_Value.setFont(font5)
        self.Chirp_StartFrequency_Value.setStyleSheet(u"")
        self.Chirp_StartFrequency_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_398.addWidget(self.Chirp_StartFrequency_Value)


        self.horizontalLayout_396.addWidget(self.Chirp_StartFrequency_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_StartFrequency_frame)

        self.Chirp_EndFrequency_frame = QFrame(self.page_Chirp)
        self.Chirp_EndFrequency_frame.setObjectName(u"Chirp_EndFrequency_frame")
        self.Chirp_EndFrequency_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_EndFrequency_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_384 = QHBoxLayout(self.Chirp_EndFrequency_frame)
        self.horizontalLayout_384.setSpacing(0)
        self.horizontalLayout_384.setObjectName(u"horizontalLayout_384")
        self.horizontalLayout_384.setContentsMargins(0, 0, 0, 0)
        self.Chirp_EndFrequency_Label_frame = QFrame(self.Chirp_EndFrequency_frame)
        self.Chirp_EndFrequency_Label_frame.setObjectName(u"Chirp_EndFrequency_Label_frame")
        self.Chirp_EndFrequency_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_EndFrequency_Label_frame.setFont(font1)
        self.Chirp_EndFrequency_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_EndFrequency_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_385 = QHBoxLayout(self.Chirp_EndFrequency_Label_frame)
        self.horizontalLayout_385.setSpacing(0)
        self.horizontalLayout_385.setObjectName(u"horizontalLayout_385")
        self.horizontalLayout_385.setContentsMargins(0, 0, 0, 0)
        self.Chirp_EndFrequency_Label = QLabel(self.Chirp_EndFrequency_Label_frame)
        self.Chirp_EndFrequency_Label.setObjectName(u"Chirp_EndFrequency_Label")
        self.Chirp_EndFrequency_Label.setMaximumSize(QSize(150, 16777215))
        self.Chirp_EndFrequency_Label.setFont(font1)
        self.Chirp_EndFrequency_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_EndFrequency_Label.setWordWrap(True)

        self.horizontalLayout_385.addWidget(self.Chirp_EndFrequency_Label)


        self.horizontalLayout_384.addWidget(self.Chirp_EndFrequency_Label_frame)

        self.Chirp_EndFrequency_Value_frame = QFrame(self.Chirp_EndFrequency_frame)
        self.Chirp_EndFrequency_Value_frame.setObjectName(u"Chirp_EndFrequency_Value_frame")
        self.Chirp_EndFrequency_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_EndFrequency_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_EndFrequency_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_386 = QHBoxLayout(self.Chirp_EndFrequency_Value_frame)
        self.horizontalLayout_386.setSpacing(0)
        self.horizontalLayout_386.setObjectName(u"horizontalLayout_386")
        self.horizontalLayout_386.setContentsMargins(0, 0, 0, 0)
        self.Chirp_EndFrequency_Value = QLineEdit(self.Chirp_EndFrequency_Value_frame)
        self.Chirp_EndFrequency_Value.setObjectName(u"Chirp_EndFrequency_Value")
        self.Chirp_EndFrequency_Value.setEnabled(False)
        self.Chirp_EndFrequency_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_EndFrequency_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_EndFrequency_Value.setFont(font5)
        self.Chirp_EndFrequency_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_386.addWidget(self.Chirp_EndFrequency_Value)


        self.horizontalLayout_384.addWidget(self.Chirp_EndFrequency_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_EndFrequency_frame)

        self.Chirp_Duration_Frame = QFrame(self.page_Chirp)
        self.Chirp_Duration_Frame.setObjectName(u"Chirp_Duration_Frame")
        self.Chirp_Duration_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Duration_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_401 = QHBoxLayout(self.Chirp_Duration_Frame)
        self.horizontalLayout_401.setSpacing(0)
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.horizontalLayout_401.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Duration_Label_Frame = QFrame(self.Chirp_Duration_Frame)
        self.Chirp_Duration_Label_Frame.setObjectName(u"Chirp_Duration_Label_Frame")
        self.Chirp_Duration_Label_Frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_Duration_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Duration_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_400 = QHBoxLayout(self.Chirp_Duration_Label_Frame)
        self.horizontalLayout_400.setSpacing(0)
        self.horizontalLayout_400.setObjectName(u"horizontalLayout_400")
        self.horizontalLayout_400.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Duration_Label = QLabel(self.Chirp_Duration_Label_Frame)
        self.Chirp_Duration_Label.setObjectName(u"Chirp_Duration_Label")
        self.Chirp_Duration_Label.setFont(font1)
        self.Chirp_Duration_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_400.addWidget(self.Chirp_Duration_Label)


        self.horizontalLayout_401.addWidget(self.Chirp_Duration_Label_Frame)

        self.Chirp_Duration_Value_Frame = QFrame(self.Chirp_Duration_Frame)
        self.Chirp_Duration_Value_Frame.setObjectName(u"Chirp_Duration_Value_Frame")
        self.Chirp_Duration_Value_Frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_Duration_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_Duration_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_399 = QHBoxLayout(self.Chirp_Duration_Value_Frame)
        self.horizontalLayout_399.setSpacing(0)
        self.horizontalLayout_399.setObjectName(u"horizontalLayout_399")
        self.horizontalLayout_399.setContentsMargins(0, 0, 0, 0)
        self.Chirp_Duration_Value = QLineEdit(self.Chirp_Duration_Value_Frame)
        self.Chirp_Duration_Value.setObjectName(u"Chirp_Duration_Value")
        self.Chirp_Duration_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_Duration_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_Duration_Value.setFont(font5)
        self.Chirp_Duration_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_399.addWidget(self.Chirp_Duration_Value)


        self.horizontalLayout_401.addWidget(self.Chirp_Duration_Value_Frame)


        self.verticalLayout_100.addWidget(self.Chirp_Duration_Frame)

        self.line_65 = QFrame(self.page_Chirp)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_65.setFrameShape(QFrame.Shape.HLine)
        self.line_65.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_100.addWidget(self.line_65)

        self.Chirp_PreChirpOn_Frame = QFrame(self.page_Chirp)
        self.Chirp_PreChirpOn_Frame.setObjectName(u"Chirp_PreChirpOn_Frame")
        self.Chirp_PreChirpOn_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOn_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_405 = QHBoxLayout(self.Chirp_PreChirpOn_Frame)
        self.horizontalLayout_405.setSpacing(5)
        self.horizontalLayout_405.setObjectName(u"horizontalLayout_405")
        self.horizontalLayout_405.setContentsMargins(0, 0, 5, 0)
        self.Chirp_PreChirpOn_Duration_Label_Frame = QFrame(self.Chirp_PreChirpOn_Frame)
        self.Chirp_PreChirpOn_Duration_Label_Frame.setObjectName(u"Chirp_PreChirpOn_Duration_Label_Frame")
        self.Chirp_PreChirpOn_Duration_Label_Frame.setMinimumSize(QSize(165, 0))
        self.Chirp_PreChirpOn_Duration_Label_Frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_PreChirpOn_Duration_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOn_Duration_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_404 = QHBoxLayout(self.Chirp_PreChirpOn_Duration_Label_Frame)
        self.horizontalLayout_404.setSpacing(0)
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.horizontalLayout_404.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOn_Duration_Label = QLabel(self.Chirp_PreChirpOn_Duration_Label_Frame)
        self.Chirp_PreChirpOn_Duration_Label.setObjectName(u"Chirp_PreChirpOn_Duration_Label")
        self.Chirp_PreChirpOn_Duration_Label.setMinimumSize(QSize(0, 0))
        self.Chirp_PreChirpOn_Duration_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Chirp_PreChirpOn_Duration_Label.setFont(font1)
        self.Chirp_PreChirpOn_Duration_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_PreChirpOn_Duration_Label.setWordWrap(True)

        self.horizontalLayout_404.addWidget(self.Chirp_PreChirpOn_Duration_Label)


        self.horizontalLayout_405.addWidget(self.Chirp_PreChirpOn_Duration_Label_Frame)

        self.Chirp_PreChirpOn_Amplitude_Value_Frame = QFrame(self.Chirp_PreChirpOn_Frame)
        self.Chirp_PreChirpOn_Amplitude_Value_Frame.setObjectName(u"Chirp_PreChirpOn_Amplitude_Value_Frame")
        self.Chirp_PreChirpOn_Amplitude_Value_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpOn_Amplitude_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOn_Amplitude_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_403 = QHBoxLayout(self.Chirp_PreChirpOn_Amplitude_Value_Frame)
        self.horizontalLayout_403.setSpacing(0)
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.horizontalLayout_403.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOn_Amplitude_Value = QLineEdit(self.Chirp_PreChirpOn_Amplitude_Value_Frame)
        self.Chirp_PreChirpOn_Amplitude_Value.setObjectName(u"Chirp_PreChirpOn_Amplitude_Value")
        self.Chirp_PreChirpOn_Amplitude_Value.setMinimumSize(QSize(50, 0))
        self.Chirp_PreChirpOn_Amplitude_Value.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpOn_Amplitude_Value.setFont(font5)
        self.Chirp_PreChirpOn_Amplitude_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_403.addWidget(self.Chirp_PreChirpOn_Amplitude_Value)


        self.horizontalLayout_405.addWidget(self.Chirp_PreChirpOn_Amplitude_Value_Frame)

        self.Chirp_PreChirpOn_Duration_Value_Frame = QFrame(self.Chirp_PreChirpOn_Frame)
        self.Chirp_PreChirpOn_Duration_Value_Frame.setObjectName(u"Chirp_PreChirpOn_Duration_Value_Frame")
        self.Chirp_PreChirpOn_Duration_Value_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpOn_Duration_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOn_Duration_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_406 = QHBoxLayout(self.Chirp_PreChirpOn_Duration_Value_Frame)
        self.horizontalLayout_406.setSpacing(0)
        self.horizontalLayout_406.setObjectName(u"horizontalLayout_406")
        self.horizontalLayout_406.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOn_Duration_Value = QLineEdit(self.Chirp_PreChirpOn_Duration_Value_Frame)
        self.Chirp_PreChirpOn_Duration_Value.setObjectName(u"Chirp_PreChirpOn_Duration_Value")
        self.Chirp_PreChirpOn_Duration_Value.setMinimumSize(QSize(50, 0))
        self.Chirp_PreChirpOn_Duration_Value.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpOn_Duration_Value.setFont(font5)
        self.Chirp_PreChirpOn_Duration_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_406.addWidget(self.Chirp_PreChirpOn_Duration_Value)


        self.horizontalLayout_405.addWidget(self.Chirp_PreChirpOn_Duration_Value_Frame)


        self.verticalLayout_100.addWidget(self.Chirp_PreChirpOn_Frame)

        self.Chirp_PreChirpOff_Frame = QFrame(self.page_Chirp)
        self.Chirp_PreChirpOff_Frame.setObjectName(u"Chirp_PreChirpOff_Frame")
        self.Chirp_PreChirpOff_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOff_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_408 = QHBoxLayout(self.Chirp_PreChirpOff_Frame)
        self.horizontalLayout_408.setSpacing(5)
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.horizontalLayout_408.setContentsMargins(0, 0, 5, 0)
        self.Chirp_PreChirpOff_Label_Frame = QFrame(self.Chirp_PreChirpOff_Frame)
        self.Chirp_PreChirpOff_Label_Frame.setObjectName(u"Chirp_PreChirpOff_Label_Frame")
        self.Chirp_PreChirpOff_Label_Frame.setMinimumSize(QSize(165, 0))
        self.Chirp_PreChirpOff_Label_Frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_PreChirpOff_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOff_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_407 = QHBoxLayout(self.Chirp_PreChirpOff_Label_Frame)
        self.horizontalLayout_407.setSpacing(0)
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.horizontalLayout_407.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOff_Label = QLabel(self.Chirp_PreChirpOff_Label_Frame)
        self.Chirp_PreChirpOff_Label.setObjectName(u"Chirp_PreChirpOff_Label")
        self.Chirp_PreChirpOff_Label.setFont(font1)
        self.Chirp_PreChirpOff_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_PreChirpOff_Label.setWordWrap(True)

        self.horizontalLayout_407.addWidget(self.Chirp_PreChirpOff_Label)


        self.horizontalLayout_408.addWidget(self.Chirp_PreChirpOff_Label_Frame)

        self.Chirp_PreChirpOff_Amplitude_Value_Frame = QFrame(self.Chirp_PreChirpOff_Frame)
        self.Chirp_PreChirpOff_Amplitude_Value_Frame.setObjectName(u"Chirp_PreChirpOff_Amplitude_Value_Frame")
        self.Chirp_PreChirpOff_Amplitude_Value_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpOff_Amplitude_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOff_Amplitude_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_410 = QHBoxLayout(self.Chirp_PreChirpOff_Amplitude_Value_Frame)
        self.horizontalLayout_410.setSpacing(0)
        self.horizontalLayout_410.setObjectName(u"horizontalLayout_410")
        self.horizontalLayout_410.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOff_Amplitude_Value = QLineEdit(self.Chirp_PreChirpOff_Amplitude_Value_Frame)
        self.Chirp_PreChirpOff_Amplitude_Value.setObjectName(u"Chirp_PreChirpOff_Amplitude_Value")
        self.Chirp_PreChirpOff_Amplitude_Value.setMinimumSize(QSize(50, 0))
        self.Chirp_PreChirpOff_Amplitude_Value.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpOff_Amplitude_Value.setFont(font5)
        self.Chirp_PreChirpOff_Amplitude_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_410.addWidget(self.Chirp_PreChirpOff_Amplitude_Value)


        self.horizontalLayout_408.addWidget(self.Chirp_PreChirpOff_Amplitude_Value_Frame)

        self.Chirp_PreChirpOff_Duration_Value_Frame = QFrame(self.Chirp_PreChirpOff_Frame)
        self.Chirp_PreChirpOff_Duration_Value_Frame.setObjectName(u"Chirp_PreChirpOff_Duration_Value_Frame")
        self.Chirp_PreChirpOff_Duration_Value_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpOff_Duration_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpOff_Duration_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_409 = QHBoxLayout(self.Chirp_PreChirpOff_Duration_Value_Frame)
        self.horizontalLayout_409.setSpacing(0)
        self.horizontalLayout_409.setObjectName(u"horizontalLayout_409")
        self.horizontalLayout_409.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpOff_Duration_Value = QLineEdit(self.Chirp_PreChirpOff_Duration_Value_Frame)
        self.Chirp_PreChirpOff_Duration_Value.setObjectName(u"Chirp_PreChirpOff_Duration_Value")
        self.Chirp_PreChirpOff_Duration_Value.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpOff_Duration_Value.setFont(font5)
        self.Chirp_PreChirpOff_Duration_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_409.addWidget(self.Chirp_PreChirpOff_Duration_Value)


        self.horizontalLayout_408.addWidget(self.Chirp_PreChirpOff_Duration_Value_Frame)


        self.verticalLayout_100.addWidget(self.Chirp_PreChirpOff_Frame)

        self.Chirp_PreChirpMid_Frame = QFrame(self.page_Chirp)
        self.Chirp_PreChirpMid_Frame.setObjectName(u"Chirp_PreChirpMid_Frame")
        self.Chirp_PreChirpMid_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpMid_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_414 = QHBoxLayout(self.Chirp_PreChirpMid_Frame)
        self.horizontalLayout_414.setSpacing(5)
        self.horizontalLayout_414.setObjectName(u"horizontalLayout_414")
        self.horizontalLayout_414.setContentsMargins(0, 0, 5, 0)
        self.Chirp_PreChirpMid_Label_Frame = QFrame(self.Chirp_PreChirpMid_Frame)
        self.Chirp_PreChirpMid_Label_Frame.setObjectName(u"Chirp_PreChirpMid_Label_Frame")
        self.Chirp_PreChirpMid_Label_Frame.setMinimumSize(QSize(165, 0))
        self.Chirp_PreChirpMid_Label_Frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_PreChirpMid_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpMid_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_411 = QHBoxLayout(self.Chirp_PreChirpMid_Label_Frame)
        self.horizontalLayout_411.setSpacing(0)
        self.horizontalLayout_411.setObjectName(u"horizontalLayout_411")
        self.horizontalLayout_411.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpMid_Label = QLabel(self.Chirp_PreChirpMid_Label_Frame)
        self.Chirp_PreChirpMid_Label.setObjectName(u"Chirp_PreChirpMid_Label")
        self.Chirp_PreChirpMid_Label.setFont(font1)
        self.Chirp_PreChirpMid_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_PreChirpMid_Label.setWordWrap(True)

        self.horizontalLayout_411.addWidget(self.Chirp_PreChirpMid_Label)


        self.horizontalLayout_414.addWidget(self.Chirp_PreChirpMid_Label_Frame)

        self.Chirp_PreChirpMid_Amplitude_Frame = QFrame(self.Chirp_PreChirpMid_Frame)
        self.Chirp_PreChirpMid_Amplitude_Frame.setObjectName(u"Chirp_PreChirpMid_Amplitude_Frame")
        self.Chirp_PreChirpMid_Amplitude_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpMid_Amplitude_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpMid_Amplitude_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_412 = QHBoxLayout(self.Chirp_PreChirpMid_Amplitude_Frame)
        self.horizontalLayout_412.setSpacing(0)
        self.horizontalLayout_412.setObjectName(u"horizontalLayout_412")
        self.horizontalLayout_412.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpMid_Amplitude = QLineEdit(self.Chirp_PreChirpMid_Amplitude_Frame)
        self.Chirp_PreChirpMid_Amplitude.setObjectName(u"Chirp_PreChirpMid_Amplitude")
        self.Chirp_PreChirpMid_Amplitude.setEnabled(True)
        self.Chirp_PreChirpMid_Amplitude.setMinimumSize(QSize(50, 0))
        self.Chirp_PreChirpMid_Amplitude.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpMid_Amplitude.setFont(font5)
        self.Chirp_PreChirpMid_Amplitude.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_412.addWidget(self.Chirp_PreChirpMid_Amplitude)


        self.horizontalLayout_414.addWidget(self.Chirp_PreChirpMid_Amplitude_Frame)

        self.Chirp_PreChirpMid_Duration_Frame = QFrame(self.Chirp_PreChirpMid_Frame)
        self.Chirp_PreChirpMid_Duration_Frame.setObjectName(u"Chirp_PreChirpMid_Duration_Frame")
        self.Chirp_PreChirpMid_Duration_Frame.setMaximumSize(QSize(75, 16777215))
        self.Chirp_PreChirpMid_Duration_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_PreChirpMid_Duration_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_413 = QHBoxLayout(self.Chirp_PreChirpMid_Duration_Frame)
        self.horizontalLayout_413.setSpacing(0)
        self.horizontalLayout_413.setObjectName(u"horizontalLayout_413")
        self.horizontalLayout_413.setContentsMargins(0, 0, 0, 0)
        self.Chirp_PreChirpMid_Duration = QLineEdit(self.Chirp_PreChirpMid_Duration_Frame)
        self.Chirp_PreChirpMid_Duration.setObjectName(u"Chirp_PreChirpMid_Duration")
        self.Chirp_PreChirpMid_Duration.setMinimumSize(QSize(50, 0))
        self.Chirp_PreChirpMid_Duration.setMaximumSize(QSize(50, 16777215))
        self.Chirp_PreChirpMid_Duration.setFont(font5)
        self.Chirp_PreChirpMid_Duration.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_413.addWidget(self.Chirp_PreChirpMid_Duration)


        self.horizontalLayout_414.addWidget(self.Chirp_PreChirpMid_Duration_Frame)


        self.verticalLayout_100.addWidget(self.Chirp_PreChirpMid_Frame)

        self.line_66 = QFrame(self.page_Chirp)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_66.setFrameShape(QFrame.Shape.HLine)
        self.line_66.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_100.addWidget(self.line_66)

        self.Chirp_IntOff_frame = QFrame(self.page_Chirp)
        self.Chirp_IntOff_frame.setObjectName(u"Chirp_IntOff_frame")
        self.Chirp_IntOff_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_IntOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_390 = QHBoxLayout(self.Chirp_IntOff_frame)
        self.horizontalLayout_390.setSpacing(0)
        self.horizontalLayout_390.setObjectName(u"horizontalLayout_390")
        self.horizontalLayout_390.setContentsMargins(0, 0, 0, 0)
        self.Chirp_IntOff_Label_frame = QFrame(self.Chirp_IntOff_frame)
        self.Chirp_IntOff_Label_frame.setObjectName(u"Chirp_IntOff_Label_frame")
        self.Chirp_IntOff_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_IntOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_IntOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_391 = QHBoxLayout(self.Chirp_IntOff_Label_frame)
        self.horizontalLayout_391.setSpacing(0)
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.horizontalLayout_391.setContentsMargins(0, 0, 0, 0)
        self.Chirp_IntOff_Label = QLabel(self.Chirp_IntOff_Label_frame)
        self.Chirp_IntOff_Label.setObjectName(u"Chirp_IntOff_Label")
        self.Chirp_IntOff_Label.setFont(font1)
        self.Chirp_IntOff_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_IntOff_Label.setWordWrap(True)

        self.horizontalLayout_391.addWidget(self.Chirp_IntOff_Label)


        self.horizontalLayout_390.addWidget(self.Chirp_IntOff_Label_frame)

        self.Chirp_IntOff_Value_frame = QFrame(self.Chirp_IntOff_frame)
        self.Chirp_IntOff_Value_frame.setObjectName(u"Chirp_IntOff_Value_frame")
        self.Chirp_IntOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_IntOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_IntOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_392 = QHBoxLayout(self.Chirp_IntOff_Value_frame)
        self.horizontalLayout_392.setSpacing(0)
        self.horizontalLayout_392.setObjectName(u"horizontalLayout_392")
        self.horizontalLayout_392.setContentsMargins(0, 0, 0, 0)
        self.Chirp_IntOff_Value = QLineEdit(self.Chirp_IntOff_Value_frame)
        self.Chirp_IntOff_Value.setObjectName(u"Chirp_IntOff_Value")
        self.Chirp_IntOff_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_IntOff_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_IntOff_Value.setFont(font5)
        self.Chirp_IntOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_392.addWidget(self.Chirp_IntOff_Value)


        self.horizontalLayout_390.addWidget(self.Chirp_IntOff_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_IntOff_frame)

        self.Chirp_StimOff_frame = QFrame(self.page_Chirp)
        self.Chirp_StimOff_frame.setObjectName(u"Chirp_StimOff_frame")
        self.Chirp_StimOff_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StimOff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_387 = QHBoxLayout(self.Chirp_StimOff_frame)
        self.horizontalLayout_387.setSpacing(0)
        self.horizontalLayout_387.setObjectName(u"horizontalLayout_387")
        self.horizontalLayout_387.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StimOff_Label_frame = QFrame(self.Chirp_StimOff_frame)
        self.Chirp_StimOff_Label_frame.setObjectName(u"Chirp_StimOff_Label_frame")
        self.Chirp_StimOff_Label_frame.setMaximumSize(QSize(175, 16777215))
        self.Chirp_StimOff_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StimOff_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_388 = QHBoxLayout(self.Chirp_StimOff_Label_frame)
        self.horizontalLayout_388.setSpacing(0)
        self.horizontalLayout_388.setObjectName(u"horizontalLayout_388")
        self.horizontalLayout_388.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StimOff_Label = QLabel(self.Chirp_StimOff_Label_frame)
        self.Chirp_StimOff_Label.setObjectName(u"Chirp_StimOff_Label")
        self.Chirp_StimOff_Label.setFont(font1)
        self.Chirp_StimOff_Label.setAlignment(Qt.AlignCenter)
        self.Chirp_StimOff_Label.setWordWrap(True)

        self.horizontalLayout_388.addWidget(self.Chirp_StimOff_Label)


        self.horizontalLayout_387.addWidget(self.Chirp_StimOff_Label_frame)

        self.Chirp_StimOff_Value_frame = QFrame(self.Chirp_StimOff_frame)
        self.Chirp_StimOff_Value_frame.setObjectName(u"Chirp_StimOff_Value_frame")
        self.Chirp_StimOff_Value_frame.setMaximumSize(QSize(150, 16777215))
        self.Chirp_StimOff_Value_frame.setFrameShape(QFrame.StyledPanel)
        self.Chirp_StimOff_Value_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_389 = QHBoxLayout(self.Chirp_StimOff_Value_frame)
        self.horizontalLayout_389.setSpacing(0)
        self.horizontalLayout_389.setObjectName(u"horizontalLayout_389")
        self.horizontalLayout_389.setContentsMargins(0, 0, 0, 0)
        self.Chirp_StimOff_Value = QLineEdit(self.Chirp_StimOff_Value_frame)
        self.Chirp_StimOff_Value.setObjectName(u"Chirp_StimOff_Value")
        self.Chirp_StimOff_Value.setMinimumSize(QSize(100, 0))
        self.Chirp_StimOff_Value.setMaximumSize(QSize(100, 16777215))
        self.Chirp_StimOff_Value.setFont(font5)
        self.Chirp_StimOff_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_389.addWidget(self.Chirp_StimOff_Value)


        self.horizontalLayout_387.addWidget(self.Chirp_StimOff_Value_frame)


        self.verticalLayout_100.addWidget(self.Chirp_StimOff_frame)

        self.StimulusGenerator_Parameter_stackedWidget.addWidget(self.page_Chirp)

        self.horizontalLayout_205.addWidget(self.StimulusGenerator_Parameter_stackedWidget)


        self.horizontalLayout_203.addWidget(self.StimulusGenerator_Parameter_frame)


        self.verticalLayout_110.addWidget(self.StimulusGenerator_Container)

        self.mainbody_stackedWidget.addWidget(self.page_401)
        self.page_501 = QWidget()
        self.page_501.setObjectName(u"page_501")
        self.horizontalLayout_192 = QHBoxLayout(self.page_501)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.Exercise101_Main_frame = QFrame(self.page_501)
        self.Exercise101_Main_frame.setObjectName(u"Exercise101_Main_frame")
        self.Exercise101_Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercise101_Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.Exercise101_Main_frame)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.Exercise101_StackedWideget_frame = QFrame(self.Exercise101_Main_frame)
        self.Exercise101_StackedWideget_frame.setObjectName(u"Exercise101_StackedWideget_frame")
        self.Exercise101_StackedWideget_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercise101_StackedWideget_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.Exercise101_StackedWideget_frame)
        self.horizontalLayout_159.setSpacing(0)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.Exercise101_stackedWidget = QStackedWidget(self.Exercise101_StackedWideget_frame)
        self.Exercise101_stackedWidget.setObjectName(u"Exercise101_stackedWidget")
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
        font11 = QFont()
        font11.setPointSize(18)
        self.Vm_IntroTitle.setFont(font11)
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

        self.Exercise101_stackedWidget.addWidget(self.page501_01_01)
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
        sizePolicy2.setHeightForWidth(self.Vm_Task01_Title_frame.sizePolicy().hasHeightForWidth())
        self.Vm_Task01_Title_frame.setSizePolicy(sizePolicy2)
        self.Vm_Task01_Title_frame.setMaximumSize(QSize(16777215, 50))
        font12 = QFont()
        font12.setPointSize(14)
        self.Vm_Task01_Title_frame.setFont(font12)
        self.Vm_Task01_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Vm_Task01_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_194 = QHBoxLayout(self.Vm_Task01_Title_frame)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.Vm_Task01_Title = QLabel(self.Vm_Task01_Title_frame)
        self.Vm_Task01_Title.setObjectName(u"Vm_Task01_Title")
        self.Vm_Task01_Title.setMaximumSize(QSize(16777215, 50))
        self.Vm_Task01_Title.setFont(font11)
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

        self.Exercise101_stackedWidget.addWidget(self.page501_01_02)
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
        self.Vm_Task02_Text.setFont(font11)
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

        self.Exercise101_stackedWidget.addWidget(self.page501_01_03)
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
        self.Vm_Task03_Title.setFont(font11)
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

        self.Exercise101_stackedWidget.addWidget(self.page501_01_04)

        self.horizontalLayout_159.addWidget(self.Exercise101_stackedWidget)


        self.verticalLayout_116.addWidget(self.Exercise101_StackedWideget_frame)

        self.Exercise101_Button_frame = QFrame(self.Exercise101_Main_frame)
        self.Exercise101_Button_frame.setObjectName(u"Exercise101_Button_frame")
        self.Exercise101_Button_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercise101_Button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_191 = QHBoxLayout(self.Exercise101_Button_frame)
        self.horizontalLayout_191.setSpacing(0)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.Exercise101_PreviousButton_frame = QFrame(self.Exercise101_Button_frame)
        self.Exercise101_PreviousButton_frame.setObjectName(u"Exercise101_PreviousButton_frame")
        self.Exercise101_PreviousButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercise101_PreviousButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_190 = QHBoxLayout(self.Exercise101_PreviousButton_frame)
        self.horizontalLayout_190.setSpacing(0)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.Exercise101_PreviousButton_pushButton = QPushButton(self.Exercise101_PreviousButton_frame)
        self.Exercise101_PreviousButton_pushButton.setObjectName(u"Exercise101_PreviousButton_pushButton")
        self.Exercise101_PreviousButton_pushButton.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_190.addWidget(self.Exercise101_PreviousButton_pushButton)


        self.horizontalLayout_191.addWidget(self.Exercise101_PreviousButton_frame)

        self.Exercise101_AfterButton_frame = QFrame(self.Exercise101_Button_frame)
        self.Exercise101_AfterButton_frame.setObjectName(u"Exercise101_AfterButton_frame")
        self.Exercise101_AfterButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Exercise101_AfterButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.Exercise101_AfterButton_frame)
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(0, 0, 0, 0)
        self.Exercise101_AfterButton_pushButton = QPushButton(self.Exercise101_AfterButton_frame)
        self.Exercise101_AfterButton_pushButton.setObjectName(u"Exercise101_AfterButton_pushButton")
        self.Exercise101_AfterButton_pushButton.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_189.addWidget(self.Exercise101_AfterButton_pushButton)


        self.horizontalLayout_191.addWidget(self.Exercise101_AfterButton_frame)


        self.verticalLayout_116.addWidget(self.Exercise101_Button_frame)


        self.horizontalLayout_192.addWidget(self.Exercise101_Main_frame)

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
        self.mainbody_footer_frame_2 = QFrame(self.frame_12)
        self.mainbody_footer_frame_2.setObjectName(u"mainbody_footer_frame_2")
        self.mainbody_footer_frame_2.setFrameShape(QFrame.StyledPanel)
        self.mainbody_footer_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_250 = QHBoxLayout(self.mainbody_footer_frame_2)
        self.horizontalLayout_250.setSpacing(0)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.horizontalLayout_250.setContentsMargins(10, 0, 10, 5)
        self.mainbody_footer_text_2 = QLabel(self.mainbody_footer_frame_2)
        self.mainbody_footer_text_2.setObjectName(u"mainbody_footer_text_2")
        sizePolicy2.setHeightForWidth(self.mainbody_footer_text_2.sizePolicy().hasHeightForWidth())
        self.mainbody_footer_text_2.setSizePolicy(sizePolicy2)
        self.mainbody_footer_text_2.setMinimumSize(QSize(0, 100))
        self.mainbody_footer_text_2.setScaledContents(False)
        self.mainbody_footer_text_2.setWordWrap(True)

        self.horizontalLayout_250.addWidget(self.mainbody_footer_text_2)


        self.verticalLayout_114.addWidget(self.mainbody_footer_frame_2)

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
        self.license_label = QLabel(self.license_frame)
        self.license_label.setObjectName(u"license_label")

        self.verticalLayout_3.addWidget(self.license_label)


        self.horizontalLayout_3.addWidget(self.license_frame)

        self.logo_frame = QFrame(self.footer_widget)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sussex_logo = QLabel(self.logo_frame)
        self.sussex_logo.setObjectName(u"sussex_logo")
        self.sussex_logo.setMinimumSize(QSize(85, 25))
        self.sussex_logo.setMaximumSize(QSize(85, 25))
        self.sussex_logo.setPixmap(QPixmap(u":/resources/resources/SN-Logo.png"))
        self.sussex_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.sussex_logo)

        self.trend_logo = QLabel(self.logo_frame)
        self.trend_logo.setObjectName(u"trend_logo")
        sizePolicy2.setHeightForWidth(self.trend_logo.sizePolicy().hasHeightForWidth())
        self.trend_logo.setSizePolicy(sizePolicy2)
        self.trend_logo.setMinimumSize(QSize(34, 30))
        self.trend_logo.setMaximumSize(QSize(34, 30))
        self.trend_logo.setToolTipDuration(-1)
        self.trend_logo.setPixmap(QPixmap(u":/resources/resources/CaMinA.png"))
        self.trend_logo.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.trend_logo)

        self.OSN_logo = QLabel(self.logo_frame)
        self.OSN_logo.setObjectName(u"OSN_logo")
        sizePolicy2.setHeightForWidth(self.OSN_logo.sizePolicy().hasHeightForWidth())
        self.OSN_logo.setSizePolicy(sizePolicy2)
        self.OSN_logo.setMinimumSize(QSize(48, 30))
        self.OSN_logo.setMaximumSize(QSize(48, 30))
        self.OSN_logo.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.OSN_logo.setScaledContents(True)
        self.OSN_logo.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.OSN_logo)


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

        self.centerMenuSubContainer_menu_stackedwidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(2)
        self.toolBox.layout().setSpacing(10)
        self.mainbody_stackedWidget.setCurrentIndex(5)
        self.Spikeling_parameter_stackedwidget.setCurrentIndex(0)
        self.DataAnalysis_Display_StackedWidget.setCurrentIndex(6)
        self.DataAnalysis_stackedWidget.setCurrentIndex(0)
        self.Imaging_parameter_stackedWidget.setCurrentIndex(2)
        self.MultipleImaging_parameter_stackedWidget.setCurrentIndex(2)
        self.StimulusGenerator_Parameter_stackedWidget.setCurrentIndex(3)
        self.Exercise101_stackedWidget.setCurrentIndex(0)


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
        self.Neuron_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Interface", None))
        self.NeuronSimulation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Neuron Emulator", None))
        self.NeuronDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.NeuronTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.ImagingStimulation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging Stimulation", None))
        self.MultipleImagingStimulation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Multiple Imaging", None))
        self.ImagingTutorial_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.ImagingDataAnalysis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.Exercice101_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.1 - Adaptation", None))
        self.Exercice102_pushButton.setText(QCoreApplication.translate("MainWindow", u"1.2 - External light stimulation", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"1.3 - Direct Current Stimulation", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"1 - Introduction to Spikeling", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"2.1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2.2", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"2 - Electrophysiology", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"3 - Photo-stimulation", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"4 - Synapses", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"5 - Neuronal network", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"6- Fluorescence Imaging", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_9), QCoreApplication.translate("MainWindow", u"7 - Spike Inference", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_10), QCoreApplication.translate("MainWindow", u"8 - Methodology", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Color theme", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"graph width", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"delay esp", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Information about the project, sussex, TReND etc", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_8.setText("")
        self.mainbody_header_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#93a1a1;\">Spikeling </span><span style=\" font-size:16pt; color:#93a1a1;\">v2.2</span></p><p align=\"center\"><span style=\" font-size:16pt;\">A hardware implementation of spiking neurons for neursocience teaching and outreach</span></p><p align=\"right\"><span style=\" font-weight:696;\">Conceived and developed by M.J.Y. Zimmermann</span></p><p align=\"right\"><span style=\" font-weight:696;\">Based on an original idea from T. Baden</span></p></body></html>", None))
        self.mainbody_content_text.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:696;\">Spikeling</span><span style=\" font-family:'Segoe UI'; font-size:12pt;\"> is an educational tool for neuroscience students and enthusiasts!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">It is an artificial neuron that can receive different inputs, integrate them and outputs its computation, just like "
                        "a spiking neuron would!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt;\">It consists of a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.</span></p></body></html>", None))
        self.label_98.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#268bd2;\">This project is licensed under the </span><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:696; color:#268bd2;\">GNU General Public License v3.0</span></p><p align=\"justify\"><span style=\" font-family:'Segoe UI'; font-size:12pt; color:#268bd2;\">The hardware is licensed under the </span><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:696; color:#268bd2;\">CERN OHL v1.2</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#268bd2;\">https://github.com/OpenSourceNeuro/Spikeling-V2</span></p></body></html>", None))
        self.Spikeling_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.Spikeling_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.Spikeling_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect Spikeling Screen", None))
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
        self.Spikeling_DataRecording_SelectRecordFolder_label.setText(QCoreApplication.translate("MainWindow", u"Data Logging: Filename", None))
        self.Spikeling_DataRecording_RecordFolder_value.setText("")
        self.Spikeling_DataRecording_RecordFolderDir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse directory", None))
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
        self.Spikeling_CustomStimulus_StimLabel.setText(QCoreApplication.translate("MainWindow", u"Select a stimulus:", None))
        self.Spikeling_CustomStimulus_Load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
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
        self.Spikeling_Synapse1_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Spikeling_Synapse1_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.Spikeling_Synapse2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 2</span></p></body></html>", None))
        self.Spikeling_Synapse2_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Gain (%)", None))
        self.Spikeling_Synapse2_readings.setText("")
        self.Spikeling_Synapse2_min.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.Spikeling_Synapse2_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Spikeling_Synapse2_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Spikeling_Synapse2_Decay_Label.setText(QCoreApplication.translate("MainWindow", u"Synaptic Decay: \u03bb (ms\u05bf \u00b9) ", None))
        self.Spikeling_Synapse2_Decay_readings.setText("")
        self.Spikeling_Synapse2_Decay_values_slow.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.Spikeling_Synapse2_Decay_values_fast.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
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
        self.DataAnalysis_Neuron0Vm_pushButton110.setText(QCoreApplication.translate("MainWindow", u"Spikeling Neuron", None))
        self.DataAnalysis_Neuron1Vm_pushButton110.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 1", None))
        self.DataAnalysis_Neuron2Vm_pushButton110.setText(QCoreApplication.translate("MainWindow", u"Aux Neuron 2", None))
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
        self.DataAnalysis_StepStim_LoadData_label.setText("")
        self.DataAnalysis_StepStim_LoadData_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Load Data   ", None))
        self.DataAnalysis_StepStim_LoadStim_label.setText("")
        self.DataAnalysis_LoadStim_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Load Stimulus   ", None))
        self.DataAnalysis_StepStim_LoadData_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Raw Data", None))
        self.DataAnalysis_StepStim_SaveImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.Imaging_pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect Imaging screen to Spikeling screen", None))
        self.Imaging_Fluorescence_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Fluorescence", None))
#if QT_CONFIG(whatsthis)
        self.Imaging_Calcium_Checkbox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Imaging_Calcium_Checkbox.setText(QCoreApplication.translate("MainWindow", u"[Ca\u00b2\u207a]", None))
        self.Imaging_Vm_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm", None))
        self.Imaging_Stimulus_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.Imaging_DataRecording_box.setTitle(QCoreApplication.translate("MainWindow", u"Data Recording", None))
        self.Imaging_DataRecording_SelectRecordFolder_label_.setText(QCoreApplication.translate("MainWindow", u"Data Logging: Filename", None))
        self.Imaging_DataRecording_RecordFolder_value.setText("")
        self.Imaging_DataRecording_RecordFolderDir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse directory", None))
        self.Imaging_SelectedFolderLabel.setText("")
        self.Imaging_DataRecording_Record_pushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.Imaging_parameter_exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Hide Parameters", None))
        self.Imaging_GECI_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium Indicator:", None))
        self.Imaging_GECI_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a GECI", None))
        self.Imaging_GECI_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GCaMP2", None))
        self.Imaging_GECI_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GCaMP6", None))
        self.Imaging_GECI_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"jRGECO", None))

        self.Imaging_GECI_ReadingsAffinity_Label.setText(QCoreApplication.translate("MainWindow", u"Affinity n:", None))
        self.Imaging_GECI_ReadingsAffinity_Value.setText("")
        self.Imaging_GECI_ReadingsKd_Label.setText(QCoreApplication.translate("MainWindow", u"Dissociation constant kd:", None))
        self.Imaging_GECI_ReadingsKd_Value.setText("")
        self.Imaging_GECI_ReadingsBrightness_Label.setText(QCoreApplication.translate("MainWindow", u"Brightness A:", None))
        self.Imaging_GECI_ReadingsBrightness_Value.setText("")
        self.Imaging_FrameRate_Label.setText(QCoreApplication.translate("MainWindow", u"Imaging frame rate (Hz)", None))
        self.Imaging_FrameRate_Readings.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Imaging_PMT_Label.setText(QCoreApplication.translate("MainWindow", u"Photo-detection gain (%)", None))
        self.Imaging_PMT_Readings.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.Imaging_Laser_Label.setText(QCoreApplication.translate("MainWindow", u"Laser power (%)", None))
        self.Imaging_Laser_Readings.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.Imaging_CalciumDecay_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium decay: \u03bb (ms\u05bf \u00b9) ", None))
        self.Imaging_CalciumDecay_Readings.setText("")
#if QT_CONFIG(whatsthis)
        self.label_55.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-3</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>2*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.Imaging_CalciumJump_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium jump per spike (\u03bcM)", None))
        self.Imaging_CalciumJump_Readings.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Imaging_CalciumNoise_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium noise scale", None))
        self.Imaging_CalciumNoise_Readings.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Imaging_CalciumBaseline_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium Baseline (\u03bcM)", None))
        self.Imaging_CalciumBaseline_Readings.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.Imaging_FluoScale_Label.setText(QCoreApplication.translate("MainWindow", u"Fluorescence scale", None))
        self.Imaging_FluoScale_Readings.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Imaging_FluoOffset_Label.setText(QCoreApplication.translate("MainWindow", u"Fluorescence offset", None))
        self.Imaging_FluoOffset_Readings.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.Imaging_FluoNoise_Label.setText(QCoreApplication.translate("MainWindow", u"Noise scale", None))
        self.Imaging_FluoNoise_Readings.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Imaging_FluoSat_Label.setText(QCoreApplication.translate("MainWindow", u"Non-linear Saturation", None))
        self.Imaging_kd_Label.setText(QCoreApplication.translate("MainWindow", u"Dissociation constant (\u03bcM)", None))
        self.Imaging_kd_Readings.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Imaging_Hill_Label.setText(QCoreApplication.translate("MainWindow", u"Affinity", None))
        self.Imaging_Hill_Readings.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"0.75", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
#if QT_CONFIG(whatsthis)
        self.Imaging_PhotoShotNoise_Label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Photon shot noise (A.photon<span style=\" vertical-align:super;\">-1</span>)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Imaging_PhotoShotNoise_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Photon shot noise (A.photon<span style=\" vertical-align:super;\">-1</span>)</p></body></html>", None))
        self.Imaging_PhotoShotNoise_Readings.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-6</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_37.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>5*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>5*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"10\u00af\u00b3", None))
        self.Imaging_rightMenuSubContainer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Parameters", None))
        self.Imaging_ImagingParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging Parameters", None))
        self.Imaging_CalciumParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcium Parameters", None))
        self.Imaging_FluoParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Fluorescence Parameters", None))
        self.MultipleImaging_pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect Multiple Imaging screen to Spikeling screen", None))
        self.MultipleImaging_Fluorescence1_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Fluorescence Spikeling", None))
        self.MultipleImaging_Fluorescence2_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Fluorescence Synapse1", None))
        self.MultipleImaging_Fluorescence3_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Fluorescence Synapse2", None))
#if QT_CONFIG(whatsthis)
        self.MultipleImaging_Calcium1_Checkbox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.MultipleImaging_Calcium1_Checkbox.setText(QCoreApplication.translate("MainWindow", u"[Ca\u00b2\u207a] Spikeling", None))
        self.MultipleImaging_Calcium2_Checkbox.setText(QCoreApplication.translate("MainWindow", u"[Ca\u00b2\u207a] Synapse1", None))
        self.MultipleImaging_Calcium3_Checkbox.setText(QCoreApplication.translate("MainWindow", u"[Ca\u00b2\u207a] Synapse2", None))
        self.MultipleImaging_Vm1_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm Spikeling", None))
        self.MultipleImaging_Vm3_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm Synapse1", None))
        self.MultipleImaging_Vm2_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Vm Synapse2", None))
        self.MultipleImaging_Stimulus_Checkbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.MultipleImaging_DataRecording_box.setTitle(QCoreApplication.translate("MainWindow", u"Data Recording", None))
        self.MultipleImaging_DataRecording_SelectRecordFolder_label.setText(QCoreApplication.translate("MainWindow", u"Data Logging: Filename", None))
        self.MultipleImaging_DataRecording_RecordFolder_value.setText("")
        self.MultipleImaging_DataRecording_RecordFolderDir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse directory", None))
        self.MultipleImaging_SelectedFolderLabel.setText("")
        self.MultipleImaging_DataRecording_Record_pushButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.MultipleImaging_parameter_exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Hide Parameters", None))
        self.MultipleImaging_GECI_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium Indicator:", None))
        self.MultipleImaging_GECI_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a GECI", None))
        self.MultipleImaging_GECI_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GCaMP2", None))
        self.MultipleImaging_GECI_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GCaMP6", None))
        self.MultipleImaging_GECI_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"jRGECO", None))

        self.MultipleImaging_GECI_ReadingsAffinity_Label.setText(QCoreApplication.translate("MainWindow", u"Affinity n:", None))
        self.MultipleImaging_GECI_ReadingsAffinity_Value.setText("")
        self.MultipleImaging_GECI_ReadingsKd_Label.setText(QCoreApplication.translate("MainWindow", u"Dissociation constant kd:", None))
        self.MultipleImaging_GECI_ReadingsKd_Value.setText("")
        self.MultipleImaging_GECI_ReadingsBrightness_Label.setText(QCoreApplication.translate("MainWindow", u"Brightness A:", None))
        self.MultipleImaging_GECI_ReadingsBrightness_Value.setText("")
        self.MultipleImaging_FrameRate_Label.setText(QCoreApplication.translate("MainWindow", u"Imaging frame rate (Hz)", None))
        self.MultipleImaging_FrameRate_Readings.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.MultipleImaging_PMT_Label.setText(QCoreApplication.translate("MainWindow", u"Photo-detection gain (%)", None))
        self.MultipleImaging_PMT_Readings.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.MultipleImaging_Laser_Label.setText(QCoreApplication.translate("MainWindow", u"Laser power (%)", None))
        self.MultipleImaging_Laser_Readings.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.MultipleImaging_CalciumDecay_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium decay: \u03bb (ms\u05bf \u00b9) ", None))
        self.MultipleImaging_CalciumDecay_Readings.setText("")
#if QT_CONFIG(whatsthis)
        self.label_67.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-3</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>2*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.MultipleImaging_CalciumJump_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium jump per spike (\u03bcM)", None))
        self.MultipleImaging_CalciumJump_Readings.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.MultipleImaging_CalciumNoise_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium noise scale", None))
        self.MultipleImaging_CalciumNoise_Readings.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.MultipleImaging_CalciumBaseline_Label.setText(QCoreApplication.translate("MainWindow", u"Calcium Baseline (\u03bcM)", None))
        self.MultipleImaging_CalciumBaseline_Readings.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.MultipleImaging_FluoScale_Label.setText(QCoreApplication.translate("MainWindow", u"Fluorescence scale", None))
        self.MultipleImaging_FluoScale_Readings.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Imaging_FluoOffset_Label_2.setText(QCoreApplication.translate("MainWindow", u"Fluorescence offset", None))
        self.MultipleImaging_FluoOffset_Readings.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.MultipleImaging_FluoNoise_Label.setText(QCoreApplication.translate("MainWindow", u"Noise scale", None))
        self.MultipleImaging_FluoNoise_Readings.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.MultipleImaging_FluoSat_Label.setText(QCoreApplication.translate("MainWindow", u"Non-linear Saturation", None))
        self.MultipleImaging_kd_Label.setText(QCoreApplication.translate("MainWindow", u"Dissociation constant (\u03bcM)", None))
        self.MultipleImaging_kd_Readings.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.MultipleImaging_Hill_Label.setText(QCoreApplication.translate("MainWindow", u"Affinity", None))
        self.MultipleImaging_Hill_Readings.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"0.75", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
#if QT_CONFIG(whatsthis)
        self.MultipleImaging_PhotoShotNoise_Label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Photon shot noise (A.photon<span style=\" vertical-align:super;\">-1</span>)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.MultipleImaging_PhotoShotNoise_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Photon shot noise (A.photon<span style=\" vertical-align:super;\">-1</span>)</p></body></html>", None))
        self.MultipleImaging_PhotoShotNoise_Readings.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>10<span style=\" vertical-align:super;\">-6</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_95.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>5*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>5*10<span style=\" vertical-align:super;\">-4</span></p></body></html>", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"10\u00af\u00b3", None))
        self.MultipleImaging_rightMenuSubContainer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Parameters", None))
        self.MultipleImaging_ImagingParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imaging Parameters", None))
        self.MultipleImaging_CalciumParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcium Parameters", None))
        self.MultipleImaging_FluoParameter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Fluorescence Parameters", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.NeuronGenerator_subframe1_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Spikeling is built on the Izhikevich model</span></p></body></html>", None))
        self.NeuronGenerator_subframe1_Izhik_textbrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">Bifurcation methodologies enable us to reduce many biophysically accurate Hodgkin\u2013Huxley-type neuronal models to a two-dimensional (2-D) system of ordinary differential equations of the form:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">v' = 0.04v</span><span style=\" font-family:'Segoe UI'; fo"
                        "nt-size:11pt; font-weight:696; vertical-align:super;\">2</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\"> + 5v + 140 - u + I                    </span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&amp;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">                    u' = a(bv - u)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">with the auxiliary after-spike resetting:   if </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">v &gt;= 30 mV</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">, then </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">v = c</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> and</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> </span><span style=\""
                        " font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">u = u + d</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt; font-weight:696;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">Here, </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">v</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> and </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">u</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> are dimensionless variables, and </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">a</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">, </span><span style="
                        "\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">b</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">, </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">c</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">, and </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">d</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> are dimensionless parameters, and </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">'= d/dt</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">, where </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">t</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> is the time. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">The variable v represents the"
                        " membrane potential of the neuron and </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">u</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> represents a membrane recovery variable, which accounts for the activation of K+ ionic currents and inactivation of Na+ ionic currents, and it provides negative feedback to </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">v</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">After the spike reaches its apex (+30 mV), the membrane voltage and the recovery variable are reset. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-siz"
                        "e:10pt;\">Synaptic currents or injected DC-currents are delivered via the variable</span><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:696;\"> </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:696;\">I</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">.</span></p></body></html>", None))
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
        self.StimulusGenerator_Selection_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Triangular wave", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Chirp", None))
        self.StimulusGenerator_Selection_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Binary noise", None))

        self.StimulusGenerator_Oscilloscope_widget_Stim_checkbox.setText(QCoreApplication.translate("MainWindow", u"Stimulus", None))
        self.StimulusGenerator_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Stimulus", None))
        self.StimulusGenerator_Save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Stimulus", None))
        self.Step_Number_Label.setText(QCoreApplication.translate("MainWindow", u"Number of steps", None))
        self.Step_Number_Value.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Step_Increment_Label.setText(QCoreApplication.translate("MainWindow", u"Intensity increment (a.u.)", None))
        self.Step_Increment_Value.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Step_First_Label.setText(QCoreApplication.translate("MainWindow", u"First step intensity (a.u.)", None))
        self.Step_First_Value.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Step_On_Label.setText(QCoreApplication.translate("MainWindow", u"Step lenght (ms)", None))
        self.Step_On_Value.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.Step_Off_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Step length (ms)", None))
        self.Step_Off_Value.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.Step_OffInt_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Step intensity (a.u.)", None))
        self.Step_OffInt_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Step_Inter_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus length (ms)", None))
        self.Step_Inter_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Step_InterInt_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus intensity (a.u.)", None))
        self.Step_InterInt_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SineWave_Amplitude_Label.setText(QCoreApplication.translate("MainWindow", u"Amplitude (a.u.)", None))
        self.SineWave_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.SineWave_Frequency_Label.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.SineWave_Frequency_Value.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.SineWave_Mean_Label.setText(QCoreApplication.translate("MainWindow", u"Mean (a.u.)", None))
        self.SineWave_Mean_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SineWave_StimOn_Label.setText(QCoreApplication.translate("MainWindow", u"Stimulus Time (ms)", None))
        self.SineWave_StimOn_Value.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.SineWave_IntOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus Intensity (a.u.)", None))
        self.SineWave_IntOff_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SineWave_StimOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-Stimulus Time (ms)", None))
        self.SineWave_StimOff_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.TriangleWave_Amplitude_Label.setText(QCoreApplication.translate("MainWindow", u"Amplitude (a.u.)", None))
        self.TriangleWave_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.TriangleWave_Frequency_Label.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.TriangleWave_Frequency_Value.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.TriangleWave_Mean_Label.setText(QCoreApplication.translate("MainWindow", u"Mean (a.u.)", None))
        self.TriangleWave_Mean_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.TriangleWave_StimOn_Label.setText(QCoreApplication.translate("MainWindow", u"Stimulus Time (ms)", None))
        self.TriangleWave_StimOn_Value.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.TriangleWave_IntOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-stimulus intensity (a.u.)", None))
        self.TriangleWave_IntOff_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.TriangleWave_StimOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-stimulus time (ms)", None))
        self.TriangleWave_StimOff_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Chirp_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear Frequency Chirp", None))
        self.Chirp_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Exponential Frequency Chirp", None))
        self.Chirp_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Linear Amplitude Chirp", None))

        self.Chirp_Amplitude_Label.setText(QCoreApplication.translate("MainWindow", u"Chirp Amplitude (a.u.)", None))
        self.Chirp_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Chirp_Frequency_Label.setText(QCoreApplication.translate("MainWindow", u"Chirp Frequency (Hz)", None))
        self.Chirp_Frequency_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Chirp_StartFrequency_Label.setText(QCoreApplication.translate("MainWindow", u"Chirp Start Frequency (Hz)", None))
        self.Chirp_StartFrequency_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Chirp_EndFrequency_Label.setText(QCoreApplication.translate("MainWindow", u"Chirp End Frequency (Hz)", None))
        self.Chirp_EndFrequency_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Chirp_Duration_Label.setText(QCoreApplication.translate("MainWindow", u"Chirp Duration (ms)", None))
        self.Chirp_Duration_Value.setText(QCoreApplication.translate("MainWindow", u"1000", None))
#if QT_CONFIG(whatsthis)
        self.Chirp_PreChirpOn_Duration_Label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre-Chirp On </p><p><span style=\" font-size:10pt;\">Amp. (a.u.) / Dur. (ms)</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Chirp_PreChirpOn_Duration_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre-Chirp On<br> <span style=\" font-size:10pt;\">Amp. (a.u.) / Dur. (ms)</span></p></body></html>", None))
        self.Chirp_PreChirpOn_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Chirp_PreChirpOn_Duration_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Chirp_PreChirpOff_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre-Chirp Off <br><span style=\" font-size:10pt;\">Amp. (a.u.) / Dur. (ms)</span></p></body></html>", None))
        self.Chirp_PreChirpOff_Amplitude_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Chirp_PreChirpOff_Duration_Value.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Chirp_PreChirpMid_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre-Chirp Mid <br><span style=\" font-size:10pt;\">Amp. (a.u.) / Dur. (ms)</span></p></body></html>", None))
        self.Chirp_PreChirpMid_Amplitude.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Chirp_PreChirpMid_Duration.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Chirp_IntOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-stimulus intensity (a.u.)", None))
        self.Chirp_IntOff_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Chirp_StimOff_Label.setText(QCoreApplication.translate("MainWindow", u"Inter-stimulus time (ms)", None))
        self.Chirp_StimOff_Value.setText(QCoreApplication.translate("MainWindow", u"100", None))
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
        self.Exercise101_PreviousButton_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.Exercise101_AfterButton_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.mainbody_footer_text_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Understanding how neurons encode and compute information is fundamental to our study of the brain, but opportunities for hands-on experience with neurophysiological techniques on live neurons are scarce in science education.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">Originally developped in the Baden Lab at the University of Sussex, Spikeling is an </span><span style=\" font-size:8pt; font-style:italic;\">in-silico</span><span style=\" font-size:8pt;\"> neuron that mimics a wide range of neuronal behaviours for classroom education and public neuroscience outreach. The current version is the result of a collective work from on-field teaching experience, both in the UK and on the African continent and from users and students feedback.</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">The GUI presented here proposed a full and didactic interaction with the neuronal model. It also contains various exercices wh"
                        "ich can be linked to classical neuroscience teachings from early to advanced degree students. Futhermore it offers the opportunity to teachers to prepare practical on: programming, data analysis scipting, methodology and protocol design. All very important skills for modern neuroscience academics but which is unfortunately widely lacking from neuroscience degrees education.</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_23.setText("")
        self.license_label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.sussex_logo.setText("")
        self.trend_logo.setText("")
        self.OSN_logo.setText("")
        self.label.setText("")
    # retranslateUi

