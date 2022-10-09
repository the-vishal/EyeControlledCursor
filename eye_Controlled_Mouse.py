import cv2
from pynput.mouse import Button,Controller

import os

mouse = Controller()
eye_Cascade_File = cv2.CascadeClassifier(os.path.dirname(cv2.__file__) + '/data/haarcascade_eye.xml')
face_Cascade_File = cv2.CascadeClassifier(os.path.dirname(cv2.__file__) + '/data/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)


def track_pupil():
    #zooming and  tracking pupil movement
    pass


while True:
    global a,b
    a,b = 0,0
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convering to gray to recognize colour change effectively
    faces = face_Cascade_File.detectMultiScale(gray, 1.3, 5)  # geometry
    for (x, y, w, h) in faces:  # draw rectangle around using x,y,w,h coordinates
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # .ending point coordinates
        # 255,0,0 ----Blue line
        # 2= line width
        # eyes inside face
        roi_gray = gray[y:y + h, x:x + w]  # eye inside region of image ROI i,e gray--face
        roi_colour = img[y:y + h, x:x + h]

        eyes = eye_Cascade_File.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:  # eye width , height length parameters
            cv2.rectangle(roi_colour, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # print(len(eyes))
            print(ex+(ex+ew)/2)
            a =int(float(ex)/8)
            b=int(float(ey)/8)
            if int(len(eyes)) == 0:
                quit()
    cv2.imshow('img', img)
    mouse.move(a,b)
    k = cv2.waitKey(30) & 0xff

    if (k == 27):
        break


cam.release()
cv2.destroyAllWindows()



