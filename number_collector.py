# Bulletproof Number Collectiong Program
# Error handling to prevent crash and error messages to ensure smooth user interaction.
try:
    num1 = int(input("Enter the 1st of 3 numbers: "))
except ValueError:
     print("Sorry, invalid number entered--using 0 instead.")
     num1 = 0
     

try:    
    num2 = int(input("Enter the 2nd of 3 numbers: "))
except ValueError:
     print("Sorry, invalid number entered--using 0 instead.")
     num2 = 0
     
    
try:
    num3 = int(input("Enter the 3rd and final number: "))
except ValueError:
     print("Sorry, invalid number entered--using 0 instead.")
     num3 = 0
     
 # Calculate the sum of all three input numbers    
add3 = num1 + num2 + num3
# Calculate the average by diving the sum by the number of inputs
average = add3 / 3 
    
print(f"Your numbers: {num1}, {num2}, {num3}")
print(f"Sum: {add3}")
print(f"Average: {average:.2f}")