# 48. Demonstrate tuple concatenation, repetition and slicing.
first = tuple(input("Enter first tuple elements separated by spaces: ").split())
second = tuple(input("Enter second tuple elements separated by spaces: ").split())
print("Concatenation:", first + second)
print("Repetition (first tuple twice):", first * 2)
print("First three elements:", first[:3])
