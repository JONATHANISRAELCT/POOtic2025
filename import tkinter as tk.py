import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def delete_task(event=None):
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def close_app(event=None):
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)

frame = tk.Frame(root)
frame.pack()

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(frame, text="Complete", command=mark_completed)
complete_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(frame, text="Delete", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Keyboard shortcuts
root.bind("<c>", lambda event: mark_completed())
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", close_app)

root.mainloop()
