# 2. Count the number of vowels in a given string.
text = input("Enter a string: ")
print("Number of vowels:", sum(1 for char in text if char in "aeiouAEIOU"))
