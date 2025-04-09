# transactions.py

import sacco_data
from datetime import datetime

def deposit_money(farmer_id, amount):
    """Deposits money into a farmer's account."""
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return

    farmer = sacco_data.get_farmer(farmer_id)
    if farmer:
        current_balance = farmer["balance"]
        new_balance = current_balance + amount
        if sacco_data.update_farmer_balance(farmer_id, new_balance):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_string = f"{farmer_id},Deposited {amount:.2f} at {timestamp}"
            sacco_data.record_transaction(farmer_id, transaction_string)
            print(f"Successfully deposited {amount:.2f} into account {farmer_id}. New balance: {new_balance:.2f}")
        else:
            print(f"Error: Could not update balance for farmer {farmer_id}.")
    else:
        print(f"Error: Farmer with ID {farmer_id} not found.")

def withdraw_money(farmer_id, amount):
    """Withdraws money from a farmer's account."""
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return

    farmer = sacco_data.get_farmer(farmer_id)
    if farmer:
        current_balance = farmer["balance"]
        if current_balance >= amount:
            new_balance = current_balance - amount
            if sacco_data.update_farmer_balance(farmer_id, new_balance):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction_string = f"{farmer_id},Withdrew {amount:.2f} at {timestamp}"
                sacco_data.record_transaction(farmer_id, transaction_string)
                print(f"Successfully withdrew {amount:.2f} from account {farmer_id}. New balance: {new_balance:.2f}")
            else:
                print(f"Error: Could not update balance for farmer {farmer_id}.")
        else:
            print(f"Error: Insufficient balance for farmer {farmer_id}. Current balance: {current_balance:.2f}")
    else:
        print(f"Error: Farmer with ID {farmer_id} not found.")

# Example usage (can be removed or commented out later):
if __name__ == "__main__":
    sacco_data.add_farmer("FR001", 1000.00)
    deposit_money("FR001", 500.00)
    withdraw_money("FR001", 200.00)
    withdraw_money("FR001", 2000.00) # Insufficient balance
    deposit_money("FR002", 100.00)