# gradebook.py - A Simple student gradebook using lists

# Student names and their test scores
students = ["Deborah", "John", "Phoebe", "Mark", "Eve"]
scores = [87, 92, 94, 84, 90]

print("=" * 35)
print("        Student Gradebook")
print("=" * 35)

# Display all students and scores
for i in range(len(students)):
    print(f"{students[i]:<12} {scores[i]}")
    
# Calculate class statistics
total = sum(scores)             # Built-in function: adds all times
average = total / len(scores)   # Total divided by count
highest = max(scores)           # Built-in: finds the largest value
lowest = min(scores)            # Built-in: finds the smallest value

print("-" * 35)
print(f"Class Average: {average:.1f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")

# Find the student with the highest score
highest_index = scores.index(highest)   # .index() returns the position of a value
top_student = students[highest_index]

print(f"Top Student:   {top_student} ({highest})")

# Add a new student
print("\n--- Adding a new student ---")
new_name = input("Student name: ")

try:
    new_score = int(input("Test score: "))
except ValueError:
    print("Invalid score/ Using 0.")
    new_score = 0
    
students.append(new_name)
scores.append(new_score)

# Recalcuate and display
new_average = sum(scores) / len(scores)
print(f"\nUpdated roster: {len(students)} students")
print(f"New class average: {new_average:.1f}")

# Sort a copy of scores (dont't modify the oroginal)
sorted_scores = sorted(scores)    #sorted() returns a new sorted list
print(f"\nScores (sorted): {sorted_scores}")

# Find median
mid = len(sorted_scores) // 2       # = 3 // is integer division (no decimal)

if len(sorted_scores) % 2 == 0:     # Even number of scores
    median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
else:
    median = sorted_scores[mid]     # Odd number
print(f"Median score: {median}")

