import matplotlib.pyplot as plt # plt - display pic
import matplotlib.image as mpimg # mpimg - read pic
import json
import random
#
#
def showImg(filepath, title):
    imgToShow = mpimg.imread(filepath) # 
    # imgToShow->np array
    #imgToShow.shape #

    plt.imshow(imgToShow) # load pic
    plt.axis('off') # turn off axis
    plt.title(title)
    plt.show()


def readImgList(listfilepath):
    imglist = []
    with open(listfilepath, "r") as fp1:
        for row in fp1:
            jsn_str = row.strip("\n").strip()
            try:
                imgObj = json.loads(jsn_str)
            except: #ignore error
                pass
            if(imgObj is not None):
                imglist.append(imgObj)
            else:
                print("Obj is None")
            #print(imgObj)
            #break
    return imglist
#just show a random picture
def showRandomPic(listfilepath):
    imglist = readImgList(listfilepath)
    listlen = len(imglist)
    print("list length:{}".format(listlen))
    idx = random.randint(0, listlen-1)

    imgToShow = imglist[idx]
    path = imgToShow["path"]
    date = imgToShow["date"]
    title = "date:{} path:{}".format(date,path)
    print(title)
    showImg(path, title)
    return


dirpath = open("readpath", "r").read().strip("\n").strip()
storageFilePath = os.path.join(dirpath, "dirTree.txt")
#print(dirpath)
showRandomPic(storageFilePath)