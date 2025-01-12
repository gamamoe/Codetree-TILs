import sys

a, n = [int(x) for x in sys.stdin.readline().split()]
answer = []
for _ in range(n):
    a += n
    answer.append(str(a))

print('\n'.join(answer))
