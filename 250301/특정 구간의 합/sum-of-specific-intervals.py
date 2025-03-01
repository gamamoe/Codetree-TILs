import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
sequence = [int(x) for x in sys.stdin.readline().split()]

answer = []
for _ in range(m):
    a1, a2 = [int(x) for x in sys.stdin.readline().split()]

    answer.append(str(sum(sequence[a1 - 1:a2])))

print('\n'.join(answer))

    