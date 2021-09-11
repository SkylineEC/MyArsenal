import xml.etree.ElementTree as ET
import numpy as np
from tqdm import tqdm
import os
import json
org_path = '/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/Annotations/'
file_list = os.listdir(org_path)

classes_dict = {'rider':[], 'car':[], 'train':[], 'person':[], 'bus':[], 'motor':[], 'truck':[], 'traffic sign':[], 'traffic light':[], 'bike':[]}


for file in tqdm(file_list):
    

    filePath = os.path.join(org_path,file)
    tree = ET.parse(filePath)

    objs = tree.findall('object')

    num_objs = len(objs)
    boxes = np.zeros((num_objs, 4), dtype=np.uint16)




    for ix, obj in enumerate(objs):
            bbox = obj.find('bndbox')
            # Make pixel indexes 0-based
            x1 = float(bbox.find('xmin').text) - 1
            y1 = float(bbox.find('ymin').text) - 1
            x2 = float(bbox.find('xmax').text) - 1
            y2 = float(bbox.find('ymax').text) - 1
            cls = obj.find('name').text.lower().strip()
            classes_dict[cls].append((x2 - x1 + 1) * (y2 - y1 + 1))
            
j = json.dumps(classes_dict)

f2 = open('/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/new_json.json', 'w')
f2.write(j)
f2.close()

            



