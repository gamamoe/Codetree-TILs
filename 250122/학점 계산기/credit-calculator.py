import sys

n = int(sys.stdin.readline())
scores = [float(x) for x in sys.stdin.readline().split()]
avg = sum(scores) / n
if avg >= 4.0:
    grade = 'Perfect'
elif avg >= 3.0:
    grade = 'Good'
else:
    grade = 'Poor'

print(f'{avg:.1f}\n{grade}')
