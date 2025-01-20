answer = []

for i in range(1, 19 + 1):
    for j in (1, 3, 5, 7, 9, 11, 13, 15, 17):
        answer.append(f'{i} * {j} = {i * j} / {i} * {j + 1} = {(j + 1) * i}')
    
    answer.append(f'{i} * 19 = {i * 19}')

print('\n'.join(answer))
