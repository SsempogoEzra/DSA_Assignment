import sacco_data

# Get the last N transactions for a given farmer in reverse order
def get_last_n_transactions(farmer_id, n):
    transactions = sacco_data.get_transactions(farmer_id)
    last_n = transactions[-n:]  # Get the last N elements
    return reversed(last_n)  # Reverse to get most recent first

# Gets and displays the last N transactions for a farmer.
def display_statement(farmer_id, n):
    transactions = get_last_n_transactions(farmer_id, n)
    print(f"\n--- Last {n} Transactions for Farmer ID: {farmer_id} ---")
    for transaction in transactions:
        print(f"- {transaction}")
    print("--- End of Statement ---")

# Checks and displays the current balance of a farmer.
def check_balance(farmer_id):
    balance = sacco_data.get_farmer_balance(farmer_id)
    if balance is not None:
        print(f"Current balance for Farmer ID {farmer_id}: {balance:.2f}")
    else:
        print(f"Error: Farmer with ID {farmer_id} not found.")

# Example usage (can be removed or commented out later):
# if __name__ == "__main__":
#     sacco_data.add_farmer("FR001", 1000.00)
#     sacco_data.record_transaction("FR001", "FR001,Deposited 500.00 at 2025-04-09 10:00:00")
#     sacco_data.record_transaction("FR001", "FR001,Withdrew 200.00 at 2025-04-09 11:00:00")
#     sacco_data.record_transaction("FR001", "FR001,Deposited 100.00 at 2025-04-09 12:00:00")
#     sacco_data.record_transaction("FR001", "FR001,Withdrew 50.00 at 2025-04-09 13:00:00")

#     display_statement("FR001", 3)
#     display_statement("FR001", 5) # More than available transactions
#     check_balance("FR001")
#     check_balance("FR002") # Non-existent farmer.