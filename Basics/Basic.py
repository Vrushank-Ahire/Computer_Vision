import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)      # ksize must be odd , decides blur level
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(blur, 100, 200)    # if blur image is passed less edge are observed
cv.imshow('Canny Edges', canny)

# 4. Dilating an image
dilated = cv.dilate(canny, (5, 5), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

cv.rectangle(resize, (125, 25), (375, 350), (0, 255, 0), thickness=3)
cv.imshow('Resize: ', resize)

# 7. Cropped
cropped = resize[25:350, 125:375]
cv.imshow('Cropped', cropped)
cv.waitKey(0)

