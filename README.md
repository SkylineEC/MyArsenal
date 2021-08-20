# Some Useful Python Scripts for Dataset

The scripts inside are suitable for converting bdd100k datasets to voc format

Convenient for format checking, batching operations (renaming, etc.)

- ***This is the first step for converting bdd100k to voc, we need to operate the json file to xml file***

MyArsenal/make_voc_dataset/bd100k_to_xml.py

- ***This is the second step to make the voc dataset, we need to rename the xml because the standard image name fomat of pascaal_voc has 6 digits***

proj/MyArsenal/make_voc_dataset/change_name.py

- ***Find a specific category of images and store them in a new path***

proj/MyArsenal/make_voc_dataset/find_category.py

- ***Make train.txt / val.txt / trainval.txt / test.txt under main directory***

proj/MyArsenal/make_voc_dataset/make_train_val_test_set.py

- ***visualize the code of VOC Dataset***

proj/MyArsenal/make_voc_dataset/visual_dataset_voc.py

VOC Fomat

└─VOC2007
    ├─JPEGImages
    │  ├─1.jpg
    │  ├─2.jpg
    │  └─3.jpg
    ├─Annotations
    │  ├─1.xml
    │  ├─2.xml
    │  └─3.xml
    ├─ImageSets
    │  ├─Layout
    │  │  ├─train.txt
    │  │  ├─trainva.txt
    │  │  ├─test.txt
    │  │  └─val.txt
    │  ├─Main
    │  │  ├─*_train.txt
    │  │  ├─*_trainva.txt
    │  │  ├─*_test.txt
    │  │  └─*_val.txt
    │  ├─Action
    │  │  ├─*_train.txt
    │  │  ├─*_trainva.txt
    │  │  ├─*_test.txt
    │  │  └─*_val.txt
    │  └─Segmentation
    │     ├─train.txt
    │     ├─trainva.txt
    │     ├─test.txt
    │     └─val.txt
    ├─SegmentationClass
    └─SegmentationObject
    
    
    
    ─coco2017
    ├─annotations
    │  ├─instances_train2017.json
    │  ├─instances_val2017.json
    │  └─*.json
    ├─train2017
    │  ├─1.jpg
    │  ├─2.jpg
    │  └─3.jpg
    ├─val2017
    │  ├─4.jpg
    │  ├─5.jpg
    │  └─6.jpg
    ├─test2017
    │  ├─7.jpg
    │  ├─8.jpg
    │  └─9.xml
    └─unlabeled2017
