# Find the most repeated character in a string

text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
max_count = 0
most_repeated = ""
for ch in frequency:
    if frequency[ch] > max_count:
        max_count = frequency[ch]
        most_repeated = ch
print("Most repeated character:", most_repeated)
print("Count:", max_count)