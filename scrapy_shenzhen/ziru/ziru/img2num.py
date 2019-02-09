import os
from PIL import Image
import numpy as np
import operator

"""img2gsi"""
def img2gsi(img,threshold):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L") # 转灰度
    pixdata = img.load()
    w, h = img.size
    #threshold = 140 
    for x in range(w):
        for y in range(h):
            if pixdata[x, y] > threshold:
                pixdata[x, y] = 1
            else:
                pixdata[x, y] = 0
    return img



def splitImage(img, rownum, colnum):
    list = []
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                list.append(np.array(img.crop(box), 'f'))#.save(os.path.join(basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
        return list #切割之后，返回每一个图片的数组阵吗
    else:
        print('不合法的行列切割参数！')

def classify0(inX, dataSet, labels, k): # inX is values you want to match, dataSet is learning database
    dataSetSize = dataSet.shape[0]

    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet

    sqDiffMat = diffMat**2 
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5 # ((x-x)**2 + (x-x)**2)**0.5, remember it is still a array
    
    sortedDistIndicies = distances.argsort() # rerurn the array's index by reverse = False
    classCount = {} # define a dictionary
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),
    key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]#,sortedClassCount[0][1],sortedClassCount[1][0],sortedClassCount[1][1]




def img2vector(data):
    returnVect = np.zeros((1,900))
    #fr = open(filename)
    #print(fr)
    count = 0
    for row in data:#range(30):
        for gsi in row:#range(30):
            returnVect[0, count] = gsi#float(lineStr[j])
            count += 1
            
    return returnVect



def handwritingClassTest(testData):
    list = []
    trainingMat = np.loadtxt(os.path.join(os.getcwd(), 'cza_values.txt'))
    with open(os.path.join(os.getcwd(), 'cza_keys.txt'),'r') as f_r:
        data = f_r.readline()
        hwLabels = [int(i) for i in data]
        print('read db done')

    for data in testData:#range(mTest):
        vectorUnderTest = img2vector(data)#os.getcwd()+'\\test\\%s'%fileNameStr)

        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        list.append(classifierResult)
        print('trainingMat_resylt_is ', classifierResult)#,'real result is ',classNumStr)

    return list

"""this is a main"""
def img2num(picture): # input a picture name is ok
    img = Image.open(picture)
    img = img2gsi(img,140)
    testData = splitImage(img, 1, 10)
    print('start handel')
    result = handwritingClassTest(testData)
    return result # this is a list including picture2num

if __name__ == '__main__':
    img2num('123.png')
    img2num('456.png')