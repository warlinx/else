# -*- coding: utf-8 -*-
import pyautogui
import time
time.sleep(5)
f = open("words.txt", "r")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")

