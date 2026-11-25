# 29. Calculate the sum and average of all elements in a list.
numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("The list is empty.")
