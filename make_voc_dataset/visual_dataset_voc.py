import os
import cv2
import re
from xml.etree.ElementTree import parse, Element
<<<<<<< HEAD


pattens = ['name','xmin','ymin','xmax','ymax']
 
=======
import os.path as osp

pattens = ['name','xmin','ymin','xmax','ymax']
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
def get_annotations(xml_path):
    bbox = []
    with open(xml_path,'r') as f:
        text = f.read().replace('\n','return')
        p1 = re.compile(r'(?<=<object>)(.*?)(?=</object>)')
        result = p1.findall(text)
        for obj in result:
            tmp = []
            for patten in pattens:
                p = re.compile(r'(?<=<{}>)(.*?)(?=</{}>)'.format(patten,patten))
                if patten == 'name':
                    tmp.append(p.findall(obj)[0])
                else:
                    tmp.append(int(float(p.findall(obj)[0])))
            bbox.append(tmp)
    return bbox

def save_viz_image(image_path,xml_path,save_path):
    bbox = get_annotations(xml_path)

    image = cv2.imread(image_path)
    for info in bbox:
        cv2.rectangle(image,(info[1],info[2]),(info[3],info[4]),(255,0,0),thickness=2)
        cv2.putText(image,info[0],(info[1],info[2]),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    dom = parse(xml_path)
    root = dom.getroot()
    for obj in root.iter('object'):#获取object节点中的name子节点
        tmp_name = obj.find('name').text
        if tmp_name == 'train': # 修改
            cv2.imwrite(os.path.join(save_path,image_path.split('/')[-1]),image)



<<<<<<< HEAD
if __name__ == '__main__':
    #/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/JPEGImages
    image_dir = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/JPEGImages'
    xml_dir = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/Annotations'
    save_dir = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/viz_images'

    imgae_set = '/home/jiawen/proj/faster-rcnn/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt'


=======

if __name__ == '__main__':
    #替换成自己的数据集目录
    voc_path ="/home/jiawen/proj/VOC2007/"
    image_dir = osp.join(voc_path,"JPEGImages")
    xml_dir = osp.join(voc_path,"Annotations")
    save_dir = osp.join(voc_path,"Visualization Dataset")
    imgae_set = osp.join(voc_path,"ImageSets/Main/trainval.txt")
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
    #白天的trainval.txt
    f_test = open(imgae_set, "r",encoding='utf-8')
    

    line = f_test.readline()
<<<<<<< HEAD
    





    image_list = os.listdir(image_dir)
    num = 0
    MAX_NUM =1000
=======
    image_list = os.listdir(image_dir)
    num = 0
    #设置一下最大轮数
    MAX_NUM =100
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
    #for i in  image_list:
    while line:
        originalLabelName = line[:-1] + ".xml"
        originalImgName = line[:-1] + ".jpg"
<<<<<<< HEAD


        #location of xml annotation
        originalLabel = os.path.join(xml_dir,originalLabelName)

        
        image_path = os.path.join(image_dir,originalImgName)
        print(image_path)



        if num == MAX_NUM:
            break
        
        save_viz_image(image_path,originalLabel,save_dir)
        line = f_test.readline()

=======
        #location of xml annotation
        originalLabel = os.path.join(xml_dir,originalLabelName)
        image_path = os.path.join(image_dir,originalImgName)
        
        if num == MAX_NUM:
            break
        save_viz_image(image_path,originalLabel,save_dir)
        line = f_test.readline()
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
        num +=1
