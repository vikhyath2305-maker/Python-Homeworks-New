import tkinter as tk

root = tk.Tk()
root.title("GUI")
root.geometry("400x200")

x = tk.Label(root, text="Welcome to Python GUI")
x.pack()

root.mainloop()