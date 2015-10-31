import cv
from time import localtime, strftime
INTERVAL = 50 #miliseconds
capture = cv.CaptureFromCAM(-1)
i = 0

while True:
    cv.WaitKey(INTERVAL)
    timenow = strftime("%H:%M:%S", localtime())
    print "Captured!      {}             {}".format(i, timenow)
    frame = cv.QueryFrame(capture)
    path = "image.jpg".format(timenow)
    cv.SaveImage(path, frame)
    i += 1
    
