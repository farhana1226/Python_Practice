# Count Characters in a String Without Using len()

text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Total number of characters:", count)
