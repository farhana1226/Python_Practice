#Replace All Vowels in a String with *

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch
print("Modified string:", result)
