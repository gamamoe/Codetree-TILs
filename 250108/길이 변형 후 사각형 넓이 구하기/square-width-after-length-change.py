import sys

width, height = [int(x) for x in sys.stdin.readline().split()]
width += 8
height *= 3
print(f'{width}\n{height}\n{width * height}')
