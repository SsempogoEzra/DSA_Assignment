import farmer_management
import transactions
import statement

def display_menu():
    print("\n--- SACCO Management System ---")
    print("1. Create New Farmer Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Get Last N Transactions")
    print("6. Exit")
    print("-----------------------------")

def get_int_input(prompt): #gets user  functions with error handling
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_float_input(prompt):
    """Gets a float input from the user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def get_string_input(prompt):
    """Gets a string input from the user."""
    return input(prompt).strip()

#Main function to run the CLI programm.
def main():
    while True:
        display_menu()
        choice = get_int_input("Enter your choice: ")

        if choice == 1:
            farmer_management.create_new_farmer()
        elif choice == 2:
            farmer_id = get_string_input("Enter Farmer ID: ")
            amount = get_float_input("Enter deposit amount: ")
            transactions.deposit_money(farmer_id, amount)
        elif choice == 3:
            farmer_id = get_string_input("Enter Farmer ID: ")
            amount = get_float_input("Enter withdrawal amount: ")
            transactions.withdraw_money(farmer_id, amount)
        elif choice == 4:
            farmer_id = get_string_input("Enter Farmer ID: ")
            statement.check_balance(farmer_id)
        elif choice == 5:
            farmer_id = get_string_input("Enter Farmer ID: ")
            n = get_int_input("Enter the number of last transactions to retrieve: ")
            statement.display_statement(farmer_id, n)
        elif choice == 6:
            print("Exiting the SACCO Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()