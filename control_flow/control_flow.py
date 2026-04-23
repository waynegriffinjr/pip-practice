# Control Flow Practice

for i in range (1, 10, 2):
    print(i)
    
ages = {"Matthew": 25, "Mark": 35, "John": 45}

for name, age in ages.items():
    print(name, age)
    
    
count = 0

while count <= 20:
    print(count)
    count += 1
    
while True:
    response = input("To exit enter 'quit' ")
    if response == "quit":
        print(f"You entered: {response}.")
        break
    
for number in [1, 2, 3, 5, 6, 7]:
    if number % 2 == 0:
        print(f"Found even number: {number}!")
        
for digit in range(50):
    if digit % 2 == 0:
        continue
    print(digit)