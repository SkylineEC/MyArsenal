import zipfile
import os
from tqdm import tqdm
def un_zip(file_name):  
    """unzip zip file"""  
    zip_file = zipfile.ZipFile(file_name)
    '''
    if os.path.isdir(file_name.split(".")[0]):  
        pass  
    else:  
        os.mkdir(file_name.split(".")[0])
    '''
    for names in tqdm(zip_file.namelist()):  
        zip_file.extract(names,file_name.split(".")[0])
    zip_file.close()

un_zip("/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/rename_images.zip")

un_zip("/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/train.zip")