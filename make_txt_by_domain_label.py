import os
import os.path as osp
import random

datasetPath = "/home/jiawen/proj/VOCdevkit2007/VOC2007/"

imgPath = osp.join(datasetPath, "JPEGImages/")
txtPath = osp.join(datasetPath, "ImageSets/Main_mini/")

#MAX_NUM = 5000

total_xml_list = os.listdir(imgPath)
total_xml_num = len(total_xml_list)

train_percent = 0.5

# train的数量

source_list = []
target_list = []

# 挑出来train和target
for filename in total_xml_list:
    if filename[0] == 's':
        source_list.append(filename)
    else:
        target_list.append(filename)
print(len(source_list))
print(len(target_list))

source_list = source_list[:1000]
target_list = target_list[:1000]

# 13633 source
# 24133 target
# source全部用来训练
source_trainval_list = random.sample(source_list, int(len(source_list) * 0.95))
source_train_list = random.sample(source_trainval_list,
                                  int(len(source_trainval_list) * 0.5))

trainvalPath_Source = os.path.join(txtPath, "trainval_s.txt")
testPath_Source = os.path.join(txtPath, "test_s.txt")
trainPath_Source = os.path.join(txtPath, "train_s.txt")
valPath_Source = os.path.join(txtPath, "val_s.txt")

ftrainval_Source = open(trainvalPath_Source, 'w')
ftest_Source = open(testPath_Source, 'w')
ftrain_Source = open(trainPath_Source, 'w')
fval_Source = open(valPath_Source, 'w')

ftrainval_Source_cnt = 0
ftest_Source_cnt = 0
ftrain_Source_cnt = 0
fval_Source_cnt = 0

#indexSource = range(len(source_list))
#indexTarget = range(len(target_list))
for i in source_list:
    name = i[:-4] + '\n'
    if i in source_trainval_list:
        ftrainval_Source.write(name)
        ftrainval_Source_cnt += 1
        if i in source_train_list:
            ftrain_Source.write(name)
            ftrain_Source_cnt += 1
        else:
            fval_Source.write(name)
            fval_Source_cnt += 1
    else:
        ftest_Source.write(name)
        ftest_Source_cnt += 1

# target
target_trainval_list = random.sample(target_list, int(len(target_list) * 0.95))
target_train_list = random.sample(target_trainval_list,
                                  int(len(target_trainval_list) * 0.5))

trainvalPath_Target = os.path.join(txtPath, "trainval_t.txt")
testPath_Target = os.path.join(txtPath, "test_t.txt")
trainPath_Target = os.path.join(txtPath, "train_t.txt")
valPath_Target = os.path.join(txtPath, "val_t.txt")

ftrainval_Target = open(trainvalPath_Target, 'w')
ftest_Target = open(testPath_Target, 'w')
ftrain_Target = open(trainPath_Target, 'w')
fval_Target = open(valPath_Target, 'w')

ftrainval_Target_cnt = 0
ftest_Target_cnt = 0
ftrain_Target_cnt = 0
fval_Target_cnt = 0

for i in target_list:
    name = i[:-4] + '\n'
    if i in target_trainval_list:
        ftrainval_Target.write(name)
        ftrainval_Target_cnt += 1
        if i in target_train_list:
            ftrain_Target.write(name)
            ftrain_Target_cnt += 1
        else:
            fval_Target.write(name)
            fval_Target_cnt += 1
    else:
        ftest_Target.write(name)
        ftest_Target_cnt += 1

ftrainval_Source.close()
ftrain_Source.close()
fval_Source.close()
ftest_Source.close()

ftrainval_Target.close()
ftrain_Target.close()
fval_Target.close()
ftest_Target.close()
print("Source:")
print("trainval:", ftrainval_Source_cnt)
print("train:", ftrain_Source_cnt)
print("val:", fval_Source_cnt)
print("test:", ftest_Source_cnt)

print("Target:")
print("trainval:", ftrainval_Target_cnt)
print("train:", ftrain_Target_cnt)
print("val:", fval_Target_cnt)
print("test:", ftest_Target_cnt)
