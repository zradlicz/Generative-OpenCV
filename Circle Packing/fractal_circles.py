# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:57:18 2022

@author: 32505
"""

import cv2
import math
import random as rand
import numpy as np

img = np.zeros((1000,1000))
cv2.namedWindow('test')

plugs = []
circles = []

class plug():
    def __init__(self,c1,c2,lr):
        self.c1 = c1
        self.c2 = c2
        self.lr = lr
        
    def new_circle(self,r):
        r1 = self.c1.r
        r2 = self.c2.r
        x1 = self.c1.x
        y1 = self.c1.y
        x2 = self.c2.x
        y2 = self.c2.y
        
        phi = math.atan2(y2-y1,x2-x1)
        try:
            theta = math.acos(((r+r1)**2+(r1+r2)**2-(r+r2)**2)/(2*(r+r1)*(r1+r2)))
        except:
            theta = .01
        
        
        if self.lr == 1:
            x = x1+(r+r1)*math.cos(phi+theta)
            y = y1+(r+r1)*math.sin(phi+theta)
            cnew = circle(x,y,r)
            if cnew.intersecting(circles):
                plugs.pop()
                return
            else: 
                circles.append(cnew)
                plugs.remove(self)
                plugs.append(plug(self.c1,cnew,1))
                plugs.append(plug(self.c1,cnew,0))
                plugs.append(plug(self.c2,cnew,1))
                plugs.append(plug(self.c2,cnew,0))
        else:
            x = x1+(r+r1)*math.cos(phi-theta)
            y = y1+(r+r1)*math.sin(phi-theta)
            cnew = circle(x,y,r)
            if cnew.intersecting(circles):
                plugs.pop()
                return
            else: 
                circles.append(cnew)
                plugs.remove(self)
                plugs.append(plug(self.c1,cnew,1))
                plugs.append(plug(self.c1,cnew,0))
                plugs.append(plug(self.c2,cnew,1))
                plugs.append(plug(self.c2,cnew,0))
        
                
        
        
        return circle(x,y,r)
    
        
        
class circle():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    
    def draw(self,img):
        cv2.circle(img,(int(self.x),int(self.y)),int(self.r),(1,1,1),1)
    
    def get_distance(self,x2,y2):
        return ((x2-self.x)**2+(y2-self.y)**2)**.5
    
    def intersecting(self,circles):
        flag = False
        for circle in circles:
            if self.x == circle.x and self.y == circle.y:
                flag = True
            elif abs(self.get_distance(circle.x,circle.y)) < self.r+circle.r:
                flag = True
        
        return flag
        
    

testc1 = circle(500,500,50)    
testc2 = circle(600,500,50)
testp1 = plug(testc1,testc2,0)
testp2 = plug(testc1,testc2,1)

circles = [testc1,testc2]
plugs = [testp1,testp2]

rstart = 50


while rstart>5:
    #plugi = rand.randrange(0,len(plugs),1)
    #plugs[plugi].new_circle(rstart)
    plugs[-1].new_circle(rstart)
    rstart-=.05

for circle in circles:
    circle.draw(img)


cv2.imshow('test',img)
key = cv2.waitKey(0)
     