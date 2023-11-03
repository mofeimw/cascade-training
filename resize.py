import os, sys
import cv2 as cv

for image_path in os.listdir('./neg'):
    path = os.path.join('./neg', image_path)
    image = cv.imread(path)
    height, width, channels = image.shape

    print(width, height)

    resized = cv.resize(image, (100, 100))
    resized_path = os.path.join('./neg-resized', image_path)
    cv.imwrite(resized_path, resized)
