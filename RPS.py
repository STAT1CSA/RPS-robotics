# python
import random

def get_user_choice():
    
    # Function to get the user's choice of rock, paper, or scissors.
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    
    # Function to randomly generate the computer's choice of rock, paper, or scissors.

    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    
    # Function to determine the winner of the game based on the user's and computer's choices.
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    
    # Function to play the rock-paper-scissors game.
    
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid choice. Please enter yes or no: ").lower()
        if play_again == "no":
            break

play_game()

