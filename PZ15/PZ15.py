#Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
#источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
#книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
#Название книги, Год выпуска, Аннотация.
import sqlite3 as sq

books_data = [
    ('001', 'Роман', 'Россия', 'Классика', 'Лев Толстой', 'Война и мир', 1869, 'Роман-эпопея о войне 1812 года'),
    ('002', 'Фантастика', 'США', None, 'Рэй Брэдбери', '451° по Фаренгейту', 1953, 'Антиутопия о мире без книг'),
    ('003', 'Детектив', 'Великобритания', None, 'Артур Конан Дойл', 'Приключения Шерлока Холмса', 1892, 'Сборник рассказов о знаменитом сыщике'),
    ('004', 'Поэзия', 'Россия', 'Золотая серия поэзии', 'Александр Пушкин', 'Евгений Онегин', 1833, 'Роман в стихах'),
    ('005', 'Научная литература', 'Великобритания', None, 'Стивен Хокинг', 'Краткая история времени', 1988, 'Популярное изложение космологии')
]

def print_table(rows, headers):
    """Альтернатива tabulate для вывода таблицы"""
    # Определяем ширину столбцов
    col_widths = [
        max(len(str(row[i])) if rows else 0 for row in rows + [headers])
        for i in range(len(headers))
    ]
    
    # Создаем строку формата
    format_str = " | ".join([f"{{:<{w}}}" for w in col_widths])
    
    # Выводим заголовки
    print("\n" + format_str.format(*headers))
    print("-" * (sum(col_widths) + 3 * len(headers)))  # Разделитель
    
    # Выводим строки данных
    for row in rows:
        print(format_str.format(*[str(x) if x is not None else '' for x in row]))

with sq.connect('library.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS catalog 
    (book_id CHAR(3) PRIMARY KEY, 
    genre TEXT NOT NULL, 
    country TEXT, 
    series TEXT, 
    author TEXT NOT NULL, 
    title TEXT NOT NULL, 
    year INTEGER, 
    annotation TEXT)""")
    cur.executemany("INSERT INTO catalog VALUES (?, ?, ?, ?, ?, ?, ?, ?)", books_data)

    headers = ["Код", "Жанр", "Страна", "Серия", "Автор", "Название", "Год", "Аннотация"]
    
    print("\nИсходный каталог книг:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    print("\n1. Книги российских авторов:")
    cur.execute("SELECT * FROM catalog WHERE country = 'Россия'")
    print_table(cur.fetchall(), headers)

    print("\n2. Количество книг российских авторов:")
    cur.execute("SELECT COUNT(*) FROM catalog WHERE country = 'Россия'")
    print(f"Результат: {cur.fetchone()[0]}")

    print("\n3. Количество книг, изданных в XX веке:")
    cur.execute("SELECT COUNT(*) FROM catalog WHERE year BETWEEN 1901 AND 2000")
    print(f"Результат: {cur.fetchone()[0]}")

    print("\n4. Обновление страны издания (Россия → РФ):")
    cur.execute("UPDATE catalog SET country = 'РФ' WHERE country = 'Россия'")
    print("Страна издания обновлена. Обновленная таблица:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    print("\n5. Изменение жанра для научной литературы:")
    cur.execute("UPDATE catalog SET genre = 'Научно-популярная' WHERE genre = 'Научная литература'")
    print("Жанр обновлен. Обновленная таблица:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    print("\n6. Добавление серии для книг без серии:")
    cur.execute("UPDATE catalog SET series = 'Без серии' WHERE series IS NULL")
    print("Серия добавлена. Обновленная таблица:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    cur.execute("DELETE FROM catalog WHERE year < 1900")
    print("\n1. После удаления книг, изданных до 1900 года:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    cur.execute("DELETE FROM catalog WHERE country = 'США'")
    print("\n2. После удаления американских книг:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)

    cur.execute("DELETE FROM catalog WHERE genre LIKE '%Роман%'")
    print("\n3. После удаления романов:")
    cur.execute("SELECT * FROM catalog")
    print_table(cur.fetchall(), headers)