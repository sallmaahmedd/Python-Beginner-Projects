import os
import csv
import datetime

filename = "expenses.csv"
BUDGET_FILE = "budget.txt"
expenses=[]

if os.path.exists(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            """ every value read from a CSV comes back as a string so we need to convert it to float """
            row["amount"] = float(row["amount"])
            expenses.append(row)

monthly_budget = 0
if os.path.exists(BUDGET_FILE):
    with open(BUDGET_FILE, "r") as file:
        monthly_budget = float(file.read())

while True:
    print("Budget Tracker")
    choice=input("""Choose an option:
                    1. View Expenses
                    2. Add Expense
                    3. Delete Expense
                    4. View Total Expenses
                    5. View Expenses by Category
                    6. View Expenses by Month
                    7. Set Monthly Budget
                    8. View Budget Status
                    9. Exit
                    """)

    def save_budget():
        with open(BUDGET_FILE, "w") as file:
            file.write(str(monthly_budget))

    def save_expenses():
        """newline="": without it, CSV files can end up with extra blank lines between rows"""
        with open(filename, "w", newline="") as file:
            """"DictWriter is a class inside the csv module. Calling csv.DictWriter(file, fieldnames=[...]) constructs a writer object, giving it the file to write into and the fieldnames to use."""
            writer = csv.DictWriter(file, fieldnames=["description", "category", "amount", "date"]) #constructs an object
            """Since the file starts completely empty, the very first save needs to write column headers as the first line"""
            writer.writeheader() #calls a method on that object
            writer.writerows(expenses)

    if choice=="1":
        if not expenses:
            print("No expenses logged yet!")
        else:
            """ reversed(): takes a sequence and gives it back in reverse order, without permanently changing expenses itself """
            for index, expense in enumerate(reversed(expenses), start=1):
                print(f"{index}. {expense['date']} - {expense['description']} - {expense['category']} - ${expense['amount']:.2f}")


    elif choice=="2":
        description=input("Enter expense description: ").strip()
        if description == "":
            print("Description cannot be empty.")
            description=input("Enter expense description: ").strip()

        category=input("Enter category: ").strip()
        if category == "":
            print("Category cannot be empty.")
            category=input("Enter category: ").strip()

        while True:
            try:
                amount = round(float(input("Enter amount: ")), 2)
                break
            except ValueError:
                print("Please enter a valid number for the amount.")

        while True:
            date = input("Enter date (YYYY-MM-DD), or leave blank for today: ").strip()
            if date == "":
                date = datetime.date.today().isoformat()
                break
            else:
                try:
                    datetime.date.fromisoformat(date)   
                    break                                 
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

        expenses.append({"description": description, "category": category, "amount": amount, "date": date})
        save_expenses()
        print("Expense added and saved!")


    elif choice=="3":
        if not expenses:
            print("Empty log! Nothing to delete.")
        else:
            for index, expense in enumerate(expenses, start=1):
                        print(f"{index}. {expense['date']} - {expense['description']} - {expense['category']} - ${expense['amount']:.2f}")

            while True:
                try:
                    expense_number = int(input("Enter the number of the expense to delete: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            if 1 <= expense_number <= len(expenses):
                expense_to_delete = expenses[expense_number - 1]
                print(f"You're about to delete: {expense_to_delete['date']} - {expense_to_delete['description']} - ${expense_to_delete['amount']:.2f}")
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == "y":
                    expenses.pop(expense_number - 1)
                    save_expenses()
                    print("Expense deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("No expense with that number.")

    elif choice=="4":
        if not expenses:
            print("Empty! No expenses to view.")
        else:
            total_expenses = sum(expense["amount"] for expense in expenses)
            print(f"Total expenses: ${total_expenses:.2f}")

    elif choice=="5":
        if not expenses:
                print("Empty! No expenses to view.")
        else:
            totals={}      #category -> total
            for expense in expenses:
                category=expense["category"]
                amount=expense["amount"]
        
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

            for category, total in totals.items():
                print(f"{category}: ${total:.2f}")

    elif choice=="6":
        if not expenses:
                    print("Empty! No expenses to view.")

        else:
            month=input("Enter month to view (YYYY-MM): ")
            month_expenses = [expense for expense in expenses if expense["date"].startswith(month)]
            if not month_expenses:
                print(f"No expenses found for {month}.")
            else:
                for index, expense in enumerate(month_expenses, start=1):
                    print(f"{index}. {expense['date']} - {expense['description']} - {expense['category']} - ${expense['amount']:.2f}")

                total = sum(expense["amount"] for expense in month_expenses)
                print(f"Total expenses for {month}: ${total:.2f}")

    elif choice=="7":
        while True:
            try:
                monthly_budget=round(float(input("What is the new monthly budget? ")),2)
                if monthly_budget <= 0:
                    print("Budget must be a positive number.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        save_budget()
        print(f"Monthly budget set to ${monthly_budget:.2f}")
            

    elif choice=="8":
        if not monthly_budget:
            print("Set a monthly budget first.")
        else:
            current_month = datetime.date.today().isoformat()[:7]   
            month_expenses = [e for e in expenses if e["date"].startswith(current_month)]
            total_spent = sum(e["amount"] for e in month_expenses)

            remaining = monthly_budget - total_spent
            print(f"Monthly budget: ${monthly_budget:.2f}")
            print(f"Total spent: ${total_spent:.2f}")
            percent_used = (total_spent / monthly_budget) * 100
            print(f"You've used {percent_used:.1f}% of your budget.")

            if remaining < 0:
                print(f"You are over budget by ${abs(remaining):.2f}!")
            else:
                print(f"Remaining budget: ${remaining:.2f}")
                

    elif choice=="9":
        save_expenses()
        save_budget()
        print("Goodbye! Your expenses and budget have been saved.")
        break

    else:
        print("Invalid choice. Please enter a number from 1-9.")

