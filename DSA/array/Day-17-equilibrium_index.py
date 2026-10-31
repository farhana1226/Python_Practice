# Find the Equilibrium Index of an Array

arr = [1, 3, 5, 2, 2]
total_sum = sum(arr)
left_sum = 0
for i in range(len(arr)):
    right_sum = total_sum - left_sum - arr[i]
    if left_sum == right_sum:
        print("Equilibrium Index:", i)
        break
    left_sum += arr[i]
else:
    print("Equilibrium Index: -1")