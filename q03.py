# 3. Count vowels and consonants separately in a string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("Vowels:", sum(1 for char in text if char in vowels))
print("Consonants:", sum(1 for char in text if char.isalpha() and char not in vowels))
