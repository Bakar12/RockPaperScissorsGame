# Rock, Paper, Scissors Game

import random
import tkinter as tk
from tkinter import messagebox


# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


# Function to determine the winner based on user and computer choice
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


# Function to handle user choice and update results
def play_round(user_choice):
    global user_score, computer_score, rounds

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Update the result label with the current round result
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

    # Update scores and round count
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    rounds += 1

    # Show the updated scores
    score_label.config(text=f"Rounds Played: {rounds}\nYour Score: {user_score}\nComputer Score: {computer_score}")

    # Ask if the user wants to play again
    play_again_frame.pack(pady=20)


# Function to handle play again decision
def play_again_decision(decision):
    if decision == "yes":
        result_label.config(text="Make your move!")
        play_again_frame.pack_forget()
    else:
        messagebox.showinfo("Game Over",
                            f"Final Score:\nRounds Played: {rounds}\nYour Score: {user_score}\nComputer Score: "
                            f"{computer_score}")
        root.quit()


# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize variables for scores and rounds
user_score = 0
computer_score = 0
rounds = 0

# Create and place GUI components

# Title Label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24))
title_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 16))
instruction_label.pack(pady=10)

# Frame for buttons (Rock, Paper, Scissors)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Rock Button
rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=10)

# Paper Button
paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=10)

# Scissors Button
scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10,
                            command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Result Label to show the round result
result_label = tk.Label(root, text="Make your move!", font=("Arial", 16))
result_label.pack(pady=20)

# Score Label to display the current scores and rounds played
score_label = tk.Label(root,
                       text=f"Rounds Played: {rounds}\nYour Score: {user_score}\nComputer Score: {computer_score}",
                       font=("Arial", 14))
score_label.pack(pady=20)

# Frame for Play Again buttons (Yes/No)
play_again_frame = tk.Frame(root)

# Do you want to play again? Label

play_again_label = tk.Label(play_again_frame, text="Do you want to play again?", font=("Arial", 14))
play_again_label.grid(row=0, column=0, columnspan=2, pady=8)

# Yes Button
yes_button = tk.Button(play_again_frame, text="Yes", font=("Arial", 14), width=10,
                       command=lambda: play_again_decision("yes"))
yes_button.grid(row=1, column=0, padx=10)

# No Button
no_button = tk.Button(play_again_frame, text="No", font=("Arial", 14), width=10,
                      command=lambda: play_again_decision("no"))
no_button.grid(row=1, column=1, padx=10)

# Run the main event loop
root.mainloop()
