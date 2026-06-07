# В матрице элементы первого столбца возвести в куб.
matrix = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 1]
]

result = list(map(lambda row: [row[0] ** 3] + row[1:], matrix))
print(matrix)
print(result)
