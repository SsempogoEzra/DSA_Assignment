# sacco_data.py

# Initialize the farmer records hash map
farmer_records = {
    "LAST_ID": 0  # To track the last generated farmer ID number
}

# Initialize the transaction history hash map
transaction_history = {}

def get_last_farmer_id():
    """Retrieves the last generated farmer ID number."""
    return farmer_records.get("LAST_ID", 0)

def increment_last_farmer_id():
    """Increments the last generated farmer ID number and returns the new value."""
    farmer_records["LAST_ID"] = get_last_farmer_id() + 1
    return farmer_records["LAST_ID"]

def add_farmer(farmer_id, initial_balance=0.0):
    """Adds a new farmer record."""
    if farmer_id not in farmer_records:
        farmer_records[farmer_id] = {"balance": initial_balance}
        transaction_history[farmer_id] = []  # Initialize an empty list (will be stack-like)
        return True
    return False

def get_farmer(farmer_id):
    """Retrieves a farmer's record."""
    return farmer_records.get(farmer_id)

def update_farmer_balance(farmer_id, new_balance):
    """Updates a farmer's balance."""
    farmer = get_farmer(farmer_id)
    if farmer:
        farmer["balance"] = new_balance
        return True
    return False

def get_farmer_balance(farmer_id):
    """Retrieves a farmer's current balance."""
    farmer = get_farmer(farmer_id)
    if farmer:
        return farmer["balance"]
    return None

def record_transaction(farmer_id, transaction_string):
    """Records a transaction for a farmer."""
    if farmer_id in transaction_history:
        transaction_history[farmer_id].append(transaction_string)
    else:
        transaction_history[farmer_id] = [transaction_string]

def get_transactions(farmer_id):
    """Retrieves the list of transactions for a farmer (acting as a stack)."""
    return transaction_history.get(farmer_id, [])

# Example of how to generate the first farmer ID
if get_last_farmer_id() == 0:
    increment_last_farmer_id() # Initialize to 1