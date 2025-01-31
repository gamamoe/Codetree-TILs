import sys

n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().rstrip())

char = sys.stdin.readline().rstrip()
answer = [s for s in strings if s[0] == char]
avg = sum(len(s) for s in answer) / len(answer)
print(f'{len(answer)} {avg:.2f}')
