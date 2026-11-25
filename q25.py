# 25. Check whether two strings are equal, ignoring their case.
first = input("Enter the first string: ")
second = input("Enter the second string: ")
print("Equal ignoring case:", first.casefold() == second.casefold())
