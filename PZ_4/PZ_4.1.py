#Ввести 4 числа. Найти и вывести на экран сумму и количество
#отрицательных чисел

while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        d = int(input("Введите четвертое число: "))
        k = 0
        l = []
        if a<0:
            l.append(a)
            k+=1 
            print(l)
        elif b<0:
            l.append(b)
            k+=1
            print(l)
        elif c<0:
            l.append(c)
            k+=1
        elif d<0:
            l.append(d)
            k+=1
        t=sum(l)
        print(t, l, k)
        break
    except ValueError:
        print("Введите число правильно!")
        
