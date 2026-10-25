#Skipping numbers divisible by 7

n=None
for i in range(1,101):
    if i%7==0:
        continue
    print(i)


#printing numbers divisible by 3 and 5

n=None
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)