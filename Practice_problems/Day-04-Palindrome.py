# n=int(input())
# order=n
# palindrome=0
# while n>0:
#     number = n % 10
#     palindrome=palindrome*10+number
#     n=n//10
# if palindrome==order:
#     print('Yes')
# else:
#     print('No')

'''OUTPUT
  789987
     Yes

'''

#Method-02

s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")