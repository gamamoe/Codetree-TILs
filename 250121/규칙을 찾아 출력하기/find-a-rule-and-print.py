import sys

n = int(sys.stdin.readline())
full_row = ' '.join('*' for _ in range(n))
answer = [full_row]

for i in range(1, n - 1):
    start = ' '.join('*' for _ in range(i))
    spaces = ' ' * (2 * (n - i - 1) - 1)
    end = '*'
    row = ' '.join([start, spaces, end])
    answer.append(row)

if n > 1:
    answer.append(full_row)
print('\n'.join(answer))
