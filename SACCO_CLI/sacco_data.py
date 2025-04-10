# The farmer records hash map
farmer_records = {
    "LAST_ID": 0  # Track the last generated farmer ID number
}

#Transaction history hash map
transaction_history = {}

#Gets the last generated farmer ID number.
def get_last_farmer_id():
    return farmer_records.get("LAST_ID", 0)

# Gets the last generated farmer ID number and returns the new value.
def increment_last_farmer_id():
    farmer_records["LAST_ID"] = get_last_farmer_id() + 1
    return farmer_records["LAST_ID"]

# Adds a new farmer record.
def add_farmer(farmer_id, initial_balance=0.0):
    if farmer_id not in farmer_records:
        farmer_records[farmer_id] = {"balance": initial_balance}
        transaction_history[farmer_id] = []  # Initialize an empty list (will be stack-like)
        return True
    return False

# Retrieves a farmer's record.
def get_farmer(farmer_id):
    return farmer_records.get(farmer_id)

# Updates a farmer's balance.
def update_farmer_balance(farmer_id, new_balance):
    farmer = get_farmer(farmer_id)
    if farmer:
        farmer["balance"] = new_balance
        return True
    return False

# Retrieves a farmer's current balance.
def get_farmer_balance(farmer_id):
    farmer = get_farmer(farmer_id)
    if farmer:
        return farmer["balance"]
    return None

# Records a transaction for a farmer.
def record_transaction(farmer_id, transaction_string):
    if farmer_id in transaction_history:
        transaction_history[farmer_id].append(transaction_string)
    else:
        transaction_history[farmer_id] = [transaction_string]

# Retrieves the list of transactions for a farmer (This acts as a stack).
def get_transactions(farmer_id):
    return transaction_history.get(farmer_id, [])

#Example generate the first farmer ID
# if get_last_farmer_id() == 0:
#     increment_last_farmer_id() # Initialize to 1