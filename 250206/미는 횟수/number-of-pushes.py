import collections
import sys

string1 = collections.deque(sys.stdin.readline().rstrip())
string2 = collections.deque(sys.stdin.readline().rstrip())

answer = 0
is_possible = False
for _ in range(len(string1)):
    string1.rotate(1)
    answer += 1

    if string1 == string2:
        print(answer)
        is_possible = True
        break

if not is_possible:
    print(-1)

