# Mini Project Expense Tracker

# List of expenses in form of dictionaries
expenses = [] 

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Utilities): ")
    description = input("Enter a brief description: ")
    amount = float(input("Enter the amount spent: "))
    expense_record = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense_record)
    print("Expense added successfully!")



def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return []
    else:
        print("\nRecorded Expenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
                  f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
        return expenses


def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses So Far: ${total:.2f}")
    return total
                 


def main():
    while True:
        print("\n" + "=" * 40)
        print("   Mini Project Expense Tracker")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        print("=" * 40)

        input_choice = int(input("Enter your choice (1-4): "))
        match input_choice:
            case 1:
                print("\nYou selected to Add Expense.")
                add_expense()
            case 2:
                print("\nYou selected to View Expenses.")
                view_expenses()
            case 3:
                print("\nYou selected to View Total Expenses.")
                total_expenses()
            case 4:
                print("\nExiting the Expense Tracker. Goodbye!")
                break
            case _:
                print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
