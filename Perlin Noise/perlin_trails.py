# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 07:19:25 2021

@author: Zach Radlicz
"""

from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random as rand
import math

WRITE_IMAGE = True

HEIGHT = 1000
WIDTH = 1000
seed = rand.randrange(0,1000,1)
print(seed)
noise = PerlinNoise(octaves=2, seed=seed)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
pic = np.array(pic)
pic = pic+(np.min(pic)*-1)
pic = cv2.resize(pic,(HEIGHT,WIDTH))
pic = cv2.merge((pic,pic,pic))
#cv2.imshow('raw',pic)

gX = cv2.Sobel(pic, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(pic, cv2.CV_64F, 0, 1)

magnitude = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

#cv2.imshow('mag',magnitude)
#cv2.imshow('orientation',orientation)



class particle():
    def __init__(self):
        self.x = rand.randrange(0,HEIGHT,1)
        self.y = rand.randrange(0,WIDTH,1)
        self.vx = 1
        self.vy = 1
        self.size = 10
        self.m = 1
    def move(self,pic,magnitude,orientation):
        
        
        mag = magnitude[self.x,self.y]
        ori = orientation[self.x,self.y]
        
        self.vx=100*mag[0]*math.cos(math.radians(ori[0]))
        self.vy=100*mag[0]*math.sin(math.radians(ori[0]))
        
        #mag = magnitude[part.x,part.y]
        #ori = orientation[part.x,part.y]
        if(self.x+int(self.vx) >= HEIGHT):
            self.xprev = int(self.x)
            #self.x+=(-HEIGHT+1)+int(self.vx)
        elif(self.x+int(self.vx) <= 0):
            self.xprev = int(self.x)
            #self.x+=(HEIGHT-1)+int(self.vx)
        else:
            self.xprev = int(self.x)
            self.x+=int(self.vx)
            
        if(self.y+int(self.vy) >= WIDTH):
            self.yprev = int(self.y)
            #self.y+=(-WIDTH+1)+int(self.vy)
        elif(self.y+int(self.vy) <= 0):
            self.yprev = int(self.y)
            #self.y+=(WIDTH-1)+int(self.vy)
        else:
            self.yprev = int(self.y)
            self.y+=int(self.vy)
            
        self.size=pic[self.x,self.y][0]
        #self.vx+=100*mag[0]*math.cos(math.radians(ori[0]))/self.m
        #self.vy+=100*mag[0]*math.sin(math.radians(ori[0]))/self.m
        
    def plot(self,image):
        #image = cv2.circle(image,(self.x,self.y),self.size,(255,255,255),-1)
        image = cv2.line(image,(self.xprev,self.yprev),(self.x,self.y),(abs(self.size*.1*(seed%58)),abs(self.size*.1*(seed%33)),abs(self.size*.1*(seed%39)),1))
        return image
    
    
parts = []
black = np.zeros((HEIGHT,WIDTH,3))
    
for num in range(500):
    parts.append(particle())

#for part in parts:
    #black = part.plot(black)
    
for num in range(1000):
    for part in parts:
        part.move(pic,magnitude,orientation)
        black = part.plot(black)
        
cv2.imshow('test',black)
if WRITE_IMAGE:
    cv2.imwrite('perlin_trail_'+str(seed)+'.png',black*255)
