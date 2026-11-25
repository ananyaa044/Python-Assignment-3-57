# 38. Remove duplicate elements from a list while preserving order.
items = input("Enter list elements separated by spaces: ").split()
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print("List without duplicates:", unique_items)
