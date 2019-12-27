
import numpy as np
import os, subprocess   # for iterate dir
from datetime import datetime
from PIL import Image
import json


def get_date_pic_shot(path):
    try:
        dt = Image.open(path)._getexif()[36867]
        #print(type(dt)) # dt as a string
    except Exception as _:
        # they either don't have exif or they don't have key 36867
        # in any situation, we'll use their modification date as shot date
        #print("Exception:{}".format(str(e)))
        ts = os.path.getmtime(path)
        dt = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #print("Path:{}, dt:{}".format(path, dt))
        #print(dt)
    # dt is a string now
    return dt

def walkDir(RootDir, storageFilePath):
    assert os.path.isdir(RootDir)
    ts1 = datetime.now()
    print("Start walking {}:".format(RootDir))
    with open(storageFilePath, "w") as fp1:
        # open in w mode truncates file to 0.
        linecount = 0
        for root, _, files in os.walk(RootDir, topdown=False):
            # root, dirs, files
            # see https://www.geeksforgeeks.org/os-walk-python/
            # root = root of current recursion
            # dirs is dir list of root
            # files is file list of root
            for name in files:
                if (name.lower().endswith(('.png', '.jpg', '.jpeg'))):    
                    #print(os.path.join(root, name))
                    fullpath = os.path.join(root, name)
                    fileInfo = {}
                    fileInfo["path"]=fullpath
                    #fileInfo["date"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")   #by default
                    fileInfo["date"]=get_date_pic_shot(fullpath)
                    #break
                    jsn_str = json.dumps(fileInfo) + "\n"
                    fp1.write(jsn_str)
                    # we only want filename so ignore dir name
                    linecount += 1

    ts2 = datetime.now()
    td = ts2 - ts1

    print("Done walking of {} line(s), time use: {}(s).".format(linecount, td.seconds))
    print("Storaged into {}".format(storageFilePath))
    return

# just one line of filepath you want to index
# example: C:\myphotos\
dirpath = open("readpath", "r").read().strip("\n").strip()
storageFilePath = dirpath + "dirTree.txt"
walkDir(dirpath, storageFilePath)