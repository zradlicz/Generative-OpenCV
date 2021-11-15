# Generative-OpenCV
My first experiments with generative art and creative coding. Every project is done using OpenCV as a drawing canvas, intended to improve my image processing skills. Code should be easy to use in your own IDE.

Packages used:cv2,perlin-noise,numpy



## Folder Layout
Folder | Contents
------------ | -------------
Boid | A flocking simulation, bird-oids
Video Writer | Program to write video from folder of images
Diffusion Limited Aggregation | random walkers colliding with a seed creates fractaline shapes
Fractional Brownian Motion | A way to create noise
Mycelium | Implementation of a physarum (slime mold) simulation
Perlin Noise | Experiments in using perlin noise to create natural looking shapes'
L-Systems | L-systems to generate either stochastic or deterministic branching shapes
Diffusion-Reaction | Simulation of two chemicals diffusing and reacting with eachother
Circle Packing | Creating circles that don't overlap

## Boid
  
![Boid Image](images/flow_diagram.jpg)
![Boid Video](images/flow_diagram.jpg)

Boid is short hand for bird-oid, or bird like entity. Each of these boid objects obey 3 very simple rules.

1. Boids adjust to steer towars the center of mass of their close neighbors.
2. Boids adjust to steer in the average direction of their close neighbors.
3. Boids do not get too close to eachother.

Relatively complex flocking behavior arises from these three simple rules.


## Diffusion Limited Aggregation 

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)

![Flow Diagram](images/flow_diagram.jpg)
## Fractional Brownian Motion
![Flow Diagram](images/flow_diagram.jpg)
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




![Output](/images/example_output.JPG)

This image is an example of the output you should get from running AutoTrim. From top left: RGB image, Depth image, shape difference, prediction, thresholded prediction, depth prediciton.


![Probe Toolpath](/images/probe_toolpath.JPG)

This image shows the data collected from the probe overlayed onto the shape of the segmented shape.

![Probe Analysis](/images/probe_analyzed.JPG)

This image shows the edge detection working on the probe data.



