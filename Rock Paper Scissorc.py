import tkinter as tk
import random

# ----------------------------
# Settings
# ----------------------------
BG = "#1e1e1e"
FRAME = "#2d2d2d"
BTN = "#3a3a3a"
BTN_HOVER = "#505050"
TEXT = "#ffffff"
ACCENT = "#00c853"

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# ----------------------------
# Game Logic
# ----------------------------
def determine_winner(user, computer):
    global player_score, computer_score

    if user == computer:
        return "Tie!"

    if (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        player_score += 1
        return "You Win!"

    computer_score += 1
    return "Computer Wins!"

def play(choice):
    disable_buttons()
    countdown(choice, 3)

def countdown(choice, num):
    if num > 0:
        result_label.config(text=f"{num}...")
        root.after(1000, lambda: countdown(choice, num - 1))
    else:
        computer = random.choice(choices)
        result = determine_winner(choice, computer)

        result_label.config(
            text=f"You: {choice}\nComputer: {computer}\n\n{result}"
        )

        score_label.config(
            text=f"Player: {player_score}   |   Computer: {computer_score}"
        )

        enable_buttons()

# ----------------------------
# Button Helpers
# ----------------------------
def disable_buttons():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def enable_buttons():
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

# ----------------------------
# Window
# ----------------------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x450")
root.configure(bg=BG)
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    bg=BG,
    fg=ACCENT,
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Score
score_label = tk.Label(
    root,
    text="Player: 0   |   Computer: 0",
    bg=BG,
    fg=TEXT,
    font=("Arial", 14)
)
score_label.pack()

# Button Frame
frame = tk.Frame(root, bg=FRAME)
frame.pack(pady=30)

# Buttons
rock_btn = tk.Button(
    frame,
    text="🪨 Rock",
    width=12,
    height=2,
    bg=BTN,
    fg=TEXT,
    font=("Arial", 12, "bold"),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10, pady=10)

paper_btn = tk.Button(
    frame,
    text="📄 Paper",
    width=12,
    height=2,
    bg=BTN,
    fg=TEXT,
    font=("Arial", 12, "bold"),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(
    frame,
    text="✂️ Scissors",
    width=12,
    height=2,
    bg=BTN,
    fg=TEXT,
    font=("Arial", 12, "bold"),
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Result
result_label = tk.Label(
    root,
    text="Choose your move!",
    bg=BG,
    fg=TEXT,
    font=("Arial", 16)
)
result_label.pack(pady=30)

root.mainloop()