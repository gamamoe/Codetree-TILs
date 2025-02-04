import sys

char1, char2 = sys.stdin.readline().rstrip().split()
print(f'{ord(char1) + ord(char2)} {abs(ord(char1) - ord(char2))}')
