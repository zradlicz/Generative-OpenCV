# Generative-OpenCV
My first experiments with generative art and creative coding. Every project is done using OpenCV as a drawing canvas, intended to improve my image processing skills. I aim to learn p5.js next and integrate some of these ideas into a comprehensive website at some point. I was just already familiar with OpenCV from previous projects. Code should be easy to use in your own IDE after installing these packages.

`pip install opencv-python`  
`pip install perlin-noise`



## Folder Layout
Folder | Contents
------------ | -------------
Boid | A flocking simulation, bird-oids
Diffusion Limited Aggregation | random walkers colliding with a seed creates fractaline shapes
Fractional Brownian Motion | A way to create noise
Mycelium | Implementation of a physarum (slime mold) simulation
Perlin Noise | Experiments in using perlin noise to create natural looking shapes'
L-Systems | L-systems to generate either stochastic or deterministic branching shapes
Diffusion-Reaction | Simulation of two chemicals diffusing and reacting with eachother
Circle Packing | Creating circles that don't overlap
Video Writer | Program to write video from folder of images

## Boid
  


https://user-images.githubusercontent.com/66800917/142296669-ca00e59f-a25e-4289-aafa-cf118ac57dea.mp4



Boid is short hand for bird-oid, or bird like entity. Each of these boid objects obey 3 very simple rules.

1. Boids adjust to steer towards the center of mass of their close neighbors.
2. Boids adjust to steer in the average direction of their close neighbors.
3. Boids do not get too close to eachother.

Relatively complex flocking behavior arises from these three simple rules.

## Diffusion-Reaction



Diffusion Reaction simulation is a fascinating way to generate organic looking shapes and patterns.  
The governing equations of this simulation are shown below. They are partial differential equations. A and B can be thought of as 2D distrobutions of two reactive chemicals.

`new_A = A+((Da*lp_A)-(A*B*B)+(f*(1-A)))*dt`  
`new_B = B+((Db*lp_B)+(A*B*B)-((k+f)*B))*dt`  

The equations both have three terms, a diffusive term, a reactive term, and a feed term. On the first line the diffusive term (Da\*lp_A) is the Laplacian of the image. This is acheived by convolving a 3x3 kernel across the image. It is essential equivalent to a heat dissipation model. The reactive term (A\*B\*B) models the A chemical reacting and turning into the B chemical. The feed term, (f*(1-A)) represents more of chemical A being continuously fed into the system. It is controlled by parameter 'f'. The second line is very similar however the feed term is a kill rate 'k' which is removing a certain amount of B continuously. By altering the parameters 'f' and 'k' many different patterns arise.
<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion%20Reaction/brain.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion%20Reaction/giraffe.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion%20Reaction/loopy.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion%20Reaction/map.png" width="400">
<p/>

The bottom right image is an image where f varies linearly along the y axis between .01 and .1, and k varies linearly along the x axis between .055 and .07.

The potential for different patterns is vast, and I need to explore it more thoroughly in the future.

## Diffusion Limited Aggregation 
![alt text](https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion-Limited%20Aggregation/fbmgrowth.jpg)
<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion-Limited%20Aggregation/fbmgrowthzoom.jpg" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion-Limited%20Aggregation/fbmgrowthzoomzoom.jpg" width="400">
<p/>


Diffusion Limited Aggregation works very simply. A random walker is spawned randomly in the canvas. It walks until it comes adjacent to a white pixel, and then its current pixel is turned white. This is very inefficient algorithm, so the spawn area for each random walker particle was reduced to be a bounding square jsut larger than the current shape. This reduces the distance the random walker has to travel to get to a white pixel.

## Fractional Brownian Motion
![alt text](https://github.com/zradlicz/Generative-OpenCV/blob/main/Fractional%20Brownian%20Motion/noise1.jpg)

https://user-images.githubusercontent.com/66800917/141801469-fe97c96b-a2f4-4769-9094-2c38f6ce17cf.mp4



Fractional Browninan motion is the type of motion that a random walker (just like the one that was used for DLA) exhibits. It is often used in creating noise, which is where the term brown noise comes from. Fractional Brownian Motion can also be used to make perlin noise look more natural.

## Mycelium

<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Mycelium/mycelium_frame_0125.jpg" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Mycelium/mycelium_frame_0130.jpg" width="400">
<p/>

The physarum simulation is also a surprising way to generate organic shapes. Each particle follows one simple rule. It has 3 sensors at the front of its head, one angled slightly left, one angled slightly right, and one straight ahead. If the sensor on the right detects a white path, then it will turn towards the path. Same on the left side. If the center sensor detects a white path then it will continue on the path. There are so many parameters to play with in theis code that I will definitely come back to this one.

## Perlin Noise
<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Perlin%20Noise/perlin_trail_478.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Perlin%20Noise/perlin_trail_607.png" width="400">
<p/>

<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Perlin%20Noise/perlin_trail_621.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Perlin%20Noise/perlin_trail_885.png" width="400">
<p/>

These images were created by finding the gradient of a perlin noise map, and getting the magnitude and orientation. Particles were then assigned a velocity based on the magnitude and orientation. By playing around with parameters many different types of images can be created. 

## L-Systems
<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree753.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree1293.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree2900.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree4034.png" width="400">
<p/>

L-systems were first created as a way to model biological growth in algae. Here it is used to generate trees with some randomness. L systems work by having a start seed, and then a list of axioms by which each variable will change into. This tree generation l-system for example contains 2 variables and 5 constants.  

-Variables: X F  
-Constants: + - [ ] L  
-Start: X  
-Rules: (X → F+[[X]-X]-F[-FX]+X), (F → FF)  

The class lsystem takes all of these as arguments. The update method then iterates through the string and recursively updates it. A separate, standalone funtion has to be written to interpret the string.

## Circle Packing

<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Circle%20Packing/big.png" width="400">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/Circle%20Packing/small.png" width="400">
<p/>

Circle packing actually seems to be a fairly complex problem to do efficiently. My method is terribly innefficient, and uses a lot of computationally intense algorithms that are built into OpenCV. It would be a fun project to attempt to make this gereration time optimal.

## Video Writer
Video Writer is a simple program to create an avi format video of a series of frames in a folder. Simply put multiple pngs in a folder and run the program with the corret folder path.




