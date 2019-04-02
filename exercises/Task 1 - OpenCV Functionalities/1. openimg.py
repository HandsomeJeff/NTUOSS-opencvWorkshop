import cv2

image = cv2.imread('../../resources/bigup.png', 0)

cv2.imshow('Result', image)

cv2.imwrite('../../resources/arrow.jpg', image)

cv2.waitKey()
