import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')

mask1 = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, (255, 255, 255), -1)
cv.imshow('Mask1', mask1)

mask2 = cv.rectangle(blank.copy(), (150, 150), (blank.shape[1]-150, blank.shape[0]-150), (255, 255, 255), -1)
cv.imshow('Mask2', mask2)

fancy_mask = cv.bitwise_and(mask1, mask2)
cv.imshow('Fancy Mask', fancy_mask)

masked_image = cv.bitwise_and(img, fancy_mask)
cv.imshow('Masked Image', masked_image)

cv.waitKey(0)
