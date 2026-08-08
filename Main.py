import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Grocery List")

tk.Label(root, text="Item:").grid(row=0, column=0)
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1)

tk.Label(root, text="Quantity:").grid(row=1, column=0)
qty_entry = tk.Entry(root)
qty_entry.grid(row=1, column=1)

tree = ttk.Treeview(root, columns=("Item", "Qty"), show="headings", height=5)
tree.heading("Item", text="Item")
tree.heading("Qty", text="Qty")
tree.grid(row=3, column=0, columnspan=2)

def add_item():
    item = item_entry.get()
    qty = qty_entry.get()
    
    if item == "" or qty == "":
        messagebox.showerror("Error", "Please fill in both fields")
        return

    tree.insert("", "end", values=(item, qty))
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

def delete_item():
    selected = tree.selection()
    if selected:
        tree.delete(selected)
    else:
        messagebox.showerror("Error", "Select an item first")

tk.Button(root, text="Add Item", command=add_item).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Delete Item", command=delete_item).grid(row=4, column=0, columnspan=2)

root.mainloop()