import os
def make_voc_dir():
    os.makedirs('VOC2007/Annotations')
    os.makedirs('VOC2007/ImageSets')
    os.makedirs('VOC2007/ImageSets/Main')
    os.makedirs('VOC2007/ImageSets/Layout')
    os.makedirs('VOC2007/ImageSets/Segmentation')
    os.makedirs('VOC2007/JPEGImages')
    os.makedirs('VOC2007/SegmentationClass')
    os.makedirs('VOC2007/SegmentationObject')
if __name__ == '__main__':
    make_voc_dir()