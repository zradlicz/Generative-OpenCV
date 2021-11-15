# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:25:09 2021

@author: zradlicz
"""
import matplotlib.pyplot as plt

#from perlin_noise import PerlinNoise
#
#noise = PerlinNoise(octaves=10, seed=1)
#xpix, ypix = 1000, 1000
#pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
#
#plt.imshow(pic, cmap='gray')
#plt.show()

from fbm import FBM
import cv2

def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

#f = FBM(n=1024, hurst=0.75, length=1, method='daviesharte')
# or
f = FBM(2000, .9)

# Generate a fBm realization
fbm_sample_x = f.fbm()
fbm_sample_y = f.fbm()
sample = f.fbm()

# Generate a fGn realization
fgn_sample = f.fgn()

# Get the times associated with the fBm
t_values = f.times()

#new = np.reshape(sample, (-1, 200))

from mpl_toolkits import mplot3d
import numpy as np



x = np.outer(t_values,np.ones(2001))
y = x.copy().T
z = np.outer(fbm_sample_x, fbm_sample_y)



fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()

test = abs(z)
test = normalize(test)
test = cv2.resize(test,(2000,2000))
cv2.imshow('test',test)


xpix, ypix = 100, 100
pic = []
yoff = 0
for i in range(xpix):
    xoff = 0
    row = []
    for j in range(ypix):
        noise_val =         fbm_sample_x[i]
        noise_val += .01
        
        
        row.append(noise_val)
    pic.append(row)
    
pic = np.array(pic)
pic = normalize(pic)
pic = cv2.resize(pic,(2000,2000))
cv2.imshow('pic',pic)