import scipy.io as sio
import sys
import math
import numpy as np
import matplotlib.pyplot as plt


def _knn_for_handwriting(xtr, ytr, xte, yte):

    def _calc_distance(x, xx):
        _sum = 0
        for i in range(len(x)):
            xi = x[i]
            xxi = xx[i]
            _sum += (xi - xxi) * (xi - xxi)
        return math.sqrt(_sum)

    def _find_min_distance_node(x, xtr, ytr):
        min_distance = sys.maxsize
        y = 0
        for i in range(len(xtr)):
            xx = xtr[i]
            yy = ytr[i]
            _distance = _calc_distance(x, xx)
            if _distance < min_distance:
                min_distance = _distance
                y = yy
        print(min_distance)
        return y[0]

    right_sample = 0
    for i in range(50):
        x = xte[i]
        y = yte[i][0]
        pre_y = _find_min_distance_node(x, xtr, ytr)
        if pre_y == y:
            right_sample += 1
        print(right_sample)
    print(right_sample)


if __name__ == "__main__":
    matfn = 'usps.mat'
    data = sio.loadmat(matfn)
    xtr = data['Xtr']
    ytr = data['Ytr']
    xte = data['Xte']
    yte = data['Yte']
    _knn_for_handwriting(xtr, ytr, xte, yte)

