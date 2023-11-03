#!/bin/bash
#
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

# mkdir data
#
/opt/homebrew/opt/opencv@3/bin/opencv_traincascade -data data-turbo -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 1500 -numStages 10 -w 50 -h 50 -precalcValBufSize 20000 -precalcIdxBufSize 20000 -maxFalseAlarmRate 0.2 -minHitRate 0.99
