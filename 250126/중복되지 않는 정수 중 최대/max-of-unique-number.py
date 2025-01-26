import sys
import collections

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort(reverse=True)

frequencies = collections.Counter(arr)
answer = -1
for element in arr:
    if (freq := frequencies[element]) == 1:
        answer = element
        break

print(answer)
