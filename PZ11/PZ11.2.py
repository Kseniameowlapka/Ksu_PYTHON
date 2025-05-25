# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.

f = open("11.2.txt", "r", encoding="utf-8")
rl = f.readlines()
text = "".join(rl)
fo = open("11.2-output.txt", "w", encoding="utf-8")
[fo.writelines(i.lower()) for i in rl]
cnt = 0
l = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
[cnt := cnt + 1 for s in text if s.lower() in l]
print(text)
print(cnt)