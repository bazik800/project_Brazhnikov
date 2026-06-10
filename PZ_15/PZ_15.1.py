""Тур-агенство. Код клиента, клиент фамилия, телефон, название страны, регион, продолжительность поездки, стоимость путевки""

import sqlite3
from db import insert_data

DB_NAME = "tour_agency.db"


def main(title, rows):
    print(f"\n{title}:")
    for row in rows:
        print(row)


with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    #создание таблицы
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tourist (
            client_code INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            country_name TEXT NOT NULL,
            region TEXT NOT NULL,
            duration INTEGER NOT NULL,
            cost REAL NOT NULL
        )
    """)

#вызов функции заполнения
insert_data()

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    #вывод всей таблицы
    cursor.execute("SELECT * FROM tourist")
    main("Исходное состояние базы данных", cursor.fetchall())

    #поиск по стране
    cursor.execute("SELECT * FROM tourist WHERE country_name = 'Италия'")
    main("Поиск туристов из страны 'Италия'", cursor.fetchall())

    #фильтр по цене и дням
    cursor.execute("SELECT * FROM tourist WHERE cost <= 100000 AND duration > 5")
    main("Поиск путевок дешевле 100000 и длиннее 5 дней", cursor.fetchall())

    #поиск по букве фамилии
    cursor.execute("SELECT * FROM tourist WHERE last_name LIKE 'С%'")
    main("Поиск туристов на букву 'С'", cursor.fetchall())

    #обновление записей
    cursor.execute("UPDATE tourist SET cost = 140000.00 WHERE client_code = 2")
    cursor.execute("UPDATE tourist SET cost = cost * 1.1 WHERE country_name = 'Турция'")
    cursor.execute("UPDATE tourist SET duration = duration - 1 WHERE client_code = 3 AND duration >= 1")
    #сохранение правок
    conn.commit()

    #вывод после редактирования
    cursor.execute("SELECT * FROM tourist")
    main("Состояние базы после редактирования", cursor.fetchall())

    #удаление записей
    cursor.execute("DELETE FROM tourist WHERE client_code = 1")
    cursor.execute("DELETE FROM tourist WHERE duration = 0")
    #сохранение удаления
    conn.commit()

    #финальный вывод
    cursor.execute("SELECT * FROM tourist")
    main("Состояние базы после удаления", cursor.fetchall())
