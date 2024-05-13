import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Split
b, g, r = cv.split(img)

cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

# Merge
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# On splitting into color channels ,each channel is represented as Gray scale image
print(" img.shape : ", img.shape)
print('b shape: ', b.shape)
print('g shape: ', g.shape)
print('r shape: ', r.shape)

cv.waitKey(0)
