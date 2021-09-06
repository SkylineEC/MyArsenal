import os
import shutil
from tqdm import tqdm
# https://blog.csdn.net/weixin_38819889/article/details/101056218


def move_file(orgin_path, moved_path, format_):
    dir_files = os.listdir(orgin_path)  # 得到该文件夹下所有的文件
    for file in tqdm(dir_files):
        file_path = os.path.join(orgin_path, file)  # 路径拼接成绝对路径
        if os.path.isfile(file_path):  # 如果是文件，就打印这个文件路径
            if file.endswith(format_):
                if os.path.exists(os.path.join(moved_path, file)):
                    print("Duplicate file again,skipping")
                    continue
                else:
                    shutil.move(file_path, moved_path)
        if os.path.isdir(file_path):  # 如果目录，就递归子目录
            move_file(file_path, moved_path, format_)
    print("移动文件成功！")


if __name__ == '__main__':
    S_images = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/images/100k/rename_images"

    S_annotations = "/home/jiawen/proj/datasets/bdd100k_images_100k/bdd100k/xml/Annotations/"

    T_images = "/home/jiawen/proj/datasets/VOCdevkit2007/VOC2007/JPEGImages/"

    T_annotations = "/home/jiawen/proj/datasets/VOCdevkit2007/VOC2007/Annotations/"

    # move_file(S_images,S_annotations,".jpg")
    # move_file(T_images,T_annotations,".xml")
    # /home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007

    move_file(S_images, T_images, ".jpg")
    #move_file(S_annotations, T_annotations, ".xml")
