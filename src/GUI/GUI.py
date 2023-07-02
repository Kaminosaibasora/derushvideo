import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QMessageBox, QAction, QFileDialog, QPushButton, QLabel
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QIcon
from list_file_widget import List_file_widget
from video_player_widget import Video_player_widget

class GUI(QMainWindow):
    def __init__(self, cutvideo, parent=None):
        super(GUI, self).__init__(parent)
        self.setWindowTitle("Cut Video CLIP")
        self.cutVideo = cutvideo
        # List File
        self.listFiles = List_file_widget(self.cutVideo)
        self.listFiles.listwidget.clicked.connect(self.clickchoosepath)

        # Video Reader
        self.videoReader = Video_player_widget(self.cutVideo)
        # self.videoReader = QLabel()
        # self.videoReader.setText("VIDEO \n \n \n \n \n \n READER")
        
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
        layout.addWidget(self.listFiles,     0, 0)
        layout.addWidget(self.videoReader,   0, 1, 1, 3)
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
        self.inLabel.setText(str(self.cutVideo.timein))

    def setOut(self):
        print("OUT")
        self.cutVideo.setTimeOut(0)
        self.outLabel.setText(str(self.cutVideo.timeout))

    def generateCut(self):
        print("Generate")
    
    def clickchoosepath(self, line):
        self.listFiles.labelchoose.setText(line.data())
        self.listFiles.linecurrent = line
        self.cutVideo.loadVideo(line.data())
        # self.video.loadMedia(self.rengine.get_current_path())
        # self.video.play()
        print(line.data())