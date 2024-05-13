import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(), (40, 40), (360, 360), (255, 255, 255), -1)
cv.imshow('Rectangle', rectangle)

circle = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 180,(255, 255, 255), -1)
cv.imshow('Circle', circle)

# bitwise_and   -> intersecting
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# bitwise_or    ->intersecting + non-intersecting
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

# bitwise_xor   ->non-intersecting
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# bitwise_not   ->compliment
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
