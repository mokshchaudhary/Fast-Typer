import pyautogui as p
import time
import mss
import cv2
import numpy as np
import pytesseract

con = r'--psm 7 -l eng -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz'
while(True):
    time.sleep(0.5)
    with mss.mss() as sct:
                monitor = {"top": 341, "left": 550, "width": 522, "height": 90}  #Defines the Region
                img=sct.grab(monitor) 
    img = np.array(img)
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img=cv2.resize(img, (0,0), fx=2.5, fy=1.5)
    a = pytesseract.image_to_string(img,config= con)
    print(a)
    if(len(a)<16):
    	p.write(a)