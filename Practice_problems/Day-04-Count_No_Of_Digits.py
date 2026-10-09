 #  Count no of digits given

num=int(input())
count=0
while num>0:
    num=num//10
    count+=1
print("Number of digits are:",count)

'''OUTPUT
   789456
   Number of digits are:     6               '''