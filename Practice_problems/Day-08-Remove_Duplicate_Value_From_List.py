# Remove duplicate values from a list while preserving the original order

numbers = [4, 2, 4, 1, 2, 5, 1]
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)
