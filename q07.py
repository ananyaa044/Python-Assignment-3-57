# 7. Count digits, alphabets and special characters in a string.
s = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits =", digits)
print("Alphabets =", alphabets)
print("Special Characters =", special)