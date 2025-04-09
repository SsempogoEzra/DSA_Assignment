# SACCO Management System  Assighnment - Architectural Overview

This README is an explanation of the internal structure and design of the terminal-based SACCO management system for farmers.

**The QN:** Design and implement a SACCO Management System for farmers that utilizes efficient data 
structures to handle deposits, withdrawals, and statement retrieval. Your system should analyze 
and compare the efficiency of different data structures (linked lists, stacks, queues, hash maps 
etc) in managing financial transactions. Provide a detailed performance evaluation and justify the 
choice of data structures used. 

## 1. Program Structure (Modular Architecture)

The application is organized into different Python modules, each responsible for a specific function in the system:

* **`sacco_data.py` (Core Data Management):** This module handles application's data. It contains this 2 data structures holding the data :
    * **`farmer_records` (Hash Map):** This hash map stores all farmer account information and the important last generated id. 
        * **`transaction_history` (Hash Map of Lists):** This hash map tracks the transaction history for each farmer. 

    This module also provides functions for manuplating  these data structures, such as getting the last geneadding new farmers, retrieving farmer data, updating balances, recording transactions, and retrieving transaction lists.rated ID, incrementing the ID counter, 

* **`farmer_management.py` (Farmer Account Lifecycle):** This module contains the logic for managing farmer accounts.

* **`transactions.py` (Financial Transaction Processing):** This module handles the core financial operations i.e withdrawls,deposit.

* **`statement.py` (Account Information Retrieval):** This module focuses on retrieving and displaying account-related information like last transactions(the statement).


* **`cli_interface.py` (User Interaction Layer):** This module provides the command-line interface through which users interact with the system. It:
    * Presents a menu of available actions.
    * Takes user input to determine the desired operation.
    * Calls the appropriate functions from the other modules (`farmer_management.py`, `transactions.py`, `statement.py`) to execute the user's request.
    * Handles some input validation (e.g., ensuring numeric input for amounts and menu choices).

## 2. Data Flow and Interaction

The `cli_interface.py` is the main function receiving user commands and sending tasks to the relevant  modules. These functional module then interact with the `sacco_data.py` module to access and modify the stored data. Lets say a user initiates a deposit, the `cli_interface.py` calls the `deposit_money()` function in `transactions.py`, which then updates the `farmer_records` and `transaction_history` in `sacco_data.py`. Now, when a user requests a statement the `cli_interface.py` calls functions in `statement.py`, which retrieve the necessary information from `sacco_data.py` for display.

## 3. Why and benefits of this Architectural Design

* **Modularity** Each module has a specific responsibility, making the codebase more organized and easier to understand.
* **Maintainability:** Changes to one area of functionality or code are less likely to impact other parts of the system.
* **Testability:** Individual modules can be tested in isolation to ensure their correctness.
* **Upgradable** New features can be added by creating new modules or modifying existing ones without major overhauls or code rewriting.
* **Easy to understand:** The modular structure and design improves the overall readability and maintainability of the code.

