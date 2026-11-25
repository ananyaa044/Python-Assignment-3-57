# 44. Copy a list and demonstrate the difference between copy() and direct assignment.
original = input("Enter list elements separated by spaces: ").split()
independent_copy = original.copy()
same_list = original
original.append("new")
print("Original after append:", original)
print("copy() result:", independent_copy)
print("Direct assignment result:", same_list)
