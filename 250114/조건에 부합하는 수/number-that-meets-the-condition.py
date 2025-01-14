import sys

a = int(sys.stdin.readline())
answer = []
for num in range(1, a + 1):
    if (num % 2 == 0 and num % 4 != 0) or ((num // 8) % 2 == 0) or (num % 7) < 4:
        continue
    
    answer.append(str(num))

print(' '.join(answer))
