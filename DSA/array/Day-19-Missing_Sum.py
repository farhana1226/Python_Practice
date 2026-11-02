#Missing value finding

arr = [1, 2, 4, 5, 6]
n = 6
expected_sum = n * (n + 1) // 2
actual_sum = 0
for i in arr:
    actual_sum += i
missing = expected_sum - actual_sum
print("Missing number =", missing)