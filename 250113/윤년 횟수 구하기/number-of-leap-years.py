import sys

n = int(sys.stdin.readline())
answer = 0
for year in range(1, n + 1):
    if year % 4 != 0 or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
        continue
    else:
        answer += 1

print(answer)
