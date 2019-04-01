from czaSpider.czaTools import *


def get_data_for_img2num():
    trainingSet = [np.loadtxt('img2num_value.txt'),]
    with open('img2num_key.txt','r') as f_r:
        data = f_r.readline()
        hwLabels = [int(i) for i in data]
        trainingSet.append(hwLabels)
    return trainingSet