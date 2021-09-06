#! /usr/bin/python
# -*- coding:UTF-8 -*-
# Convert cityscape dataset to pascal voc format dataset
#https://blog.csdn.net/weixin_36670529/article/details/107301950
# 2. convert '.txt' to '.xml'

import os, sys,shutil
import glob
from PIL import Image
from tqdm import tqdm

from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom

def get_size(image_path):
    i = Image.open(image_path)
    sz = Element('size')
    SubElement(sz, 'width').text = str(i.width)
    SubElement(sz, 'height').text = str(i.height)
    SubElement(sz, 'depth').text = str(3)
    return sz

def get_owner():
    owner = Element('owner')
    SubElement(owner, 'flickrid').text ='NULL'
    SubElement(owner, 'name').text = 'Wang_Jiawen'


    return owner

def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def get_source():
    source = Element('source')
    SubElement(source, 'database').text ='voc_bdd'
    SubElement(source, 'annotation').text ='VOC2007'
    SubElement(source, 'image').text = 'daytime'
    SubElement(source, 'weather').text ='unknown'
    return source


def get_bbox(spt):
    bndbox = Element('bndbox')
    SubElement(bndbox, 'xmin').text = str(spt[1])
    SubElement(bndbox, 'ymin').text = str(spt[2])
    SubElement(bndbox, 'xmax').text = str(spt[3])
    SubElement(bndbox, 'ymax').text = str(spt[4])
    return bndbox


def txt_to_xml(src_img_root_dir,src_txt_root_dir,dst_xml_root_dir,dst_img_dir,MAX_SIZE):
    classes = set()    
    #  图像存储位置
    

    cnt = 0
    for regionNameDir in os.listdir(src_img_root_dir):
        src_img_dir = os.path.join(src_img_root_dir,regionNameDir)
        src_txt_dir = os.path.join(src_txt_root_dir,regionNameDir)
        
        img_Lists = glob.glob(src_img_dir + '/*.png')
        
        img_basenames = []  # e.g. 100.jpg
        for item in img_Lists:
            img_basenames.append(os.path.basename(item))
        
        img_names = []  # e.g. 100
        for item in img_basenames:
            temp1, temp2 = os.path.splitext(item)
            img_names.append(temp1)
        
        for img in tqdm(img_names):
            tmp_list = []
            cnt += 1
            if cnt > MAX_SIZE:
                break
            srcImageDir = os.path.join(src_img_dir  , img + '.png')
            im = Image.open(srcImageDir)
            
            dstImageDir = os.path.join(dst_img_dir,img + '.jpg')
            shutil.copy(srcImageDir,dstImageDir)
            width, height = im.size
        
            # open the crospronding txt file
            gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
            # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()
        
            # write in xml file
            annotation = Element('annotation')
            SubElement(annotation, 'folder').text ='Cityscapes'
            SubElement(annotation, 'filename').text = str(img) + '.jpg'
            source = get_source()
            owner = get_owner()
            annotation.append(source)
            annotation.append(owner)
            size = get_size(dstImageDir)
            annotation.append(size)
            SubElement(annotation, 'segmented').text ='0'
            # bounding box
            for label in gt:
                tmp_list.append(1)
                spt = label.split(' ')

                object_ = Element('object')
                SubElement(object_, 'name').text = str(spt[0])

                SubElement(object_, 'pose').text = "Unspecified"
                SubElement(object_, 'truncated').text = '0'
                SubElement(object_, 'difficult').text = '0'
                classes.add(str(spt[0]))
                #classes.add(color)
                try:
                    bndbox = get_bbox(spt)
                except KeyError:
                    continue
                
                object_.append(bndbox)


                annotation.append(object_)
            if len(tmp_list) == 0:
                continue
            xmlName = img + ".xml"
            xml_filename =  os.path.join(dst_xml_root_dir,xmlName)

            
            with open(os.path.join(xml_filename), 'w') as f:
                f.write(prettify(annotation))
    print(classes)

            