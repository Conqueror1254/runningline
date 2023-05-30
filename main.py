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








