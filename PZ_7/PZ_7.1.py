#Дан символ С, изображающий цифру или букву (латинскую или русскую). Если С изображает цифру,
# то вывести строку «digit», если латинскую букву — вывести строку «lat», если русскую — вывести строку «rus».
while True:
    from langdetect import detect
    t = str(input("Введите текст rus/en - ")) #Вводить какое то слово - Россия\English
    if t.isdigit():
        print("digit")
        break
    s = detect(t)
    if s == 'ru':
        print("rus")
    elif s == 'en':
        print("lat")
    break
