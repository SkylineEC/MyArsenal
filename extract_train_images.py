import os
import cv2
import  xml.dom.minidom

image_path="/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/train/"
annotation_path="/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xmltrain/train/"

files_name = os.listdir(annotation_path)

for filename_ in files_name:
    filename, extension= os.path.splitext(filename_)
    print(filename)
    img_path =image_path+filename+'.jpg'
    xml_path =annotation_path+filename+'.xml'

    img = cv2.imread(img_path)
    if img is None:
        pass
    dom = xml.dom.minidom.parse(xml_path)
    root = dom.documentElement
    objects=dom.getElementsByTagName("object")
    for object in objects:
        bndbox = root.getElementsByTagName('bndbox')[0]
        xmin = bndbox.getElementsByTagName('xmin')[0]
        ymin = bndbox.getElementsByTagName('ymin')[0]
        xmax = bndbox.getElementsByTagName('xmax')[0]
        ymax = bndbox.getElementsByTagName('ymax')[0]
        xmin_data=xmin.childNodes[0].data
        ymin_data=ymin.childNodes[0].data
        xmax_data=xmax.childNodes[0].data
        ymax_data=ymax.childNodes[0].data
        cv2.rectangle(img,(int(xmin_data),int(ymin_data)),(int(xmax_data),int(ymax_data)),(55,255,155),5)
    flag=0
    try:
        flag=cv2.imwrite("/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/visualize/{}.jpg".format(filename),img)
    except:
        pass
    if(flag):
        print(filename,"done")
print("all done ====================================")