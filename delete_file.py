import os
import sys
# 删除一个文件目录下所有的文件
from tqdm import tqdm
currDir = sys.path[0]


def removeFile(dir, postfix):
    if os.path.isdir(dir):
        #print("Delete Path:",os.listdir(dir))
        for file in tqdm(os.listdir(dir)):
            removeFile(dir+'/'+file, postfix)

    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)


removeFile(
    '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/pretrained_model', '.pth')
