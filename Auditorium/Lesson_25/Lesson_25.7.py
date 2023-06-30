import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Hello, World!")
        self.button = QPushButton("Hello, World!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)
        self.tf = True
    def button_clicked(self):
        print("Clicked!")
        if self.tf:
            self.setWindowTitle("Привет, Мир!")
            self.button.setText("Привет, Мир!")
            self.tf = False
        else:
            self.tf = True
            self.setWindowTitle("Hello, World!")
            self.button.setText("Hello, World!")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()