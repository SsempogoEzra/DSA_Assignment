# SACCO Management System (Terminal Application) - Architectural Overview

This document provides an overview of the internal structure and design of the terminal-based SACCO (Savings and Credit Cooperative Organization) management system for farmers. The system is built with a focus on modularity and efficient data handling for core functionalities.

## 1. Program Structure (Modular Architecture)

The application is organized into several distinct Python modules, each responsible for a specific aspect of the system:

* **`sacco_data.py` (Core Data Management):** This module serves as the central repository for the application's data. It initializes and manages the primary data structures:
    * **`farmer_records` (Hash Map):** This hash map stores all farmer account information. The keys are unique Farmer IDs (e.g., "FR001"), and the values are dictionaries containing the farmer's `balance` and an internal key `"LAST_ID"` used for generating new farmer IDs. The use of a hash map allows for efficient ($O(1)$ average time complexity) access to individual farmer records based on their ID.
    * **`transaction_history` (Hash Map of Lists):** This hash map tracks the transaction history for each farmer. The keys are Farmer IDs, and the values are Python lists containing formatted strings representing each transaction (deposit or withdrawal) along with its timestamp. These lists are treated as stacks (Last-In, First-Out) for managing and retrieving recent transactions.

    This module also provides functions for interacting with these data structures, such as getting the last generated ID, incrementing the ID counter, adding new farmers, retrieving farmer data, updating balances, recording transactions, and retrieving transaction lists.

* **`farmer_management.py` (Farmer Account Lifecycle):** This module encapsulates the logic for managing farmer accounts. It includes functions like:
    * **`generate_farmer_id()`:** Creates a new unique Farmer ID using the tracking mechanism in `sacco_data.py`.
    * **`create_new_farmer()`:** Utilizes `generate_farmer_id()` and functions from `sacco_data.py` to add a new farmer record to the system with an initial balance.
    * **`get_farmer_details()`:** Retrieves and displays basic information about a farmer using data from `sacco_data.py`.

* **`transactions.py` (Financial Transaction Processing):** This module handles the core financial operations:
    * **`deposit_money()`:** Takes a Farmer ID and an amount as input, updates the farmer's balance in `sacco_data.py`, and records the deposit transaction (with timestamp) in the `transaction_history` within `sacco_data.py`.
    * **`withdraw_money()`:** Takes a Farmer ID and an amount, checks for sufficient balance in `sacco_data.py`, updates the balance upon successful withdrawal, and records the withdrawal transaction (with timestamp) in `transaction_history` in `sacco_data.py`. It also handles insufficient balance scenarios.

* **`statement.py` (Account Information Retrieval):** This module focuses on retrieving and displaying account-related information:
    * **`get_last_n_transactions()`:** Retrieves the last `N` transaction records from the list associated with a given Farmer ID in `transaction_history` (via `sacco_data.py`) and returns them in reverse chronological order.
    * **`display_statement()`:** Formats and displays the last `N` transactions for a farmer using the output of `get_last_n_transactions()`.
    * **`check_balance()`:** Retrieves and displays the current balance of a farmer by accessing the `farmer_records` in `sacco_data.py`.

* **`cli_interface.py` (User Interaction Layer):** This module provides the command-line interface through which users interact with the system. It:
    * Presents a menu of available actions.
    * Takes user input to determine the desired operation.
    * Calls the appropriate functions from the other modules (`farmer_management.py`, `transactions.py`, `statement.py`) to execute the user's request.
    * Handles basic input validation (e.g., ensuring numeric input for amounts and menu choices).

## 2. Data Flow and Interaction

The `cli_interface.py` acts as the orchestrator, receiving user commands and delegating tasks to the relevant functional modules. These functional modules, in turn, interact with the `sacco_data.py` module to access and modify the stored data. For instance, when a user initiates a deposit, the `cli_interface.py` calls the `deposit_money()` function in `transactions.py`, which then updates the `farmer_records` and `transaction_history` in `sacco_data.py`. Similarly, when a user requests a statement, the `cli_interface.py` calls functions in `statement.py`, which retrieve the necessary information from `sacco_data.py` for display.

## 3. Benefits of this Architectural Design

* **Separation of Concerns:** Each module has a specific responsibility, making the codebase more organized and easier to understand.
* **Maintainability:** Changes to one area of functionality are less likely to impact other parts of the system.
* **Testability:** Individual modules can be tested in isolation to ensure their correctness.
* **Extensibility:** New features can be added by creating new modules or modifying existing ones without major overhauls.
* **Readability:** The modular structure improves the overall readability and maintainability of the code.

This well-defined structure allows for a more manageable and scalable SACCO management system, even in its current terminal-based form.