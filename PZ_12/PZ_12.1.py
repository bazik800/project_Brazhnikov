import random
x = int(input("Введите количество строк: "))
y = int(input("Введите количество столбцов: "))

# Создаем матрицу с случайными числами от 1 до 10
matrix = [
    [random.randint(1, 10) for _ in range(y)]
    for _ in range(x)
]

for row in matrix:
    print(row)

result = list(map(lambda row: [row[0] ** 3] + row[1:], matrix))
print("\n")
for row in result:
    print(row)
