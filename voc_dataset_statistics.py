import os
import os.path
from xml.etree.ElementTree import parse, Element
from tqdm import tqdm
classes = {
    'rider': 0,
    'car': 0,
    'train': 0,
    'person': 0,
    'bus': 0,
    'motor': 0,
    'truck': 0,
    'traffic_sign': 0,
    'traffic_light': 0,
    'bike': 0
}


def showDataset(xml_fold):
    files = tqdm(os.listdir(xml_fold))
    cnt = 0
    for xmlFile in files:
        file_path = os.path.join(xml_fold, xmlFile)
        dom = parse(file_path)
        root = dom.getroot()
        for obj in root.iter('object'):  #获取object节点中的name子节点
            classes[obj.find('name').text] += 1
    print(classes)


showDataset('/home/jiawen/proj/VOCdevkit2007/VOC2007/Annotations')
classes.clear()
