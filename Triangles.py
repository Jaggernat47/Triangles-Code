a = 5
b = 5
c = 6
d = 5
e = 5
f = 5
g = 6
h = 5

for i in range(a):
    for j in range(i,b):
        print("*", end=" ")
    print()

for i in range(c):
    for j in range(i):
        print("*", end=" ")
    print()

print()

for i in range(e):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, f):
        print("*", end=" ")
    print()

for i in range(g):
    for j in range(i, h):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

