# -*- coding: utf-8 -*-
# @Author  : matthew
# @File    : make_train_val_test_set.py
# @Software: PyCharm

import os
import random


def _main():
    trainval_percent = 0.9
    train_percent = 0.5
    xmlFilePath_Source = '/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/day_time/'
    
    
    
    
    
    total_xml_Source = os.listdir(xmlFilePath_Source)

    num_Source = len(total_xml_Source)
    
    
    
    num_Source = 5000
    
    
    
    
    
    
    
    
    
    
    list_Source = range(num_Source)
    tv_Source = int(num_Source * trainval_percent)
    tr_Source = int(tv_Source * train_percent)
    trainval_Source = random.sample(list_Source, tv_Source)
    train_Source = random.sample(trainval_Source, tr_Source)
    imageSetsDir = "/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/ImageSets/Main"
    
    
    
    trainvalPath_Source = os.path.join(imageSetsDir,"trainval_s.txt")
    testPath_Source = os.path.join(imageSetsDir,"test_s.txt")
    trainPath_Source = os.path.join(imageSetsDir,"train_s.txt")
    valPath_Source = os.path.join(imageSetsDir,"val_s.txt")
    
   

    
    ftrainval_Source = open(trainvalPath_Source, 'w')
    ftest_Source = open(testPath_Source, 'w')
    ftrain_Source = open(trainPath_Source, 'w')
    fval_Source = open(valPath_Source, 'w')
    
  
    for i in list_Source:
        name = total_xml_Source[i][:-4] + '\n'
        if i in trainval_Source:
            ftrainval_Source.write(name)
            if i in train_Source:
                ftrain_Source.write(name)
            else:
                fval_Source.write(name)
        else:
            ftest_Source.write(name)

    ftrainval_Source.close()
    ftrain_Source.close()
    fval_Source.close()
    ftest_Source.close()
    
    
    xmlFilePath_Target = '/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/night_time/'
    
    
    
    
    
    total_xml_Target = os.listdir(xmlFilePath_Target)

    num_Target = len(total_xml_Target)
    
    
    
    num_Target = 5000
    
    
    
    
    
    
    
    
    
    
    list_Target = range(num_Target)
    tv_Target = int(num_Target * trainval_percent)
    tr_Target = int(tv_Target * train_percent)
    trainval_Target = random.sample(list_Target, tv_Target)
    train_Target = random.sample(trainval_Target, tr_Target)
    imageSetsDir = "/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/ImageSets/Main"
    
    
    
    trainvalPath_Target = os.path.join(imageSetsDir,"trainval_t.txt")
    testPath_Target = os.path.join(imageSetsDir,"test_t.txt")
    trainPath_Target = os.path.join(imageSetsDir,"train_t.txt")
    valPath_Target = os.path.join(imageSetsDir,"val_t.txt")
    


    
    ftrainval_Target = open(trainvalPath_Target, 'w')
    ftest_Target = open(testPath_Target, 'w')
    ftrain_Target = open(trainPath_Target, 'w')
    fval_Target = open(valPath_Target, 'w')
    
    for i in list_Target:
        name = total_xml_Target[i][:-4] + '\n'
        if i in trainval_Target:
            ftrainval_Target.write(name)
            if i in train_Target:
                ftrain_Target.write(name)
            else:
                fval_Target.write(name)
        else:
            ftest_Target.write(name)

    ftrainval_Target.close()
    ftrain_Target.close()
    fval_Target.close()
    ftest_Target.close()


if __name__ == '__main__':
    _main()

    