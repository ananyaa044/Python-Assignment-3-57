# 37. Find the second-largest distinct element in a list.
numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
distinct = sorted(set(numbers), reverse=True)
if len(distinct) >= 2:
    print("Second-largest:", distinct[1])
else:
    print("There is no second-largest distinct element.")
