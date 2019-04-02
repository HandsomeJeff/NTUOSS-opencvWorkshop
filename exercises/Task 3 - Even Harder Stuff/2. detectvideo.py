
import cv2

face_cascade = cv2.CascadeClassifier('../../resources/haarcascade_frontalface_default.xml')
# face_cascade2 = cv2.CascadeClassifier('../../resources/haarcascade_frontalface_alt.xml')
# face_cascade3 = cv2.CascadeClassifier('../../resources/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('../../resources/haarcascade_eye.xml')
# up_cascade = cv2.CascadeClassifier('../../resources/up_cascade.xml')


capture = cv2.VideoCapture(0)


while(True):
    flag, frame = capture.read()

    if not flag:
        exit(1)

    
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5)
#    faces2 = face_cascade2.detectMultiScale(grayFrame, 1.3, 5)
#    faces3 = face_cascade3.detectMultiScale(grayFrame, 1.3, 5)
#    ups = up_cascade.detectMultiScale(grayFrame, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(grayFrame, 1.3, 5)
    

    for (x, y, w, h) in faces:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Face',(x+w-50,y+h-50), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

##    font = cv2.FONT_HERSHEY_SIMPLEX
##    for (x, y, w, h) in faces2:
##        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
##        cv2.putText(frame,'Face',(x+w-50,y+h-50), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

##    eyes = eye_cascade.detectMultiScale(grayFrame, 1.3, 5)
##    for (ex, ey, ew, eh) in eyes:
##        cv2.putText(frame,'eye',(ex+ew-30,ey+eh-10), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

##    for (x, y, w, h) in ups:
##        font = cv2.FONT_HERSHEY_SIMPLEX
##        cv2.putText(frame,'Arrow',(x+w-50,y+h-50), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
##        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
