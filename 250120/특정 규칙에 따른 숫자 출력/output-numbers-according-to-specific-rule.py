import sys

n = int(sys.stdin.readline())
answer = []
current = 1
for i in range(n):
    spaces = ' ' * (2 * i)
    sequences = []
    for j in range(n, i, -1):
        if current == 10:
            current = 1
        sequences.append(str(current))
        current += 1
    
    sequences = ' '.join(sequences)
    answer.append(f'{spaces}{sequences}')

print('\n'.join(answer))
