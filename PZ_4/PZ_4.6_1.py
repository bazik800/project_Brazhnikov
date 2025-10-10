#Даны два целых числа A и B, причем A < B.
#Необходимо найти сумму всех целых чисел в промежутке от A до B включительно.

while True:
    try:
        k = 0
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if a > b:
            print("Введите числа правильно!")
            break
        while a <= b:
            k += b
            b -= 1
        print("Сумма промежутка: ", k)
        break
    except ValueError:
        print("Введите числа правильно!")
