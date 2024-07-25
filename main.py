
def welcome_message():
    print('Welcome to the Daily Expense Tracker!')


def get_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category (e.g., Food, Transport, Entertainment): ")
    description = input("Enter a description for the expense: ")
    return {"amount": amount, "category": category, "description": description}

def display_summary(expenses):
    total_amount = sum(expense["amount"] for expense in expenses)
    print("\nExpense Summary:")
    print(f"Total amount spent: £{total_amount:.2f}")
    print("Detailed Expenses:")
    for expense in expenses:
        print(f"£{expense['amount']:.2f} on {expense['category']}: {expense['description']}")

def main():
    welcome_message()
    expenses = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Log an expense")
        print("2. View summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            expense = get_expense()
            expenses.append(expense)
            print("Expense logged successfully.")
        elif choice == "2":
            display_summary(expenses)
        elif choice == "3":
            print("Thank you for using the Daily Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()





