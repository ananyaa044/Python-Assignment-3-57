# 50. Create two sets and perform union, intersection, difference and symmetric difference.
first = set(input("Enter first set elements separated by spaces: ").split())
second = set(input("Enter second set elements separated by spaces: ").split())
print("First set:", first)
print("Second set:", second)
print("Union:", first | second)
print("Intersection:", first & second)
print("Difference (first - second):", first - second)
print("Symmetric difference:", first ^ second)
