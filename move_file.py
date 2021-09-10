'''
Author: Wang Jiawen
Date: 2021-08-2u 14:06:34
LastEditTime: 2021-08-27 16:18:20
LastEditors: your name
Description: In User Settings Edit
FilePath: /proj/MyArsenal/move_file.py
'''
#将一个文件夹下面的文件移动到另外一个文件夹


import shutil
import os
from tqdm import tqdm

def moveFiles(oldPath,newPath):
    print()
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

moveFiles("/home/jiawen/proj/VOC2007","/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007")
