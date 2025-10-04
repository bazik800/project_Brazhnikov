#Ввести N чисел. Найти и вывести их среднее арифмитическое.

while True:
    try:
        count=0
        sum=0
        k = int(input("Введите количество симловов для ввода: "))
        while k>count:
            a = int(input("Введите число "))
            sum+=a
            count+=1
        print(sum / count)
    except ValueError:
        print("Введенно неправильное число!")
