import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = [0] * 9
for element in arr:
    answer[element - 1] += 1

print('\n'.join(str(x) for x in answer))
