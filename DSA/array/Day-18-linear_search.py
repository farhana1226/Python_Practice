#searching problem

arr = [5, 15, 25, 35, 45]
target = 35
found = False
for i in range(len(arr)):
    if target == arr[i]:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")