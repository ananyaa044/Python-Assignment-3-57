# 43. Find the index of a specified element in a list.
items = input("Enter list elements separated by spaces: ").split()
element = input("Enter element to find: ")
if element in items:
    print("Index:", items.index(element))
else:
    print("Element not found.")
