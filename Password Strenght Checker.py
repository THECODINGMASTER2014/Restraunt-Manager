import tkinter as tk
from tkinter import messagebox
import re

def check_strength():
    password = entry.get()

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        result.config(text="Weak Password", fg="red")
    elif score <= 4:
        result.config(text="Medium Password", fg="orange")
    else:
        result.config(text="Strong Password", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#222222")

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="#222222",
    fg="white"
)
title.pack(pady=15)

entry = tk.Entry(
    root,
    show="*",
    width=30,
    font=("Arial", 12)
)
entry.pack(pady=10)

check_btn = tk.Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="#444444",
    fg="white",
    font=("Arial", 11)
)
check_btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#222222"
)
result.pack(pady=15)

root.mainloop()