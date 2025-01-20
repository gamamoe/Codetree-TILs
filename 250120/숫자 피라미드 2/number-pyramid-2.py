import sys

n = int(sys.stdin.readline())

answer = []
num_of_elements = 1
current = 1
while len(answer) < n:
    row = []
    for _ in range(num_of_elements):
        row.append(str(current))
        current += 1
    answer.append(' '.join(row))
    num_of_elements += 1

print('\n'.join(answer))
