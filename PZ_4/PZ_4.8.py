#Даны два целых числа A и B (A < B). Найдите сумму всех целых чисел от A до B включительно.
# Для решения используйте оператор цикла.
while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите первое число: "))

        if a > b or a < 0 or b < 0:
            print("Введите числа правильно!")
            break
        c = 0
        current = a
        while current <= b:
            c += current
            current += 1
        print("сумма всех целых чисел от A до B: ", c)
    except ValueError:
        print("Введите числа правильно!")
