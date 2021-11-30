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
def seed_image(B,num_pts,mag,size):
    indices = np.arange(0, num_pts, dtype=float) + .5
    
    r = np.sqrt(indices/num_pts)
    theta = np.pi * (1 + 5**0.5) * indices
    #points = (r*np.cos(theta),r*np.sin(theta))
    x = (mag*r*(np.cos(theta))+(WIDTH/2))
    y = (mag*r*(np.sin(theta))+(HEIGHT/2))
    
    for index in range(len(x)):
        cv2.circle(B,(int(x[index]),int(y[index])),size,(.5,.5,.5),-1)

def seed_image_symmetric(B,num_pts,mag,size):
    while 360%num_pts != 0:
        num_pts-=1
    theta = 0
    step = 360/(num_pts+1)
    
    while theta <= 360:
        print(theta)
        
        x = (mag*(np.cos(math.radians(theta)))+(WIDTH/2))
        y = (mag*(np.sin(math.radians(theta)))+(HEIGHT/2))
        cv2.circle(B,(int(x),int(y)),size,(.5,.5,.5),-1)
        theta+=step
        

#f = .1
#k = .055 #giraffe/voronoi

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



    

def laplacian(img):
    kernel = np.array([[.05,.2,.05],
                   [.2,-1,.2],
                   [.05,.2,.05]])
    return signal.convolve2d(img,kernel,boundary='symm',mode='same')
    
def diff_react(A,B,f,k):
    dt = 1
    Da = 1
    Db = .5
    lp_A = laplacian(A)
    lp_B = laplacian(B)
    new_A = A+((Da*lp_A)-(A*B*B)+(f*(1-A)))*dt
    new_B = B+((Db*lp_B)+(A*B*B)-((k+f)*B))*dt
    return new_A,new_B

def make_visual(A,B,num):
    
    black = np.zeros((HEIGHT,WIDTH,3))
    black = np.uint8(black)
    black = cv2.cvtColor(black,cv2.COLOR_BGR2HSV)
    black[:,:,0] = B*((num+80)-(num-80))+num-80
    black[:,:,1] = 200
    black[:,:,2] = 200
    black = np.uint8(black)
    black = cv2.cvtColor(black,cv2.COLOR_HSV2BGR)
    #black[A-B<thresh] = 1
    #return A-B
    black = cv2.resize(black,(2000,2000))
    return black

def rates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f[y,x],k[y,x])
    
        
#num = rand.randrange(80,180,1)
#
##for num in range(100):
#seed_image(B,200,400,1)
#count = 0
#while(True):
#    print(count)
#    A,B = diff_react(A,B,.0545,.062)
#    test = make_visual(A,B,num)
#    
#    cv2.imshow('test',test)
#    count+=1
#    cv2.setMouseCallback('test',rates)
#    key = cv2.waitKey(1)
#    if key & 0xFF == ord('q') or key == 27:
#                cv2.destroyAllWindows()
#                break