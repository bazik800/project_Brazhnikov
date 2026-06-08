"""Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
а во второй – все остальные. Посчитать количество полученных строк в каждом
файле."""

with open('ip_address.txt', 'r') as f:
    lines = f.readlines()

with open('reserved_qualified.txt', 'w') as f1, open('reserved_others.txt', 'w') as f2:
    count_first = 0
    count_second = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        ip_part = line.split('/')[0]
        octets = ip_part.split('.')
        first_octet = int(octets[0])
        second_octet = int(octets[1])
        if first_octet != 0 and second_octet != 0:
            f1.write(line + '\n')
            count_first += 1
        else:
            f2.write(line + '\n')
            count_second += 1

print(f'В файле reserved_qualified.txt: {count_first} строк')
print(f'В файле reserved_others.txt: {count_second} строк')
