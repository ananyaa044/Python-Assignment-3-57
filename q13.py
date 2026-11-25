# 13. Check whether a string starts and ends with a particular character.
text = input("Enter a string: ")
character = input("Enter one character: ")
if len(character) == 1:
    print("Starts with character:", text.startswith(character))
    print("Ends with character:", text.endswith(character))
else:
    print("Please enter exactly one character.")
