#Divide with 10 so that we can get last digits

num=int(input())
while num>0:
    last_digit=num%10   # % mean remainder
    print(last_digit)
    num=num//10


'''output  
5499    

   9
   9
   4
   5'''