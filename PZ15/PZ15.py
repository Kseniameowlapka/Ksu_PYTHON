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

def add_client(full_name, periodic_payment, annual_rate, deposit_term, has_card):
    final_amount = calculate_final(periodic_payment, annual_rate, deposit_term)
    cursor.execute('''
    INSERT INTO Clients (full_name, periodic_payment, annual_rate, deposit_term, has_card, final_amount)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (full_name, periodic_payment, annual_rate, deposit_term, has_card, final_amount))
    conn.commit()

def calculate_final(periodic_payment, annual_rate, deposit_term):
    total = 0
    for _ in range(deposit_term * 12):  # 12 месяцев в году
        total = (total + periodic_payment) * (1 + annual_rate / 12 / 100)
    return round(total, 2)

add_client("Иванов Иван Иванович", 5000, 5, 3, True)

cursor.execute("SELECT * FROM Clients")
for row in cursor.fetchall():
    print(row)

conn.close()