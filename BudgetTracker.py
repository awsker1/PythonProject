# Budget Tracker Program
# This program tracks income and expenses, displays a summary, and stores all transactions.  

# Initializes the variables and list for transactions
total_income = 0.0
total_expenses = 0.0

# List which stores all transactions in the format (type, category, amount)
transactions = []

# Start of the main loop which prompts the user
while True:
    print("\nWhat would you like to do?")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Quit")

# Capture the user’s choice
    choice = input("Enter the number of your choice: ")

# Option 1 – Add income
    if choice == "1":
        try:
            # Ask the user for an income amount and category
            amount = float(input("Enter income amount: $"))
            category = input("Enter income category: ")

            # Update total income and store trasaction
            total_income += amount
            transactions.append(("Income", category, amount))


            # Confirm message and handle invalid number input
            print("Income added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    #Option 2 – Add expense
    elif choice == "2":
        try:
            # Ask the user for an expense amount and category
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")

            # Update total expenses and store transaction
            total_expenses += amount
            transactions.append(("Expense", category, amount))

            #Confirm message and handle invalid number input
            print("Expense added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Option 3 – View summary 
    elif choice == "3":
        # Calculates remaining balance
        balance = total_income - total_expenses
        print("\n--- Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Balance: ${balance:.2f}")

        # Ask user if they want to see full transaction history
        view_all = input("Would you like to see all transactions? (yes/no): ").lower()
        if view_all == "yes":
            print("\n--- All Transactions ---")
            for t_type, category, amount in transactions:
                print(f"{t_type} | {category} | ${amount:.2f}")

# Option 4 – Exits program
    elif choice == "4":
        print("Exiting Budget Tracker. Goodbye!")
        break

# Handles invalid menu selection
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
