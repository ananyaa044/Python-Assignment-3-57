# 33. Delete an element from a list using the remove() method.
items = input("Enter list elements separated by spaces: ").split()
element = input("Enter the element to remove: ")
if element in items:
    items.remove(element)
    print("Updated list:", items)
else:
    print("Element not found:", items)
