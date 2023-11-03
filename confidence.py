import cv2 as cv
import numpy as np

CONFIDENCE_BASELINE = 1.5

capture = cv.VideoCapture(0)

walk_cascade = cv.CascadeClassifier('./data-turbo/cascade.xml')

while True:
    ret, imageFrame = capture.read()

    hits, rejectLevels, levelWeights = walk_cascade.detectMultiScale3(imageFrame, scaleFactor=1.2, minNeighbors=8, outputRejectLevels=1)

    i = 0
    while i < len(levelWeights):
        confidence = levelWeights[i]
        if confidence >= CONFIDENCE_BASELINE:
            (x,y,w,h) = hits[i]
            imageFrame = cv.rectangle(imageFrame, (x,y), (x+w,y+h), (255,0,0), 2)
            status = "walk [" + str(confidence)[:4] + "]"
            cv.putText(imageFrame, status, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 4)
        i += 1

    cv.imshow('title', imageFrame)
    cv.waitKey(1)
