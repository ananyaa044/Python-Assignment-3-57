# 35. Sort a list in ascending and descending order.
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
