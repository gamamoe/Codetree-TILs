import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    result = 1
    for num in range(a, b + 1):
        result *= num
    answer.append(str(result))

print('\n'.join(answer))
