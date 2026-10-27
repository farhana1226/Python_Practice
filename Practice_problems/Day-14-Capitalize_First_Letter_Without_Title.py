# Capitalize the First Letter of Every Word


text = input("Enter a string: ")
words = text.split()
result = []
for word in words:
    word = word[0].upper() + word[1:].lower()
    result.append(word)
output = " ".join(result)
print("Capitalized string:", output)
