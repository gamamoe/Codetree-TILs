import sys

def abs_(seq):
    for i in range(len(seq)):
        seq[i] = abs(seq[i])

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
abs_(arr)
print(' '.join(str(x) for x in arr))