# 11. Count the occurrences of a particular character in a string.
text = input("Enter a string: ")
character = input("Enter one character to count: ")
if len(character) == 1:
    print("Occurrences:", text.count(character))
else:
    print("Please enter exactly one character.")
