import os
import numpy as np 
import json
import pdb 

path = '/home/wangxiao/Documents/rgb_event_tracking_benchmark/rtmdnet-visEvent-tracking-baseline/visEvent_dataset/test_subset/' 
files = os.listdir(path) 


for vid in range(len(files)): 
    jsonPath = path + files[vid] + '/json/'
    jsonfiles = os.listdir(jsonPath) 
    
    fid = open(path + files[vid] + '/groundtruth.txt', 'w') 

    for jsonID in range(len(jsonfiles)): 
        eachJsonfile = jsonPath + jsonfiles[jsonID] 

        file = open(eachJsonfile, 'r', encoding='utf-8')
        anno = json.load(file) 
        print("==>> Processing video: ", files[vid], ' ImgIDX: ', jsonID)  
        # pdb.set_trace() 

        x1 = anno['bbox'][0]['top']
        y1 = anno['bbox'][0]['left']
        x2 = anno['bbox'][0]['bottom']
        y2 = anno['bbox'][0]['right']  

        width  = x2 - x1 
        height = y2 - y1 

        fid.write(str(x1))
        fid.write(',')
        fid.write(str(y1))
        fid.write(',')
        fid.write(str(width))
        fid.write(',')
        fid.write(str(height)) 
        fid.write('\n')

    fid.close()