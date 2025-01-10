import sys

age1, gender1 = sys.stdin.readline().rstrip().split()
age2, gender2 = sys.stdin.readline().rstrip().split()

if (int(age1) >= 19 and gender1 == 'M') or (int(age2) >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)