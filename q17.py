# 17. Join a list of words into a single string using the join() method.
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator (blank for space): ")
if separator == "":
    separator = " "
print(separator.join(words))
