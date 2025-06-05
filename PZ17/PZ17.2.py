# PZ 7.2 в Tk 

import tkinter as tk

def code():
    result.set(str(entry.get()[::2]+entry.get()[1::2][::-1])[::-1])

root = tk.Tk()
root.title("Шифратор")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Введите строку:").pack()
entry = tk.Entry(frame, width=30)
entry.pack()

result = tk.StringVar()
tk.Button(frame, text="Зашифровать", command=code).pack(pady=5)
tk.Label(frame, textvariable=result, font=("Arial", 12, "bold")).pack()

root.mainloop()