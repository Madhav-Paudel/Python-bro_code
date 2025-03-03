# Weather App By using Python 
import sys
from urllib import request, response
from urllib.error import HTTPError 
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
        # error handling 
        response = None
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:
            if 'response' in locals():
                if response is not None:
                    match response.status_code:
                        case 400:
                            self.display_error("Bad Request!:\n Please Check Your input")
                        case 401:
                            self.display_error("Unauthorized:\n Invalid API key")
                        case 403:
                            self.display_error("Forbidden:\nAccess is Denied")
                        case 404:
                            self.display_error("Not Found:\nCity Not found")

                        case 500:
                            self.display_error("Internal Server Error!:\n Please Try Again Later")
                        case 502:
                           self.display_error("Bad Gateway:\n Invalid response from server")
                        case 503:
                            self.display_error("Service Unavailable:\n Server is Down") 
                        case 504:
                            self.display_error("Gateway Timeout:\n No response from the server") 
                        case _:
                           self.display_error(f"HTTP error occurred:\n {http_error}")
                
                
                

        except requests.exceptions.ConnectionError:
           self.display_error("Connection Error:\n Check Your Internet Connection") 
        except requests.exceptions.Timeout:
            self.display_error("Time Error:\n Request Time out") 
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\n Check Your URL")
        except requests.exceptions.RequestException as rec_error:
            self.display_error(f"Request Error:\n{rec_error}")
    
# if above error will happen then we will show 
    def display_error(self,message):
        # setting the size of the text
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message) 
        self.emoji_label.clear()
        self.description_label.clear()
        


    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;")

        # temperature in kelvin 
        temperature_k=data["main"]["temp"]
        #temperature in celsius 
        temperature_c=temperature_k-273.15
        # temperature in Fahrenheit 
        temperature_f=(temperature_k*9/5)-459.67
        self.temperature_label.setText(f"{temperature_c:.0f}°c")
        weather_id=data["weather"][0]["id"]
        weather_description=data["weather"][0]["description"]
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return"⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🎐"
        elif weather_id == 762:
            return "🌋"
        elif weather_id== 771:
            return "💨"
        elif weather_id== 781:
            return "🌪️"
        elif weather_id== 800:
            return "☀️"
        elif 801 <= weather_id <=804:
            return "☁️"
        else :
            return " "
        






        

    
if __name__=="__main__":
    app=QApplication(sys.argv)
    # constructing weather app object and calling WeatherApp class 
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
