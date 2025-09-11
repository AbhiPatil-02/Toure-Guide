import tkinter as tk
from tkinter import messagebox, simpledialog
from auth import signup, login

class LoginDialog(simpledialog.Dialog):

    def body(self, master):
        self.title("Login")

        tk.Label(master, text="Username:").grid(row=0)
        tk.Label(master, text="Password:").grid(row=1)

        self.username_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show='*')

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        return self.username_entry  # initial focus

    def apply(self):
        self.result = (self.username_entry.get(), self.password_entry.get())

class SignupDialog(simpledialog.Dialog):

    def body(self, master):
        self.title("Signup")

        tk.Label(master, text="Username:").grid(row=0)
        tk.Label(master, text="Password:").grid(row=1)
        tk.Label(master, text="Confirm Password:").grid(row=2)

        self.username_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show='*')
        self.confirm_entry = tk.Entry(master, show='*')

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        self.confirm_entry.grid(row=2, column=1)
        return self.username_entry  # initial focus

    def apply(self):
        self.result = (self.username_entry.get(), self.password_entry.get(), self.confirm_entry.get())

# Helper wrapper functions for use in your main app

def show_login(root):
    dialog = LoginDialog(root)
    if dialog.result:
        username, password = dialog.result
        if username and password:
            user = login(username, password)
            if user:
                messagebox.showinfo("Success", f"Logged in as {username}")
                return user  # tuple with DB user data
            else:
                messagebox.showerror("Error", "Invalid username or password")
        else:
            messagebox.showwarning("Input required", "Please enter username and password")
    return None

def show_signup(root):
    dialog = SignupDialog(root)
    if dialog.result:
        username, password, confirm = dialog.result
        if not (username and password and confirm):
            messagebox.showwarning("Input required", "All fields are required")
            return None
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return None
        try:
            signup(username, password)
            messagebox.showinfo("Success", "Account created successfully")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Signup failed: {str(e)}")
    return None
