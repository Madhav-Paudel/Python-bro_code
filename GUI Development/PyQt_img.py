# PyQt5 image 
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)


        pixmap=QPixmap("904443.png")
        label.setPixmap(pixmap)






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






if __name__ == '__main__':
    main()
