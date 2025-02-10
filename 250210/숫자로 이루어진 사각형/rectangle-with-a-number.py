import sys

def print_square(n: int) -> None:
    answer = [[0 for _ in range(n)] for _ in range(n)]

    current = 1
    for row in range(n):
        for col in range(n):
            answer[row][col] = current
            current += 1

            if current == 10:
                current = 1
    
    for row in range(n):
        print(' '.join(str(x) for x in answer[row]))

n = int(sys.stdin.readline())
print_square(n)
