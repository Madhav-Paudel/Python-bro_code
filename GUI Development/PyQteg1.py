# Introduction of PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # her geometry determine the opening of window in screen x=700,y=300,width=500,height=500
        self.setGeometry(700,300,500,500)
        # this code main to  give fabicon of app in screen 
        self.setWindowIcon(QIcon("904443.png"))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
