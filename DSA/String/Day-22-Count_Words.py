# Count the number of words without using split()

text = input("Enter a sentence: ")
count = 0
in_word = False
for ch in text:
    if ch != " ":
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False
print("Number of words:", count)