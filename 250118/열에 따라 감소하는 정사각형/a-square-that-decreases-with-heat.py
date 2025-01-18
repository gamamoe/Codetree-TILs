import sys

n = int(sys.stdin.readline())
row = ' '.join(str(num) for num in range(n, 0, -1))
answer = []
for _ in range(n):
    answer.append(row)
print('\n'.join(answer))
