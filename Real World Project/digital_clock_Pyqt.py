# Digital clock using python 
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout 
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase  
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)

        self.initUI()
        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)

    # here we design the layout of the clock 
    def initUI(self):
        self.setWindowTitle("Digital Clock") 
        self.setGeometry(600,400,300,100)
        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)
        # Set background color to black
        self.setStyleSheet("background-color: black;")

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        # aligning the text of clock in the center 
        self.time_label.setAlignment(Qt.AlignCenter)
        # decorating the text 
        self.time_label.setStyleSheet("font-size:150px;"
                                      "color:#26ff00;")
        
        current_time = QTime.currentTime().toString("hh:mm:ss")
        
        self.time_label.setText(current_time)
        font_id=QFontDatabase.addApplicationFont("C:/Users/Acer/OneDrive/Desktop/broCode/Real World Project/DS-DIGIT.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,150)
        self.time_label.setFont(my_font)
    # updating time 
    def Update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    # creating clock object and calling constructor 
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())
