# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:38:35 2021

@author: zradlicz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import random as rand

WRITE_IMAGE = False

mask = cv2.imread('face.jpg')
    
mask = (mask/255.0)
locs = np.where(mask>=0.3) #this one is for completely random, where mask controls initial loc
#locs = np.where(mask==0) #this one is for strict b and w
locs = np.asarray(locs)
vals = np.arange(locs.shape[1])

blocs = np.where(mask<.2)
blocs = np.asarray(blocs)
bvals = np.arange(blocs.shape[1])



width = mask.shape[0]
height = mask.shape[1]
#width = 2000
#height = 2000
center = np.array([1000,1000])

class Ant():
    def __init__(self,species):
        
        
        
        self.direction = rand.randrange(0,360,1)
        self.species = species #white red blue
        if self.species == 'white':
            #self.location = np.array([rand.randrange(0,math.floor(height/3),1),rand.randrange(0,width,1)])
            #self.location = np.array([rand.randrange(math.floor(height/4),math.floor(3*height/4),1),rand.randrange(math.floor(width/4),math.floor(3*width/4),1)])
            #self.location = np.array([rand.randrange(math.floor(3*height/8),math.floor(5*height/8),1),rand.randrange(math.floor(3*width/8),math.floor(5*width/8),1)])
            #self.location = np.array([rand.randrange(0,length),rand.randrange(0,width)])
            #randnum = rand.randrange(0,locs.shape[1])
            randnum = np.random.choice(vals)
            #randnum = rand.choices(vals,rip)
            
            #print(randnum)
            self.location = np.array([locs[0][randnum],locs[1][randnum]])
        if self.species == 'blue':
            #self.location = np.array([rand.randrange(math.floor(height/3),math.floor(2*height/3),1),rand.randrange(0,width,1)])
            randnum = np.random.choice(bvals)
            #randnum = rand.choices(vals,rip)
            
            #print(randnum)
            self.location = np.array([blocs[0][randnum],blocs[1][randnum]])
        if self.species == 'red':
            self.location = np.array([rand.randrange(math.floor(2*height/3),height,1),rand.randrange(0,width,1)])
    
    def draw(self,image):
        if self.species == 'white':
            image = cv2.circle(image,(self.location[1],self.location[0]),3,(1,1,1),-1)
        if self.species == 'blue':
            image = cv2.circle(image,(self.location[1],self.location[0]),3,(1,0,0),-1)
        if self.species == 'red':
            image = cv2.circle(image,(self.location[1],self.location[0]),2,(0,0,1),-1)
        
        
    def move(self,image):
        locationleft = np.copy(self.location)
        locationleft[0] += 40*math.cos(math.radians(self.direction-45))
        locationleft[1] += 40*math.sin(math.radians(self.direction-45))
        
        
        locationright = np.copy(self.location)
        locationright[0] += 40*math.cos(math.radians(self.direction+45))
        locationright[1] += 40*math.sin(math.radians(self.direction+45))
        
        
        locationfront = np.copy(self.location)
        locationfront[0] += 40*math.cos(math.radians(self.direction))
        locationfront[1] += 40*math.sin(math.radians(self.direction))
      
        
        if locationleft[1] > height-1 or locationleft[0] > width-1 or locationfront[1] > height-1 or locationfront[0] > width-1 or locationright[1] > height-1 or locationright[0] > width-1:
            self.direction += 0
        else:
            if self.species == 'white':
                if image[locationfront[0],locationfront[1],1] > .5:
                    self.direction -= 0
                elif image[locationright[0],locationright[1],1] > .5:
                    self.direction += 45
                elif image[locationleft[0],locationleft[1],1] > .5:
                    self.direction -=45
                else:
                    self.direction += rand.randrange(-10,10,1)
            if self.species == 'blue':
                if image[locationfront[0],locationfront[1],0] > .9:
                    self.direction += 0
                elif image[locationright[0],locationright[1],0] > .9:
                    self.direction += 45
                elif image[locationleft[0],locationleft[1],0] > .9:
                    self.direction -= 45
                else:
                    self.direction += rand.randrange(-10,10,1)
            if self.species == 'red':
                if image[locationleft[1],locationleft[0],2] > .8:
                    self.direction -= 45
                elif image[locationright[1],locationright[0],2] > .8:
                    self.direction += 45
                elif image[locationfront[1],locationfront[0],2] > .8:
                    self.direction += 0
                else:
                    self.direction += rand.randrange(-5,5,1)
            
        
        self.location[0] += 5*math.cos(math.radians(self.direction))
        self.location[1] += 5*math.sin(math.radians(self.direction))
        if self.location[1] > height:
            self.location[1] = 0
        if self.location[1] < 0:
            self.location[1] = height
        if self.location[0] > width:
            self.location[0] = 0
        if self.location[0] < 0:
            self.location[0] = width
            
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = center[0]
        y2 = center[1]
        angle = math.degrees(math.atan2(y2-y1,x2-x1))
        if angle > self.direction:
            self.direction += 0
        else:
            self.direction -= 0
            
        
        
        


ants = []
white = 'white'
red = 'red'
blue = 'blue'

for num in range(5000):
    ants.append( Ant(white) )
    
for num in range(0):
    ants.append( Ant(blue) )
for num in range(0):
    ants.append( Ant(red) )
    
image = np.zeros([2000,2000,3])
image = np.copy(mask)


    
count = 0
while True:
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q') or key == 27:
                    cv2.destroyAllWindows()
                    break
    
    if key & 0xFF == ord('w'):
                    center[1]-=100
                    key=1
                    
    if key & 0xFF == ord('s'):
                    center[1]+=100
                    key=1
                    
    if key & 0xFF == ord('a'):
                    center[0]-=100
                    key=1
                    
    if key & 0xFF == ord('d'):
                    center[0]+=100
                    key=1
    

    
    for ant in ants:
        ant.move(image)
        ant.draw(image) 
    image[image>0]/=1.02

    
    
    
    image = cv2.circle(image,(center[0],center[1]),10,(1,1,1),-1)
    cv2.imshow('image',image)
    if WRITE_IMAGE:
        cv2.imwrite('mycelium_images/mycelium_frame_'+str(count).zfill(4)+'.jpg',image*255)
    print(count)
    count+=1

        
        