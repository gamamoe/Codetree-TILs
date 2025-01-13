import sys

a = 0
b = 0
for _ in range(10):
    num = int(sys.stdin.readline())
    if num % 3 == 0:
        a += 1
    
    if num % 5 == 0:
        b += 1

print(a, b)
