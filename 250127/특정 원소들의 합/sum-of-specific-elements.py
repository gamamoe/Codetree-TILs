import sys

answer = 0
for index in range(4):
    row = [int(x) for x in sys.stdin.readline().split()]
    answer += sum(row[:index + 1])

print(answer)
