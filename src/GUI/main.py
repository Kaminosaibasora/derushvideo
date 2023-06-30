import sys
sys.path.append('./engine')
from cutvideo import CutVideo
from PyQt5.QtWidgets import QApplication
from GUI import GUI

cutVideo = CutVideo()

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

fen = GUI(cutVideo)
fen.show()

app.exec_()