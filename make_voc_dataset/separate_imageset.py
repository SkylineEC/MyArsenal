
import cv2 as cv
import os,shutil

#首先遍历annotations文件夹里所有的文件

labelDstPath_daytime = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/Annotations/'


originalImagePath = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/JPEGImages/'


newImagePath = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/daytimeImages/'



file_list = os.listdir(labelDstPath_daytime)
i = 0
for idx, file in enumerate(file_list):
    #提取文件名,找到对应rename文件夹当中的文件
    imgName = file[:-4]+'.jpg'
    '''
    print(imgName)
    i +=1
    if i == 10:
        break
    
    '''
    try:
        shutil.copyfile(os.path.join(originalImagePath,imgName), os.path.join(newImagePath,imgName))
    except Exception as e:
        print(imgFileName)

        continue
    else:
        os.remove(os.path.join(originalImagePath,imgName))
#将文件移动到新建的文件夹当中 完成数据集分离
