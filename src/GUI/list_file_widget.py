import sys
import os

sys.path.append('./engine')

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QFileDialog, QLabel, QVBoxLayout, QWidget, QListWidget, QListWidgetItem

class List_file_widget(QWidget):
    def __init__(self, cutvideo):
        QWidget.__init__(self)
        self.cutVideo = cutvideo

        self.labelchoose = QLabel()

        self.choosebuttonin = QPushButton("choose folder in")
        self.choosebuttonin.clicked.connect(self.choosefolderin)
        self.choosebuttonout = QPushButton("choose folder out")
        self.choosebuttonout.clicked.connect(self.choosefolderout)

        self.listwidget  = QListWidget(self)
        self.listpath    = []
        self.filechoose  = ""
        self.linecurrent = None

        layout = QVBoxLayout()
        layout.addWidget(self.choosebuttonin)
        layout.addWidget(self.choosebuttonout)
        layout.addWidget(self.listwidget)
        layout.addWidget(self.labelchoose)

        self.setLayout(layout)
        self.setFixedWidth(200)
        # MAJ de la liste
        self.list_video_folder(self.cutVideo.folderin)
        self.maj_list_files()



    def choosefolderin(self):
        try :
            valid = False
            folderPath = ""
            while not valid :
                try :
                    folderPath = QFileDialog.getExistingDirectory(self, "Choose Folder")
                    valid = True
                except Exception as e :
                    print(e)
            self.list_video_folder(folderPath)
            self.maj_list_files()
        except Exception as e :
            print(e)
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Error :"+e)
            error.setWindowTitle("Erreur de validation")
    
    def choosefolderout(self):
        try :
            valid = False
            folderPath = ""
            while not valid :
                try :
                    folderPath = QFileDialog.getExistingDirectory(self, "Choose Folder")
                    valid = True
                except Exception as e :
                    print(e)
            self.cutVideo.folderout = folderPath + "/"
        except Exception as e :
            print(e)
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Error :"+e)
            error.setWindowTitle("Erreur de validation")
    
    def maj_list_files(self):
        """Met à jour les widget de la liste de lien.
        """
        self.listwidget.clear()
        for f in self.listpath :
            self.listwidget.addItem(
                QListWidgetItem(f)
            )

    def clicklist(self, test):
        print(test.data())
        self.filechoose = test.data()
        self.labelchoose.setText(test.data())
    
    def updateList(self):
        self.labelchoose.setText("")
        self.listwidget.removeItemWidget(
            self.listwidget.takeItem(self.listwidget.currentRow())
        )
        self.listwidget.repaint()
        self.linecurrent = None
    
    def list_video_folder(self, path):
        """Met à jour le path du folderin de l'objet cut_video et récupère la liste des fichiers."""
        self.cutVideo.folderin = path + "/"
        self.listpath = self.list_video(path)

    def list_video(self, path = "./../file_in", types_accepted = ["mp4", "mov", "avi"]):
        if path[-1] == "/" :
            path = path[:-1]
        files = os.listdir(path)
        liste_v = []
        for f in files :
            # TODO : bricoler les types
            if f[-3:] in types_accepted and not os.path.isdir(path+'/'+f):
                liste_v += [f]
        return liste_v