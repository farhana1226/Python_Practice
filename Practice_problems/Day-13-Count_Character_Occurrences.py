#Count Occurrences of a Character in a String

text = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0
for ch in text:
    if ch == char:
        count += 1
print("Character appears", count, "times")
