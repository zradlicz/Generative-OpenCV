# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:10:09 2021

@author: zradlicz
"""

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import cv2
import numpy as np
from mpl_toolkits import mplot3d
import random as rand
import math

image = cv2.imread('noise1.jpg')
step = 50


def points_on_circumference(center, r, n):
    return [
        (
            center[0]+(math.cos(2 * math.pi / n * x) * r),  # x
            center[1] + (math.sin(2 * math.pi / n * x) * r)  # y

        ) for x in range(0, n + 1)]

class particle():
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.xprev = 0
        self.yprev = 0
        self.v = 1
        self.hold = 0
        self.eyes = [[self.x+rand.randrange(0,step,1),self.y],
                    [self.x+rand.randrange(0,step,1),self.y+rand.randrange(0,step,1)],
                    [self.x,self.y+rand.randrange(0,step,1)],
                    [self.x-rand.randrange(0,step,1),self.y],
                    [self.x-rand.randrange(0,step,1),self.y-rand.randrange(0,step,1)],
                    [self.x,self.y-rand.randrange(0,step,1)],
                    [self.x-rand.randrange(0,step,1),self.y+rand.randrange(0,step,1)],
                    [self.x+rand.randrange(0,step,1),self.y-rand.randrange(0,step,1)]]
        
        self.eyes = [[self.x+step,self.y],
                    [self.x+step,self.y+step],
                    [self.x,self.y+step],
                    [self.x-step,self.y],
                    [self.x-step,self.y-step],
                    [self.x,self.y-step],
                    [self.x-step,self.y+step],
                    [self.x+step,self.y-step]]
        
        self.eyes = np.array(points_on_circumference((self.x,self.y),step,10),dtype='int32')
        
    def grad_desc(self,image):
        minx = self.x
        miny = self.y
        mini = [255,255,255]
        #mini = image[minx,miny]
        
        for x,y in self.eyes:
            try:
                (image[x,y][0] < mini[0])
            except:
                break
            if (image[x,y][0] < mini[0] and x != self.xprev and y != self.yprev):
                mini = image[x,y]
                minx = x
                miny = y
        return minx,miny,mini
    
    def move(self,image):
        
        newx,newy,val = self.grad_desc(image)
        #diff = image[self.x,self.y] - image[newx,newy]
        #self.v = diff[0]/255
        #print(self.v)
        if (image[self.x,self.y][0]) > 25:
            num = image[self.x,self.y] /1.01
            num = int(num[0])
            image = cv2.circle(image,(self.y,self.x),1,(num,num,num),-1)
        else:
            image = cv2.circle(image,(self.y,self.x),3,(20,20,20),-1)
            newx = rand.randrange(0,2000,1)
            newy = rand.randrange(0,2000,1)
        
        
        self.xprev = np.copy(self.x)
        self.yprev = np.copy(self.y)
        self.x = newx
        self.y = newy
        
        self.eyes = [[self.x+step,self.y],
                    [self.x+step,self.y+step],
                    [self.x,self.y+step],
                    [self.x-step,self.y],
                    [self.x-step,self.y-step],
                    [self.x,self.y-step],
                    [self.x-step,self.y+step],
                    [self.x+step,self.y-step]]
        
        self.eyes = np.array(points_on_circumference((self.x,self.y),step,10),dtype='int32')
        
    def show(self,image):
        #image[self.x,self.y] = [255,255,255]
        #image[self.x,self.y] -= 20
        #print(self.x,self.y)
        cv2.imshow('rain',image)

for count in range(100):
    if count != 0:
        image = cv2.imread('rain.jpg')
    particles = []      
    for num in range(100):
        particles.append( particle(rand.randrange(0,2000,1),rand.randrange(0,2000,1)))
        #particles.append( particle(1000,1000))
    
    
    for test in particles:
        for i in range(10):
            test.move(image)
            
        
        
    cv2.imwrite('rain.jpg',image)
    print(count)
cv2.imshow('rain',image)


