import tkinter as tk
import random
user_score = 0
computer_score = 0
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"
def user_choice(choice):
    global user_score, computer_score
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_scores()
def update_scores():
    user_label.config(text=f"User: {user_score}")
    computer_label.config(text=f"Computer: {computer_score}")
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x350")
root.config(bg="#F0F8FF")
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#F0F8FF")
title_label.pack(pady=10)
scores_frame = tk.Frame(root, bg="#F0F8FF")
scores_frame.pack(pady=5)
user_label = tk.Label(scores_frame, text=f"User: {user_score}", font=("Helvetica", 12), bg="#F0F8FF")
user_label.grid(row=0, column=0, padx=5)
computer_label = tk.Label(scores_frame, text=f"Computer: {computer_score}", font=("Helvetica", 12), bg="#F0F8FF")
computer_label.grid(row=0, column=1, padx=5)
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#F0F8FF")
result_label.pack(pady=10)
buttons_frame = tk.Frame(root, bg="#F0F8FF")
buttons_frame.pack(pady=10)
rock_button = tk.Button(buttons_frame, text="Rock", font=("Helvetica", 12), width=10, bg="#3498DB", fg="#ECF0F1", command=lambda: user_choice("rock"))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(buttons_frame, text="Paper", font=("Helvetica", 12), width=10, bg="#3498DB", fg="#ECF0F1", command=lambda: user_choice("paper"))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(buttons_frame, text="Scissors", font=("Helvetica", 12), width=10, bg="#3498DB", fg="#ECF0F1", command=lambda: user_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=5)
reset_button = tk.Button(root, text="Reset Scores", font=("Helvetica", 12), width=15, bg="#E74C3C", fg="#ECF0F1", command=reset_scores)
reset_button.pack(pady=10)
root.mainloop()
