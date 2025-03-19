#1. Design a Python GUI program that takes user input for the length and width of arectangle, and when a button is pressed, calculates and displays the area of therectangle.(2024 may)

import tkinter as tk

def calculate_area():
        label_result.config(text="Invalid input! Enter numbers.")
root = tk.Tk()
root.title("Rectangle Area Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Label(root, text="Enter Width:").pack()
entry_width = tk.Entry(root)
entry_width.pack()

button_calculate = tk.Button(root, text="Calculate Area", command=calculate_area)
button_calculate.pack()

label_result = tk.Label(root, text="Area: ")
label_result.pack()

root.mainloop()

# 2.Write a Python program to convert a color image to a grayscale image. (2024 jan)

import cv2

image = cv2.imread("example.jpg")  
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_image.jpg", gray_image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 3.Write Python GUI program to input two strings and output a concatenated stringwhen a button is pressed.(jan 2024)

import tkinter as tk

def concatenate_strings():
    str1 = entry1.get()  
    str2 = entry2.get()  
    result_label.config(text="Concatenated String: " + str1 + str2) 

root = tk.Tk()
root.title("String Concatenation")

tk.Label(root, text="Enter first string:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second string:").pack()
entry2 = tk.Entry(root)
entry2.pack()
concat_button = tk.Button(root, text="Concatenate", command=concatenate_strings)
concat_button.pack()
result_label = tk.Label(root, text="Concatenated String: ")
result_label.pack()
root.mainloop()

# 4.Write Python GUI program to take the birth date and output the age when abutton is pressed.How do you display(june 2022)

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birth_date_str = entry.get()  
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")  
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Your Age: {age} years")  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter date in YYYY-MM-DD format.")   handling

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):").pack()
entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(root, text="Your Age: ")
result_label.pack()


root.mainloop()

# 5.Write a python program to convert a colour image to black and white image.Explain the image methods used in it.(2023 may)

import cv2

image = cv2.imread("example.jpg")

bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("black_white.jpg", bw_image)

cv2.imshow("Black & White Image", bw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6.Write a GUI-based program that allows the user to convert amount in IndianRupees to amount in Euro.The interface should have labeled entry fields for these two values. Thesecomponents should be arranged in a grid where the labels occupy the first rowand the corresponding fields occupy the second row.
# At start-up, the Rupees field should contain 0.0, and the Euro field should contain0.0. The third row in the window contains two command buttons, labeled R->E
# and E->R. When the user presses the first button, the program should use the datain the Rupee field to compute the amount in Euro, which should then be outputto the Euro field. The second button should perform the inverse function.(june 2023)

import tkinter as tk

EXCHANGE_RATE = 0.011  # 1 INR ≈ 0.011 EUR (Example rate)

def convert_rupees_to_euro():
    """Convert Rupees to Euros"""
    try:
        rupees = float(rupees_entry.get())
        euros = round(rupees * EXCHANGE_RATE, 2)
        euro_entry.delete(0, tk.END)
        euro_entry.insert(0, str(euros))
    except ValueError:
        euro_entry.delete(0, tk.END)
        euro_entry.insert(0, "Invalid Input")

def convert_euro_to_rupees():
    """Convert Euros to Rupees"""
    try:
        euros = float(euro_entry.get())
        rupees = round(euros / EXCHANGE_RATE, 2)
        rupees_entry.delete(0, tk.END)
        rupees_entry.insert(0, str(rupees))
    except ValueError:
        rupees_entry.delete(0, tk.END)
        rupees_entry.insert(0, "Invalid Input")

root = tk.Tk()
root.title("Currency Converter (INR <-> EUR)")

tk.Label(root, text="Rupees (INR):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Euros (EUR):").grid(row=0, column=1, padx=10, pady=5)

rupees_entry = tk.Entry(root)
rupees_entry.grid(row=1, column=0, padx=10, pady=5)
rupees_entry.insert(0, "0.0")  
euro_entry = tk.Entry(root)
euro_entry.grid(row=1, column=1, padx=10, pady=5)
euro_entry.insert(0, "0.0")  

tk.Button(root, text="R->E", command=convert_rupees_to_euro).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="E->R", command=convert_euro_to_rupees).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()

