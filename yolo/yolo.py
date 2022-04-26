import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

yolo = cv2.dnn.readNet('C:/Users/laksh/Desktop/VScode/Python/proj/yolo/yolov3-tiny.weights',
                       'C:/Users/laksh/Desktop/VScode/Python/proj/yolo/yolov3-tiny.cfg')

classes = []

with open("C:/Users/laksh/Desktop/VScode/Python/proj/yolo/coco.names", 'r') as f:
    classes = f.read().splitlines()

img = cv2.imread('img.jpg')

blob = cv2.dnn.blobFromImage(
    img, 1/255, (320, 320), (0, 0, 0), swapRB=True, crop=False)

i = blob[0].reshape(320, 320, 3)
plt.imshow(i)
