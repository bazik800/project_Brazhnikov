"""Составить генератор yield, который преобразует символы строки из
верхнего регистра в нижний"""

def WW(f):
    for i in f:
        yield i.lower()

d = str(input("--"))
s = WW(d)
for i in s:
    print(i)
