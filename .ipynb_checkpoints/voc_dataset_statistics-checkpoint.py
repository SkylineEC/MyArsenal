<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
from xml.etree.ElementTree import parse, Element
def changeName(xml_fold, origin_name, new_name):
    '''
    xml_fold: xml存放文件夹
    origin_name: 原始名字，比如弄错的名字，原先要cow,不小心打成cwo
    new_name: 需要改成的正确的名字，在上个例子中就是cow
    '''
=======
import os
import os.path
from xml.etree.ElementTree import parse, Element


classes = {'rider':0, 'car':0, 'train':0, 'person':0, 'bus':0, 'motor':0, 'truck':0, 'traffic sign':0, 'traffic light':0, 'bike':0}

def showDataset(xml_fold):
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
    files = os.listdir(xml_fold)
    cnt = 0 
    for xmlFile in files:
        file_path = os.path.join(xml_fold, xmlFile)
        dom = parse(file_path)
        root = dom.getroot()
        for obj in root.iter('object'):#获取object节点中的name子节点
<<<<<<< HEAD
            tmp_name = obj.find('name').text
            if tmp_name == origin_name: # 修改
                obj.find('name').text = new_name
                print("change %s to %s." % (origin_name, new_name))
                cnt += 1
                print( cnt)
        dom.write(file_path, xml_declaration=True)#保存到指定文件   
changeName('/notebooks/storage/data/VOC2007/Annotations', '04_Amorphous', '04_amorphous')
=======
            classes[obj.find('name').text] += 1
    print(classes)
print("Day Images:")
showDataset('/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/night_time')
classes.clear()
print("Night Images:")
showDataset('/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train/day_time')



'''
20210817_bdd100k_clear
Day Images:
{'rider': 743, 'car': 211127, 'train': 26, 'person': 15336,
'bus': 1761, 'motor': 584, 'truck': 4276, 'traffic sign': 74184,
'traffic light': 67662, 'bike': 1258}
Night Images:
{'rider': 1953, 'car': 350534, 'train': 62, 'person': 32113,
'bus': 4489, 'motor': 1489, 'truck': 11689, 'traffic sign': 118050,
'traffic light': 93664, 'bike': 2874}
'''
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
