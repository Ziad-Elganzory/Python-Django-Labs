from utils import add_employee, transfer, fire, show, list_all_employees
from db import initialize_db

def display_menu():
    """Displays the main menu options to the user."""
    print("\nEmployee Management System")
    print("Options:")
    print("  - Add Employee or Manager: 'add'")
    print("  - Transfer Employee: 'transfer'")
    print("  - Fire Employee: 'fire'")
    print("  - Show Employee: 'show'")
    print("  - List ALL Employees: 'list'")
    print("  - Exit Program: 'q'")
    print()

def main():
    """Main function to handle user inputs and control the program flow."""
    initialize_db()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == 'add':
            role = input("Are you adding an Employee ('e') or a Manager ('m')? ")
            add_employee(role)
        elif choice == 'transfer':
            transfer()
        elif choice == 'show':
            show()
        elif choice == 'fire':
            fire()
        elif choice == 'list':
            list_all_employees()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()