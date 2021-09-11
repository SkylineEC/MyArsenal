<<<<<<< HEAD

#This is the second step to make the voc dataset, we need to rename the xml because the standard image name fomat of pascaal_voc has 6 digits
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 11:59
# @Author  : Wang Jiawen
# @File    : rename_images.py
import cv2 as cv
import os,shutil
from xml.etree.ElementTree import parse, Element

# ==================可能需要修改的地方=====================================#
g_root_path = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/"

org_path = g_root_path+"train/"  # 原图片目录
dst_path = g_root_path+"rename_images/"  # 目标图片目录
dst_path_night = dst_path + "night/"
dst_path_day = dst_path + "day/"

labelRootPath = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/train/"
labelDstPath_daytime = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/day_time"
labelDstPath_nighttime = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/night_time"
img_cnt = 0000 # 图片的起始名字，这里是‘005000.jpg’
error_cnt = 0
# ==================================================================#

file_list = os.listdir(org_path)
if not os.path.exists(dst_path):
    os.makedirs(dst_path)

if not os.path.exists(dst_path_night):
    os.makedirs(dst_path_night)

if not os.path.exists(dst_path_day):
    os.makedirs(dst_path_day)

if not os.path.exists(labelDstPath_daytime):
    os.makedirs(labelDstPath_daytime)
if not os.path.exists(labelDstPath_nighttime):
    os.makedirs(labelDstPath_nighttime)

for idx, file in enumerate(file_list):
    '''
        if img_cnt == 60000:
        print("----------------------------")
        print(error_cnt)
        print("----------------------------")
        break
    '''
    

    #获取原始的文件名称
    imgFileName = org_path+file
    img = cv.imread(imgFileName)
    # img=cv.resize(img,(512,512))
    

    #根据原本图片文件名寻找对应旧的label文件名
    labelOldName = file.split('.')[0]+'.xml'

    try:
    #找到原本label文件对应图像的timeofday
        originalLabelPath = os.path.join(labelRootPath,labelOldName)
        dom = parse(originalLabelPath)
        root = dom.getroot()
        timeofday = root.find('source').find('image').text
        if root.find('source').find('weather').text != 'clear':
            continue

    except Exception as e:
        print(imgFileName)
        error_cnt += 1
        continue

    #修改文件名
    img_name = os.path.join(dst_path, "%06d.jpg" % img_cnt)
    img_name_night = os.path.join(dst_path_night, "%06d.jpg" % img_cnt)
    img_name_day = os.path.join(dst_path_day, "%06d.jpg" % img_cnt)

    #新的label文件名应该与img文件名保持一致
    labelNewName = "%06d.xml" % img_cnt
    if timeofday == 'daytime':
        try:
            shutil.copyfile(originalLabelPath, os.path.join(labelDstPath_daytime,labelNewName))
        except Exception as e:
            print(imgFileName)
            error_cnt += 1
            continue
        else:
            cv.imwrite(img_name_day, img)
    if timeofday == 'night':
        try:
            shutil.copyfile(originalLabelPath, os.path.join(labelDstPath_nighttime,labelNewName))
        except Exception as e:
            print(imgFileName)
            error_cnt += 1
            continue
        else:
            cv.imwrite(img_name_night, img)
        
    #进行拷贝 
    

    
    
    img_cnt += 1
    if img_cnt%100 == 0:
        print(img_cnt)
print("----------------------------")
print(error_cnt)
print("----------------------------")

print("============================")
print(img_cnt)
=======
# This is the second step to make the voc dataset, we need to rename the xml because the standard image name fomat of pascaal_voc has 6 digits
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 11:59
# @Author  : CSDN
# @File    : rename_images.py
import cv2 as cv
import os
import shutil
from xml.etree.ElementTree import parse, Element
from tqdm import tqdm
img_cnt = 0  # 图片的起始名字，这里是‘005000.jpg’
error_cnt = 0
dayTime_cnt = 0
nightTime_cnt = 0
for trainval in ['train', 'val']:
    # ==================可能需要修改的地方=====================================#
    g_root_path = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/"

    org_path = g_root_path + trainval + "/"  # 原图片目录
    dst_path = g_root_path + "rename_images/"  # 目标图片目录
    dst_path_night = dst_path + "night/"
    dst_path_day = dst_path + "day/"

    labelRootPath = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/" + trainval + "/"
    labelDstPath_daytime = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/" + trainval + "/day_time"
    labelDstPath_nighttime = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/" + \
        trainval+"/night_time"

    # ==================================================================#

    file_list = os.listdir(org_path)
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    if not os.path.exists(dst_path_night):
        os.makedirs(dst_path_night)

    if not os.path.exists(dst_path_day):
        os.makedirs(dst_path_day)

    if not os.path.exists(labelDstPath_daytime):
        os.makedirs(labelDstPath_daytime)
    if not os.path.exists(labelDstPath_nighttime):
        os.makedirs(labelDstPath_nighttime)

    for idx, file in tqdm(enumerate(file_list)):

        # 获取原始的文件名称
        imgFileName = org_path + file
        img = cv.imread(imgFileName)
        # img=cv.resize(img,(512,512))

        # 根据原本图片文件名寻找对应旧的label文件名
        labelOldName = file.split('.')[0] + '.xml'

        try:
            # 找到原本label文件对应图像的timeofday
            originalLabelPath = os.path.join(labelRootPath, labelOldName)
            dom = parse(originalLabelPath)
            root = dom.getroot()
            timeofday = root.find('source').find('image').text
            # 我们只要晴天的图像
            if root.find('source').find('weather').text != 'clear':
                continue

        except Exception as e:
            error_cnt += 1
            continue

        # 修改文件名

        img_cnt += 1
        if timeofday == 'daytime':
            try:
                img_name_day = os.path.join(dst_path_day,
                                            "source_%06d.jpg" % img_cnt)
                # 新的label文件名应该与img文件名保持一致

                labelNewName = "source_%06d.xml" % img_cnt
                shutil.copyfile(
                    originalLabelPath,
                    os.path.join(labelDstPath_daytime, labelNewName))
            except Exception as e:
                print(labelNewName)
                error_cnt += 1
                continue
            else:
                dayTime_cnt += 1

                cv.imwrite(img_name_day, img)
        if timeofday == 'night':
            try:
                img_name_night = os.path.join(dst_path_night,
                                              "target_%06d.jpg" % img_cnt)
                # 新的label文件名应该与img文件名保持一致

                labelNewName = "target_%06d.xml" % img_cnt
                shutil.copyfile(
                    originalLabelPath,
                    os.path.join(labelDstPath_nighttime, labelNewName))
            except Exception as e:
                print(labelNewName)
                error_cnt += 1
                continue
            else:
                nightTime_cnt += 1
                cv.imwrite(img_name_night, img)

print("----------------------------")
print("A total of ", error_cnt, " images failed to be renamed")
print("----------------------------")

print("A total of ", dayTime_cnt,
      " daytime clear weather images were renamed successfully")
print("============================")

print("A total of ", nightTime_cnt,
      " nighttime clear weather images were renamed successfully")
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
print("============================")
