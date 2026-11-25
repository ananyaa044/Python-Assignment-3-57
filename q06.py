# 6. Count uppercase and lowercase characters in a string.
text = input("Enter a string: ")
print("Uppercase:", sum(1 for char in text if char.isupper()))
print("Lowercase:", sum(1 for char in text if char.islower()))
