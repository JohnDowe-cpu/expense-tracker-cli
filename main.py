EXPENSES_FILE = "expenses.txt"


def show_menu() -> None:
    """Display the main menu options."""

    print("\nExpense Tracker CLI")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Search expenses")
    print("4. View spending summary")
    print("5. Quit")


def get_menu_choice() -> str:
    """Prompt the user to choose a menu option."""

    return input("Please choose a menu option: ").strip()


def get_expense_amount() -> float:
    """Prompt for a valid expense amount."""

    while True:
        try:
            amount = float(input("What is the expense amount?: "))
            if amount <= 0:
                print("Please enter an amount above 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def get_required_text(prompt: str) -> str:
    """Prompt for required text input."""

    while True:
        text = input(prompt).strip()

        if text:
            return text
        else:
            print("This field cannot be blank.")


def add_expense() -> dict:
    """Collect expense information from the user."""

    expense_date = get_required_text("What is the expense date? (YYYY-MM-DD): ")
    category = get_required_text(
        "What is the category of expense? (Rent/Hygiene/etc.): "
    )
    amount = get_expense_amount()
    notes = input("Notes: ").strip()

    expense = {
        "date": expense_date,
        "category": category,
        "amount": amount,
        "notes": notes,
    }

    print("\nExpense Added")
    print(f"Date: {expense['date']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: ${expense['amount']:.2f}")
    print(f"Notes: {expense['notes']}")

    return expense


def save_expense(expense: dict) -> None:
    """Save an expense entry to the expenses file."""

    with open(EXPENSES_FILE, "a", encoding="utf-8") as file:
        file.write("Expense Log\n")
        file.write(f"Date: {expense['date']}\n")
        file.write(f"Category: {expense['category']}\n")
        file.write(f"Amount: ${expense['amount']:.2f}\n")
        file.write(f"Notes: {expense['notes']}\n")
        file.write("--------------------\n")


def view_expenses() -> None:
    """Display all saved expense entries."""

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            saved_expenses = file.read()

            if saved_expenses.strip():
                print("\nSaved Expenses")
                print(saved_expenses)
            else:
                print("No saved expenses found yet.")
    except FileNotFoundError:
        print("No saved expenses found yet.")


def search_expenses() -> None:
    """Search saved expense entries."""

    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Please enter something to search.")
        return

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            saved_expenses = file.read()

            if not saved_expenses.strip():
                print("No saved expenses found yet.")
            elif search_term.lower() in saved_expenses.lower():
                print(f"{search_term} found in expenses.")
            else:
                print(f"{search_term} not found.")
    except FileNotFoundError:
        print("No saved expenses found yet.")


def count_expenses() -> int:
    """Count the total number of saved expenses."""

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            return content.count("Expense Log")
    except FileNotFoundError:
        return 0


def calculate_total_spent() -> float:
    """Calculate the total amount of money spent."""

    total = 0.0

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Amount: $"):
                    amount_text = line.replace("Amount: $", "").strip()
                    total += float(amount_text)

        return total
    except FileNotFoundError:
        return 0


def view_spending_summary() -> None:
    """Display a summary of saved expenses."""

    total_expenses = count_expenses()
    total_spent = calculate_total_spent()

    print("\nSpending Summary")
    print(f"Total expenses logged: {total_expenses}")
    print(f"Total spent: ${total_spent:.2f}")


def main() -> None:
    """Run the Expense Tracker CLI application."""

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            expense = add_expense()
            save_expense(expense)
            print(f"Expense saved to {EXPENSES_FILE}")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            view_spending_summary()
        elif choice == "5":
            print("Expense Tracker CLI closed.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()
