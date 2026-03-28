import random
a = open('text.txt', 'w')
d = []
d1 = []
c=0
c1=0
for i in range(10):
    n = random.randint(-10,10)  #Запись файла
    a.write(str(n) + ' ')
a.write('\n')

for i in range(10):
    c+=1
a.write('Number of numbers: ')     #Количество элементов
a.write(str(c))   
a.close()

s = open('text.txt', 'r+')
cont = s.readline()
numbers = [int(x) for x in cont.split()]
total = sum(numbers)        #Сумма
s.write('\nTotal sum: ')
s.write(str(total))
s.close()

q = open('text.txt', 'r+')
cont1 = q.readline()
for x in numbers:
    if numbers.count(x) > 1 and x not in d:        #Нахождение повторов
        d.append(x)
for i in d:         #Счетчик повторов
    c1+=1
q.write('\nRepeat: ')
q.write(str(d))
q.write('\nCount of repeat: ')
q.write(str(c1))
q.close()

e = open('text.txt', 'r+')
cont2 = e.readline()
for i in range(len(numbers)):
    if numbers[i] > 5:
        numbers[i] = numbers[i] * 2         #Увелечение элементов
e.write('\n<5: ')
e.write(str(numbers))





