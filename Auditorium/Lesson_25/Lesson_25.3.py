import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.button_clicked)
        #Установить центральный виджет Window
        self.setCentralWidget(self.button)
    def button_clicked(self):
        self.button.setText("You've already clicked me")
        self.button.setEnabled(False)
        #Изменить заголовок окна
        self.setWindowTitle("Oneshot Button App")
app = QApplication(sys.argv)
window = MainWindow()
window.show() #Отобразить виджет
app.exec()