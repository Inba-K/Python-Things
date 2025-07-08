import tkinter as tk
import random

window=tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1000x600")

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result_text = ""
    if player_choice == computer_choice:
        result_text = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_text = f"You win! {player_choice} beats {computer_choice}."
    else:
        result_text = f"You lose! {computer_choice} beats {player_choice}."

    player_label.config(text=f"You chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result_text)

player_label = tk.Label(window, text="You chose: ")
player_label.pack(pady=5)

computer_label = tk.Label(window, text="Computer chose: ")
computer_label.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

window.mainloop()
