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

def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            print("Add expense feature coming soon.")
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

