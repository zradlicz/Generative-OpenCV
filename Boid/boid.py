# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:16:51 2021

@author: zradlicz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time

WRITE_IMAGES = False #Change this to true if you want to save frames to create an animation
LENGTH = 1000 #This value is the length of the animation


height = 2000
width = 2000

class Boid():
    def __init__(self,x,y,direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        
        
    def sense(self):
        #num_pts = 1000
        #indices = np.arange(0, num_pts, dtype=float) + 5
        #r = np.sqrt(indices/num_pts)
        #theta = np.pi * (1 + 5**0.5) * indices
        
        
        self.eyes = np.array([[]])
        eyel = np.array([self.x + int(20*math.cos(math.radians(self.direction-90))),self.y + int(20*math.sin(math.radians(self.direction-90)))])
        eyer = np.array([self.x + int(20*math.cos(math.radians(self.direction+90))),self.y + int(20*math.sin(math.radians(self.direction+90)))])
        eyef = np.array([self.x + int(50*math.cos(math.radians(self.direction))),self.y + int(50*math.sin(math.radians(self.direction)))])
        self.eyes = np.int32(np.append(self.eyes,eyel))
        self.eyes = np.int32(np.append(self.eyes,eyer))
        self.eyes = np.int32(np.append(self.eyes,eyef))
    
        pass
    
    def direct(self,image):
        sum = 0
        sumx = 0
        sumy = 0
        count = .00001
        for boid in boids:
            if boid.x < self.x + 100 and boid.y < self.y + 100 and boid.x > self.x - 100 and boid.y > self.y - 100:
                count+=1
                sum += boid.direction
                sumx += boid.x
                sumy += boid.y
            avg_direction = sum/count
            avgx = sumx/count
            avgy = sumy/count
        
        if np.any(self.eyes > height-1):
            self.direction+=1
            pass
        else:
            
            if np.all(image[self.eyes[5],self.eyes[4]] > .9):
                self.direction -= 85
                pass
            else:
                self.direction += rand.randrange(-25,26,1)
                #print('random')
                pass
            if np.all(image[self.eyes[3],self.eyes[2]]  > .9):
                self.direction += 45
                #print('left')
            else:
                pass
                #self.direction -= 5
            if np.all(image[self.eyes[1],self.eyes[0]] > .9):
                self.direction -=45
                #print('right')
            else:
                #self.direction += 5
                pass
        if self.direction > avg_direction:
            self.direction -= 10
        else:
            self.direction += 10
            
        x1 = self.x
        y1 = self.y
        x2 = avgx
        y2 = avgy
        #print(avgx)
        #print(avgy)
        angle = math.degrees(math.atan2(y2-y1,x2-x1))
        if angle > self.direction:
            self.direction += 2
        else:
            self.direction -= 2
        
        
        
        if self.direction > 360:
            self.direction -= 360
            
        #print(self.direction)
        
    
    def move(self):
        self.x += int(5*math.cos(math.radians(self.direction)))
        self.y += int(5*math.sin(math.radians(self.direction)))
        
        if self.x > height:
            self.x = 0
        if self.x < 0:
            self.x = height
        if self.y > width:
            self.y = 0
        if self.y < 0:
            self.y = width
    
    
    
    
    def draw(self,image):
        image = cv2.circle(image,(self.x,self.y),8,(1,1,1),-1)
        #image = cv2.circle(image,(self.eyes[0],self.eyes[1]),3,(0,1,1),-1)
        #image = cv2.circle(image,(self.eyes[2],self.eyes[3]),3,(1,1,0),-1)
        #image = cv2.circle(image,(self.eyes[4],self.eyes[5]),3,(1,0,1),-1)
        
image = np.zeros((height,width,3))
#test = Boid(500,500,30)

boids = []

for num in range(500):
    
    x = rand.randrange(0,height,1)
    y = rand.randrange(0,width,1)
    direction = rand.randrange(0,360,1)
    boids.append( Boid(x,y,direction) )


count = 0
while count < LENGTH:
    image[image>0]/=1.5
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q') or key == 27:
                    cv2.destroyAllWindows()
                    break
    for boid in boids:
        boid.sense()
        boid.direct(image)
        boid.move()
        boid.draw(image)
    cv2.imshow('image',image)
    if WRITE_IMAGES:
        cv2.imwrite('boid_images/boid_frame_'+str(count).zfill(4)+'.jpg',image*255)
    
    count+=1
    print(count)
    

    
    
        
    
        
