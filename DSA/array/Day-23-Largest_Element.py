# Find the largest element in an array

arr = [12, 45, 7, 89, 23]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("Largest element:", largest)
