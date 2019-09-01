#This program Automatically captures images without displaying webcam and saves with the timestamp as the file name
import cv2
import time#, os, fnmatch, shutil

camera=cv2.VideoCapture(0)
for i in range(10):
    return_value, image = camera.read()
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
    
cv2.imwrite(timestamp+"("+str(i)+")"+'.png', image)
            
del(camera)
