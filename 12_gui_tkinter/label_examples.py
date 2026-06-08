# Tkinter Label Examples

from tkinter import *

window = Tk()

window.geometry("250x180")

label_text = "Styled Label"

Label(
    window,
    text="No Font",
    bg="#000000",
    fg="#ffff00",
    padx=9,
    pady=5
).pack()

Label(
    window,
    text="Red Label",
    bg="#ff0000",
    fg="#ffffff"
).pack(pady=20)

Label(
    window,
    text=label_text,
    font=("Helvetica", 20, "bold")
).pack()

Label(
    window,
    text="STOP",
    font=("Arial", 15, "bold")
).pack()

window.mainloop()
