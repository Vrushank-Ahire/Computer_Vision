import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cat 2', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', HSV)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
bgr2rbg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('BGR -->> RBG', bgr2rbg)

# L*a*b to BGR
BGR = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB -->> BGR', BGR)

plt.imshow(bgr2rbg)     # Matplotlib follows RGB & OpenCV follows BGR
plt.show()

cv.waitKey(0)
