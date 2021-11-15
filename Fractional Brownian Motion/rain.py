# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:31:38 2021

@author: zradlicz
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import time
import random as rand

def points_on_circumference(center, r, n):
    return [
        (
            center[0]+(math.cos(2 * math.pi / n * x) * r),  # x
            center[1] + (math.sin(2 * math.pi / n * x) * r)  # y

        ) for x in range(0, n + 1)]
        
def normalize(data):
    #data  = data - np.min(data)
    return (data - np.min(data)) / (np.max(data) - np.min(data))


class rain():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
        self.step = 1
        self.holding = 0
        self.eyes = np.array(points_on_circumference((self.x,self.y),self.step,4),dtype='int32')
        
    def sense(self):
        #num_pts = 1000
        #indices = np.arange(0, num_pts, dtype=float) + 5
        #r = np.sqrt(indices/num_pts)
        #theta = np.pi * (1 + 5**0.5) * indices
        
        
        self.eyes = np.array(points_on_circumference((self.x,self.y),self.step,4))
        
    def move(self,image):
        
        self.eyes = np.array(points_on_circumference((self.x,self.y),self.step,4),dtype='int32')
        
        
        new_image = np.copy(image)
        minx = self.eyes[0][0]
        miny = self.eyes[0][1]
        mini = image[minx,miny]
        for x,y in self.eyes:
            if np.all(image[x,y] < mini):
                mini = image[x,y]
                minx = x
                miny = y
        
        
        dif = abs(image[self.x,self.y] - image[minx,miny])
        self.speed = (dif[0]+dif[1]+dif[2])/3
        self.x = minx
        self.y = miny
        
#        if self.speed > .1:
#            self.holding += .1
#            new_image[self.x,self.y] = image[self.x,self.y] - .1
#        elif self.speed < .01:
#            self.holding -= .1
#            new_image[self.x,self.y] = image[self.x,self.y] + .1
#        else:
#            pass
        
    def draw(self,image):
        color = image[self.x,self.y]/1.05
        disp = cv2.circle(image,(self.x,self.y),3,color,-1)
        return disp
    
        
image = cv2.imread('noise.jpg')
image = image/255
particles = []
for i in range(1):
    particles.append( rain(rand.randrange(500,600,1),rand.randrange(500,600,1)) )

count = 0
for particle in particles:
    count+=1
    print(count)
    for i in range(10):
        particle.move(image)
        disp = particle.draw(image)
        
cv2.imshow('test',image)
        
    


    
        
        
    