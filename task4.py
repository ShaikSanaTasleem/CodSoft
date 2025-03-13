import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        update_score('user')
    else:
        result = "You lose!"
        update_score('computer')
    
    # Update the result label
    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Function to update scores
def update_score(winner):
    global user_score, computer_score
    if winner == 'user':
        user_score += 1
    else:
        computer_score += 1
    label_score.config(text=f"User  Score: {user_score} | Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_score.config(text=f"User  Score: {user_score} | Computer Score: {computer_score}")
    label_result.config(text="")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create buttons for user choices
tk.Button(root, text="Rock", command=lambda: determine_winner('Rock')).pack(pady=10)
tk.Button(root, text="Paper", command=lambda: determine_winner('Paper')).pack(pady=10)
tk.Button(root, text="Scissors", command=lambda: determine_winner('Scissors')).pack(pady=10)

# Label to display results
label_result = tk.Label(root, text="", font=("Helvetica", 14))
label_result.pack(pady=20)

# Label to display scores
label_score = tk.Label(root, text=f"User  Score: {user_score} | Computer Score: {computer_score}", font=("Helvetica", 14))
label_score.pack(pady=20)

# Button to reset the game
tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

# Start the GUI event loop
root.mainloop()