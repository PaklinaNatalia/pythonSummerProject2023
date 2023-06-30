import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Нажми меня")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        #Установить центральный виджет Window
        self.setCentralWidget(self.button)
        self.count = 0
    def the_button_was_clicked(self):
        self.count += 1
        print(f"Нажато {str(self.count)} раз")
        self.button.setText("Нажато " + str(self.count) + " раз")
app = QApplication(sys.argv)
window = MainWindow()
window.show() #Отобразить виджет
app.exec()