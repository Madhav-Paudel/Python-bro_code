# Weather App By using Python 
import sys 
# for requesting data from api 
import requests

from PyQt5.QtWidgets import (QApplication, QWidget,QLineEdit,
                              QLabel, QVBoxLayout, QPushButton,
                                QHBoxLayout)

from PyQt5.QtCore import QTimer, Qt, QTime

# creating a class weather app and it will inherited from its parent QWidget 
class WeatherApp(QWidget):
    # creating default constructor
    def __init__(self):
        super().__init__() 
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    # constructing weather app object and calling WeatherApp class 
    weather_app=WeatherApp()
    weather_app.show()
    