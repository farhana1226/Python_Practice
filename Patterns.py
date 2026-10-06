#
# # Pattern 1
#
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print("* ", end="")
#     print()
#
#
# # Pattern 2
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == 10 or j == 1 or j == 10:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 3
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == 10 or j == 1 or j == 10 or j == (n - i):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 4
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or j == (n - i) or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 5
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j == (n - i) or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 6
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or i <= ((n - 1) // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 7
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or i >= ((n - 1) // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 8
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or j >= ((n - 1) // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 9
#
n = int(input())

for i in range(1, n):
    for j in range(1, n):
        if i == 1 or i == n - 1 or j == 1 or j == n - 1 or j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#
#
# # Pattern 10
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 11
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or (i >= n // 2 and j >= n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 12
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or (i <= n // 2 and j > n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 13
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or (i >= n // 2 and j <= n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 14
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or (i > n // 2 and j > n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 15
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j <= i:
#             print("*", end="")
#     print()
#
# for i in range(1, n - 1):
#     for j in range(1, n - 1):
#         if j >= i:
#             print("*", end="")
#     print()
#
#
# # Pattern 16
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j >= n - 1 or (i <= j and i <= n - j):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 17
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or i == n - 1 or j == 1 or j == n - 1 or (j >= n - i and i <= j):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 18
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or j == 1 or i == n - 1 or j == n - 1 or (i <= j and i <= n - j):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 19
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if i == 1 or j == 1 or i == n - 1 or j == n - 1 or (i >= j and j >= n - i):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 20
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, i + 1):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 21
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, i + 1):
#         if j > n - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 22
#
# n = int(input())
#
# for i in range(1, n):
#     for k in range(1, n - i):
#         print(" ", end=" ")
#
#     for j in range(1, i + 1):
#         print("*", end=" ")
#
#     print()
#
#
# # Pattern 23
#
# n = int(input())
# n = n + 1
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j >= n - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 24
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j <= n - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 25
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j >= n - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(1, n):
#     for k in range(1, n):
#         if k > i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 26
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, n):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(1, n - 1):
#     for k in range(1, n - 1):
#         if k < n - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 27
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, 2 * n):
#         if j >= n - i + 1 and j <= n + i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(1, n):
#     for j in range(1, 2 * n):
#         if j >= i + 1 and j <= 2 * n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 28
#
# n = int(input())
#
# for i in range(1, n):
#     for j in range(1, 2 * n):
#         if j >= n - i + 1 and j <= n + i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(2, n):
#     for j in range(1, 2 * n):
#         if j >= i + 1 and j <= 2 * n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
#
# # Pattern 29
#
# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i, end=" ")
#     print()
#
