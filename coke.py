# Cost of the coke
cost = 50
amount_due = cost


# Lista of values
accepted_coins = [25, 10, 5]

# Function that shows the amount still owed
def display_amount_due(amount_due):
    print(f"Amount Due: {amount_due}")

# Prompt the user until the total inserted amount reaches or exceeds the cost

while amount_due > 0:

    display_amount_due(amount_due) # Call the function to show the amount owed

    try:
        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the inserted coin is one of the accepted denominations
        if coin in accepted_coins:
            amount_due -= coin
        else:
            print(f"Invalid coin. Please insert 25, 10, or 5 cents only.")

    except ValueError:
        print("Invalid input. Please insert an integer.")

# Calculate change if any
change = abs(amount_due)
print(f"Change Owed: {change}")
