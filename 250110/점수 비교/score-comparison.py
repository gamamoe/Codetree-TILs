import sys

score_of_a = [int(x) for x in sys.stdin.readline().split()]
score_of_b = [int(x) for x in sys.stdin.readline().split()]

if all((a > b for a, b in zip(score_of_a, score_of_b))):
    print(1)
else:
    print(0)
