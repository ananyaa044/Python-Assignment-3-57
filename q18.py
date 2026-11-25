# 18. Find the longest word in a given sentence using string operations.
words = input("Enter a sentence: ").split()
if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("No words were entered.")
