import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    """
    Calculate BMI based on user input and display the result in the GUI.
    """
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display BMI and category
        result_label.config(
            text=f"Your BMI is: {bmi:.2f}\nCategory: {category}", fg="blue"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")


def reset_inputs():
    """
    Clear all input and output fields.
    """
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


# Create the main application window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("400x300")
app.resizable(False, False)

# Heading
heading = tk.Label(app, text="BMI Calculator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Input fields for weight and height
weight_frame = tk.Frame(app)
weight_frame.pack(pady=5)
weight_label = tk.Label(weight_frame, text="Weight (kg):", font=("Arial", 12))
weight_label.pack(side=tk.LEFT, padx=5)
weight_entry = tk.Entry(weight_frame, width=10, font=("Arial", 12))
weight_entry.pack(side=tk.LEFT)

height_frame = tk.Frame(app)
height_frame.pack(pady=5)
height_label = tk.Label(height_frame, text="Height (m):", font=("Arial", 12))
height_label.pack(side=tk.LEFT, padx=5)
height_entry = tk.Entry(height_frame, width=10, font=("Arial", 12))
height_entry.pack(side=tk.LEFT)

# Buttons for Calculate and Reset
button_frame = tk.Frame(app)
button_frame.pack(pady=20)
calculate_button = tk.Button(
    button_frame, text="Calculate", font=("Arial", 12), command=calculate_bmi
)
calculate_button.pack(side=tk.LEFT, padx=10)
reset_button = tk.Button(
    button_frame, text="Reset", font=("Arial", 12), command=reset_inputs
)
reset_button.pack(side=tk.LEFT, padx=10)

# Result label to display the BMI and category
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the application
app.mainloop()
