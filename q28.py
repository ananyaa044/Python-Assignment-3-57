# 28. Find the largest and smallest elements in a list.
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
else:
    print("The list is empty.")
