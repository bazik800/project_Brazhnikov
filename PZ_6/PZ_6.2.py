#Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум - это элемент, который меньше любого из своих соседей).
import random
n = int(input("Введите размер списка - "))
s = [random.randint(0,100) for i in range(n)]
d = []
for i in range(1, n-1):
    if s[i] < s[i-1] and s[i] < s[i+1]:
        d.append((i,s[i]))

print(s)
print(d)
print(max(d))
