# Finding the maximum difference where the larger element appears after the smaller element.


arr = [2, 3, 10, 6, 4, 8, 1]
minimum = arr[0]
max_difference = 0
for i in range(1, len(arr)):
    difference = arr[i] - minimum
    if difference > max_difference:
        max_difference = difference
    if arr[i] < minimum:
        minimum = arr[i]
print("Maximum difference:", max_difference)