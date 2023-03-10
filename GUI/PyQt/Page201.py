import Settings


class Imaging201():

    def ShowPage(self):
        self.ui.mainbody_stackedWidget.setCurrentWidget(self.ui.page_201)
        self.ui.Imaging_Oscilloscope_widget.setBackground(Settings.DarkSolarized[0])

