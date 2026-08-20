import tkinter as tk

students = [
    {"name": "Alice", "science": 85},
    {"name": "Bob", "science": 92},
    {"name": "Charlie", "science": 78},
    {"name": "Daisy", "science": 98},
    {"name": "Ethan", "science": 88}
]

def get_top_student(data):
    if not data:
        return None
    top = data[0]
    for s in data:
        if s["science"] > top["science"]:
            top = s
    return top

root = tk.Tk()
root.title("Science Scores")

top_student = get_top_student(students)

tk.Label(root, text="Name", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Science", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)

for i, student in enumerate(students, start=1):
    if student == top_student:
        color = "red"
        text = student["name"] + " ⭐"
    else:
        color = "black"
        text = student["name"]

    tk.Label(root, text=text, fg=color).grid(row=i, column=0, padx=10, pady=2)
    tk.Label(root, text=student["science"], fg=color).grid(row=i, column=1, padx=10, pady=2)

root.mainloop()