import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.clicked.connect(self.the_third)
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked!")
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
    def the_third(self, *args):
        print("3", *args)
app = QApplication(sys.argv)
window = MainWindow()
window.show() #Отобразить виджет
app.exec()