import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    answer.append('*' * n)

square = '\n'.join(answer)
print('\n\n'.join([square for _ in range(2)]))