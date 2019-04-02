import cv2
import numpy as np

#Create a blank image.
image = np.zeros((512, 512, 3), np.uint8)

image = cv2.line(image, (0,0), (511, 511), (255,0,0), 5)

# Draw a rectangle
# image = cv2.rectangle(image, (20,0), (100,100), (0, 255, 0), 5)

# Draw a circle
# image = cv2.circle(image, (300,60), 50, (0,0,255), -1)

# Write a sentence
# cv2.putText(image, 'I like this workshop and the speaker', (8,500), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0, 0), 2, cv2.LINE_AA)


cv2.imshow('Result', image)

cv2.waitKey()
