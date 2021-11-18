# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:39:44 2021

@author: Zach Radlicz
"""

from scipy import signal
from scipy import misc
import numpy as np
import math
import random as rand
import cv2

HEIGHT = 500
WIDTH = 500

A = np.ones((HEIGHT,WIDTH))
B = np.zeros((HEIGHT,WIDTH))
#for num in range(10):
    #B[rand.randrange(0,HEIGHT,1),rand.randrange(0,WIDTH,1)] = 1
    #cv2.circle(B,(rand.randrange(0,HEIGHT,1),rand.randrange(0,WIDTH,1)),1,(1,1,1),-1)
# cv2.circle(B,(450,500),1,(1,1,1),-1)
# cv2.circle(B,(550,500),1,(1,1,1),-1)
# cv2.circle(B,(500,450),1,(1,1,1),-1)
# cv2.circle(B,(500,550),1,(1,1,1),-1)
# cv2.circle(B,(500,500),1,(1,1,1),-1)

# cv2.circle(B,(225,250),10,(1,1,1),-1)
# cv2.circle(B,(275,250),10,(1,1,1),-1)
# cv2.circle(B,(250,225),10,(1,1,1),-1)
# cv2.circle(B,(250,275),10,(1,1,1),-1)
# cv2.circle(B,(250,250),10,(1,1,1),-1)

num_pts = 100
indices = np.arange(0, num_pts, dtype=float) + .5

r = np.sqrt(indices/num_pts)
theta = np.pi * (1 + 5**0.5) * indices
#points = (r*np.cos(theta),r*np.sin(theta))
x = ((WIDTH/3)*r*(np.cos(theta))+(WIDTH/2))
y = ((HEIGHT/3)*r*(np.sin(theta))+(HEIGHT/2))

for index in range(len(x)):
    cv2.circle(B,(int(x[index]),int(y[index])),1,(1,1,1),-1)

Da = 1.
Db = .5


f = .1
k = .055 #giraffe/voronoi

#f = .094
#k = .056  #loopy voronoi

# f = .0367
# k = .0649 #mitosis

#f = .0545
#k = .062 #brain

#f = .0695
#k = .0602 #mix between brain and voronoi

#f =.022
#k = .049 #cool

#f=.022
#k=.051 #another cool

#f = .02
#k = .049 #kinda crazy spirals, insane coolness make sure to use 1000x1000

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T
    
#f = get_gradient_2d(.01,.1,WIDTH,HEIGHT,False) #pattern map
#k = get_gradient_2d(.055,.07,WIDTH,HEIGHT,True)

#x_axis = np.linspace(-.3, .3, WIDTH)
#y_axis = np.linspace(-.3, .3, HEIGHT)

#xx, yy = np.meshgrid(x_axis, y_axis)
#arr = np.sqrt((xx) ** 2 + (yy) ** 2)
#f = np.copy(arr)

#x_axis = np.linspace(-.07, .07, WIDTH)
#y_axis = np.linspace(-.07, .07, HEIGHT)

#xx, yy = np.meshgrid(x_axis, y_axis)
#arr = np.sqrt((xx) ** 2 + (yy) ** 2)

#k = np.copy(arr)


dt = 1
kernel = np.array([[.05,.2,.05],
                   [.2,-1,.2],
                   [.05,.2,.05]])

    

def laplacian(img,kernel):
    return signal.convolve2d(img,kernel,boundary='symm',mode='same')
    
def diff_react(A,B):
    lp_A = laplacian(A,kernel)
    lp_B = laplacian(B,kernel)
    new_A = A+((Da*lp_A)-(A*B*B)+(f*(1-A)))*dt
    new_B = B+((Db*lp_B)+(A*B*B)-((k+f)*B))*dt
    return new_A,new_B

def make_visual(A,B,num):
    color_grad = get_gradient_2d(rand.randrange(0,157,1)/255,rand.randrange(158,255,1)/255,WIDTH,HEIGHT,False)
    thresh = .1
    black = np.zeros((HEIGHT,WIDTH,3))
    #black[:,:,0] = abs(A-1)/rand.randrange(1,8,1)
    #black[:,:,1] = B/rand.randrange(1,8,1)
    #black[:,:,2] = color_grad/rand.randrange(1,8,1)
    
    black[:,:,0] = B
    black[:,:,1] = num
    black[:,:,2] = A
    
    #black[A-B<thresh] = 1
    #return A-B
    return black

def rates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f[y,x],k[y,x])
    
        
num = rand.randrange(0,255,1)/255

#for num in range(100):
while(True):
    A,B = diff_react(A,B)
    #test = make_visual(A,B,num)
    test = cv2.resize(B,(1000,1000))
    cv2.imshow('test',test)
    cv2.setMouseCallback('test',rates)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
            
