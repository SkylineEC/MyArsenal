
#This is the second step to make the voc dataset, we need to rename the xml because the standard image name fomat of pascaal_voc has 6 digits
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 11:59
# @Author  : lazerliu
# @File    : rename_images.py
import cv2 as cv
import os,shutil


# ==================可能需要修改的地方=====================================#
g_root_path = "/home/skyline/Documents/proj/dataset/bdd100k_images_100k/bdd100k/images/100k/"

org_path = g_root_path+"train/"  # 原图片目录
dst_path = g_root_path+"rename_images/"  # 目标图片目录
labelRootPath = "/home/skyline/Documents/proj/dataset/bdd100k_images_100k/bdd100k/xml/train/"
labelDstPath = "/home/skyline/Documents/proj/dataset/bdd100k_images_100k/bdd100k/Annotations/train/"
img_cnt = 0000 # 图片的起始名字，这里是‘005000.jpg’
error_cnt = 0
# ==================================================================#

file_list = os.listdir(org_path)
if not os.path.exists(dst_path):
    os.makedirs(dst_path)



if not os.path.exists(labelDstPath):
    os.makedirs(labelDstPath)

for idx, file in enumerate(file_list):
    if img_cnt == 8000:
        print("----------------------------")
        print(error_cnt)
        print("----------------------------")
        break
    #获取原始的文件名称
    imgFileName = org_path+file
    img = cv.imread(imgFileName)
    # img=cv.resize(img,(512,512))
    #修改文件名
    img_name = os.path.join(dst_path, "%06d.jpg" % img_cnt)

    #根据原本图片文件名寻找对应旧的label文件名
    labelOldName = file.split('.')[0]+'.xml'

    #新的label文件名应该与img文件名保持一致
    labelNewName = "%06d.xml" % img_cnt

    #进行拷贝 
    try:
        shutil.copyfile(os.path.join(labelRootPath,labelOldName), os.path.join(labelDstPath,labelNewName))
    except Exception as e:
        print(imgFileName)
        error_cnt += 1
        continue
    else:
        cv.imwrite(img_name, img)

    
    
    img_cnt += 1
