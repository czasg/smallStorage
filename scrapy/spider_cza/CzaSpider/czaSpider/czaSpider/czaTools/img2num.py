from PIL import Image

from .database import get_data_for_img2num
from czaSpider.czaTools import *


class IMG(object):
    def __init__(self, pic):
        self.img = Image.open(pic)
        self.row = 0
        self.col = 0
        self.imgList = []

    def img2gsi(self, threshold):
        self.img = self.img.convert('L')
        coorData = self.img.load()
        self.row, self.col = self.img.size
        for x in range(self.row):
            for y in range(self.col):
                if coorData[x, y] > threshold:
                    coorData[x, y] = 1
                else:
                    coorData[x, y] = 0

    def splitImg(self, coor):
        _row, _col = coor
        list = []
        num = 0
        height = self.row // _row
        weight = self.col // _col
        for r in range(_row):
            for c in range(_col):
                box = (c * weight, r * height, (c + 1) * weight, (r + 1) * height)
                list.append(np.array(self.img.corp(box), 'f'))
                num += 1
        self.imgList = list

class KNN(object):
    def __init__(self, k=3):
        self.trainingSet = get_data_for_img2num()
        self.vector = None
        self.vector = []
        self.k = k

    def box2vector(self, box):
        row, col = np.shape(box)
        vector = np.zeros((1,row*col))
        count = 0
        for row in box:
            for gsi in row:
                vector[0, count] = gsi
                count += 1
        return vector

    def classify(self, dataSet=None, labels=None, k=None):


def img2num(picture, threshold=140, coor=(1, 10)):
    picture = IMG(picture)
    picture.img2gsi(threshold)
    picture.splitImg(coor)
    pass
