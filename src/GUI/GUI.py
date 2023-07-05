import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QMessageBox, QAction, QFileDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QIcon
from list_file_widget import List_file_widget
from video_player_widget import Video_player_widget
sys.path.append('./engine')
import filegestion as fg

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
        
        # Clip Gestion
        self.inButton   = QPushButton("In")
        self.inButton   .clicked.connect(self.setIn)
        self.inLabel    = QLineEdit()
        self.inLabel    .setText("0.000")
        self.inLabel    .textEdited.connect(self.setInManual)
        self.outButton  = QPushButton("Out")
        self.outButton  .clicked.connect(self.setOut)
        self.outLabel   = QLineEdit()
        self.outLabel   .setText("0.000")
        self.outLabel   .textEdited.connect(self.setOutManual)
        self.generate   = QPushButton("Generate")
        self.generate   .clicked.connect(self.generateCut)

        # LAYOUT
        layout = QGridLayout()
        layout.addWidget(self.listFiles,     0, 0, 2, 1)
        layout.addWidget(self.videoReader,   0, 1, 1, 4, alignment=Qt.AlignHCenter)
        layout.addWidget(self.inButton,      1, 1)
        layout.addWidget(self.inLabel,       1, 2)
        layout.addWidget(self.outButton,     1, 3)
        layout.addWidget(self.outLabel,      1, 4)
        layout.addWidget(self.generate,      1, 5)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)
        self.resize(1200, 720)

    def setIn(self):
        print("IN")
        self.cutVideo.setTimeIn(self.videoReader.mediaPlayer.position()/1000)
        self.inLabel.setText(str(self.cutVideo.timein))
    
    def setInManual(self):
        print("IN manual")
        self.cutVideo.setTimeIn(float(self.inLabel.text()))

    def setOut(self):
        print("OUT")
        self.cutVideo.setTimeOut(self.videoReader.mediaPlayer.position()/1000)
        self.outLabel.setText(str(self.cutVideo.timeout))
    
    def setOutManual(self):
        print("OUT manual")
        self.cutVideo.setTimeOut(float(self.outLabel.text()))

    def generateCut(self):
        print("Generate")
        name_clip = fg.generateNewName(self.cutVideo.folderout, self.cutVideo.videopath)
        print(name_clip)
        self.cutVideo.cutVideoClip(name_clip)

    
    def clickchoosepath(self, line):
        self.listFiles.labelchoose.setText(line.data())
        self.listFiles.linecurrent = line
        self.cutVideo.loadVideo(line.data())
        # Charger la vidéo dans le lecteur
        self.videoReader.loadMedia(self.cutVideo.getFullPathVideo())
        self.videoReader.play_pause()