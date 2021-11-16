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
  
![Boid Image](images/flow_diagram.jpg)
![Boid Video](images/flow_diagram.jpg)

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

The equations both have three terms, a diffusive term, a reactive term, and a feed term. On the first line the diffusive term (Da\*lp_A) is the Laplacian of the image. This is acheived by convolving a 3x3 kernel across the image. It is essential equivalent to a heat dissipation model. The reactive term (A\*B\*B) models the A chemical reacting and turning into the B chemical. The feed term, (f*(1-A)) represents more of chemical A being continuously fed into the system. It is controlled by parameter 'p'. The second line is very similar however the feed term is a kill rate 'k' which is removing a certain amount of B continuously. By altering the parameters 'p' and 'k' many different patterns arise.

![Voronoi](images/flow_diagram.jpg)
![Loopy Voronoi](images/flow_diagram.jpg)
![Mitosis Video](images/flow_diagram.jpg)
![Brain](images/flow_diagram.jpg)
![Brain/Voronoi](images/flow_diagram.jpg)
![Full Distrobution](images/flow_diagram.jpg)
The bottom right image is an image where f varies linearly along the y axis between .01 and .1, and k varies linearly along the x axis between .055 and .07. 
## Diffusion Limited Aggregation 

![Growth](https://github.com/zradlicz/DLA/blob/main/fbmgrowth.jpg)

![Growth Zoom](https://github.com/zradlicz/Generative-OpenCV/blob/main/Diffusion-Limited%20Aggregation/fbmgrowthzoom.jpg)

![Flow Diagram](images/flow_diagram.jpg)

Diffusion Limited Aggregation works very simply. A random walker is spawned randomly in the canvas. It walks until it comes adjacent to a white pixel, and then its current pixel is turned white. This is very inefficient algorithm, so the spawn area for each random walker particle was reduced to be a bounding square jsut larger than the current shape. This reduces the distance the random walker has to travel to get to a white pixel.

## Fractional Brownian Motion
![alt text](https://github.com/zradlicz/Generative-OpenCV/blob/main/Fractional%20Brownian%20Motion/noise1.jpg)

https://user-images.githubusercontent.com/66800917/141801469-fe97c96b-a2f4-4769-9094-2c38f6ce17cf.mp4



Fractional Browninan motion is the type of motion that a random walker (just like the one that was used for DLA) exhibits. It is often used in creating noise, which is where the term brown noise comes from. Fractional Brownian Motion can also be used to make perlin noise look more natural.

## Mycelium

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

## Perlin Noise
![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)
## L-Systems
<p float="left">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree753.png" width="320">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree1293.png" width="320">
<img src="https://github.com/zradlicz/Generative-OpenCV/blob/main/L-Systems/tree2900.png" width="320">
<p/>
## Diffusion-Reaction
## Circle Packing
## Video Writer




