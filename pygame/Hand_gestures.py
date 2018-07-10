import sys, os, random
import cv2
import numpy as np
import wx
import cv2
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect

#from gui import BaseLayout
from gestures import HandGestureRecognition
def main():
    device = cv2.cv.CV_CAP_OPENNI
    capture = cv2.VideoCapture()
    if not(capture.isOpened()):
        capture.open(device)
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    
main()
