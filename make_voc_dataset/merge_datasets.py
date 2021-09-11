
import cv2 as cv
import os,shutil
from tqdm import tqdm


cnt = 0
txt_tables = []
#首先读取文件路径
#白天的xml


##########################################################################################################################################


originalTestingDatasetPath = "/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/"
originTrainingDatasetPath = "/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007_day_clear_20220816/"
dstDatasetPath = "/home/jiawen/proj/datasets/hybirdDayTrainNightTest/VOC2007/"


##########################################################################################################################################




#--------------------------------------------------------操作训练集--------------------------------------------------------
#白天的trainval.txt
f_trainval = open(os.path.join(originTrainingDatasetPath,"ImageSets/Main/trainval.txt"), "r",encoding='utf-8')

#黑夜的test.txt
f_night_test = open(os.path.join(originalTestingDatasetPath,"ImageSets/Main/test.txt"), "r",encoding='utf-8')


#白天训练集以及验证集的图像--->要复制到hybrid里面
trainImgPath = os.path.join(originTrainingDatasetPath,"JPEGImages")
#黑夜的测试集图像--->要复制到hybrid里面
testImgPath = os.path.join(originalTestingDatasetPath,"JPEGImages")





#白天训练集以及验证集的标注--->要复制到hybrid里面
trainLabelPath = os.path.join(originTrainingDatasetPath,"Annotations")
#黑夜的测试集标注--->要复制到hybrid里面
testLabelPath = os.path.join(originalTestingDatasetPath,"Annotations")


#目标hybrid集图像地址
dstImgPath = os.path.join(dstDatasetPath,"JPEGImages")

#目标hybrid集标注地址
dstLabelPath = os.path.join(dstDatasetPath,"Annotations")
dstMainFolderPath = os.path.join(dstDatasetPath,"ImageSets/Main")


#如果不存在就创建文件夹
if not os.path.exists(dstImgPath):
    os.makedirs(dstImgPath)
if not os.path.exists(dstLabelPath):
    os.makedirs(dstLabelPath)
if not os.path.exists(dstMainFolderPath):
    os.makedirs(dstMainFolderPath)

#lineNum = len(f_trainval.readlines())
#首先复制训练集和验证集的图像和标签
line = f_trainval.readline()

while line:

    originalImgName = line[:-1]+ ".jpg"
    originalLabelName = line[:-1] + ".xml"
    print(originalImgName)


    if line[:-1] == '':
        line = f_trainval.readline()
        continue
    #得到原始图像地址
    originalImg = os.path.join(trainImgPath, originalImgName)

    #得到目标图像地址
    dstImg= os.path.join(dstImgPath, originalImgName)

    #复制图像
    shutil.copy(originalImg,dstImg)


    #得到原始标签地址
    originalLabel = os.path.join(trainLabelPath,originalLabelName)

    #得到目标标签地址
    dstLabel = os.path.join(dstLabelPath, originalLabelName)
    #复制标签
    shutil.copy(originalLabel,dstLabel)





    line = f_trainval.readline() # 读取下一行
    cnt += 1
    
print("---------------")
print("-----train-----")
print(cnt)
print("-----images----")
print("---------------")

f_trainval.close()



#--------------------------------------------------------操作测试集--------------------------------------------------------



lineNum = len(f_night_test.readlines())


line = f_night_test.readline()
cnt = 0
for i in tqdm(range(lineNum)):

    originalImgName = line[:-1] + ".jpg"
    originalLabelName = line[:-1] + ".xml"

    if line[:-1] == '':
        line = f_night_test.readline()
        continue
    originalImg = os.path.join(testImgPath,originalImgName)
    dstImg = os.path.join(dstImgPath,originalImgName)
    #复制图像
    shutil.copy(originalImg,dstImg)


    originalLabel = os.path.join(testLabelPath,originalLabelName)
    dstLabel = os.path.join(dstLabelPath,originalLabelName)
    shutil.copy(originalLabel,dstLabel)

    

    line = f_test.readline() # 读取下一行

print("---------------")
print("-----test------")
print(cnt)
print("-----images----")
print("---------------")


#到最后复制test.txt和trainval.txt train.txt val.txt
shutil.copy(os.path.join(originTrainingDatasetPath,"ImageSets/Main/trainval.txt"),os.path.join(dstMainFolderPath,"trainval.txt"))
shutil.copy(os.path.join(originTrainingDatasetPath,"ImageSets/Main/val.txt"),os.path.join(dstMainFolderPath,"val.txt"))
shutil.copy(os.path.join(originTrainingDatasetPath,"ImageSets/Main/train.txt"),os.path.join(dstMainFolderPath,"train.txt"))
shutil.copy(os.path.join(originalTestingDatasetPath,"ImageSets/Main/test.txt"),os.path.join(dstMainFolderPath,"test.txt"))

f_night_test.close()

