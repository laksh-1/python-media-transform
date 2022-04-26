import cv2 as cv
import numpy as np
import sys

file_name = sys.argv[1]

img = cv.imread('img/' + file_name)

print(file_name)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.flip(img, 0)
img = cv.resize(img, None, fx=0.2, fy=0.2)


cv.imwrite('img/bw_' + file_name, img)

cv.waitKey(0)
