# farmer_management.py

import sacco_data

def generate_farmer_id():
    """Generates a new unique farmer ID."""
    last_id = sacco_data.get_last_farmer_id()
    new_id_number = last_id + 1
    sacco_data.increment_last_farmer_id()
    return f"FR{str(new_id_number).zfill(3)}"

def create_new_farmer():
    """Creates a new farmer account."""
    new_farmer_id = generate_farmer_id()
    if sacco_data.add_farmer(new_farmer_id):
        print(f"New farmer account created with ID: {new_farmer_id}")
    else:
        print(f"Error: Could not create farmer account with ID: {new_farmer_id}")

def get_farmer_details(farmer_id):
    """Retrieves and displays the details of a farmer."""
    farmer = sacco_data.get_farmer(farmer_id)
    if farmer:
        print(f"Farmer ID: {farmer_id}")
        print(f"Current Balance: {farmer['balance']:.2f}")
    else:
        print(f"Error: Farmer with ID {farmer_id} not found.")

# Example usage (can be removed or commented out later):
if __name__ == "__main__":
    create_new_farmer()
    create_new_farmer()
    get_farmer_details("FR001")
    get_farmer_details("FR002")
    get_farmer_details("FR003")