# Simple Calculator GUI using Tkinter

from tkinter import *

expression = ""


def press(key):
    global expression
    expression += str(key)
    display.set(expression)


def equal():
    global expression

    try:
        result = str(eval(expression))
        display.set(result)
        expression = ""

    except Exception:
        display.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    display.set("")


root = Tk()

root.title("Simple Calculator")
root.geometry("270x180")
root.configure(bg="lightgreen")

display = StringVar()

entry = Entry(
    root,
    textvariable=display
)

entry.grid(
    columnspan=4,
    ipadx=70
)

# Number Buttons

Button(root, text="1", command=lambda: press(1), width=7).grid(row=2, column=0)
Button(root, text="2", command=lambda: press(2), width=7).grid(row=2, column=1)
Button(root, text="3", command=lambda: press(3), width=7).grid(row=2, column=2)

Button(root, text="4", command=lambda: press(4), width=7).grid(row=3, column=0)
Button(root, text="5", command=lambda: press(5), width=7).grid(row=3, column=1)
Button(root, text="6", command=lambda: press(6), width=7).grid(row=3, column=2)

Button(root, text="7", command=lambda: press(7), width=7).grid(row=4, column=0)
Button(root, text="8", command=lambda: press(8), width=7).grid(row=4, column=1)
Button(root, text="9", command=lambda: press(9), width=7).grid(row=4, column=2)

Button(root, text="0", command=lambda: press(0), width=7).grid(row=5, column=0)

# Operator Buttons

Button(root, text="+", command=lambda: press("+"), width=7).grid(row=2, column=3)
Button(root, text="-", command=lambda: press("-"), width=7).grid(row=3, column=3)
Button(root, text="*", command=lambda: press("*"), width=7).grid(row=4, column=3)
Button(root, text="/", command=lambda: press("/"), width=7).grid(row=5, column=3)

# Other Buttons

Button(root, text="=", command=equal, width=7).grid(row=5, column=2)
Button(root, text="Clear", command=clear, width=7).grid(row=5, column=1)
Button(root, text=".", command=lambda: press("."), width=7).grid(row=6, column=0)

root.mainloop()
