#!/bin/bash
#
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

/opt/homebrew/opt/opencv@3/bin/opencv_createsamples -info info/info.lst -num 3333 -w 50 -h 50 -vec positives.vec
