import sys

strings = []
for _ in range(10):
    strings.append(sys.stdin.readline().rstrip())

char = sys.stdin.readline().rstrip()
answer = [s for s in strings if s[-1] == char]
print('\n'.join(answer) if answer else 'None')
