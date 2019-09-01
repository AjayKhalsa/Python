#When we run the program ,The webcam launches and we can take any number of images By pressing space
#and we can exit by pressing esc
#Drawbacks-Can't Take multiple images at once
#         -Cannot capture images automatically
#         -If esc is not pressed ,image will not be saved

import cv2
import time, os, fnmatch, shutil


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.png".format(timestamp)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


