import tkinter as tk

ALL_STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

def update_search(*args):
    query = search_var.get().strip().lower()
    state_listbox.delete(0, tk.END)
    matching_states = [s for s in ALL_STATES if query in s.lower()]
    
    if matching_states:
        for state in matching_states:
            state_listbox.insert(tk.END, state)
        status_label.config(text=f"Found {len(matching_states)} state(s)", fg="green")
    else:
        status_label.config(text="No matching states found", fg="red")

def clear_search():
    search_var.set("")
    update_search()

root = tk.Tk()
root.title("U.S. State Search")
root.geometry("340x380")
root.resizable(False, False)

title_label = tk.Label(root, text="U.S. State Search Tool", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=8)

search_label = tk.Label(root, text="Search:", font=("Arial", 10))
search_label.grid(row=1, column=0, sticky="e", padx=5, pady=2)

search_var = tk.StringVar()
search_var.trace_add("write", update_search)

search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 10), width=18)
search_entry.grid(row=1, column=1, sticky="w", padx=5, pady=2)

clear_btn = tk.Button(root, text="Clear Search", command=clear_search, font=("Arial", 9))
clear_btn.grid(row=2, column=0, columnspan=2, pady=4)

state_listbox = tk.Listbox(root, font=("Arial", 10), width=28, height=10)
state_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

status_label = tk.Label(root, text="", font=("Arial", 9, "italic"))
status_label.grid(row=4, column=0, columnspan=2, pady=2)

update_search()

root.mainloop()