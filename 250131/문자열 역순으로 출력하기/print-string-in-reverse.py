import collections
import sys

answer = collections.deque()
for _ in range(4):
    answer.appendleft(sys.stdin.readline().rstrip())

print('\n'.join(answer))
