import cv2

face_cascade = cv2.CascadeClassifier('../../resources/haarcascade_frontalface_default.xml')

img = cv2.imread('../../resources/lena.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('FACES',img)
cv2.waitKey()
cv2.destroyAllWindows()
