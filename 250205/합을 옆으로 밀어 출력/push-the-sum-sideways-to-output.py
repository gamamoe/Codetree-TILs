import sys

n = int(sys.stdin.readline())
answer = 0
for _ in range(n):
    answer += int(sys.stdin.readline())

answer = str(answer)
print(f'{answer[1:]}{answer[0]}')
