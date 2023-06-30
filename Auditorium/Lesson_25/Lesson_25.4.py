import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
window_titles = ["Still My App", "What's on Earth", "This is surprise!", "Something went wrong!"]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("MyApp")
        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.title_changed)
        self.setCentralWidget(self.button)
    def button_clicked(self):
        print("Clicked")
        new_win_title = choice(window_titles)
        print(f"Setting title: {new_win_title}")
        self.setWindowTitle(new_win_title)
    def title_changed(self, window_title):
        print(f"Window title changed: {window_title}")
        self.button.setDisabled(True)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()