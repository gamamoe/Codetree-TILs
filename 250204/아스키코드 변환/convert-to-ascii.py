import sys

char, code = sys.stdin.readline().rstrip().split()
print(f'{ord(char)} {chr(int(code))}')
