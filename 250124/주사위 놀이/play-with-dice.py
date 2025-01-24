import sys

arr = [int(x) for x in sys.stdin.readline().split()]
counts = [0] * 6
for element in arr:
    counts[element - 1] += 1

answer = []
for index, cnt in enumerate(counts):
    answer.append(f'{index + 1} - {cnt}')
print('\n'.join(answer))
