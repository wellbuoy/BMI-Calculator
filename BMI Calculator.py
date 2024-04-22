# Import necessary modules
import tkinter as tk
from tkinter import messagebox

# function to calculate BMI
def calculate_bmi(weight, height):
    try:
        height_m = height / 100  # convert height from cm to meters
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

# function to categorize BMI
def categorize_bmi(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# function to handle button click event
def calculate_button_click():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    
    result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

# function to save BMI data to a text file
def save_bmi_data():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    
    with open("bmi_data.txt", "a") as file:
        file.write(f"Weight: {weight}, Height: {height}, BMI: {bmi}, Category: {category}\n")
    messagebox.showinfo("BMI Calculator", "BMI data saved successfully!")

# create main window
root = tk.Tk()
root.title("BMI Calculator")

# create labels
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# create entry fields
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_button_click)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# create save button
save_button = tk.Button(root, text="Save Data", command=save_bmi_data)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

# to run the main loop or the application
root.mainloop()
