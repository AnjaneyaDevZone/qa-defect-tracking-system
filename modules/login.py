import customtkinter as ctk
from tkinter import messagebox
import sqlite3


# ==========================================
# LOGIN FUNCTION
# ==========================================

def login():

    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("database/defect_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT role FROM users
    WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        role = user[0]

        messagebox.showinfo(
            "Login Successful",
            f"Welcome {role}"
        )

    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )


# ==========================================
# MAIN WINDOW
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("QA Defect Tracking System")
app.geometry("500x500")


# ==========================================
# TITLE
# ==========================================

title = ctk.CTkLabel(
    app,
    text="QA Defect Tracking System",
    font=("Arial", 24, "bold")
)

title.pack(pady=30)


# ==========================================
# USERNAME
# ==========================================

username_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Username",
    width=300,
    height=40
)

username_entry.pack(pady=20)


# ==========================================
# PASSWORD
# ==========================================

password_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Password",
    show="*",
    width=300,
    height=40
)

password_entry.pack(pady=20)


# ==========================================
# LOGIN BUTTON
# ==========================================

login_button = ctk.CTkButton(
    app,
    text="Login",
    command=login,
    width=200,
    height=40
)

login_button.pack(pady=30)


# ==========================================
# RUN APPLICATION
# ==========================================

app.mainloop()