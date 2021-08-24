

import pandas as pd
import json

jsonPath = "/home/jiawen/proj/da-faster-rcnn-PyTorch/data/VOCdevkit2007/VOC2007/new_json.json"
#读取json文件

with open(jsonPath,'r') as f: data=json.load(f)
#csvDir = fileDir[:-5]+"csv"


#json_data = pd.read_json(fileDir)

#json_data.to_csv('csvDir',index=False)

df = pd.DataFrame.from_dict(data, orient='index').T
df = df.stack()

print(df.head())




# my_title_layout = dict({"text":"my distribution", 'xanchor':'center', 'x':0.5, 'y':0.9, 'font':{'size':24}})
# my_xaxis_layout = dict(title=dict(text="my x axis", font={'size':16}))
# my_layout = dict(title=my_title_layout,
#                 xaxis= my_xaxis_layout)