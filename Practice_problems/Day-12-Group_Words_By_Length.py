#GROUP WORDS BY LENGTH

words = ["apple", "bat", "cat", "dog", "mango", "hi"]
grouped = {}
for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)
print(grouped)