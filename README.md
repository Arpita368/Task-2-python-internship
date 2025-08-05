# 📝 To-Do List Console Application

This is a simple Python-based **To-Do List** app that allows users to manage tasks using a command-line interface. Users can add, remove, view tasks, and save the list to a file before exiting.

## 🚀 Features

- ✅ Add new tasks to your to-do list
- ❌ Remove tasks by their number
- 👁️ View all current tasks
- 💾 Save tasks to a file (`to_do_list.txt`) before exiting

## 🛠️ How It Works

The app runs in a continuous loop, presenting a menu with options. The user selects an option by entering the corresponding number:
MENU:
1. Add Task
2. Remove Task
3. View Tasks
4. Save tasks and Close the app

### 1. Add Task
Prompts the user to enter a task which is then appended to the list.

### 2. Remove Task
Asks for the task number to remove. If the task number is valid, it removes the corresponding task from the list.

### 3. View Tasks
Displays all tasks with their respective numbers.

### 4. Save and Exit
Saves all tasks to a file named `to_do_list.txt` and exits the application.

## 💻 How to Run

Make sure you have Python installed.

1. Copy the code into a file named `todo.py`.
2. Open terminal or command prompt.
3. Run the script:
python todo.py

# SAMPLE OUTPUT:
MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 1
Enter your task: Finish work presentation
Task added in the list

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 1
Enter your task: Pay utility bills
Task added in the list

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 1
Enter your task: Schedule doctor appointment
Task added in the list

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 1
Enter your task: Submit project report
Task added in the list

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 3

----------------------------
Tasks:
1. Finish work presentation
2. Pay utility bills
3. Schedule doctor appointment
4. Submit project report
----------------------------

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 2
Enter the task number: 3
Task removed from the list

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 3

----------------------------
Tasks:
1. Finish work presentation
2. Pay utility bills
3. Submit project report
----------------------------

MENU 
1. Add Task 
2. Remove Task 
3. View Tasks 
4. Save tasks and Close the app
Enter a number: 4
Tasks saved to 'to_do_list.txt'. Closing the application.

## Outputs saved in to_do_list.txt
1. Finish work presentation
2. Pay utility bills
3. Submit project report
   
## Author 
Created by Arpita Jitendra Sonparote

## 📜 License 
This project is open for educational use. You may modify or reuse the scripts.
