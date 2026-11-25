
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid values!")
            return

        height = height / 100
        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"Your BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Error", "Please enter valid numbers!"
        )

def clear():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x450")
root.configure(bg="#EDE7F6")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 22, "bold"),
    bg="#EDE7F6",
    fg="#512DA8"
)
title.pack(pady=25)

# Weight
tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 12),
    bg="#EDE7F6"
).pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 13),
    justify="center"
)
weight_entry.pack(pady=10)

# Height
tk.Label(
    root,
    text="Height (cm)",
    font=("Arial", 12),
    bg="#EDE7F6"
).pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 13),
    justify="center"
)
height_entry.pack(pady=10)

# Calculate Button
tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#673AB7",
    fg="white",
    command=calculate_bmi,
    width=18
).pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#EDE7F6",
    fg="#311B92"
)
result_label.pack(pady=15)

# Clear Button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    command=clear,
    width=12
).pack(pady=5)

root.mainloop()
