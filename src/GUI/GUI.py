import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QMessageBox, QAction, QFileDialog, QPushButton, QLabel
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QIcon

class GUI(QMainWindow):
    def __init__(self, cutvideo, parent=None):
        super(GUI, self).__init__(parent)
        self.setWindowTitle("Cut Video CLIP")
        self.cutVideo = cutvideo
        # Video Reader
        self.videoReader = QLabel()
        self.videoReader.setText("VIDEO \n \n \n \n \n \n READER")
        # Clip Gestion
        self.inButton = QPushButton("In")
        self.inButton.clicked.connect(self.setIn)
        self.inLabel = QLabel()
        self.inLabel.setText("00:00")
        self.outButton = QPushButton("Out")
        self.outButton.clicked.connect(self.setOut)
        self.outLabel = QLabel()
        self.outLabel.setText("00:00")
        self.generate = QPushButton("Generate")
        self.generate.clicked.connect(self.generateCut)

        # LAYOUT
        layout = QGridLayout()
        layout.addWidget(self.videoReader,   0, 0)
        layout.addWidget(self.inButton,      1, 0)
        layout.addWidget(self.inLabel,       1, 1)
        layout.addWidget(self.outButton,     1, 2)
        layout.addWidget(self.outLabel,      1, 3)
        layout.addWidget(self.generate,      1, 4)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)
        self.resize(1200, 720)

    def setIn(self):
        print("IN")
        self.cutVideo.setTimeIn(0)
        self.inLabel.setText(str(0.0))

    def setOut(self):
        print("OUT")
        self.cutVideo.setTimeOut(0)
        self.outLabel.setText(str(0.0))

    def generateCut(self):
        print("Generate")