# 34. Delete an element from a specified index using pop().
items = input("Enter list elements separated by spaces: ").split()
if items:
    index = int(input(f"Enter an index from 0 to {len(items) - 1}: "))
    if 0 <= index < len(items):
        print("Removed:", items.pop(index))
        print("Updated list:", items)
    else:
        print("Index is out of range.")
else:
    print("The list is empty.")
