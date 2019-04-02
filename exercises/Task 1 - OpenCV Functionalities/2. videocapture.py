
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('../../resources/result.avi', fourcc, 20.0, (640,480), False)

while(True):
    flag, frame = capture.read()

    if not flag:
        exit(1)

    # grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    output.write(frame)

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
output.release()
cv2.destroyAllWindows()
