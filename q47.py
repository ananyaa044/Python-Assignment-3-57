# 47. Count occurrences of a given element in a tuple using count().
items = tuple(input("Enter tuple elements separated by spaces: ").split())
element = input("Enter element to count: ")
print("Occurrences:", items.count(element))
