import sys

num = int(sys.stdin.readline())
answer = [num]
if num < 0:
    answer.append('minus')

print('\n'.join([str(x) for x in answer]))
