# Generative-OpenCV
My first experiments with generative art and creative coding. Every project is done using OpenCV as a drawing canvas, intended to improve my image processing skills. Code should be easy to use in your own IDE after installing these packages.

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


## Diffusion Limited Aggregation 

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

Diffusion Limited Aggregation works very simply. A random walker is spawned randomly in the canvas. It walks until it comes adjacent to a white pixel, and then its current pixel is turned white. This is very inefficient algorithm, so the spawn area for each random walker particle was reduced to be a bounding square jsut larger than the current shape. This reduces the distance the random walker has to travel to get to a white pixel.

## Fractional Brownian Motion
![alt text](/Fractional_Brownian_Motion/noise1.jpg)

https://user-images.githubusercontent.com/66800917/141801469-fe97c96b-a2f4-4769-9094-2c38f6ce17cf.mp4



Fractional Browninan motion is the type of motion that a random walker exhibits. It is often used in creating noise, which is where the term brown noise comes from. Fractional Brownian Motion can also be used to make perlin noise look more natural.

## Mycelium

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

## Perlin Noise
![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)
## L-Systems
## Diffusion-Reaction
## Circle Packing
## Video Writer




