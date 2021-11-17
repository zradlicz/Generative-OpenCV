# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:35:52 2021

@author: Zach Radlicz
"""

import cv2
import numpy as np

HEIGHT = 500
WIDTH = 500

class mb():
    def __init__(self,rst,ren,ist,ien,MAX_ITER):
        self.rst = rst
        self.ren = ren
        self.ist = ist
        self.ien = ien
        self.MAX_ITER = MAX_ITER
        self.img = cv2.cvtColor(np.uint8(np.zeros((HEIGHT,WIDTH,3))),cv2.COLOR_BGR2HSV)
    def calc(self,c):
        z=0
        n=0
        while abs(z) <=2 and n < self.MAX_ITER:
            z = z**2 + c
            n+=1
        return n
    def draw(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                c = complex(self.rst + (x / WIDTH) * (self.ren - self.rst),
                            self.ist + (y / HEIGHT) * (self.ien - self.ist))
                m = self.calc(c)
                #color = 255 - int(m*255/MAX_ITER)
                h = int(255*m/self.MAX_ITER)
                #print(h)
                s = 255
                v = 255 if m < self.MAX_ITER else 0
                self.img[x,y] = [h,s,v]
        self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        return self.img
    def update(self,x1,x2,y1,y2,MAX_ITER):
        rst = self.rst
        ren = self.ren
        ist = self.ist
        ien = self.ien
        self.rst = rst+(x1/WIDTH)*(ren-rst)
        self.ren = rst+(x2/WIDTH)*(ren-rst)
        self.ist = ist+(y2/HEIGHT)*(ien-ist)
        self.ien = ist+(y1/HEIGHT)*(ien-ist)


refPt = []


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(y, x)]
        cropping = True
        print('point 1')
        print(refPt)

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((y, x))
        cropping = False
        
        print('point 2')
        print(refPt)
        print('updating')
        mandelbrot.update(refPt[0][0],refPt[1][0],refPt[0][1],refPt[1][1],mandelbrot.MAX_ITER)
        mandelbrot.draw()
        print('updated')

        # draw a rectangle around the region of interest
        #cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        #cv2.imshow("image", img)
    #if len(refPt) == 2:
        #img = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        
        
        #roi = plot()
        #img = cv2.resize(img,(HEIGHT,WIDTH))
        #cv2.imshow("image", img)
        #cv2.setMouseCallback('image', click_and_crop)
        #cv2.waitKey(0)
        
mandelbrot = mb(-2,1,-1,1,255)
mandelbrot.draw()
while True:
    
    cv2.imshow('mb',cv2.resize(mandelbrot.img,(1000,1000)))
    cv2.setMouseCallback('mb',click_and_crop)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
        