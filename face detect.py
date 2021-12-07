import cv2
import os
vidcap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

di = input("enter name ")
path = "/Users/Administrator/PycharmProjects/tts/opencv/src/images"
way = os.path.join(path, di)


def imgcap(directory):
    i = 0
    count = 0
    while True:
        success, image = vidcap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
            roi_color = image[y:y + h, x:x + w]
        cv2.imshow('snapping', image)
        os.chdir(directory)
        if cv2.waitKey(10) & 0xff == ord('r'):
            if count < 5:
                i += 1
                cv2.imwrite(di + str(i) + '.jpg', roi_color)
                color = (255, 0, 0)  # BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(image, (x, y), (end_cord_x, end_cord_y), color, stroke)
               # cv2.imwrite(di + str(i) + '.jpg', image)
                cv2.imshow("captured pic", image)
                print('taking pics')
                count += 1
            else:
                print('max amount of pics are stored')
                break
        if cv2.waitKey(10) & 0xff == ord('v'):
            break


try:
    os.mkdir(way)
    print("dir created successfully")
    f = 1
    imgcap(way)
except OSError:
    print("dir exixts")
    f = 2


vidcap.release()
cv2.destroyAllWindows()

