import sys

scores = [float(x) for x in sys.stdin.readline().split()]
print(f'{sum(scores) / len(scores):.1f}')