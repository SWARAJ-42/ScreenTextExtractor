import cv2
import numpy as np
import time
import re
import pyautogui
from text_extractor import *


screenshot = pyautogui.screenshot()
screenshot.save('./Images/screenshot.png')

img = cv2.imread("./Images/screenshot.png")
cv2.namedWindow(winname="window")
cv2.destroyWindow("window")
roi = cv2.selectROI(img)

cropped = img[int(roi[1]):int(roi[1]+roi[3]),
			int(roi[0]):int(roi[0]+roi[2])]
img = cv2.imwrite("Images/screenshot.png", cropped)

while True:
    cv2.imshow("new_window", cropped)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        ir = ImageReader()
        print(ir.extract_text())
        exit(0)



while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()
