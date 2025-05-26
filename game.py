import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie game!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win the game!")
elif user_choice in choices:
    print("You lose the game!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
