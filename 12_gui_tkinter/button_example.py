# Tkinter Button Example

from tkinter import *

window = Tk()

window.title("Button Example")
window.geometry("600x300")

frame = Frame(window)
frame.grid()

close_button = Button(
    frame,
    text="CLOSE",
    width=50,
    height=5,
    command=window.destroy
)

close_button.grid(
    padx=110,
    pady=80
)

window.mainloop()
