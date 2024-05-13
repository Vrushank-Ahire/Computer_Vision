import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):   # Change Resolution
    # live Videos
    capture.set(3, width)
    capture.set(4, height)


# Scaling Images
img = cv.imread("../Resources/Photos/cat_large.jpg")
cv.imshow('Cat', img)
rescaled_image = rescaleFrame(img,scale=0.5)
cv.imshow('Rescaled Cat', rescaled_image)

# Scaling Videos
capture = cv.VideoCapture("../Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow("Video Rescaled", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

