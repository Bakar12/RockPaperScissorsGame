# Rock, Paper, Scissors Game (GUI Version)

This project is a graphical user interface (GUI) version of the classic **Rock, Paper, Scissors** game, implemented using Python's `tkinter` library. The user plays against the computer, and the program determines the winner according to the traditional game rules.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Data Structures Used](#data-structures-used)
4. [Algorithm](#algorithm)
5. [GUI Design](#gui-design)
6. [How to Run the Game](#how-to-run-the-game)
7. [Requirements](#requirements)
8. [Future Improvements](#future-improvements)

---

## Overview

In this game:
- The player selects **Rock**, **Paper**, or **Scissors** using buttons.
- The computer randomly selects its choice from the same set of options.
- The game compares both choices and declares the winner.
- After each round, the user is asked if they want to play again via Yes/No buttons.

The game continues until the user chooses to stop. Scores are updated and displayed after every round.

---

## Features

- **Graphical User Interface**: Interactive buttons for gameplay.
- **Score Tracking**: The game keeps track of the player's and computer's scores across multiple rounds.
- **Random Computer Choice**: The computer makes a random selection each round.
- **Play Again Option**: After each round, the player can decide whether to continue playing or exit.
- **Result Display**: Shows the outcome of each round (win, lose, tie) and the current scores.

---

## Data Structures Used

The program utilizes a few basic data structures:

1. **List**:
   - The possible choices for the game (`rock`, `paper`, `scissors`) are stored in a list. This makes it easy to randomly select one for the computer.
   - Example: `["rock", "paper", "scissors"]`

2. **String Variables**:
   - The user's choice and the computer's choice are stored as strings for easy comparison.
   - Example: `user_choice = "rock"` and `computer_choice = "scissors"`

3. **Integer Variables**:
   - Counters for **user score**, **computer score**, and **rounds played** are stored as integer variables.
   - Example:
     ```python
     user_score = 0
     computer_score = 0
     rounds = 0
     ```

---

## Algorithm

The game follows a simple algorithm to determine the winner in each round:

1. **Input**:
   - The user makes a choice by clicking a button (either "Rock", "Paper", or "Scissors").
   - The computer makes a random choice using Python's `random.choice()` function from the list of available options.

2. **Comparison**:
   - The program compares the user's choice and the computer's choice using the following logic:
     - **Rock beats Scissors**
     - **Scissors beat Paper**
     - **Paper beats Rock**
   - If both the user and the computer choose the same option, the round is a tie.

3. **Output**:
   - The result of each round (win, lose, or tie) is displayed to the user along with the updated scores.
   - After each round, the user is prompted with Yes/No buttons to decide whether to continue playing or quit.

4. **Decision Flow**:
   - After displaying the result of the current round, the game waits for the user to decide if they want to play again.
   - If the user chooses "Yes", the game resets for another round.
   - If the user chooses "No", the game ends, and the final score is displayed.

### Pseudo-Code for the Algorithm:

```pseudo
while user wants to play:
    get user_choice (from GUI button click)
    computer_choice = random_choice(rock, paper, scissors)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or
         (user_choice == "scissors" and computer_choice == "paper") or
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    display result and updated scores

    ask if the user wants to play again
    if user chooses "No":
        display final scores
        exit
```

---

## GUI Design

The graphical interface for the game is built using the tkinter library, which allows for interactive elements like buttons and labels. Below is an explanation of the key GUI components:

1. Main Window:

   * The main game window is created using tk.Tk(). All buttons and labels are placed inside this window.

2. Buttons:

   * Rock, Paper, Scissors Buttons: These buttons allow the user to make their move. Each button is associated with a function that processes the user’s choice and triggers the round.
   * Yes/No Buttons: After each round, these buttons ask the user if they want to play again.
   
3. Labels:

   * Title and Instructions: The title of the game and a brief instruction are displayed at the top.
   * Result Label: After each round, this label shows the user’s choice, the computer’s choice, and the result of the round.
   * Score Label: Displays the current scores and the total number of rounds played.

4. Layouts:

    * Widgets are placed using pack() and grid() methods from tkinter, which help in arranging buttons and labels in the desired locations within the window.

---

## How to Run the Game

To run the game, follow these steps:

1. **Clone the Repository**:
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone
        ```
2. **Navigate to the Directory**:

3. **Run the Python Script**:
   - Run the Python script `rock_paper_scissors.py` using the following command:
     ```bash
     python rock_paper_scissors.py
     ```
---

## Future Improvements:

Here are some potential improvements that can be added to the game:

1. Best of N Rounds: Add an option to play a fixed number of rounds (like best of 3 or best of 5).
2. Animations: Add animations or effects for when the user and computer make their choices.
3. Sound Effects: Add sound effects for when the user clicks a button, or a round result is displayed.
4. Leaderboard: Keep track of the highest scores across multiple sessions.
