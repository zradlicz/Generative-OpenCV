# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 10:21:58 2021

@author: zradlicz
"""

import cv2
import numpy as np
import math
def make_turtle(pattern):
    
    black = np.zeros((2000,2000,3))
    black = np.uint8(black)
    black = cv2.cvtColor(black,cv2.COLOR_BGR2HSV)
    pattern = cv2.cvtColor(pattern,cv2.COLOR_BGR2HSV)
    pattern = cv2.rotate(pattern, cv2.cv2.ROTATE_90_CLOCKWISE)
    bgcolor = pattern[0,0]
    turt_color = (bgcolor[0]+50,bgcolor[1],bgcolor[2])
    #cv2.circle(black,(1000,1100),700,(1,1,1),-1) #body
    #cv2.circle(black,(1000,160),150,(1,1,1),-1)
    cv2.ellipse(pattern, (1000,180), (120,140), 180, 0, 360, (int(turt_color[0]),int(turt_color[1]),int(turt_color[2])),-1) #head
    #cv2.ellipse(black,(1000,1700),(50,100),(1,1,1),1)
    
    xloc = 1000+700*math.cos(math.radians(55)) #back right leg
    yloc = 1000+700*math.sin(math.radians(55))
    cv2.ellipse(pattern, (int(xloc),int(yloc)), (100,200), -45, 0, 360, (int(turt_color[0]),int(turt_color[1]),int(turt_color[2])),-1)
    
    xloc = 1000+700*math.cos(math.radians(125)) #back left leg
    yloc = 1000+700*math.sin(math.radians(125))
    cv2.ellipse(pattern, (int(xloc),int(yloc)), (100,200), 45, 0, 360, (int(turt_color[0]),int(turt_color[1]),int(turt_color[2])),-1)
    
    xloc = 1000+800*math.cos(math.radians(-35)) #front right leg
    yloc = 1000+800*math.sin(math.radians(-35))
    cv2.ellipse(pattern, (int(xloc),int(yloc)), (100,350), -45, 0, 360, (int(turt_color[0]),int(turt_color[1]),int(turt_color[2])),-1)
    
    xloc = 1000+800*math.cos(math.radians(-145)) #front left leg
    yloc = 1000+800*math.sin(math.radians(-145))
    cv2.ellipse(pattern, (int(xloc),int(yloc)), (100,350), 45, 0, 360, (int(turt_color[0]),int(turt_color[1]),int(turt_color[2])),-1)
    
    cv2.circle(pattern,(1000,1000),700,(int(turt_color[0]),int(turt_color[1]),int(turt_color[2])-50),40) #spacing circle
    pattern = cv2.cvtColor(pattern,cv2.COLOR_HSV2BGR)
    return pattern

def natural_turtle(B, pattern):
    black = np.zeros((2000,2000,3))
    black = np.uint8(black)
    
    pattern = cv2.rotate(pattern, cv2.cv2.ROTATE_90_CLOCKWISE)
    pattern = cv2.resize(pattern, (500,500))
    imgray = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
    #ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)
    sorted_cnt = sorted(contours, key=cv2.contourArea, reverse=True)
    (x,y), r = cv2.minEnclosingCircle(sorted_cnt[1])
    #cv2.drawContours(black, sorted_cnt[1] ,-1, (255,255,255), 3)
    
    #cv2.circle(black,(int(y),int(x)),int(r),(255,255,255),-1) #body
    #cv2.circle(black,(1000,160),150,(1,1,1),-1)
    cv2.ellipse(black, (int(255-r),250), (28,24), 180, 0, 360, (255,255,255),-1) #head
    #cv2.ellipse(black,(1000,1700),(50,100),(1,1,1),1)
    
    yloc = 250+r*math.cos(math.radians(55)) #back right leg
    xloc = 250+r*math.sin(math.radians(55))
    cv2.ellipse(black, (int(xloc+30),int(yloc)), (15,35), -45, 0, 360, (255,255,255),-1)
    
    yloc = 250+r*math.cos(math.radians(125)) #back left leg
    xloc = 250+r*math.sin(math.radians(125))
    cv2.ellipse(black, (int(xloc+30),int(yloc)), (15,35), 45, 0, 360, (255,255,255),-1)
    
    yloc = 250+(r+10)*math.cos(math.radians(-35)) #front right leg
    xloc = 250+(r+10)*math.sin(math.radians(-35))
    cv2.ellipse(black, (int(xloc+30),int(yloc)), (15,65), -45, 0, 360, (255,255,255),-1)
    
    yloc = 250+(r+10)*math.cos(math.radians(-145)) #front left leg
    xloc = 250+(r+10)*math.sin(math.radians(-145))
    cv2.ellipse(black, (int(xloc+30),int(yloc)), (15,65), 45, 0, 360, (255,255,255),-1)
    #cv2.imshow('nemo',black)
    
    
    imgray = cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    black = np.zeros((500,500,3))
    black = np.uint8(black)
    cv2.drawContours(B, contours ,-1, (.75,.75,.75), 1)
    return B
    

#for num in range(100):
#    pat = cv2.imread('patterns_4/turtle_pattern_'+str(num)+'.png')
#    black = make_turtle(pat)
#    cv2.imwrite('turtles_2/turtle_'+str(num)+'.png',black)
#    #cv2.imshow('black',black)
    
#pat = cv2.imread('patterns_4/turtle_pattern_12.png')
#black = natural_turtle(B,pat)
#cv2.imwrite('turtles_2/turtle_'+str(num)+'.png',black)
#cv2.imshow('black',black)
