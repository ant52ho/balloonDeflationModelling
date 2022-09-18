import balloonWidth
import numpy as np
import cv2

cap = cv2.VideoCapture('IMG_6369.MOV')
f = open("data.txt", "a")
frameCount = 0
blanks = []
while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        frame = cv2.resize(frame, (0,0), None, 0.4, 0.4)
    except cv2.error:
        break
    a = balloonWidth.findWidth(frame)
    if a != None:
        f.write(str(a) + " ")
    else:
        print("trgi")
        blanks.append(frameCount)
    frameCount += 1
    print(frameCount)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
f.write("\n" + str(blanks))
f.close()
