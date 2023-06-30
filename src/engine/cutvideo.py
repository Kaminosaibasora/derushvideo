from moviepy.editor import VideoFileClip
import filegestion as fg

class CutVideo:
    def __init__(self)-> None:
        #INIT
        self.folderin = "../file_in/"
        self.folderout = "../file_out/"
        self.videopath = ""
        self.video = None
        self.videoplayer = None
        self.timein = 0
        self.timeout = 0
    
    def loadVideo(self, videopath = "videotest.mp4"):
        self.videopath = videopath
        self.video = VideoFileClip(self.folderin + videopath)
        self.video_player = self.video.ipython_display()
        print("Video chargée")
    
    def playVideo(self):
        self.verifVideoLoad()
        self.video_player.play()
    
    def pauseVideo(self):
        self.verifVideoLoad()
        self.video_player.pause()
    
    def closeVideo(self):
        self.verifVideoLoad()
        self.video_player.close()
    
    def previewVideo(self):
        self.verifVideoLoad()
        self.video.preview()
    
    def cutVideoClip(self, cutnamevideo = "cut.mp4"):
        self.verifVideoLoad()
        try :
            videocut = self.video.subclip(self.timein, self.timeout)
            videocut.write_videofile(self.folderout + cutnamevideo)
        except Exception as e:
            print("Error ", e)
    
    def setTimeIn(self, time):
        self.timein = time

    def setTimeOut(self, time):
        self.timeout = time
    
    def verifVideoLoad(self):
        if self.video == None :
            print("Error : video None")
            raise ValueError("Aucune vidéo n'a été chargée !")


if __name__ == '__main__':
    cv = CutVideo()
    cv.loadVideo()
    cv.setTimeOut(2.5)
    name_clip = fg.generateNewName(cv.folderout, cv.videopath)
    print(name_clip)
    cv.cutVideoClip(name_clip)
    cv.setTimeIn(3)
    cv.setTimeOut(3.5)
    name_clip = fg.generateNewName(cv.folderout, cv.videopath)
    print(name_clip)
    cv.cutVideoClip(name_clip)
    # cv.previewVideo()