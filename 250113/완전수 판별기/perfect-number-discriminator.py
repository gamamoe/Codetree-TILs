import sys

n = int(sys.stdin.readline())
divisors = []
for i in range(1, n):
    if n % i == 0:
        divisors.append(i)

if sum(divisors) == n:
    print('P')
else:
    print('N')
