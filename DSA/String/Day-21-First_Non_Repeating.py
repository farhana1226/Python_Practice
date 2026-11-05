name = input("Enter a string: ")
for ch in name:
    if name.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character")