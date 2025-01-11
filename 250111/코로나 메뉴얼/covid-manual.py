import sys

case1 = sys.stdin.readline().rstrip().split()
case2 = sys.stdin.readline().rstrip().split()
case3 = sys.stdin.readline().rstrip().split()

emergencies = 0
for a, b in (case1, case2, case3):
    if a == 'Y' and int(b) >= 37:
        emergencies += 1

print('E' if emergencies >= 2 else 'N')
