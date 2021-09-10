import os


def make_voc_dir():
    os.makedirs('/home/jiawen/proj/VOC2007/Annotations')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Main')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Layout')
    os.makedirs('/home/jiawen/proj/VOC2007/ImageSets/Segmentation')
    os.makedirs('/home/jiawen/proj/VOC2007/JPEGImages')
    os.makedirs('/home/jiawen/proj/VOC2007/SegmentationClass')
    os.makedirs('/home/jiawen/proj/VOC2007/SegmentationObject')


if __name__ == '__main__':
    make_voc_dir()