from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen

from py_animated_menu import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QApplication([])

w = MainWindow()
w.show()

app.exec()