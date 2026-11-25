# 30. Count the number of even and odd elements in a list.
numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
even = sum(1 for number in numbers if number % 2 == 0)
print("Even elements:", even)
print("Odd elements:", len(numbers) - even)
