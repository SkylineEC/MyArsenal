#压缩
import zipfile
import os
from tqdm import tqdm
def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in tqdm(filenames):
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()
zipDir('/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/ImageSets/Main','/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/ImageSets/Main_组会前一天晚上可以用.zip')


       