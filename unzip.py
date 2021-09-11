import zipfile
import os
def un_zip(file_name):  
    """unzip zip file"""  
    zip_file = zipfile.ZipFile(file_name)
    '''
    if os.path.isdir(file_name.split(".")[0]):  
        pass  
    else:  
        os.mkdir(file_name.split(".")[0])
    '''
    for names in zip_file.namelist():  
        zip_file.extract(names,file_name.split(".")[0])
    zip_file.close()

un_zip("/home/jiawen/proj/datasets/bdd100k_labels_release.zip")