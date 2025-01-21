import sys

m = int(sys.stdin.readline())
answer = []

for _ in range(m):
    n = int(sys.stdin.readline())
    result = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        
        result += 1
    answer.append(str(result))

print('\n'.join(answer))
