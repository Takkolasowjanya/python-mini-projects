# PERSONAL EXPENSE TRACKER APPLICATION

expenses = []


# Function to add an expense
def add_expense():
    date = input("Enter Date: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Function to view all expenses
def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found.")
    else:
        print("\n========== ALL EXPENSES ==========")

        for expense in expenses:
            print("Date        :", expense["date"])
            print("Category    :", expense["category"])
            print("Amount      : ₹", expense["amount"])
            print("Description :", expense["description"])
            print("---------------------------------")


# Function to calculate total expenses
def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expenses = ₹", total)


# Function to search expenses by category
def category_expenses():
    category = input("Enter Category: ")

    found = False

    print("\n========== CATEGORY EXPENSES ==========")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("Date        :", expense["date"])
            print("Amount      : ₹", expense["amount"])
            print("Description :", expense["description"])
            print("---------------------------------")
            found = True

    if found == False:
        print("No expenses found in this category.")


# Main program
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Wise Expenses")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total_expenses()

    elif choice == 4:
        category_expenses()

    elif choice == 5:
        print("Thank You for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Please try again.")