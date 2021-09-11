import os
<<<<<<< HEAD
def make_voc_dir():
    os.makedirs('VOC2007/Annotations')
    os.makedirs('VOC2007/ImageSets')
    os.makedirs('VOC2007/ImageSets/Main')
    os.makedirs('VOC2007/ImageSets/Layout')
    os.makedirs('VOC2007/ImageSets/Segmentation')
    os.makedirs('VOC2007/JPEGImages')
    os.makedirs('VOC2007/SegmentationClass')
    os.makedirs('VOC2007/SegmentationObject')
=======


def make_voc_dir():
    os.makedirs('/home/jiawen/proj/VOC2007/Annotations')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Main')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Layout')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Segmentation')
    os.makedirs('/home/jiawen/proj/VOC2007/JPEGImages')
    os.makedirs('/home/jiawen/proj/VOC2007/SegmentationClass')
    os.makedirs('/home/jiawen/proj/VOC2007/SegmentationObject')


>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
if __name__ == '__main__':
    make_voc_dir()