import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

# walk_cascade = cv.CascadeClassifier('./walk-cascade-turbo.xml')
walk_cascade = cv.CascadeClassifier('./test/cascade.xml')

CONFIDENCE_BASELINE = 2

while True:
    ret, imageFrame = capture.read()

    hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
    render = imageFrame
    cv.imshow('walk_cascade', imageFrame)
    cv.waitKey(1)

    # refine this
    red_lower = np.array([0, 175, 20], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask = cv.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 100, 60], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv.inRange(hsvFrame, green_lower, green_upper)

    kernel = np.ones((5, 5), "uint8")

    red_mask = cv.dilate(red_mask, kernel)
    res_red = cv.bitwise_and(imageFrame, imageFrame, mask = red_mask)
    # cv.imshow('red', res_red)
    green_mask = cv.dilate(green_mask, kernel)
    res_green = cv.bitwise_and(imageFrame, imageFrame, mask = green_mask)
    # cv.imshow('green', res_green)

    red_contours, red_hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(red_contours):
        area = cv.contourArea(contour)
        if(area > 350):
            x, y, w, h = cv.boundingRect(contour)
            render = cv.rectangle(render, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.putText(render, "Red Color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
            cv.imshow('walk_cascade', render)
            cv.waitKey(1)

    green_contours, green_hierarchy = cv.findContours(green_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(green_contours):
        area = cv.contourArea(contour)
        if(area > 350):
            x, y, w, h = cv.boundingRect(contour)
            render = cv.rectangle(render, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(render, "Green Color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
            cv.imshow('walk_cascade', render)
            cv.waitKey(1)

    # hits = walk_cascade.detectMultiScale(imageFrame, 1.2, 6)
    hits, rejectLevels, levelWeights = walk_cascade.detectMultiScale3(imageFrame, scaleFactor=1.2, minNeighbors=8, outputRejectLevels=1)

    i = 0
    while i < len(levelWeights):
        confidence = levelWeights[i]
        if confidence >= CONFIDENCE_BASELINE:
            (x,y,w,h) = hits[i]
            render = cv.rectangle(render, (x,y), (x+w,y+h), (255,0,0), 2)
            status = "walk [" + str(confidence)[:4] + "]"
            cv.putText(render, status, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 4)
            cv.imshow('walk_cascade', render)
            cv.waitKey(1)
        i += 1

    # for (x,y,w,h) in hits:
    #     img = cv.rectangle(imageFrame, (x,y), (x+w,y+h), (255,0,0), 2)
    #     cv.imshow('title', img)
    #     cv.waitKey(1)
