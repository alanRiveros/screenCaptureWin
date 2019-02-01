import numpy as np
import cv2
from PIL import ImageGrab
import sys
from winguiauto import findTopWindow
import win32gui
import win32con

hwnd = findTopWindow("Calculadora")
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


rect = win32gui.GetWindowPlacement(hwnd)[-1]
print(rect[2:4])

#fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
#vid = cv2.VideoWriter('record.avi', fourcc, 8, rect[2:4])


while(True):
    img = ImageGrab.grab(bbox=rect) #x, y, w, h
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #vid.write(img_np)
    cv2.imshow("frame", img_np)
    key = cv2.waitKey(1)
    if key == 27:
        break

#vid.release()
cv2.destroyAllWindows()
