#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:08:29 2017

@author: wangs
"""

import numpy as np
import sys 

img = 'flower.jpg'
from cnn_feat_extract_fc7 import *
feat = cnn_feat_extract(img)

code_root = '/home/wangs/Work/Flower_CNN/'
ts_file_path = code_root + 'test.txt'

#生成liblinear数据格式的数据
with open(ts_file_path, 'w') as tsfile:      
    label = 0 #测试数据label默认设为0
    ts_svm_format = "%s "%(label)
    for k in range(4096):
        if feat[k] != 0:            
            ts_svm_format += "%d:%s "%((k+1), feat[k])
    ts_svm_format += "\n"
    tsfile.write(ts_svm_format)  
                
#用liblinear分类器分类
sys.path.insert(0, code_root+'liblinear/python')
from liblinearutil import *
m = load_model('heart_scale.model') 
yt, xt = svm_read_problem(ts_file_path)
p_labels, p_acc, p_vals = predict(yt, xt, m)
