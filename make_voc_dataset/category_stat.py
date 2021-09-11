#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
from xml.etree.ElementTree import parse, Element
from tqdm import tqdm
classes = set()


def stat(xml_fold):
    files = os.listdir(xml_fold)
    cnt = 0
    for xmlFile in tqdm(files):
        file_path = os.path.join(xml_fold, xmlFile)
        dom = parse(file_path)
        root = dom.getroot()
        for obj in root.iter('object'):  #获取object节点中的name子节点
            tmp_name = obj.find('name').text
            classes.add(tmp_name)
    print(classes)


stat('/home/jiawen/proj/VOCdevkit2007/VOC2007/Annotations')