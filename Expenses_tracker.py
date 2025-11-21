import os
# It is file name where data will be stored
Record_book = "expenses.txt" # [1]

def add_expense():
    """Asks user for details and add to file."""
    print("\n--- Add New Expense ---")
    name = input("Enter name of expense(e.g., Burger): ")
    try:
        amount = float(input("Enter amount (e.g., 50): "))
    except ValueError:
        print("Error: Please enter a valid number for the amount.") # [1]
        return
    # We use 'a' mode to Append # [5]
    with open(Record_book, "a") as f:
        f.write(f"{name} = {amount}\n")
    print("Expense saved successfully!") # [5]

def view_expenses():
    """Reads the file and displays all items."""
    print("\n--- Your Expense History ---")
    if not os.path.exists(Record_book):
        print("No records found.")
        return # [5]
    with open(Record_book, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No expenses recorded yet.") # [5]
        else:
            print(f"{'Item Name':<20} {'Cost':<10}") # Formatting for alignment # [6]
            print("-" * 30)
            for line in lines:
                try:
                    name,amount = line.strip().split(" = ")
                    print(f"{name:<20} ₹{amount}")
                except ValueError:
                    continue # [6]

def calculate_total():
    """Calculates the sum of all expenses."""
    print("\n--- Total Spending ---")
    if not os.path.exists(Record_book):
        print("Total Spent: ₹0.0") # [7]
        return
    total = 0.0
    with open(Record_book, "r") as f:
        for line in f:
            try:
                parts = line.strip().split(" = ")
                total += float(parts[1])
            except (ValueError, IndexError):
                continue # [7]
    print(f"Total Amount Spent: ₹{total}") # [7]

def clear_history():
    """Wipes the file clean."""
    confirm = input("\nAre you sure you want to delete all records? (y/n): ")
    if confirm.lower() == 'y':
        with open(Record_book, "w") as f: # [9]
            f.write("") # Overwrite with nothing
            print("History cleared.")
    else:
        print("Operation cancelled.") # [9]

def main():
    """Main controller function.""" # [9] 
    while True:
        print("\n==========================")
        print(" PERSONAL EXPENSE TRACKER ")
        print("==========================")
        print("1. Add Expense")
        print("2. View Expense History")
        print("3. Show Total Spent")
        print("4. Clear Expense History")
        print("5. Exit") # [9]
        choice = input("Enter your choice (1-5): ") # [10]
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            clear_history()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") # [10]

# This line starts the program # [10]
if __name__ == "__main__":
    main()