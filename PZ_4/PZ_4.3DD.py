#Найти и вывести на экран S=1!+2!+3!...+n! (n>1)


while True:
    try:
        n=int(input("Введите число: "))
        s = 0
        f = 1
        i = 1
        
        if n < 1:
            print("Введите число правильно!")
        
        while i <= n:
            f *= i
            s+=F
            i+=1
        print(s)
        break
    except ValueError:
        print("Введите число правильно!")
