# Разработать программу с применением пакета tk

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма регистрации пользователя")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Форма регистрации пользователя", font=("Arial", 12, "bold")).pack(pady=5)

fields = [
    "Ваше имя:", "Пароль:", "Возраст:", "Пол:", "Ваши увлечения:", "Ваша страна:", "Ваш город:", "Кратко о себе:",
    "Решите пример, запишите результат в поле ниже:"
]

entries = {}
for field in fields[:3]:
    row = tk.Frame(frame)
    row.pack(fill="x", pady=2)
    tk.Label(row, text=field, width=15, anchor="w").pack(side="left")
    entries[field] = tk.Entry(row, width=30, show="*" if field == "Пароль" else None)
    entries[field].pack(side="right", fill="x", expand=True)

genderFrame = tk.Frame(frame)
genderFrame.pack(fill="x", pady=2)
tk.Label(genderFrame, text="Пол:", width=15, anchor="w").pack(side="left")
tk.Radiobutton(genderFrame, text="Мужской", value=1).pack(side="left")
tk.Radiobutton(genderFrame, text="Женский", value=2).pack(side="left")

hobbiesFrame = tk.Frame(frame)
hobbiesFrame.pack(fill="x", pady=2)
tk.Label(hobbiesFrame, text="Ваши увлечения:", width=15, anchor="w").pack(side="left")
tk.Checkbutton(hobbiesFrame, text="Музыка").pack(side="left")
tk.Checkbutton(hobbiesFrame, text="Видео").pack(side="left")
tk.Checkbutton(hobbiesFrame, text="Рисование").pack(side="left")

countryFrame = tk.Frame(frame)
countryFrame.pack(fill="x", pady=2)
tk.Label(countryFrame, text="Ваша страна:", width=15, anchor="w").pack(side="left")
ttk.Combobox(countryFrame, values=["Россия", "США", "Германия"]).pack(side="right", fill="x", expand=True)

cityFrame = tk.Frame(frame)
cityFrame.pack(fill="x", pady=2)
tk.Label(cityFrame, text="Ваш город:", width=15, anchor="w").pack(side="left")
ttk.Combobox(cityFrame).pack(side="right", fill="x", expand=True)

bioFrame = tk.Frame(frame)
bioFrame.pack(fill="x", pady=2)
tk.Label(bioFrame, text="Кратко о себе:", width=15, anchor="w").pack(side="left")
bioEntry = tk.Text(bioFrame, height=3, width=30)
bioEntry.pack(side="right", fill="x", expand=True)

taskFrame = tk.Frame(frame)
taskFrame.pack(fill="x", pady=2)
tk.Label(taskFrame, text="Решите пример:", width=15, anchor="w").pack(side="left")
tk.Entry(taskFrame, width=30).pack(side="right", fill="x", expand=True)

btnFrame = tk.Frame(frame)
btnFrame.pack(pady=10)
tk.Button(btnFrame, text="Отменить ввод").pack(side="left", padx=5)
tk.Button(btnFrame, text="Данные подтверждаю").pack(side="right", padx=5)

root.mainloop()