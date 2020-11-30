import tkitFile
import tkitText
# from config import *
from tqdm import tqdm
import time
import numpy as np   
import math
import os

def _read_data( input_file):
    """Reads a BIO data."""
    max_length=480
    # num=max_length #定义每组包含的元素个数
    with open(input_file) as f:
        datas = []
        words = []
        labels = []
        # stop = ["。","!","！"]
        stop=[]
        one=[]
        for line in f:
            # print(line)
            contends = line.strip()
            
            # print(len(line.strip().split(' ')))
            word = line.strip().split(' ')[0]
            label = line.strip().split(' ')[-1]
            if word=='':
                # continue
                if len(one)>0:
                    datas.append(one)
                one=[]
            else:
                # print((word,label))
                one.append((word,label))
                

            if contends.startswith("-DOCSTART-"):
                words.append('')
                continue
        if len(one)>0:
            datas.append(one)
        return datas

def load_pre(file="data.txt",save_data="save_data.txt"):
    """
    加载之前数据
    """
    with open(file) as f:
        lines = f.read()
        # print(type(lines))
        # print(lines)
    with open(save_data,'w',encoding = 'utf-8') as f1:
        f1.write(lines)
        f1.write("\n")
        f1.write("\n")

def save_data(data,file="data.txt"):
    """
    构建数据保存
    """
    with open(file,'a+',encoding = 'utf-8') as f1:
        for it in data:
            for w,m in it:
                # print(m,w)
                f1.write(w+" "+m+"\n")
            # print("end\n\n\n\n")
            f1.write("\n")


def save_labels(data,file="labels.txt"):
    """
    构建数据保存
    """
    labels={}
    if os.path.exists(file):
        print(file,"已经存在！")
    else:
        with open(file,'w',encoding = 'utf-8') as f1:
            for it in data:
                for w,m in it:
                    labels[m]=1
                    # print(m,w)
            keys=[]
            for key in labels.keys():
                keys.append(key)
            f1.write("\n".join(keys))


# data_path='../data'
data_path=input("Data Path:")
if data_path:
    pass
else:
    data_path="/home/t/dev/auto-translation-plan/clear-content-marker/data/"
ttf=tkitFile.File()
tt=tkitText.Text()
data=[]
anns=[]
bad=0
good=0
bad_files=[]
for f_path in ttf.all_path(data_path):
    # print(f_path)
    if f_path.endswith(".anns"):
        # print(f_path)
        anns.append(f_path)
        # print(_read_data(f_path))
        one_data=_read_data(f_path)
        # print(one_data)
        if  len(one_data)==0:
            print("no")
        data=data+one_data
 

 
c=int(len(data)*0.7)
b=int(len(data)*0.85)
print(len(data))


train_data=data[:c]
dev_data=data[c:b]
test_data=data[b:]

ttf=tkitFile.File()
ttf.mkdir("../output")


# load_pre('../data/data/train.txt',"../output/train.txt")
# load_pre('../data/data/dev.txt',"../output/dev.txt")
# load_pre('../data/data/test.txt',"../output/test.txt")
save_data(train_data,file="../output/train.txt")
save_data(dev_data,file="../output/dev.txt")
save_data(test_data,file="../output/test.txt")



# #一般无需重新生成labels文件
save_labels(data,"../output/labels.txt")

