# move all zeros in a list to the end without changing the order of the non-zero numbers.


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
non_zeros = []
zeros = []
for num in numbers:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)
result = non_zeros + zeros
print("List after moving zeros:", result)
