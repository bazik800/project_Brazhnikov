#Средствами языка Python сформировать текстовый файл txt содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый файл txt следующего вида, предварительно выполнив требуемую обработку элементов
#Исходные данные
#Кол-во элементов, произведение элементов, повторяющиеся элементы, кол-во повторяющихся элементов, элементы больше 5 увеличены в 2 раза
import random

a = open('text.txt', 'w')
numbers = []
for i in range(10):
    n = random.randint(-10, 10)
    numbers.append(n) # Сохраняем в список, чтобы потом обработать
    a.write(str(n) + ' ')
a.close()

ss = open('text1.txt', 'w')

# 1. Кол-во элементов
c = 0
for i in numbers:
    c += 1
ss.write('Number of numbers: ' + str(c) + '\n')

# 2. Произведение элементов
prod = 1
for x in numbers:
    prod *= x
ss.write('Product: ' + str(prod) + '\n')

# 3. Повторяющиеся элементы и их количество
d = []
for x in numbers:
    if numbers.count(x) > 1 and x not in d:
        d.append(x)

c1 = 0
for i in d:
    c1 += 1

ss.write('Repeat: ' + str(d) + '\n')
ss.write('Count of repeat: ' + str(c1) + '\n')

# 4. Элементы больше 5 увеличены в 2 раза
new_numbers = []
for x in numbers:
    if x > 5:
        new_numbers.append(x * 2)
    else:
        new_numbers.append(x)
ss.write('Elements > 5 doubled: ' + str(new_numbers) + '\n')

ss.close()
