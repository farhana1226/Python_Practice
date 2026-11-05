# Method 1 (Using sorted)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

# Method 2 – Without sorted()

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            print("Not Anagram")
            break
    else:
        print("Anagram")
else:
    print("Not Anagram")