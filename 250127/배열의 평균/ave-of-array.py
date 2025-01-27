import sys

matrix = []
row_average = []
for _ in range(2):
    row = [int(x) for x in sys.stdin.readline().split()]
    matrix.append(row)
    row_average.append(f'{sum(row) / 4:.1f}')

col_average = []
for i in range(4):
    col_average.append(f'{(matrix[0][i] + matrix[1][i]) / 2:.1f}')

total_average = f'{(sum(matrix[0]) + sum(matrix[1])) / 8:.1f}'
print(' '.join(row_average))
print(' '.join(col_average))
print(total_average)
