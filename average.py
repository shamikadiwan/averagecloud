# Input: Get 5 numbers from the user
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the average
average = sum(numbers) / len(numbers)

# Output the result
print(f"The average of the 5 numbers is: {average}")
