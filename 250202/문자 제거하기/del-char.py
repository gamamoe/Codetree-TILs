import sys
import collections

string = collections.deque(sys.stdin.readline().rstrip())
while len(string) > 1:
    pos = int(sys.stdin.readline())

    if pos >= len(string):
        _ = string.pop()
        print(''.join(string))
        continue

    temp = []
    for _ in range(pos):
        temp.append(string.popleft())
    string.popleft()
    while string:
        temp.append(string.popleft())
    string = collections.deque(temp)
    print(''.join(string))

