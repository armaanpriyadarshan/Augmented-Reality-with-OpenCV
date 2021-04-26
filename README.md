# Augmenting Reality with ArUco Markers and OpenCV
<p align="left">
  <img src="doc/demo.gif">
</p>

**The tutorial/demonstration video associated with this repository can be found below.**

[![Link to my vid](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/doc/thumbnail.png)]()

## Introduction
This repository contains everything you need to augment webcam footage using OpenCV. The program which does this is [aruco_ar.py](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/aruco_ar.py). However, there's a more to it than just projecting a video into a videostream. The program is built around a printed sheet of paper with 4 markers in each corner. A printable copy of the paper with the markers I used can be found under [printable.png](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/printable.png). Simply put, the program detects these markers as well as counting rotation and position. Using the 4 corner markers, the program finds the homography and warps mask onto the paper. Overlayed on this mask is the provided video, [Ronaldo.mp4](https://github.com/armaanpriyadarshan/Augmented-Reality-with-OpenCV/blob/main/Ronaldo.mp4) in this case.
<p align="left">
  <img src="aruco_ar.py">
</p>
