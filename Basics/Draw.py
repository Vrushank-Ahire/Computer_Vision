import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# # 1. Paint the image a certain colour
# blank[50:150, 50:150] = 255, 0, 0
# blank[200:300, 200:300] = 0, 255, 0
# blank[350:450, 350:450] = 0, 0, 255
# cv.imshow('RGB', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (125, 125), (300, 300), (0, 255, 0), thickness=2)     # -ve thickness means fill colour
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)


# 4. Draw a line
# cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=4)
cv.line(blank, (137, 137), (377, 377), (123, 123, 123), 3)
cv.imshow('Line', blank)

# 5. Write Text
cv.putText(blank, 'Hey! Vrushank Here.', (50, 250), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 255, 255),
           thickness=1)
cv.imshow('Text',blank)
cv.waitKey(0)












