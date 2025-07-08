# CodSoft Internship - July B37
# Domain - "PYTHON PROGRAMMING"
# Task 1: TO-DO LIST
# Created by: AJAI SAM.A
# Date:  03 July 2025

tasks = []  # (This list will store all the tasks)

def show_menu():
    print("\n=== AJAI SAM's TO-DO LIST ===")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Mark a task as done")
    print("5. Exit the app")

def view_tasks():
    if not tasks:
        print("📝 Your task list is empty.")
    else:
        print("\n📋 Tasks:")
        for i, (task, done, priority) in enumerate(tasks, 1):
            status = "✅" if done else "❌"
            print(f"{i}. {task} [{status}] - Priority: {priority}")

def add_task():
    task = input("Enter your task: ")
    priority = input("Set priority (High/Medium/Low): ").capitalize()
    tasks.append((task, False, priority))
    print("✅ Task added successfully!")

def remove_task():
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("🗑️ Task removed.")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            task, _, priority = tasks[num - 1]
            tasks[num - 1] = (task, True, priority)
            print("🎊 Task marked as done!")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🔁 Main program loop
while True:
    show_menu()
    choice = input("Select an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print(" 👍 Your All Set ❣️💫✨ Have a Good day!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
