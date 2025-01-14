import sys

n = int(sys.stdin.readline())
answer = 0
for num in range(1, 100 + 1):
    answer += num

    if answer >= n:
        print(num)
        break
    
