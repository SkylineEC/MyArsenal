
#This is the second step to make the voc dataset, we need to rename the xml because the standard image name fomat of pascaal_voc has 6 digits
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 11:59
# @Author  : CSDN
# 这个脚本的意义就在于只把夜晚的图像挑出来并重命名
# @File    : rename_images.py
import cv2 as cv
import os,shutil
from xml.etree.ElementTree import parse, Element
from tqdm import tqdm
img_cnt = 0 # 图片的起始名字，这里是‘005000.jpg’
for trainval in ['train', 'val']:
    # ==================可能需要修改的地方=====================================#
    g_root_path = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/"

    org_path = g_root_path+trainval+"/"  # 原图片目录
    dst_path = g_root_path+"rename_images/"  # 目标图片目录
    dst_path_night = dst_path + "night_time_all/"


    labelRootPath = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/"+trainval+"/"
    labelDstPath_nighttime = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/"+trainval+"/night_time_all"
    
    error_cnt = 0


    nightTime_cnt = 0
    # ==================================================================#

    file_list = os.listdir(org_path)
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    if not os.path.exists(dst_path_night):
        os.makedirs(dst_path_night)




    if not os.path.exists(labelDstPath_nighttime):
        os.makedirs(labelDstPath_nighttime)

    for idx, file in tqdm(enumerate(file_list)):

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

        except Exception as e:
            error_cnt += 1
            continue

        #修改文件名

        
        if timeofday == 'night':
            nightTime_cnt += 1
            img_name_night = os.path.join(dst_path_night,trainval, "%06d.jpg" % img_cnt)
            img_cnt +=1
            cv.imwrite(img_name_night, img)


    print("----------------------------")
    print("A total of ",error_cnt," images failed to be renamed possibly due to an unknown error")
    print("----------------------------")

    print("A total of ",nightTime_cnt," nighttime images were generated")
    print("============================")