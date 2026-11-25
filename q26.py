# 26. Create a list of 10 numbers and display all its elements.
numbers = []
for index in range(10):
    numbers.append(int(input(f"Enter number {index + 1}: ")))
print("List elements:", numbers)
