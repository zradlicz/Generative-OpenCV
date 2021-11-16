import cv2
import math
import numpy as np
import random as rand

HEIGHT = 1000
WIDTH = 1000
MAX_R = 25

img = np.zeros((WIDTH,HEIGHT,3))

class circle():
    def __init__(self,mask):
        self.mask = mask
        poss = np.where(mask==0)
        ind = rand.randrange(0,len(poss[0]),1)
        self.x = poss[1][ind]
        self.y = poss[0][ind]
        #self.x = rand.randrange(0,WIDTH,1)
        #self.y = rand.randrange(0,HEIGHT,1)
        self.r = 1
        self.expanding = True
    def draw(self,img):
        cv2.circle(img,(self.x,self.y),self.r,(1,1,1),1)
        
    def expand(self):
        self.r+=1
        cv2.circle(self.mask,(self.x,self.y),self.r,(1,1,1),-1)
        if self.r > MAX_R:
            self.expanding = False
    def get_distance(self,x2,y2):
        return ((x2-self.x)**2+(y2-self.y)**2)**.5
    def check_intersection(self,circles):
        flag = False
        for circle in circles:
            if self.x == circle.x and self.y == circle.y:
                flag = False
            elif abs(self.get_distance(circle.x,circle.y)) < self.r+circle.r:
                flag = True
        #print(not flag)
        self.expanding = not flag
        

# circles = []
# for num in range(100):
#     circles.append( circle() )
    

# for num in range(100):
#     for circle in circles:
        
#         intersection = circle.check_intersection(circles)
#         print(intersection)
#         if not intersection:
#             circle.expand()
#             circle.draw(img)
#     cv2.imshow('circles',img)
#     key = cv2.waitKey(1)
#     if key & 0xFF == ord('q') or key == 27:
#         cv2.destroyAllWindows()
#         break
black = np.zeros((WIDTH,HEIGHT,3))
circles = []
for num in range(1000):
    circ = circle(black)
    while circ.expanding:
        circ.check_intersection(circles)
        circ.expand()
    circles.append(circ)
    
    
for circle in circles:
    circle.draw(img)
    

            
cv2.imshow('circles',img)