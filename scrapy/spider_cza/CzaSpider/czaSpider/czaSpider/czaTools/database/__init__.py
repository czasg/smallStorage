# from czaSpider.czaTools import *
import numpy as np
import os

def get_data_for_img2num():
    trainingSet = [np.loadtxt(os.path.dirname(__file__) + os.sep +'img2num_value.txt'),]
    with open((os.path.dirname(__file__) + os.sep +'img2num_key.txt'),'r') as f_r:
        data = f_r.readline()
        hwLabels = [int(i) for i in data]
        trainingSet.append(hwLabels)
    return trainingSet