# convert cityscape dataset to pascal voc format dataset
#将Cityscape转换为PASACAL VOC格式的目标检测数据集
# 1. convert every cityscape image label '.json' to '.txt'
#https://blog.csdn.net/weixin_36670529/article/details/107301950
import json
import os
from os import listdir, getcwd
from os.path import join
import os.path
from tqdm import tqdm
rootDir = '/home/jiawen/proj/cityscapes/leftImg8bit_trainvaltest/leftImg8bit/train/'
rootAnnotationsDir = '/home/jiawen/proj/cityscapes/gtFine_trainvaltest/gtFine/train/'
def position(pos):
    # 该函数用来找出xmin,ymin,xmax,ymax即bbox包围框
    x = []
    y = []
    nums = len(pos)
    for i in range(nums):
        x.append(pos[i][0])
        y.append(pos[i][1])
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    # print(x_max,y_max,x_min,y_min)
    b = (float(x_min), float(y_min), float(x_max), float(y_max))
    # print(b)
    return b
 
# pascal voc 标准格式
# < xmin > 174 < / xmin >
# < ymin > 101 < / ymin >
# < xmax > 349 < / xmax >
# < ymax > 351 < / ymax >
 
def convert(size, box):
    # 该函数将xmin,ymin,xmax,ymax转为x,y,w,h中心点坐标和宽高
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    print((x, y, w, h))
    return (x, y, w, h)
 
 
def convert_annotation(image_id,dirname):

    
    # load_f = open("/home/ubuntu/PycharmProjects/city2pascal/source/train/tubingen/%s_gtFine_polygons.json" % (image_id), 'r')  # 导入json标签的地址
    load_f = open(os.path.join(rootAnnotationsDir,dirname,"%s_gtFine_polygons.json" % (image_id)), 'r')  # 导入json标签的地址
    load_dict = json.load(load_f)

    
    out_file = open(os.path.join(rootAnnotationsDir,dirname,"%s_leftImg8bit.txt" % (image_id)), 'w')  # 输出标签的地址
    # keys=tuple(load_dict.keys())
    w = load_dict['imgWidth']  
    h = load_dict['imgHeight']
    # print(h)
    objects = load_dict['objects']
    nums = len(objects)
    # print(nums)
    # object_key=tuple(objects.keys()
    cls_id = ''
    for i in range(0, nums):
        labels = objects[i]['label'].replace(" ", "_")
        if labels in ['out_of_roi','vegetation','ego_vehicle','pole','terrain','sidewalk','dynamic','polegroup','road','rectification_border','rail_track','sky','tunnel']:
            continue
        pos = objects[i]['polygon']
        bb = position(pos)
        # bb = convert((w, h), b)
        cls_id = labels  
        out_file.write(cls_id + " " + " ".join([str(a) for a in bb]) + '\n')
 
    if cls_id == '':
        print('no label json:',"%s_gtFine_polygons.json" % (image_id))
 
 
def image_id(rootdir):
    a = []
    for parent, rootDir, filenames in os.walk(rootdir):
        for filename in filenames:
            filename = filename[:-16]
            # filename = filename.strip('_leftImg8bit.png')
            a.append(filename)
    return a
 
 
if __name__ == '__main__':

    for dirname in os.listdir(rootDir):
        
        regionDir = os.path.join(rootDir,dirname)
        print(dirname,":")
        names = image_id(regionDir)
        for id in tqdm(names):
            convert_annotation(id,dirname)
    