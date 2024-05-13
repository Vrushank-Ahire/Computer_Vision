import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging Blur
average = cv.blur(img, (5, 5))
cv.imshow('Average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 5)      # Giving single odd digit in kernel size is necessary
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 25, 15, 20)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
