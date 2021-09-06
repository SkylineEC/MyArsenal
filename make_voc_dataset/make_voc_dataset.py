# -*- coding: utf-8 -*-
# @Author  : matthew
# @File    : make_train_val_test_set.py
# @Software: PyCharm

import os
import random


def make_voc_dataset(xmlFilePath,imageSetsDir):
    trainval_percent = 0.9
    train_percent = 0.5
    
    
    
    
    
    
    total_xml = os.listdir(xmlFilePath)

    num = len(total_xml)
    
    
    
    
    
    
    
    
    
    
    
    
    
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)
    
    
    
    
    trainvalPath = os.path.join(imageSetsDir,"trainval.txt")
    print(trainvalPath)
    testPath = os.path.join(imageSetsDir,"test.txt")
    trainPath = os.path.join(imageSetsDir,"train.txt")
    valPath = os.path.join(imageSetsDir,"val.txt")

    
    ftrainval = open(trainvalPath, 'w')
    ftest = open(testPath, 'w')
    ftrain = open(trainPath, 'w')
    fval = open(valPath, 'w')
    
  
    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()
    
    



    