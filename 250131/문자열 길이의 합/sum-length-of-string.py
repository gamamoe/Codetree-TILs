import sys

n = int(sys.stdin.readline())

total_length = 0
frequency = 0
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    total_length += len(string)
    frequency += 1 if string[0] == 'a' else 0

print(f'{total_length} {frequency}')
