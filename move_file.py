#将一个文件夹下面的文件移动到另外一个文件夹


import shutil
import os
from tqdm import tqdm

def moveFiles(oldPath,newPath):
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    if not os.path.exists(oldPath):
        print("path not exits")
        return
#good
    files = os.listdir(oldPath)
    #print(files)
    for file in tqdm(files):
        #print(os.path.isfile(os.path.join(oldPath,file)))
        if os.path.isfile(os.path.join(oldPath,file)):
            shutil.copy(os.path.join(oldPath,file),os.path.join(newPath,file))

moveFiles("/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/day/","/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/JPEGImages/")


moveFiles("/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/night/","/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/JPEGImages/")