import tkinter as tk
from tkinter import messagebox

def check_number():
    raw_value = entry_num.get().strip()

    if not raw_value:
        messagebox.showwarning("Warning", "Please enter a number.")
        return

    try:
        val = float(raw_value)
        if val > 0:
            lbl_result.config(text="Result: Positive", fg="green")
        elif val < 0:
            lbl_result.config(text="Result: Negative", fg="red")
        else:
            lbl_result.config(text="Result: Zero", fg="blue")
    except ValueError:
        lbl_result.config(text="Result: Invalid Input", fg="darkorange")

root = tk.Tk()
root.title("Number Sign Checker")
root.geometry("280x180")

lbl_title = tk.Label(root, text="Enter a Number:")
lbl_title.pack(pady=(15, 5))

entry_num = tk.Entry(root, width=20)
entry_num.pack(pady=5)

btn_check = tk.Button(root, text="Check", command=check_number, width=12)
btn_check.pack(pady=10)

lbl_result = tk.Label(root, text="Result: -", font=("Arial", 10, "bold"))
lbl_result.pack(pady=5)

root.mainloop()