#Даны два целых числа: A, B. 
#Проверить истинность высказывания: "Хотя бы одно из чисел A и b четное"

while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if a % 2 == 0 or b % 2 == 0:
            print("True")
        else:
            print("False")
        break
    except ValueError:
        print("Введите число правильно!")
