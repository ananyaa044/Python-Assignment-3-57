# 12. Find the first and last occurrence of a character using string methods.
s = input("Enter a string: ")
ch = input("Enter a character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence =", first)
print("Last occurrence =", last)