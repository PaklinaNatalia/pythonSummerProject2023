from PyQt6.QtWidgets import QApplication, QWidget
#import sys
#app = QApplication(sys.argv)
app = QApplication([])
window = QWidget() #Создать виджет
window.show() #Отобразить виджет
app.exec()

from PyQt6.QtWidgets import QApplication, QPushButton
import sys
app = QApplication(sys.argv)
window = QPushButton("НАЖМИ МЕНЯ!")
window.show() #Отобразить виджет
app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.show() #Отобразить виджет
app.exec()

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
app = QApplication(sys.argv)
window = MainWindow()
window.show() #Отобразить виджет
app.exec()