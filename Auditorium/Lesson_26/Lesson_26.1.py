import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit
from PyQt6.QtGui import QIcon, QAction

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        b1Action = QAction(QIcon("D:\Settings\Icons\Magic Forces\Air.ico"), "Air", self)
        b1Action.setStatusTip("Air")
        b1Action.triggered.connect(self.close)

        exitAction = QAction(QIcon("D:\Settings\Icons\Magic Forces\Death.ico"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit")
        exitAction.triggered.connect(self.close)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)
        helpMenu = menubar.addMenu("&Help")

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(b1Action)
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("My App")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())