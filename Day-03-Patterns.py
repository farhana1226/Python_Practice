##Pattern-01

# n=int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

##pattern-02

# n=int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         if i>=j:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


##pattern-03

# n=int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         if i<=j:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


##pattern-04
#
# n=int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         if i<=n-j and j<=n-i:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

##Patterns-05

# n=int(input())
# for i in range(n,-1,-1):
#     for j in range(n,-1,-1):
#         if i<=n-j and j<=n-i:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


##pattern-06

n=int(input())
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()