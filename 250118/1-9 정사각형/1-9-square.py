import sys

n = int(sys.stdin.readline())
sequence = []
current = 1
for _ in range(n * n):
    if current == 10:
        current = 1
    sequence.append(current)
    current += 1

answer = []
for i in range(0, n * n, n):
    answer.append(''.join(str(x) for x in sequence[i : i + n]))

print('\n'.join(answer))
