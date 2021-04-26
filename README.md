# Augmenting Reality with ArUco Markers and OpenCV
<p align="left">
  <img src="doc/demo.gif">
</p>


## Introduction
This repository contains everything you need to augment webcam footage using OpenCV. The program which does this is [aruco_ar.py](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/aruco_ar.py). However, there's a more to it than just projecting a video into a videostream. The program is built around a printed sheet of paper with 4 markers in each corner. A printable copy of the paper with the markers I used can be found under [printable.png](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/printable.png). Simply put, the program detects these markers as well as counting rotation and position. Using the 4 corner markers, the program finds the homography and warps mask onto the paper. Overlayed on this mask is the provided video, [Ronaldo.mp4](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/Ronaldo.mp4) in this case. **Most of the code is referenced from [Adrian Rosenbrock's article](https://www.pyimagesearch.com/2021/01/11/opencv-video-augmented-reality/) on the same subject.**

### The tutorial/demonstration video associated with this repository can be found below with an important step [here](https://www.youtube.com/channel/UCT9t2Bug62RDUfSBcPt0Bzg?sub_confirmation=1)!

[![Link to my vid](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/doc/thumbnail.png)]()

## Table of Contents
1. [Organizing our Prequisites and Virtual Environment](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV#organizing-our-prequisites-and-virtual-environment)
2. [Drawing ArUco Markers (Optional)](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV#drawing-aruco-markers-optional)
3. [Augmenting Reality](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV#augmenting-reality)

## Organizing our Prequisites and Virtual Environment

Like many of my other projects, this one also uses a virtual environment to avoid version conflicts with previously installed packages on our system. To do so, [Anaconda](https://www.anaconda.com/products/individual) is, again, my choice. In an Anaconda terminal, run

```
conda create -n opencvar pip python=3.8
```

and then

```
conda activate opencvar
```

Now that we have created and activated our virtual environment, we can install OpenCV_contrib with

```
pip install opencv-contrib-python
```

**Note: For this project, I you must use versions 4.3.0+.**
## Drawing ArUco Markers (Optional)

ArUco Markers, standing for Augmented Reality University of Cordoba, are fiducial markers as mentioned earlier, a key step in the process. In the real world, markers can be placed and captured through photo, video, etc. In this project, the corner markers are identified and the encapsulated frame is replaced with a video. 

OpenCV has multiple dictionaries of AruCo Markers built it. I have attached all the markers I used separately, as well as in the printable sheet of paper used. However, if you want, I've also included a [program for drawing new AruCo markers](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/draw_marker.py). There are a few changes you must make to the script to generate new markers

* **Line 7**:

## Augmenting Reality
