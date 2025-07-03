import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        # Title Label
        tk.Label(root, text="My To-Do List", font=("Helvetica", 18)).pack(pady=10)

        # Entry for new tasks
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, fill=tk.X, padx=20)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Task", width=12, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete Task", width=12, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Save Tasks", width=12, command=self.save_tasks).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Load Tasks", width=12, command=self.load_tasks).grid(row=1, column=1, padx=5, pady=5)

        # Task listbox
        self.listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE, width=35, height=15)
        self.listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
