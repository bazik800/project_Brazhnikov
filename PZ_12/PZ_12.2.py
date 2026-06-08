import random
x = int(input("Введите количество строк: "))
y = int(input("Введите количество столбцов: "))

# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
matrix = [
    [random.randint(1, 20) for _ in range(y)]
    for _ in range(x)
]
for row in matrix:
    print(row)


matrix2 = [
    list(map(lambda x: 0 if x > 10 else x, row))
    for row in matrix
]
print("\n")
for row in matrix2:
    print(row)
