import tkinter as tk
from tkinter import ttk

data = {
    "S001": {
        "name": "Aarav Sharma",
        "course": "Python",
        "score": 92,
        "attendance": 96,
        "performance": "Excellent",
        "status": "Active",
        "classes": 24,
    },
    "S002": {
        "name": "Diya Patel",
        "course": "Data Science",
        "score": 84,
        "attendance": 91,
        "performance": "Good",
        "status": "Active",
        "classes": 21,
    },
    "S003": {
        "name": "Rohan Das",
        "course": "Web Development",
        "score": 67,
        "attendance": 78,
        "performance": "Average",
        "status": "Active",
        "classes": 18,
    },
    "S004": {
        "name": "Ananya Roy",
        "course": "Python",
        "score": 45,
        "attendance": 65,
        "performance": "Needs Improvement",
        "status": "At Risk",
        "classes": 12,
    },
    "S005": {
        "name": "Vikhyath Pragadareddi",
        "course": "Python",
        "score": 88,
        "attendance": 94,
        "performance": "Good",
        "status": "Active",
        "classes": 22,
    },
    "S006": {
        "name": "Vihaan Kumar",
        "course": "Data Science",
        "score": 79,
        "attendance": 85,
        "performance": "Good",
        "status": "Active",
        "classes": 20,
    },
}

root = tk.Tk()
root.title("Performance Dashboard")
root.geometry("1200x720")
root.minsize(1000, 600)

root.configure(bg="#f4f6f8")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="white",
    foreground="#263238",
    rowheight=42,
    fieldbackground="white",
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    background="#263238",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[("selected", "#dbeafe")],
    foreground=[("selected", "#111827")]
)

style.configure(
    "Horizontal.TProgressbar",
    thickness=8,
    background="#2563eb",
    troughcolor="#e5e7eb"
)

header = tk.Canvas(
    root,
    height=150,
    highlightthickness=0
)

header.pack(fill="x")

header.create_rectangle(0, 0, 1200, 150, fill="#2563eb", outline="")
header.create_text(30, 75, text="Science Fair Dashboard", fill="white", font=("Segoe UI", 20, "bold"), anchor="w")

lbl = tk.Label(root, text="Student Performance Overview", bg="#f4f6f8", fg="#6b7280", font=("Segoe UI", 10))
lbl.pack(anchor="w", padx=20, pady=(15, 5))

tree = ttk.Treeview(root, columns=("id", "name", "course", "score", "status"), show="headings")
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("course", text="Course")
tree.heading("score", text="Score")
tree.heading("status", text="Status")

tree.tag_configure("active", foreground="green")
tree.tag_configure("at_risk", foreground="red")

for sid, info in data.items():
    tag = "at_risk" if info["status"] == "At Risk" else "active"
    tree.insert("", "end", values=(sid, info["name"], info["course"], info["score"], info["status"]), tags=(tag,))

tree.pack(fill="both", expand=True, padx=20, pady=20)

root.mainloop()