#!/bin/bash
#
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

# mkdir info
#
/opt/homebrew/opt/opencv@3/bin/opencv_createsamples -img walking-bw.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3333
