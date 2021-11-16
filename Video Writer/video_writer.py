# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:01:14 2021
@author: zradlicz
"""

import cv2
import numpy as np
import glob
 
img_array = []
for filename in sorted(glob.glob('C:/Users/zradlicz/Desktop/Misc Art/raytracing/cloud_images/*.jpg')):
    img = cv2.imread(filename)
    print(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('clouds.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
