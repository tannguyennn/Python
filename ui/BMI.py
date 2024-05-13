import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    height = float(height_entry.get()) / 100 # Chuyển đổi chiều cao từ cm sang mét
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.configure(text="Your BMI: {:.2f}".format(bmi))
    if bmi < 18.5:
        messagebox.showinfo("BMI Result", "Underweight")
    elif 18.5 <= bmi < 25:
        messagebox.showinfo("BMI Result", "Normal weight")
    elif 25 <= bmi < 30:
        messagebox.showinfo("BMI Result", "Overweight")
    else:
        messagebox.showinfo("BMI Result", "Obese")

# Tạo cửa sổ
window = tk.Tk()
window.title("BMI Calculator")

# Tạo các widget
height_label = tk.Label(window, text="Height (cm):")
height_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

height_entry = tk.Entry(window)
height_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Mở cửa sổ
window.mainloop()