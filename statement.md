# Personal Expense Tracker

A simple, effective Python program designed to help students manage daily expenses and track pocket money.

## Problem Definition
As a student, it is often difficult to keep track of daily pocket money and expenses. We tend to spend money on small things like food or stationery and forget where the money went by the end of the month. We need a simple way to record these expenses on a computer so that the data is saved permanently.

## Proposed Solution
This **Personal Expense Tracker** allows the user to save their daily expenses into a text file. By using file handling, data is persistent—meaning it is not lost when the program is closed, unlike variables stored only in memory.

## Key Features (Scope)
The application performs the following four core tasks:

* ** Add Expense:** Takes the item name and cost from the user and appends it to the database.
* **View Records:** Reads the file and displays a history of all past expenses on the screen.
* **Calculate Total:** Reads costs from the file and sums them up to display total spending.
* **Reset:** Clears the file content to start a fresh record.

## Project Objectives
The main objective of this project is to demonstrate and practice basic Python programming concepts taught in the first semester:

1.  **Input/Output:** Handling user interaction via the console.
2.  **File Handling:** Implementing persistent storage using text files (`.txt`) for reading and writing data.
3.  **Data Type Conversion:** Converting string inputs into numerical values (integers/floats) for calculations.
4.  **Error Handling:** Implementing `try-except` blocks to prevent the program from crashing due to invalid inputs (e.g., entering text where a number is required).

## Tools & Technologies
* **Language:** Python 3.14
* **Editor:** Basic Code Editor (VS Code, IDLE, etc.)
* **Database:** Simple Text File (`expenses.txt`)

## How to Run
1.  Ensure you have Python installed on your system.
2.  Download the script file.
3.  Run the following command in your terminal:
    ```bash
    python your_script_name.py
    ```
4.  Follow the on-screen menu prompts to manage your expenses.
