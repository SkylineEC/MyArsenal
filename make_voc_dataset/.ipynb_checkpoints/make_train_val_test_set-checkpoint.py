# -*- coding: utf-8 -*-
# @Author  : matthew
# @File    : make_train_val_test_set.py
# @Software: PyCharm

import os
import random


def _main():
    trainval_percent = 0.1
    train_percent = 0.9
    xmlfilepath = '/home/skyline/Documents/proj/Arsenal/VOC2007/Annotations'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open('/home/skyline/Documents/proj/Arsenal/VOC2007/ImageSets/Main/trainval.txt', 'w')
    ftest = open('/home/skyline/Documents/proj/Arsenal/VOC2007/ImageSets/Main/test.txt', 'w')
    ftrain = open('/home/skyline/Documents/proj/Arsenal/VOC2007/ImageSets/Main/train.txt', 'w')
    fval = open('/home/skyline/Documents/proj/Arsenal/VOC2007/ImageSets/Main/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftest.write(name)
            else:
                fval.write(name)
        else:
            ftrain.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()


if __name__ == '__main__':
    _main()