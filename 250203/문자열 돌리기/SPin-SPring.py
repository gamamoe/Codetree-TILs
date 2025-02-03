import sys
import collections

queue = collections.deque(sys.stdin.readline().rstrip())
print(''.join(queue))
for _ in range(len(queue)):
    queue.rotate(1)
    print(''.join(queue))
