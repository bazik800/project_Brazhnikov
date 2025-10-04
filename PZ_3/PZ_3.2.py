#Смоделировать простейший калькулятор, умеющий выполнять 4 основные
#арифмитические операции


while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        d = input("Введите функцию + - * /: ")
        
        if d == "+":
            print(a+b)
            
        elif d == "-":
            print(a-b)
            
        elif d == "*":
            print(a*b)
            
        elif d == "/":
            print(a/b)
            
        break
    except ValueError:
        print("Введите число правильно!")
