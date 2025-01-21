import sys

n = int(sys.stdin.readline())
answer = []
current = ord('A')
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(chr(current))

        if chr(current) == 'Z':
            current = ord('A')
        else:
            current += 1
    answer.append(''.join(row))

print('\n'.join(answer))
