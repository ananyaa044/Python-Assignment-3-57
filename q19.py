# 19. Count the frequency of each character in a string.
text = input("Enter a string: ")
frequencies = {}
for char in text:
    frequencies[char] = frequencies.get(char, 0) + 1
for char, count in frequencies.items():
    print(f"{char!r}: {count}")
