import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        layout = QGridLayout()
        b_1 = QPushButton("1")
        b_2 = QPushButton("2")
        b_3 = QPushButton("3")
        b_4 = QPushButton("4")
        b_5 = QPushButton("5")
        b_6 = QPushButton("6")
        b_7 = QPushButton("7")
        b_8 = QPushButton("8")
        b_9 = QPushButton("9")

        layout.addWidget(b_1, 0, 0)
        layout.addWidget(b_2, 0, 1)
        layout.addWidget(b_3, 0, 2)
        layout.addWidget(b_4, 1, 0)
        layout.addWidget(b_5, 1, 1)
        layout.addWidget(b_6, 1, 2)
        layout.addWidget(b_7, 2, 0)
        layout.addWidget(b_8, 2, 1)
        layout.addWidget(b_9, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()