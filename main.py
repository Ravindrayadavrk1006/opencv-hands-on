import cv2 as cv

img = cv.imread('hsv.jpg')
win = cv.namedWindow('display_image')
cv.imshow(win,img)
cv.waitKey(0)
cv.destroyWindow(win)