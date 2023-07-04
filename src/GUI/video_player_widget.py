from PyQt5.QtCore import QDir, Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtWidgets import QWidget, QPushButton
import sys
import time

class Video_player_widget(QWidget):
    def __init__(self, cutVideo):
        QWidget.__init__(self)
        self.cutVideo = cutVideo
        self.targetPosition = 0
        self.activationSearchPosition = ""
        # lecteur vidéo
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setNotifyInterval(1)
        self.mediaPlayer.positionChanged.connect(self.updatePlayerImage)
        # widget video
        self.videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        # Bouton Play
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play_pause)
        # Bouton Little Past
        self.littlePastButton = QPushButton("<")
        self.littlePastButton.clicked.connect(self.littlePastJump)
        # Bouton Grand Past
        self.grandPastButton = QPushButton("<<")
        self.grandPastButton.clicked.connect(self.grandPastJump)
        # Bouton Little Futur
        self.littleFuturButton = QPushButton(">")
        self.littleFuturButton.clicked.connect(self.littleFuturJump)
        # Bouton Grand Futur
        self.grandFuturButton = QPushButton(">>")
        self.grandFuturButton.clicked.connect(self.grandFuturJump)
        # Label position
        self.labelPosition = QLabel()

        # Slider
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)
        
        # CONNECT
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

        # LAYOUT
        layout = QGridLayout()
        layout.addWidget(self.videoWidget,      0, 0, 1, 9)
        layout.addWidget(self.positionSlider,   1, 0, 1, 9)
        layout.addWidget(self.grandPastButton,  2, 2)
        layout.addWidget(self.littlePastButton, 2, 3)
        layout.addWidget(self.playButton,       2, 4)
        layout.addWidget(self.littleFuturButton,2, 5)
        layout.addWidget(self.grandFuturButton, 2, 6)
        layout.addWidget(self.labelPosition,    2, 7)
        layout.addWidget(self.errorLabel,       2, 0)
        # layout.addLayout(controlLayout)

        # Set widget to contain window contents
        self.setLayout(layout)
        # self.resize(640, 480)
        self.setMinimumWidth(1000)
        self.setMinimumHeight(500)
        # self.setFixedWidth(1000)
    
    def loadMedia(self, fileName):
        """Charge la vidéo dans le lecteur

        Args:
            fileName (String): chemin complet vers la vidéo.
        """
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
        # self.playButton.setEnabled(True)

    def play_pause(self):
        self.mediaPlayer.setPlaybackRate(1.0)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
    
    def grandPastJump(self):
        print("grand past jump", self.mediaPlayer.position())
        self.mediaPlayer.setPlaybackRate(-1.0)
        self.mediaPlayer.play()
        

    def littlePastJump(self):
        print("little past jump", self.mediaPlayer.position())
        self.mediaPlayer.setPlaybackRate(-0.5)
        self.mediaPlayer.play()
    
    def grandFuturJump(self):
        print("grand futur jump", self.mediaPlayer.position())
        self.mediaPlayer.setPlaybackRate(2.0)
        self.mediaPlayer.play()

    def littleFuturJump(self):
        print("little futur jump", self.mediaPlayer.position())
        self.mediaPlayer.setPlaybackRate(0.5)
        self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def updatePlayerImage(self, position):
        self.labelPosition.setText(f"Position : {position} ms")
    
    def exitCall(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = Video_player_widget()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())