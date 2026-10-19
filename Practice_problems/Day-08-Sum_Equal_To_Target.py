numbers = [2, 7, 11, 15]
target = int(input())
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
else:
    print(" There is no target value")

#................OR......................


numbers = [2, 7, 11, 15]
target = int(input())
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            found = True
if not found:
    print("There is no target value")
