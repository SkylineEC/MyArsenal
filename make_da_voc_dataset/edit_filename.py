import os

#找到source.txt里面的所有文件，生成一个列表，遍历这个列表
imgae_set = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt'
image_dir = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/JPEGImages/'
f_test = open(imgae_set, "r",encoding='utf-8')


line = f_test.readline()






image_list = os.listdir(image_dir)
num = 0
#设置一下最大轮数
MAX_NUM =1000
#for i in  image_list:
while line:

#然后在前面加上source_


#修改对应image的名称

