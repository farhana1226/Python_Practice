
#METHOS-1

arr = [12, 35, 1, 10, 34, 1]
largest = arr[0]
second = None
for i in range(len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] < largest:
        if second is None or arr[i] > second:
            second = arr[i]
print(second)

#METHOD-2

arr=[5,6,7,23,5,54,5542,6,4]
largest=arr[0]
second=None
for i in range(len(arr)):
    if arr[i]>largest:
        second=largest
        largest=arr[i]
    elif second==None or arr[i]>second:
        second=arr[i]
print(second)
print(largest)


# Duplicate values in array

arr = [15, 8, 22, 22, 11, 19]
largest = arr[0]
second = None
for i in range(1, len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] < largest and (second is None or arr[i] > second):
        second = arr[i]
print(second)
print(largest)