# tip_calculator.py - Interactive tip calculator

print("=" * 35)
print("    Tip Calculator")
print("=" * 35)

# Get the bill amount (input returns a string, so I need to conert to a float data type)
  # Add error handling to prevent program crash
try:
    bill_string = input("\nEnter the bill amount: $")
    bill = float(bill_string)
    if bill < 0:
            print("Error: Bill amount can't be negative.")
            exit()
    if bill == 0:
            print("You don't owe anything!")
            exit()
except ValueError:
    print("Please enter a valid number.")
    exit()           


# Calculate tip amounts for common percentages
# Percentage of total amount
tip_15_per = bill * 0.15
tip_18_per = bill * 0.18
tip_20_per = bill * 0.20
tip_25_per = bill * 0.25

total_15 = bill + tip_15_per
total_18 = bill + tip_18_per
total_20 = bill + tip_20_per
total_25 = bill + tip_25_per

# Add error handling for tip percentages
try:
    tip_rate = float(input("Enter tip percentage (e.g., 20): "))
    if tip_rate < 0:
        print("Error: Tip percentage can't be negative")
        exit()
    if tip_rate > 100:
        print(f"Wow, {tip_rate:.0f}% is very generous!")
        # Graceful comment to ensure this was a logical choice
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Ask about splitting
people_string = input("How many people are splitting the bill? ")
people = int(people_string)

# Display results
print(f"\nBill amount: ${bill:.2f}")
print(f"Number of people: {people}")
print("-" * 35)
print(f"{'Tip %':<10} {'Tip':<10} {'Total':<10} {'Per Person':<10}")
print("-" * 35)
print(f"{'15%':<10} ${tip_15_per:<9.2f} ${total_15:<9.2f} ${total_15/people:<9.2f}")
print(f"{'18%':<10} ${tip_18_per:<9.2f} ${total_18:<9.2f} ${total_18/people:<9.2f}")
print(f"{'20%':<10} ${tip_20_per:<9.2f} ${total_20:<9.2f} ${total_20/people:<9.2f}")
print(f"{'25%':<10} ${tip_25_per:<9.2f} ${total_25:<9.2f} ${total_25/people:<9.2f}")
print("=" * 35)

