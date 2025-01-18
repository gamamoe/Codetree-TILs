import sys

n = int(sys.stdin.readline())
sequence = []
current = 1
for _ in range(n * n):
    if current == 5:
        current = 1
    sequence.append(str(2 * current))
    current += 1

answer = []
for i in range(0, n * n, n):
    answer.append(' '.join(x for x in sequence[i : i + n]))

print('\n'.join(answer))
