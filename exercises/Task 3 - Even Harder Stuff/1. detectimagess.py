

import cv2
import numpy as np
import os


up_cascade = cv2.CascadeClassifier('../../resources/up_cascade.xml')


def exists(img, cascade):
    out = cascade.detectMultiScale(img, 1.3, 5)
    print out
    for (x, y, w, h) in out:
        imge = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('UPS',imge)
        cv2.waitKey()
        cv2.destroyAllWindows()
    return 0
    


for name in os.listdir('../../resources/upinfo'):
    if name[-3:] != 'dat':
        
        img = cv2.imread('../../resources/upinfo/' + name, 0)
        
        exists(img, up_cascade)

