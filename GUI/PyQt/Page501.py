import numpy as np
import pyqtgraph
import Settings


def ShowPage(self):
    self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_501)
    self.ui.Exercise101_PreviousButton_pushButton.setEnabled(False)
    self.ui.Exercise101_PreviousButton_pushButton.setStyleSheet("background-color: rgb(80, 96, 100);" 
                                                                "border: 2px solid rgb(80, 96, 100);" 
                                                                "border-radius: 10px;" 
                                                                "padding: 2px;"
                                                                )
    self.ui.Exercise101_AfterButton_pushButton.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                             "border: 2px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                             "border-radius: 10px" + ";\n"
                                                             "padding: 2px;"
                                                             )
    self.ui.Exercise101_stackedWidget.setCurrentIndex(0)

def Previous(self):
    self.Exercice101_CurrentIndex = self.ui.Exercise101_stackedWidget.currentIndex()
    self.ui.Exercise101_stackedWidget.setCurrentIndex(self.Exercice101_CurrentIndex - 1)
    self.Exercice101_CurrentIndex = self.ui.Exercise101_stackedWidget.currentIndex()
    if self.Exercice101_CurrentIndex < 3:
        self.ui.Exercise101_AfterButton_pushButton.setEnabled(True)
        self.ui.Exercise101_AfterButton_pushButton.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                                 "border: 2px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                                 "border-radius: 10px" + ";\n"
                                                                 "padding: 2px;"
                                                                 )
    if self.Exercice101_CurrentIndex == 0:
        self.ui.Exercise101_PreviousButton_pushButton.setEnabled(False)
        self.ui.Exercise101_PreviousButton_pushButton.setStyleSheet("background-color: rgb(80, 96, 100)" + ";\n"
                                                                    "border: 2px solid rgb(80, 96, 100)" + ";\n"
                                                                    "border-radius: 10px" + ";\n"
                                                                    "padding: 2px;"
                                                                    )

def After(self):
    self.Exercice101_CurrentIndex = self.ui.Exercise101_stackedWidget.currentIndex()
    self.ui.Exercise101_stackedWidget.setCurrentIndex(self.Exercice101_CurrentIndex + 1)
    self.Exercice101_CurrentIndex = self.ui.Exercise101_stackedWidget.currentIndex()
    if self.Exercice101_CurrentIndex > 0:
        self.ui.Exercise101_PreviousButton_pushButton.setEnabled(True)
        self.ui.Exercise101_PreviousButton_pushButton.setStyleSheet("background-color: rgb" + str(tuple(Settings.DarkSolarized[2])) + ";\n"
                                                                    "border: 2px solid rgb" + str(tuple(Settings.DarkSolarized[14])) + ";\n"
                                                                    "border-radius: 10px" + ";\n"
                                                                    "padding: 2px;"
                                                                    )
    if self.Exercice101_CurrentIndex == 3:
        self.ui.Exercise101_AfterButton_pushButton.setEnabled(False)
        self.ui.Exercise101_AfterButton_pushButton.setStyleSheet("background-color: rgb(80, 96, 100)" + ";\n"
                                                                "border: 2px solid rgb(80, 96, 100)" + ";\n"
                                                                "border-radius: 10px" + ";\n"
                                                                "padding: 2px;"
                                                                )



