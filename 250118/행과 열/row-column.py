import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = []
for row in range(1, a + 1):
    temp = []
    for col in range(1, b + 1):
        temp.append(str(row * col))
    answer.append(' '.join(temp))
print('\n'.join(answer))
