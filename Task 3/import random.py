# CodSoft Internship - July B37
# Domain - "PYTHON PROGRAMMING"
# Task 3: Password Generator
# Created by: AJAI SAM
# Date:  15 July 2025


import random
import string

print("🔐 Welcome to the New Password Generator!")

while True:
    # Step 1: Ask user for desired password length
    while True:
        user_input = input("\n😇 Please enter the length for your password: ")
        try:
            password_length = int(user_input)
            if password_length > 0:
                break
            else:
                print("😕 Password length must be a positive number.")
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    # Step 2: Prepare the character set
    letters = string.ascii_letters  # a-z and A-Z
    numbers = string.digits         # 0-9
    symbols = string.punctuation    # Special characters like !@#$

    all_characters = letters + numbers + symbols

    # Step 3: Generate the password
    generated_password = ""
    for i in range(password_length):
        generated_password += random.choice(all_characters)

    # Step 4: Display the generated password
    print(f"\n✅ Your new password is: {generated_password}")

    # Step 5: Ask if user wants another password
    again = input("\n🔁 Do you want to generate another password? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thank you for using the Password Generator! .")
        break