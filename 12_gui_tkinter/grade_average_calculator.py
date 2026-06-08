# Grade Average Calculator GUI

import tkinter as tk


def calculate_average():
    grade1 = float(grade1_entry.get())
    grade2 = float(grade2_entry.get())
    grade3 = float(grade3_entry.get())

    average = (grade1 + grade2 + grade3) / 3

    result_label.config(text=f"Average: {average:.2f}")


window = tk.Tk()
window.title("Grade Average Calculator")

grade1_label = tk.Label(window, text="Grade 1:")
grade1_entry = tk.Entry(window)

grade2_label = tk.Label(window, text="Grade 2:")
grade2_entry = tk.Entry(window)

grade3_label = tk.Label(window, text="Grade 3:")
grade3_entry = tk.Entry(window)

calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate_average
)

result_label = tk.Label(window, text="Average:")

grade1_label.grid(row=0, column=0)
grade1_entry.grid(row=0, column=1)

grade2_label.grid(row=1, column=0)
grade2_entry.grid(row=1, column=1)

grade3_label.grid(row=2, column=0)
grade3_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=0)

result_label.grid(row=4, column=0)

window.mainloop()
