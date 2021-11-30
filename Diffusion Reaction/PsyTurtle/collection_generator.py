# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:56:29 2021

@author: zradlicz
"""

import math
import random as rand
import diffusion_reaction
import numpy as np
import cv2
import turtle_maker

seeds = [123]
#fs = [.1,.0367,.0545,.0695,.02]
#ks = [.055,.0649,.062,.0602,.049]
fs = [.022,.022,.02]
ks = [.049,.051,.049]

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


for seed in seeds:
    symmetric = False
    HEIGHT = 500
    WIDTH = 500

    A = np.ones((HEIGHT,WIDTH))
    B = np.zeros((HEIGHT,WIDTH))
    
    rand.seed(seed)
    num_iter = rand.randrange(900,901,1)
    num_pts = rand.randrange(1,12,1)
    if num_pts < 10:
        symmetric = True
    mag = rand.randrange(50,100,1)
    size = rand.randrange(10,30,1)
    ind = rand.randrange(0,len(fs),1)
    print(ind)
    if ind <4:
        symmetric = True
    color = rand.randrange(80,180,1)
    f = fs[ind]
    k = ks[ind]
    print(f)
    print(k)
    if symmetric:
        diffusion_reaction.seed_image_symmetric(B,num_pts,mag,size)
    else:
        diffusion_reaction.seed_image(B,num_pts,mag,size)
    
    for num in range(num_iter):
        if num == 850:
            color_img = diffusion_reaction.make_visual(A,B,color)
            B = turtle_maker.natural_turtle(B,color_img)
        A,B = diffusion_reaction.diff_react(A,B,f,k)
        print((num/num_iter)*100)
        disp = diffusion_reaction.make_visual(A,B,color)
        cv2.imshow('disp',disp)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
    disp = cv2.rotate(disp, cv2.cv2.ROTATE_90_CLOCKWISE)
    #cv2.imwrite('patterns_5/turtle_pattern_'+str(seed)+'.png',disp)


#Variables
#num pts 50-200
#mag
#size of circles
#f
#k
#
#

#make visual
#mask visual with body shape
#draw contours of legs and head
# draw outline circle