#Введите N чисел. Посчитать и вывести количество чисел равных нулю.

while True:
    try:
        count = 0
        a = int(input("Введите количество симловов для ввода: "))
        for _ in range(a):
            c = int(input("Введите число: "))
            if c == 0:
                count += 1
        print(count)


    except ValueError:
        print("Введенно неправильное число!")
