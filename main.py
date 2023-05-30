from tkinter import *
import numpy as np
import cv2
import pyautogui
import pygetwindow as gw
import time
from threading import Thread

def ticker():
    w = Tk()
    ticker.msg=ticker.msg[1:]+ticker.msg[0]
    variable = StringVar()
    ms = 300
    variable.set(ticker.msg)
    w.after(ms, ticker)
    w.geometry("100x100")
    w.config(bg="#549")
    label = Label(w, textvariable=variable, height=100)
    ticker.msg = input()
    ticker()
    label.pack()
    w.mainloop()

def videomake():
    window_name = "tk"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30.0
    record_sec = 3
    win = gw.getWindowsWithTitle(window_name)[0]
    win.activate()
    out = cv2.VideoWriter('video.avi', fourcc, fps, tuple(win.size))
    for i in range(int(record_sec*fps)):
        img = pyautogui.screenshot(region=(win.left, win.top, win.width, win.height))
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("screenshot", frame)
        if cv2.waitKey(1) == 'q':
            break






