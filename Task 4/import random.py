# CodSoft Internship - July B37
# Domain - "PYTHON PROGRAMMING"
# Task 4: Rock-Paper-Scissors Game! 
# Created by: AJAI SAM
# Date:  20 July 2025

import random

print("😎 Welcome to the Rock-Paper-Scissors Game!")
print("📜 Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
print("🔁 You can keep playing until you decide to quit.\n")

# Score tracking variables
user_score = 0
computer_score = 0

# Available choices
choices = ["rock", "paper", "scissors"]

# Game loop
while True:
    # Get user input and normalize
    user_choice = input("👉 Choose Rock, Paper, or Scissors: ").strip().lower()

    if user_choice not in choices:
        print("❌ Invalid choice. Please enter 'rock', 'paper', or 'scissors'.\n")
        continue

    # Generate computer's random choice
    computer_choice = random.choice(choices)
    print(f"🧠 Computer chose: {computer_choice.capitalize()}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("💻 Computer wins this round.")
        computer_score += 1

    # Show current scores
    print(f"📊 Score → You: {user_score} | Computer: {computer_score}\n")

    # Ask if user wants to continue
    play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        print(f"🏁 Final Score → You: {user_score} | Computer: {computer_score}")
        break