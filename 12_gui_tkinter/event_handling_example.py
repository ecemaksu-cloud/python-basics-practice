# Tkinter Event Handling Example

from tkinter import *

window = Tk()
window.geometry("700x350")


def mouse_click(event):
    message_label.config(
        text="Mouse button clicked",
        font=("Helvetica", 17, "bold")
    )

    key_label.config(text="")


def key_pressed(event):
    message_label.config(
        text="A key was pressed",
        font=("Helvetica", 17, "bold")
    )


def a_key_pressed(event):
    key_label.config(
        text="The 'A' key was pressed",
        font=("Helvetica", 17, "bold")
    )


message_label = Label(window, text="")
message_label.pack(pady=50)

key_label = Label(window, text="")
key_label.pack(pady=100)

window.bind("<Button-1>", mouse_click)
window.bind("<KeyRelease>", key_pressed)
window.bind("a", a_key_pressed)

window.mainloop()
