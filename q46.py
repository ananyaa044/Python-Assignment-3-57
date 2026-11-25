# 46. Create a tuple and access its elements using positive and negative indexing.
items = tuple(input("Enter tuple elements separated by spaces: ").split())
if items:
    print("Tuple:", items)
    print("First (positive index 0):", items[0])
    print("Last (negative index -1):", items[-1])
    index = int(input(f"Enter a valid index from 0 to {len(items) - 1}: "))
    if 0 <= index < len(items):
        print("Positive indexing:", items[index])
        print("Negative indexing:", items[index - len(items)])
    else:
        print("Index is out of range.")
else:
    print("The tuple is empty.")
