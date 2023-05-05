import cv2
import numpy as np
import time
import re
import pyautogui
from text_extractor import *


def extract():
    screenshot = pyautogui.screenshot()
    screenshot.save('./Images/screenshot.png')
    img = cv2.imread("./Images/screenshot.png")
    cv2.namedWindow(winname="window")
    cv2.destroyWindow("window")

    roi = cv2.selectROI("Crop a section", img)
    cropped = img[int(roi[1]):int(roi[1]+roi[3]),
                  int(roi[0]):int(roi[0]+roi[2])]
    if len(cropped) > 0:
        img = cv2.imwrite("Images/screenshot.png", cropped)
        while True:
            cv2.imshow("Final Image", cropped)
            if cv2.waitKey(1) & 0xFF == 13:
                ir = ImageReader()
                print(ir.extract_text())
                exit(0)
            if cv2.getWindowProperty('Final Image', cv2.WND_PROP_VISIBLE) < 1:
                exit(0)
    exit(0)
