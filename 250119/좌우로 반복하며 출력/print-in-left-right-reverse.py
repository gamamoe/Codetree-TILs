import sys

n = int(sys.stdin.readline())
forward = ''.join(str(x) for x in range(1, n + 1))
backward = ''.join(str(x) for x in range(n, 0, -1))
answer = []
for i in range(n):
    if i % 2 == 0:
        answer.append(forward)
    else:
        answer.append(backward)

print('\n'.join(answer))
