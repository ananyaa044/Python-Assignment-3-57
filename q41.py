# 41. Demonstrate list slicing with different index ranges.
items = input("Enter list elements separated by spaces: ").split()
print("Complete list:", items[:])
print("First three:", items[:3])
print("Index 2 through 5:", items[2:6])
print("From index 2 onward:", items[2:])
print("All except last two:", items[:-2])
print("Every second element:", items[::2])
