#!/bin/bash
#
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

# mkdir data
#
/opt/homebrew/opt/opencv@3/bin/opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1600 -numNeg 800 -numStages 10 -w 50 -h 50
