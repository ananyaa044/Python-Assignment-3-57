# 49. Demonstrate tuple immutability and create a modified tuple using concatenation.
original = tuple(input("Enter tuple elements separated by spaces: ").split())
print("Original tuple:", original)
try:
    original[0] = "changed"
except (TypeError, IndexError) as error:
    print("Tuples cannot be changed in place:", error)
new_element = input("Enter an element to add: ")
modified = original + (new_element,)
print("Modified tuple:", modified)
