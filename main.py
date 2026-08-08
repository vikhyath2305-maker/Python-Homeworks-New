import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Books and Authors")
root.geometry("400x250")

tree = ttk.Treeview(root, columns=("Book", "Author"), show="headings")

tree.heading("Book", text="Book")
tree.heading("Author", text="Author")

tree.column("Book", width=200)
tree.column("Author", width=150)

tree.insert("", "end", values=("The Hunger Games", "Suzanne Collins"))
tree.insert("", "end", values=("The Maze Runner", "James Dashner"))
tree.insert("", "end", values=("Divergent", "Veronica Roth"))
tree.insert("", "end", values=("Percy Jackson", "Rick Riordan"))
tree.insert("", "end", values=("Diary of a Wimpy Kid", "Jeff Kinney"))

tree.pack(padx=10, pady=10)

root.mainloop()