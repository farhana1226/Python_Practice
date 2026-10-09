n = int(input())
order = n
count = 0
temp = n
while temp > 0:
    count = count + 1
    temp = temp // 10
armstrong = 0
temp = n
while temp > 0:
    number = temp % 10
    armstrong = armstrong + number ** count
    temp = temp // 10
if armstrong == order:
    print("Yes")
else:
    print("No")

