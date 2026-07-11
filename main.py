def show_menu():
    print("\nExpense Tracker CLI")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Search expenses")
    print("4. View spending summary")
    print("5. Quit")

def get_menu_choice():
    choice = input("Please choose a menu option: ").strip()
    return choice

def get_expense_amount():
    while True:
        try:
            amount = float(input("What is the expense amount?: "))
            if amount <= 0:
                print("Please enter an amount above 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def add_expense():
    expense_date = input("What is the expense date? (YYYY-MM-DD): ").strip()
    category = input("What is the category of expense? (Rent/Hygiene/etc.): ").strip()
    amount = get_expense_amount()
    notes = input("Notes: ").strip()

    expense = {
        "date": expense_date,
        "category": category,
        "amount": amount,
        "notes": notes
    }
    
    print("\nExpense Added")
    print(f"Date: {expense['date']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: ${expense['amount']}")
    print(f"Notes: {expense['notes']}")

    return expense

def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("View expenses feature coming soon.")
        elif choice == "3":
            print("Search expenses feature coming soon.")
        elif choice == "4":
            print("View spending summary feature coming soon.")
        elif choice == "5":
            print("Expense Tracker CLI closed.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")

if __name__ == "__main__":
    main()

