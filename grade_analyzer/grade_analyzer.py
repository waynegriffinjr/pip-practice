# Student grade analyzer
print("=" * 30)
print("---GRADE ANALYZER---")
print("=" * 30)

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

A = 0
B = 0
C = 0
D = 0
F = 0

total_scores = 0
sum_score = 0
high_score = 88 #assuming first score is highest and lowest
low_score = 88
passing = 0
failing = 0

for score in scores:
    
    if score > high_score:
        high_score = score
    
    if score < low_score:
        low_score = score

# Calculate pass/fail score counter 
    if score >= 60:
        passing += 1
    else:
        failing += 1
        

    if score >= 90:
        A = A + 1
        total_scores = total_scores + 1
        sum_score += score
    elif score >= 80:
        B = B + 1
        total_scores = total_scores + 1
        sum_score += score
    elif score >= 70:
        C = C + 1
        total_scores = total_scores + 1
        sum_score += score
    elif score >= 60:
        D = D + 1
        total_scores = total_scores + 1
        sum_score += score
    else:
        F = F + 1
        total_scores = total_scores + 1
        sum_score += score

sum_score = sum_score / len(scores)

    
# CALCULATIONS
# Total number of scores
print(f"Total scores: {total_scores}")
# Average Score
print(f"Average score: {sum_score:.1f}")
# Highest and Lowest Score
print(f"High Score: {high_score} ")
print(f"Low Score: {low_score}")
# Number of passing scores (60+) and failing scores (below 60)
print(f"Passing Scores: {passing}")
print(f"Failing Scores: {failing}")
# Distribution of letter grades
print("\nGrade Distribution:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")
print(f"F: {F}")

print("--- Add More Scores ---")

while True:
    add_score = input("\nEnter new score (or type 'quit' to finish): ").lower()
    
    if add_score == "quit":
        print("Session Complete.")
        break
    
    try:
        add_score = int(add_score)
    except:
        print("Please enter valid number: ")    
        continue
    
    scores.append(add_score)
    
    # Recalculate average
    new_average = sum(scores) / len(scores)
    
    print(f"Updated average: {new_average:.1f}")
       
    