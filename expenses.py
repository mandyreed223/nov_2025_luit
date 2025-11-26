# -----------------------
# Version 1: Initial Code
# -----------------------
def version1():

    # List of expenses for the week
    expenses = [10.50, 8, 5, 15, 20, 5, 3]

    # Start a running total at 0
    sum = 0

    # Loop through each expense in the list
    for x in expenses:
        # Add the current expense to the total
        sum = sum + x

    # Print the total amount spent with no extra spaces
    print('You spent $', sum, sep='')
    pass


# -----------------------
# Version 2: Added Feature
# -----------------------
def version2():

    # List of expenses for the week
    expenses = [10.50, 8, 5, 15, 20, 5, 3]

    # Use Python's built-in sum() function to add all expenses
    total = sum(expenses)

    # Print the total amount spent with no extra spaces
    print('You spent $', total, sep='')
    pass


# -----------------------
# Version 3: Optimization
# -----------------------
def version3():

    # Start the running total at 0
    total = 0

    # Create an empty list to store expenses
    expenses = []

    # Loop exactly 7 times to collect 7 expenses
    for i in range(7):
        # Ask the user for an expense and add it to the list
        expenses.append(float(input("Enter an expense:")))

    # Add all expenses together using the built-in sum() function
    total = sum(expenses)

    # Print the total spent with no extra spaces
    print('You spent $', total, sep='')
    pass


# -----------------------
# Version 4: Final Outcome
# -----------------------
def version4():

    # Start the running total at 0
    total = 0

    # Create an empty list to store expenses
    expenses = []

    # Ask the user how many expenses they want to enter
    num_expenses = int(input("Enter # of expenses:"))

    # Loop the given number of times
    for i in range(num_expenses):
        # Ask the user for an expense and add it to the list
        expenses.append(float(input("Enter an expense:")))

    # Calculate the total using Python's built-in sum() function
    total = sum(expenses)

    # Print the total amount spent with no extra spaces
    print('You spent $', total, sep='')
    pass


# -----------------------
# Main Execution
# -----------------------
if __name__ == "__main__":

    # Display version options to the user
    print("Choose which version to run:")
    print("1 - Initial Code")
    print("2 - Added Feature")
    print("3 - Optimization")
    print("4 - Final Outcome")

    # Ask the user which version they want to run
    choice = input("Enter 1, 2, 3, or 4: ")

    # Run Version 1 if user selects 1
    if choice == "1":
        version1()

    # Run Version 2 if user selects 2
    elif choice == "2":
        version2()

    # Run Version 3 if user selects 3
    elif choice == "3":
        version3()

    # Run Version 4 if user selects 4
    elif choice == "4":
        version4()

    # Default behavior for invalid input
    else:
        print("Invalid choice. Running Final Outcome by default.")
        version4()
