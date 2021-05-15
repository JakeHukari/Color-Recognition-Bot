from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Click define 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_pyLEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Stopping event 
while keyboard.is_pressed('q') == False:

# Tells bot where to click    
    if pyautogui.pixel(-1426, 555)[0] == 0:
        click(-1426, 555)
    if pyautogui.pixel(-1426, 555)[0] == 0:
        click(-1339, 555)
    if pyautogui.pixel(-1426, 555)[0] == 0:
        click(-1260, 555)
    if pyautogui.pixel(-1426, 555)[0] == 0:
        click(-1150, 555)