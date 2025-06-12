# 💸 Personal Finance Tracker (Python CLI)

## 📋 Project Overview
This is a simple command-line personal finance tracker built in Python. It allows users to log expenses, categorize them, and view summaries of their spending. The project reinforces core Python programming skills by simulating a real-world task in personal budgeting.

---

## ▶️ How to Run the Script
- Make sure you have Python installed (Python 3.x recommended).
- Open a terminal or command prompt.
- Navigate to the folder where the file is saved.
- Run the program using: **ctrl +f5**  
- Follow the menu prompts by entering the menu item numbers and later the data type requested

---

## 🧠 Python Concepts Used

This project applies several fundamental Python programming concepts:

- **Variables and Data Types**
  - Strings (`str`) for descriptions and categories  
  - Floats (`float`) for monetary amounts  
  - Tuples (`(description, amount)`) to store individual expense entries  
  - Lists (`[tuple1, tuple2, ...]`) to store multiple entries per category  
  - Dictionaries (`{category: list}`) to organize data  

- **Control Structures**
  - `if`, `else`, and `while` statements for menu logic and input validation  

- **Loops**
  - `for` loops to iterate through expense data  
  - `while` loops to keep the program running and manage repeated input  

- **Functions**
  - Modular design using functions like `view_expenses()` and `view_summary()` for clarity and reuse  

- **String Operations**
  - Using f-strings to format printed output  

- **Exception Handling**
  - `try-except` blocks to catch invalid input types (like letters instead of numbers)

---

## ✅ Features

- Add expense entries with a description, category, and amount  
- View all expenses grouped by category  
- Summarize total spending by category  
- Handle invalid inputs gracefully  
- Simple and clean command-line interface  

---

## 📌 Example

Welcome to the Personal Finance Tracker!
What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit > 1

Enter expense description: Lunch
Enter category: Food
Enter amount: 12.5
Expense added successfully.

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit > 2

Category: Food
- Lunch : $12.5

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit > 3

Summary:
Food: $12.50
