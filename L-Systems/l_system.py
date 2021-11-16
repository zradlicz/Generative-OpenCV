# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:56:12 2021

@author: Zach Radlicz
"""

from test import PerlinNoise
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random as rand
import math

def update(str):
    newstr = ''
    for char in str:
        if char == 'F':
            newstr += 'FF'
        elif char == 'X':
            newstr += 'F+[[-X]-X]-FL[-FXL]+XL'
        else:
            newstr+=char
    return newstr
        

class turt():
   
    def __init__(self,image):
        self.x = 500
        self.y = 1000
        self.angle = -90
        self.image = image
        self.store_x = []
        self.store_y = []
        self.store_angle = []
    
    def draw_forward(self,dist):
        newx = self.x+int(dist*math.cos(math.radians(self.angle)))
        newy = self.y+int(dist*math.sin(math.radians(self.angle)))
        cv2.line(self.image,(newx,newy),(self.x,self.y),(19/255,69/255,139/255),4)
        self.x+=int(dist*math.cos(math.radians(self.angle)))
        self.y+=int(dist*math.sin(math.radians(self.angle)))
    
    def draw_leaf(self):
        cv2.circle(self.image,(self.x,self.y),rand.randrange(3,15,1),(rand.randrange(0,50,1)/255,rand.randrange(90,180,1)/255,rand.randrange(0,50,1)/255),-1)
    
    def change_angle(self,angle):
        self.angle+=angle
    
    def store_loc(self):
        self.store_x.append(int(self.x))
        self.store_y.append(int(self.y))
        self.store_angle.append(self.angle)
    
    def go_to_stored(self):
        self.x = self.store_x.pop()
        self.y = self.store_y.pop()
        self.angle = self.store_angle.pop()


def interpret(string,turt):
    for char in string:
        if char == 'F':
            turt.draw_forward(3)
        if char == 'L':
            turt.draw_leaf()
        if char == '+':
            turt.change_angle(rand.randrange(10,45,1))
        if char == '-':
            turt.change_angle(rand.randrange(-45,-10,1))
        if char == '[':
            turt.store_loc()
        if char == ']':
            turt.go_to_stored()
            
black = np.ones((1000,1000,3))
drawer = turt(black)
instructions = 'X'

for num in range(7):
    instructions = update(instructions)

#instructions = 'F+[[X]-X]-F[-FX]+X'

interpret(instructions,drawer)

cv2.imshow('test',drawer.image)
    