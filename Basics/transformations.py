import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# 1.Translation


def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)


#   x +ve ->> Right Shift       x -ve ->> Left Shift
#   y +ve ->> Downwards shift   y -ve ->> Upwards Shift

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# 2.Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# angle +ve ->> acw rotation    -ve ->> ckw rotation
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# 3.Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# flip code = (0 x-axis) (> 0 y-axis) (< 0 both)
# 4.Flipping
flipped = cv.flip(img, 0)
cv.imshow('Flipped', flipped)

# 5.Cropped
cropped = resized[25:350, 125:375]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
