# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 06:31:19 2021

@author: Zach Radlicz
"""

from test import PerlinNoise
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random as rand
import math

black = (0,0,0)
blue = (245, 69, 66)
light_blue = (245, 221, 66)
green = (25, 97, 30)
light_green = (65, 232, 77)
red = (14, 14, 240)
pink = (234, 92, 250)
purple = (247, 72, 195)
orange = (53, 157, 242)
#colors = [black, blue, light_blue, green, light_green, red, pink, purple, orange]
colors = [red, orange, pink, light_green, green, light_blue, blue, purple, black]

HEIGHT = 2000
WIDTH = 2000
seed = rand.randrange(0,100,1)
print(seed)
noise = PerlinNoise(octaves=3, seed=seed)
xpix, ypix = 500, 500
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
pic = np.array(pic)
pic = pic+(np.min(pic)*-1)
pic = cv2.resize(pic,(HEIGHT,WIDTH))
pic = cv2.merge((pic,pic,pic))

cv2.imshow('raw',pic)

black = np.zeros_like(pic)
step = .015
thresh = .002
count = 0
for val in np.arange(np.min(pic),np.max(pic),step):
    black[(abs(pic-val)<thresh).all(axis=2)]=np.array(colors[count%9])/255
    count+=1
    
    
    

cv2.imshow('cont',black)
