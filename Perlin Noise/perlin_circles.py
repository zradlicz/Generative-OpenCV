# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:07:15 2021

@author: Zach Radlicz
"""

from test import PerlinNoise
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random as rand
import math

HEIGHT = 500
WIDTH = 500
seed = rand.randrange(0,1000,1)
print(seed)
noise = PerlinNoise(octaves=5, seed=seed)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
pic = np.array(pic)

pic = cv2.resize(pic,(HEIGHT,WIDTH))
pic = cv2.merge((pic,pic,pic))
cv2.imshow('raw',pic)



gX = cv2.Sobel(pic, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(pic, cv2.CV_64F, 0, 1)

magnitude = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

cv2.imshow('mag',magnitude)
cv2.imshow('orientation',orientation)

class particle():
   
    def __init__(self,image):
        self.x = rand.randrange(0,HEIGHT,1)
        self.y = rand.randrange(0,WIDTH,1)
        self.size = image[self.x,self.y][0]
    
    def move(self,image,mag,ori):
        self.x+=int(70*mag[self.x,self.y][0]*math.cos(ori[self.x,self.y][0]))
        self.y+=int(70*mag[self.x,self.y][0]*math.sin(ori[self.x,self.y][0]))
        #self.x+=40
        #self.y+=40
        #self.size=image[self.x,self.y][0]
        self.size-=.001
    
    def plot(self,image):
        image = cv2.circle(image,(self.x,self.y),int(abs(self.size*10))+3,(abs(self.size*(seed%13)),abs(self.size*(seed%11)),abs(self.size*(seed%39))),2)
        return image
        #return cv2.circle(image,(self.x,self.y),int(abs(self.size*10)),(abs(self.size*8),abs(self.size*1),abs(self.size*2)),-1)

parts = []
black = np.zeros((HEIGHT,WIDTH,3))

for num in range(10000):
    parts.append(particle(pic))

#for part in parts:
    #black = part.plot(black)
    
for num in range(100):
    for part in parts:
        try:
            part.move(pic,magnitude,orientation)
        except:
            pass
        black = part.plot(black)





cv2.imshow('test',black)