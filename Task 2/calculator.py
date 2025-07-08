# CodSoft Internship - July B37
# Domain - "PYTHON PROGRAMMING"
# Task 2: CALCULATOR 
# Created by: AJAI SAM
# Date:  08 July 2025


print("Welcome to Simple Calculator 🔢")

while True:              # To create an infinite loop that keeps running ,unless you break it manually using break
    print("\nChoose num1")
    num1 = float(input("Enter first number: "))
    print("\nChoose num2")
    num2 = float(input("Enter second number: "))

    print("Choose operation: +  -  *  /")
    operation = input("Enter operation: ")

    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print(" Oops 😇 That operation isn't Recognized ")

    # Ask if user wants to continue

    again = input("\n Do you want to perform another calculation? (yes/no): ").lower() #It converts the input string to lowercase
    if again != 'yes':
        print("Thanks for using the calculator! ❤️")
        break