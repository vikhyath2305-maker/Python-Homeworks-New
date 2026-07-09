import tkinter as tk

def check_number():
    user_input = entry.get()
    try:
        number = float(user_input)
        if number > 0:
            result_label.config(text="Positive")
        elif number < 0:
            result_label.config(text="Negative")
        else:
            result_label.config(text="Zero")
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Number Sign Checker")

instruction_label = tk.Label(root, text="Enter a number:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_number)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()