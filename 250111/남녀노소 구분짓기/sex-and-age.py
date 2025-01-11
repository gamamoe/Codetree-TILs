import sys

gender = int(sys.stdin.readline())
age = int(sys.stdin.readline())

if gender == 1:
    if age >= 19:
        print('WOMAN')
    else:
        print('GIRL')
else:
    if age >= 19:
        print('MAN')
    else:
        print('BOY')
