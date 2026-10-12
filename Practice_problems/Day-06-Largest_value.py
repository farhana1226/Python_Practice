
#LARGEST VALUE IN AN ARRAY

arr = [12, 5, 28, 9, 17]
largest = arr[0]
for i in range(len(arr)):
    if arr[i] >= largest:
        largest = arr[i]
print(largest)

#SMALLEST VALUE IN ARRAY

arr = [12, 5, 28, 9, 17]
smallest= arr[0]
for i in range(len(arr)):
    if arr[i] <= smallest:
        smallest = arr[i]
print(smallest)