# 31. Insert an element at a specified position in a list.
items = input("Enter list elements separated by spaces: ").split()
element = input("Enter the element to insert: ")
position = int(input(f"Enter an index from 0 to {len(items)}: "))
if 0 <= position <= len(items):
    items.insert(position, element)
    print("Updated list:", items)
else:
    print("Position is out of range.")
