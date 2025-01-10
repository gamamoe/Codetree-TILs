import sys

math_a, english_a = [int(x) for x in sys.stdin.readline().split()]
math_b, english_b = [int(x) for x in sys.stdin.readline().split()]

if math_a > math_b:
    print('A')
elif math_a < math_b:
    print('B')
else:
    if english_a > english_b:
        print('A')
    else:
        print('B')
