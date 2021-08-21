import sys
#删除一个文件目录下所有的文件

currDir = sys.path[0]

import os
def removeFile(dir,postfix):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            removeFile(dir+'/'+file,postfix)
            print()
    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)
removeFile('/notebooks/storage/','.jpg')