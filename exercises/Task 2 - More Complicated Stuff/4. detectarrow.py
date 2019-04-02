import cv2

up_cascade = cv2.CascadeClassifier('../../resources/up_cascade.xml')

img = cv2.imread('../../resources/upinfo/1704_0075_0059_0106_0106.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ups = up_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in ups:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('UPS',img)
cv2.waitKey()
cv2.destroyAllWindows()
