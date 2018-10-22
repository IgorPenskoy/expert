# -*- coding: utf-8 -*-

import random

import numpy as np
import cv2
import matplotlib.pyplot as plt


def fcm(_img, c, q, alpha):

    plt.figure(1)

    # Вывод исходного изображения
    plt.imshow(cv2.cvtColor(_img, cv2.COLOR_GRAY2RGB))

    [row, column] = _img.shape
    n = _img.size
    U = []

    # Инициализировать случайными значениями принадлежность
    for i in range(c):
        temp = []
        for j in range(n):
            temp.append(random.random())
        U.append(temp)

    U = np.array(U, dtype=float)
    Un = U.copy()
    V = getV(_img, U, q)
    Un = getU(_img, V, q)

    t = 1

    while(np.sum(np.sum(np.abs(U - Un))) > alpha):
    
        V = getV(_img, Un, q)
        U = Un.copy()
        Un = getU(_img, V, q)
    
        print(t, np.sum(np.sum(np.abs(U - Un))))

        t += 1

    color = np.linspace(0, 255, c)

    plt.figure(2)

    # Массивы для рисования функций принадлежности
    X = [[] for x in range(c)]
    Y = [[] for x in range(c)]

    # Вычисление итогового кластера для каждой точки по наибольшей принадлежности
    for i in range(row):
        for j in range(column):
            l = np.argsort(Un[:, i * column + j])
            for k in range(c):
                X[k].append(_img[i][j])
                Y[k].append(Un[k][i * column + j])
            _img[i][j] = color[l[-1]]

    colours = "bgrkcym"

    # Рисование функций принадлежности
    for k in range(c):
        order = np.argsort(X[k])
        xs = np.array(X[k])[order]
        ys = np.array(Y[k])[order]
        plt.plot(xs, ys, colours[k])

    plt.figure(3)

    # Вывод кластеризованного изображения
    plt.imshow(cv2.cvtColor(_img, cv2.COLOR_GRAY2RGB))

    plt.show()

    return _img


# Вычислить центроид
def getV(_img, U, q):

    n = _img.size
    [row, colum] = _img.shape
    V = []
    
    for i, _ in enumerate(U):
        a = np.sum([u**q for u in U[i]])
        b = 0.0
        for j in range(row):
            for k in range(colum):
                b += ((U[i][j*colum+k])**q * _img[j][k])
        V.append(b / a)

    return V


# Вычислить принадлежность каждой точки к каждому кластеру
def getU(_img, V, q):

    c = len(V)
    [row, column] = _img.shape
    n = _img.size
    Un = np.zeros([c,n])

    for i in range(row):
        for j in range(column):
            for k in range(c):
                x = 0.0
                for l in range(c):
                    x += ((_img[i][j] - V[k]) / (_img[i][j] - V[l])) ** (2.0 / (q - 1.0))
                Un[k][i * column + j] = 1.0 / x
 
    return Un


if __name__ == '__main__':
    _img = cv2.imread('9.png', 0)
    fcm(_img, 3, 2, 0.01)
