# import cv2 as cv
import cv2
import numpy as np
import sys

file_name = sys.argv[1]

# img = cv.imread('img/' + file_name)

# print(file_name)

# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # img = cv.flip(img, 0)
# img = cv.resize(img, None, fx=0.6, fy=0.6)


# cv.imwrite('img/bw_' + file_name, img)

# cv.waitKey(0)


video = cv2.VideoCapture('img/' + file_name)

if (video.isOpened() == False):
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('img/bw_' + file_name,
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         15, size, False)

while(True):
    ret, gray = video.read()

    if ret == True:

        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

        # gray = cv2.flip(gray, 0)
        # gray = cv2.resize(
        #     gray, (int(frame_width/2), int(frame_height/2)), interpolation=cv2.INTER_AREA)
        result.write(gray)

        cv2.imshow('Frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    else:
        break

video.release()
result.release()

cv2.destroyAllWindows()

print("The video was successfully saved")
