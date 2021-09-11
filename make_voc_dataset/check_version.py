<<<<<<< HEAD
import torch 
print(torch.__version__) 
=======
#检查pytorch版本
import torch 
import os
print(torch.__version__) 
#检查nvidia显存占用情况
os.system('nvidia-smi')
#检查CPU占用情况
os.system('top')
>>>>>>> ae8bfcd968f97cfcd5f24f5a89deb7f7a26676fc
