# .....................................Day 2: Python Pattern Practice...............................

#Pattern-01

n=int(input())
for i in range(1, n):
    for j in range(1, n):
        print(j, end=" ")
    print()

#Pattern-02

n=int(input())
for i in range(n,0,-1):
    for j in range(1, n):
        print(i, end=" ")
    print()


# Pattern-03

n=int(input())
for i in range(1,n):
    for j in range(n,-1,-1):
        print(j, end=" ")
    print()

# Pattern-04

n=int(input())
for i in range(1,n):
    for j in range(1,n):
        print("*",end=" ")
    print()


# Pattern-05

n=int(input())
for i in range(1,n):
    for j in range(1,n):
        print("a",end=" ")
    print()

# pattern-06

n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(chr(65+i),end=" ")
    print()

#Pattern-07

n=int(input())
for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        print(chr(97+i),end=" ")
    print()


#pattern-08

n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(chr(65+j),end=" ")
    print()

#pattern-09

n=int(input())
for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        print(chr(65+j),end=" ")
    print()

#patterm-10

n=int(input())
k=0
for i in range(0,n):
    for j in range(0,n):
        print(chr(97+k),end=" ")
        k+=1
    print()


#Pattern-11

n=int(input())
k=0
for i in range(0,n):
    for j in range(0,n):
        print(chr(65+k),end=" ")
        k+=1
    print()


