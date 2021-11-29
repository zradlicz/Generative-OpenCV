# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:01:16 2021

@author: zradlicz
"""

import numpy as np
import cv2

input_h = 2000
input_w = 2000
output_w = 1400
output_h = 400
grid_x = 10
grid_y = 3
images = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,16,17,19,20,21,22,24,26,27,29,30,31,32,33,34,37]

black = np.zeros((output_h,output_w,3))

tile_size_x = int(output_w/grid_x)
tile_size_y = int(output_h/grid_y)

xiter = np.linspace(0,output_w-tile_size_x,grid_x,dtype=int)
yiter = np.linspace(0,output_h-tile_size_y,grid_y,dtype=int)
#print(xiter,yiter)



count = 0
for y in yiter:
    for x in xiter:
        img = cv2.imread('patterns_5/turtle_pattern_'+str(images[count])+'.png')
        img = cv2.resize(img,(tile_size_x,tile_size_y))
        #print(x,y)
        black[y:(y+tile_size_y),x:(x+tile_size_x)] = img/255
        cv2.imshow('black',black)
        count+=1
        

