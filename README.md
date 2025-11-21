# Expenses_tracker
________________________________________
Project Title: Personal Expense Tracker
Domain: Finance & Banking
Course: Vityarthi Python Programming
________________________________________
Phase 1: Problem Definition
Real-World Problem:
University students often operate on a fixed monthly budget. Due to frequent small transactions (snacks, stationery, transport), it is difficult to mentally track spending. This leads to overspending and financial stress by the month-end.
Objective:
To develop a command-line interface (CLI) application that allows users to record daily expenses, view their spending history, and see the total amount spent, ensuring better financial awareness.
________________________________________
Phase 2: Requirement Analysis
To solve this problem, the system requires the following features:
1.	Input Mechanism: The user must be able to input the Description (e.g., "Lunch") and the Amount (e.g., 50).
2.	Data Persistence: The data must be saved to a text file (expenses.txt) so records remain even after the program is closed.
3.	Reporting: The system must read the file and display all past expenses.
4.	Calculation: The system must sum up all expense amounts to show a "Total Spent."
5.	Reset: A feature to clear all data (e.g., for a new month).
________________________________________
Phase 3: Top-Down Design (Modularization)
We will break the program into specific functions to keep the code clean.
•	main(): The central controller that shows the menu and handles user choices.
•	add_expense(): Handles input validation and writing data to the file.
•	view_expenses(): Reads the file and prints the history line-by-line.
•	calculate_total(): Reads the file, extracts the numbers, and sums them up.
•	clear_history(): Deletes the content of the file.
________________________________________
Phase 4: Algorithm Development (Pseudocode)
START
  Create file 'expenses.txt' if it doesn't exist
  LOOP forever:
    Display Menu (1. Add, 2. View, 3. Total, 4. Clear, 5. Exit)
    Get User Choice
    IF Choice is 1:
      Ask for Expense Name and Amount
      Append "Name = Amount" to file
    ELSE IF Choice is 2:
      Read file line by line
      Print each line
    ELSE IF Choice is 3:
      Initialize Total = 0
      For every line in file:
        Split line by comma
        Add Amount to Total
      Print Total
    ELSE IF Choice is 5:
      Break Loop
  END LOOP
STOP
________________________________________
Phase 5: Implementation (Python Code)
It is in the file named “Expenses_tracker.py”
________________________________________
Phase 6: Testing and Refinement
When we run the code, we should perform these tests to ensure it works correctly. 
Test Case 1: Input Validation
•	Action: Select "Add Expense". Enter "Lunch" for the name and "abc" for the amount.
•	Expected Result: The program should catch the error and say "Please enter a valid number" instead of crashing.
Test Case 2: Data Accuracy
•	Action: Add "Pen" (10) and "Notebook" (40). Then select "Show Total Spent".
•	Expected Result: The output should be exactly ₹50.0.
Test Case 3: Persistence
•	Action: Add an expense. Close the Python program. Run it again. Select "View History".
•	Expected Result: The expense you added previously should still be there (loaded from the file).



