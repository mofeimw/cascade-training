import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

walk_cascade = cv.CascadeClassifier('./data-turbo/cascade.xml')

while True:
    ret, imageFrame = capture.read()

    hits = walk_cascade.detectMultiScale(imageFrame, 1.2, 6)

    for (x,y,w,h) in hits:
        imageFrame = cv.rectangle(imageFrame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv.imshow('title', imageFrame)
    cv.waitKey(1)
