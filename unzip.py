import zipfile
import os
<<<<<<< HEAD
=======
from tqdm import tqdm
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
def un_zip(file_name):  
    """unzip zip file"""  
    zip_file = zipfile.ZipFile(file_name)
    '''
    if os.path.isdir(file_name.split(".")[0]):  
        pass  
    else:  
        os.mkdir(file_name.split(".")[0])
    '''
<<<<<<< HEAD
    for names in zip_file.namelist():  
        zip_file.extract(names,file_name.split(".")[0])
    zip_file.close()

un_zip("/home/jiawen/proj/datasets/bdd100k_labels_release.zip")
=======
    for names in tqdm(zip_file.namelist()):  
        zip_file.extract(names,file_name.split(".")[0])
    zip_file.close()


un_zip("/home/jiawen/proj/VOCFromJeremy/JPEGImages.zip")
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
