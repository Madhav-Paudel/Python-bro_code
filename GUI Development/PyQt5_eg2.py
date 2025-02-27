import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note by PG")
        self.setGeometry(700, 300, 500, 500)

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a label
        label = QLabel("Madhav", self)
        label.setFont(QFont("Arial", 15))
        label.setStyleSheet("color: blue;"
                            "background-color: green;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            "padding: 10px;"  # Added padding for better visibility
                            "border-radius: 5px;")  # Rounded corners
        # label.setAlignment(Qt.AlignTop) #       this align the text to the vertically  top 
        # label.setAlignment(Qt.AlignBottom) #       this align the text to the vertically  Bottom 
        # label.setAlignment(Qt.AlignVCenter) #       this align the text to the vertically  center 

        # label.setAlignment(Qt.AlignRight)  #       this align the text to the horizontally right  
        # label.setAlignment(Qt.AlignHCenter)  #       this align the text to the horizontally center  
        # label.setAlignment(Qt.AlignLeft)  #       this align the text to the horizontally left 
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # Center horizontally and align to bottom

        # layout.addWidget(label, alignment=Qt.AlignHCenter | Qt.AlignBottom)
        # layout.addWidget(label, alignment=Qt.AlignHCenter | Qt.AlignVCenter) #center and center 
        layout.addWidget(label, alignment=Qt.AlignCenter)
 


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
