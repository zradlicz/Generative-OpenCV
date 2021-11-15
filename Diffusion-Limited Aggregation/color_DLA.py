# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:41:27 2021

@author: zradlicz
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:27:29 2021

@author: zradlicz
"""

import cv2
import numpy as np
from mpl_toolkits import mplot3d
import random as rand
import math

image = np.zeros((2000,2000))
image = np.uint8(image)
#image = cv2.circle(image,(1000,1000),5,(1,1,1),-1)

color = cv2.imread('flower.jpg')
canim = cv2.Canny(color,150,255, L2gradient = True)
contours, hierarchy = cv2.findContours(canim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

b_w_image = cv2.drawContours(image, contours, -1, (255,255,255), 3)




#cv2.imshow('test',image)

def points_on_circumference(center, r, n):
    return [
        (
            center[0]+(math.cos(2 * math.pi / n * x) * r),  # x
            center[1] + (math.sin(2 * math.pi / n * x) * r)  # y

        ) for x in range(0, n + 1)]

class particle():
    def __init__(self,image):
        contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key=cv2.contourArea)
        #(x,y),radius = cv2.minEnclosingCircle(cnt)
        xr,yr,w,h = cv2.boundingRect(cnt)
        
        
        
#        self.xc = int(x) #
#        self.yc = int(y) #
#        self.r = int(radius) #
#        
#        self.mask = cv2.circle(np.copy(image),(self.xc,self.yc),self.r+5,(1,1,1),-1)   #
#        self.black_mask = cv2.circle(self.mask,(self.xc,self.yc),self.r,(0,0,0),-1)   #
#        
#        self.xes,self.yes = np.where(self.mask == 1)  #
#        self.xv,self.yv = np.where(self.mask == 1)      #
#        self.rando = rand.randrange(0,len(self.xes),1)  #
#        self.x = self.xes[self.rando]          #
#        self.y = self.yes[self.rando]          #
        
        
        self.rect_x = xr - 50
        self.rect_y = yr - 50
        self.rect_w = w + 100
        self.rect_h = h + 100
        
        self.rect_x_s = xr
        self.rect_y_s = yr
        self.rect_w_s = w
        self.rect_h_s = h
        
        
        self.x = rand.randrange(self.rect_x,self.rect_x+self.rect_w,1)
        self.y = rand.randrange(self.rect_y,self.rect_y+self.rect_h,1)
        
    def move(self):
        chance = rand.randrange(0,4,1)
        if chance == 0:
            if self.x > self.rect_x+self.rect_w:
                self.x = rand.randrange(self.rect_x,self.rect_x+self.rect_w,1)
                self.y = rand.randrange(self.rect_y,self.rect_y+self.rect_h,1)
            self.x+=1
        elif chance == 1:
            if self.x < self.rect_x:
                self.x = rand.randrange(self.rect_x,self.rect_x+self.rect_w,1)
                self.y = rand.randrange(self.rect_y,self.rect_y+self.rect_h,1)
            self.x-=1
        elif chance == 2:
            if self.y > self.rect_y+self.rect_h:
                self.x = rand.randrange(self.rect_x,self.rect_x+self.rect_w,1)
                self.y = rand.randrange(self.rect_y,self.rect_y+self.rect_h,1)
            self.y+=1
        elif chance == 3:
            if self.y < self.rect_y:
                self.x = rand.randrange(self.rect_x,self.rect_x+self.rect_w,1)
                self.y = rand.randrange(self.rect_y,self.rect_y+self.rect_h,1)
            self.y-=1
        
#        chance = rand.randrange(0,4,1)
#        if chance == 0:
#            if self.x not in self.xv or self.y not in self.yv:
#                self.rando = rand.randrange(0,len(self.xes),1)
#                self.x = self.xes[self.rando]
#                self.y = self.yes[self.rando]
#            self.x+=1
#        elif chance == 1:
#            if self.x not in self.xv or self.y not in self.yv:
#                self.rando = rand.randrange(0,len(self.xes),1)
#                self.x = self.xes[self.rando]
#                self.y = self.yes[self.rando]
#            self.x-=1
#        elif chance == 2:
#            if self.x not in self.xv or self.y not in self.yv:
#                self.rando = rand.randrange(0,len(self.xes),1)
#                self.x = self.xes[self.rando]
#                self.y = self.yes[self.rando]
#            self.y+=1
#        elif chance == 3:
#            if self.x not in self.xv or self.y not in self.yv:
#                self.rando = rand.randrange(0,len(self.xes),1)
#                self.x = self.xes[self.rando]
#                self.y = self.yes[self.rando]
#            self.y-=1
        
    
    def detect(self,image):
        
        contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key=cv2.contourArea)
        #(x,y),radius = cv2.minEnclosingCircle(cnt)
        xr,yr,w,h = cv2.boundingRect(cnt)
        
        self.rect_x = xr - 50
        self.rect_y = yr - 50
        self.rect_w = w + 100
        self.rect_h = h + 100
        
#        self.xc = int(x)  #
#        self.yc = int(y)   #
#        self.r = int(radius)   #
        
        
        flag = True
        while(flag):
            if image[self.x+1,self.y] == 1 or image[self.x-1,self.y] == 1 or image[self.x,self.y+1] == 1 or image[self.x,self.y-1] ==1:
                #image = cv2.circle(image,(self.x,self.y),5,(1,1,1),-1)
                image[self.x,self.y] = color[self.x,self.y]
                flag = False
            self.move()

count = 0
for num in range(1000000):
    test = particle(image)
    test.detect(image)
    print(num)
    #if num%200 == 0:
        #cv2.imwrite('DLA_images/DLA_frame_'+str(count).zfill(4)+'.jpg',image*255)
        #count+=1
cv2.imshow('show',image*255)
