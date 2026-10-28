# Rotate a List to the Right

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter rotation positions: "))
if numbers:
    k = k % len(numbers)
    rotated = numbers[-k:] + numbers[:-k] if k else numbers
    print("Rotated list:", rotated)
else:
    print("The list is empty")