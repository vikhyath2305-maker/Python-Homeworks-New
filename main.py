import tkinter as tk

root = tk.Tk()
root.title("Welcome App")
root.geometry("300x150")

label = tk.Label(root, text="Welcome to Python GUI")
label.pack(pady=40)

root.mainloop()