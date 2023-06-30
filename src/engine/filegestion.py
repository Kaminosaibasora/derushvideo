import os

def getListFileOut(folderpath):
    return os.listdir(folderpath)

def generateNewName(folderpath, basename = "video_cut.mp4"):
    name = basename.split('.')[0]
    id = 1
    for filename in getListFileOut(folderpath) :
        filename = filename.split('.')[0]
        temp_id = filename.split('_')[-1]
        try :
            if int(temp_id) >= id :
                id = int(temp_id)+1
        except Exception as e :
            print("error ", e, " : ", temp_id)
    return name + '_' + str(id) + ".mp4"

if __name__ == '__main__':
    # print(getListFileOut("../file_in/"))
    # print(getListFileOut("../file_out/"))
    print(generateNewName("../file_out/", "videotest.mp4"))