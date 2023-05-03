import cv2
import numpy as np
import time

import pyautogui


screenshot = pyautogui.screenshot()
screenshot.save('./Images/screenshot.png')

img = cv2.imread("Images/screenshot.png")
cv2.namedWindow(winname="window")
roi = cv2.selectROI(img)

cropped = img[int(roi[1]):int(roi[1]+roi[3]),
			int(roi[0]):int(roi[0]+roi[2])]
cv2.destroyWindow("window")
while True:
    cv2.imshow("new_window", cropped)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        exit(0)


while True:
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
