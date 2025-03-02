# Weather App By using Python 
import sys
from urllib import request, response 
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
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel( self)
        self.description_label = QLabel( self)
        self.initUI()

# creating function for the graphical user interface 

    def initUI(self):
        # here setting the name of window 
        self.setWindowTitle("Weather App")
        # using QVBoxLayout for vertical management 
        vbox=QVBoxLayout()


        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # aligning the following item to the center of the window 

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # using css in particular place 
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        # applying from here based on class id 
        # here the first is the class and after # sign we give class_id 

        self.setStyleSheet("""
        QLabel, QPushButton {
            font-family: Arial;
        }
        QLabel#city_label {
            font-size: 40px;
            font-style:italic;
        }
        QLineEdit#city_input
        {
        font-size: 40px;

        }
        QPushButton#get_weather_button{
        font-size: 35px;
        font-weight:bold;
        }
        QLabel#temperature_label
        {
        font-size:75px;
        }
        QLabel#emoji_label
        {
        font-size:100px;
        font-family:segoe UI emoji;

        }
        QLabel#description_label
        {
        font-size:50px;
        }


        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # creating local variable 
        api_key="9d1543939a56a617c3c918a163fe2a44"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response=requests.get(url)
        data=response.json()
        print(data)

        if data["cod"]==200:
            self.display_weather(data)


    def display_error(self,message):
        pass 

    def display_weather(self,data):
        pass 



        

    
if __name__=="__main__":
    app=QApplication(sys.argv)
    # constructing weather app object and calling WeatherApp class 
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
