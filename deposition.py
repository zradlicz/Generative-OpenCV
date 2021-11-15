# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:58:02 2021

@author: zradlicz
"""

import matplotlib.pyplot as plt

import cv2
import numpy as np
from mpl_toolkits import mplot3d
import random as rand
import math

def points_on_circumference(center, r, n):
    return [
        (
            center[0]+(math.cos(2 * math.pi / n * x) * r),  # x
            center[1] + (math.sin(2 * math.pi / n * x) * r)  # y

        ) for x in range(0, n + 1)]

class particle():
    def __init__(self):
        self.points = points_on_circumference((1000,1000),50,100)
        self.x,self.y = self.points[rand.randrange(0,99,1)]
        self.x = int(self.x)
        self.y = int(self.y)
    def move(self):
        chance = rand.randrange(0,3,1)
        if chance == 0:
            if self.x == 1998:
                self.x = 0
            self.x+=1
        elif chance == 1:
            if self.x == 0:
                self.x = 1998
            self.x-=1
        elif chance == 2:
            if self.y == 1998:
                self.y = 0
            self.y+=1
        elif chance == 3:
            if self.y == 0:
                self.y = 1998
            self.y-=1
    def detect(self,image):
        flag = True
        while(flag):
            if image[self.x+1,self.y] == 1 or image[self.x-1,self.y] == 1 or image[self.x,self.y+1] == 1 or image[self.x,self.y-1] ==1:
                image = cv2.circle(image,(self.x,self.y),2,(1,1,1),-1)
                flag = False
            self.move()
        
    
start = np.zeros((2000,2000))
start = cv2.circle(start,(1000,1000),10,(1,1,1),-1)
start[1000,1000] = 1

for num in range(1000):
    test = particle()
    test.detect(start)
    print(num)
cv2.imshow('show',start)


        
        