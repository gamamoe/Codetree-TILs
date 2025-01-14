import sys

n = int(sys.stdin.readline())
answer = []
for num in range(1, n + 1):
    if num % 2 == 0 or num % 5 == 0 or (num % 3 == 0 and num % 9 != 0):
        continue
    
    answer.append(str(num))

print(' '.join(answer))
