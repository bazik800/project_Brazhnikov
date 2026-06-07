# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
source_matrix = [
    [5, 12, 3],
    [20, 8, 11],
    [1, 15, 7]
]

print(source_matrix)

matrix2 = [
    list(map(lambda x: 0 if x > 10 else x, row)) 
    for row in source_matrix
]

print(matrix2)
