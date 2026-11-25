# 32. Append five elements to an existing list.
items = input("Enter existing list elements separated by spaces: ").split()
for index in range(5):
    items.append(input(f"Enter element {index + 1} to append: "))
print("Updated list:", items)
