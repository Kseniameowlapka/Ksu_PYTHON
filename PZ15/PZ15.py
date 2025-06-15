#Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
#источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
#книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
#Название книги, Год выпуска, Аннотация.

import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    periodic_payment REAL NOT NULL,
    annual_rate REAL NOT NULL,
    deposit_term INTEGER NOT NULL,
    has_card BOOLEAN NOT NULL,
    final_amount REAL NOT NULL
)
''')

data = [
    ("Bwfe F F", 7, 3.4, 12, True, 1400),
    ("wefe F", 7, 7.5, 122, True, 400),
    ("gkjow F F", 7, 3, 1, False, 140),
    ("pfwj F F", 7, 4, 24, True, 100),
]
cursor.executemany('''
        INSERT INTO Clients 
        (full_name, periodic_payment, annual_rate, deposit_term, has_card, final_amount)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
conn.commit()
def add_clients():
    print(f"\n Добавление клиента:")
    full_name = input("ФИО: ")
    periodic_payment = float(input("Периодический платёж: "))
    annual_rate = float(input("Годовая ставка (%): "))
    deposit_term = int(input("Срок вклада (в месяцах): "))
    has_card = int(input("Есть карта? (1 - да, 0 - нет): "))
    final_amount = float(input("Итоговая сумма вклада: "))

    cursor.execute('''
        INSERT INTO Clients 
        (full_name, periodic_payment, annual_rate, deposit_term, has_card, final_amount)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (full_name, periodic_payment, annual_rate, deposit_term, has_card, final_amount))
    conn.commit()

def search_clients():
    print("\n Поиск клиентов:")
    print("1. По ФИО")
    print("2. По годовому проценту")
    print("3. По наличию карты")

    choice = input("Выберите вариант: ")

    if choice == "1":
        val = input("ФИО: ")
        cursor.execute("SELECT * FROM Clients WHERE full_name = ?", (val,))
    elif choice == "2":
        val = float(input("Годовая ставка: "))
        cursor.execute("SELECT * FROM Clients WHERE annual_rate = ?", (val,))
    elif choice == "3":
        val = int(input("Есть карта? (1 - да, 0 - нет): "))
        cursor.execute("SELECT * FROM Clients WHERE has_card = ?", (val,))
    else:
        print("Неверный выбор.")
        return

    for row in cursor.fetchall():
        print(row)
    else:
        print("Никого нет")

def delete_clients():
    print("\n Удаление клиентов:")
    print("1. По ID")
    print("2. По ФИО")
    print("3. По итоговой сумме вклада")

    choice = input("Выберите вариант: ")

    if choice == "1":
        val = int(input("ID клиента: "))
        cursor.execute("DELETE FROM Clients WHERE id = ?", (val,))
    elif choice == "2":
        val = input("ФИО: ")
        cursor.execute("DELETE FROM Clients WHERE full_name = ?", (val,))
    elif choice == "3":
        val = float(input("Итоговая сумма: "))
        cursor.execute("DELETE FROM Clients WHERE final_amount = ?", (val,))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print("Удаление завершено.")

def edit_clients():
    print("\n Редактирование клиентов:")
    print("1. Изменить платёж по ID")
    print("2. Изменить процент по ФИО")
    print("3. Изменить итоговую сумму по ID")

    choice = input("Выберите вариант: ")

    if choice == "1":
        client_id = int(input("ID клиента: "))
        new_value = float(input("Новый периодический платёж: "))
        cursor.execute("UPDATE Clients SET periodic_payment = ? WHERE id = ?", (new_value, client_id))
    elif choice == "2":
        name = input("ФИО клиента: ")
        new_rate = float(input("Новая годовая ставка: "))
        cursor.execute("UPDATE Clients SET annual_rate = ? WHERE full_name = ?", (new_rate, name))
    elif choice == "3":
        client_id = int(input("ID клиента: "))
        new_amount = float(input("Новая итоговая сумма: "))
        cursor.execute("UPDATE Clients SET final_amount = ? WHERE id = ?", (new_amount, client_id))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print("Редактирование завершено.")

while True:
    print("1. Добавить клиентов")
    print("2. Поиск")
    print("3. Удаление")
    print("4. Редактирование")
    print("5. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_clients()
    elif choice == "2":
        search_clients()
    elif choice == "3":
        delete_clients()
    elif choice == "4":
        edit_clients()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Повторите.")

conn.close()