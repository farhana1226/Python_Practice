#FINDING EVEN AND ODD NUMBERS

numbers = [12, 7, 9, 4, 15, 8, 20]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
