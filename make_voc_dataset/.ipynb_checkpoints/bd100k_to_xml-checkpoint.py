#This is the first step for converting bdd100k to voc, we need to operate the json file to xml file

import os
import os.path as osp

import json

from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom

from PIL import Image

from tqdm import tqdm

DEBUG = False

#"/home/skyline/Documents/proj/dataset/bdd100k"
BDD_FOLDER = "/home/skyline/Documents/proj/dataset/bdd100k_images_100k/bdd100k/"
if DEBUG:
    XML_PATH = "./xml"
else:
    XML_PATH = BDD_FOLDER + "/xml"


def bdd_to_voc(bdd_folder, xml_folder):
    image_path = bdd_folder + "/images/100k/%s"
    label_path = bdd_folder + "/labels/bdd100k_labels_images_%s.json"
    classes = set()

    for trainval in ['train', 'val']:
        image_folder = image_path % trainval
        json_path = label_path % trainval
        xml_folder_ = osp.join(xml_folder, trainval)

        if not os.path.exists(xml_folder_):
            os.makedirs(xml_folder_)

        with open(json_path) as f:
            j = f.read()
        data = json.loads(j)
        for datum in tqdm(data):
            tmp_list = []
            annotation = Element('annotation')
            SubElement(annotation, 'folder').text ='VOC2007'
            SubElement(annotation, 'filename').text = datum['name']
            source = get_source()
            owner = get_owner()
            annotation.append(source)
            annotation.append(owner)
            size = get_size(osp.join(image_folder, datum['name']))
            annotation.append(size)
            SubElement(annotation, 'segmented').text ='0'
            # additional information
            #for key, item in datum['attributes'].items():
            #    SubElement(annotation, key).text = item

            # bounding box
            for label in datum['labels']:
                tmp_list.append(1)
                #if label['category'] != "traffic light":
                #    continue
                #else:
                    
                #color = label['attributes']["trafficLightColor"]
                try:
                    box2d = label['box2d']
                except KeyError:
                    continue
                else:
                    bndbox = get_bbox(box2d)

                object_ = Element('object')
                SubElement(object_, 'name').text = label['category']
                #SubElement(object_, 'name').text = color
                SubElement(object_, 'pose').text = "Unspecified"
                SubElement(object_, 'truncated').text = '0'
                SubElement(object_, 'difficult').text = '0'
                classes.add(label['category'])
                #classes.add(color)

                object_.append(bndbox)
                annotation.append(object_)
            if len(tmp_list) == 0:
                continue
            xml_filename = osp.splitext(datum['name'])[0] + '.xml'
            with open(osp.join(xml_folder_, xml_filename), 'w') as f:
                f.write(prettify(annotation))
    print(classes)

def get_owner():
    owner = Element('owner')
    SubElement(owner, 'flickrid').text ='NULL'
    SubElement(owner, 'name').text ='lijing'
    return owner

def get_source():
    source = Element('source')
    SubElement(source, 'database').text ='voc_bdd'
    SubElement(source, 'annotation').text ='VOC2007'
    SubElement(source, 'image').text ='flickr'
    SubElement(source, 'flickrid').text ='NULL'
    return source




def get_size(image_path):
    i = Image.open(image_path)
    sz = Element('size')
    SubElement(sz, 'width').text = str(i.width)
    SubElement(sz, 'height').text = str(i.height)
    SubElement(sz, 'depth').text = str(3)
    return sz


def get_bbox(box2d):
    bndbox = Element('bndbox')
    SubElement(bndbox, 'xmin').text = str(int(round(box2d['x1'])))
    SubElement(bndbox, 'ymin').text = str(int(round(box2d['y1'])))
    SubElement(bndbox, 'xmax').text = str(int(round(box2d['x2'])))
    SubElement(bndbox, 'ymax').text = str(int(round(box2d['y2'])))
    return bndbox


def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


if __name__ == "__main__":
    bdd_to_voc(BDD_FOLDER, XML_PATH)
