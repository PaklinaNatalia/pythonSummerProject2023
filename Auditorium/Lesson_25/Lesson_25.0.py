import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        self.setFixedSize(QSize(300, 300))
        #Установить центральный виджет Window
        self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.show() #Отобразить виджет
app.exec()