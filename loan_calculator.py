# Get the amount of money owed
money_owed = float(input('How much money do you owe, in dollars?\n'))  # Example: 50000

# Get the annual percentage rate (APR)
apr = float(input('What is the annual percentage rate of the loan?\n'))  # Example: 3%

# Get the monthly payment amount
payment = float(input('How much will you pay off each month in dollars?\n'))  # Example: 1000

# Get how many months the user wants to see results for
months = int(input('How many months do you want to see the results for?\n'))  # Example: 24

# Convert APR to a monthly interest rate
monthly_rate = apr / 100 / 12

# Loop through each month
for i in range(months):

    # Calculate the interest for this month
    interest_paid = money_owed * monthly_rate

    # Add interest to the total owed
    money_owed = money_owed + interest_paid

    # Check if this payment will finish the loan
    if (money_owed - payment < 0):
        # Print final payment amount
        print('The last payment is', money_owed)

        # Print how many months it took to pay off
        print('You paid off the loan in', i + 1, 'months')

        # Exit the loop
        break

    # Subtract the monthly payment from the loan
    money_owed = money_owed - payment

    # Show payment details
    print('Paid', payment, 'of which', interest_paid, 'was interest')

    # Show remaining balance
    print('Now I owe', money_owed)
