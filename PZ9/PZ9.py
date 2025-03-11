#Дан словарь с четным количеством элементов. Найти суммы значений
#элементов первой и второй половин с использованием функции. Результаты вывести
#на экран.


def sum_h(a):

  if len(a) % 2 != 0:
    print("Словарь должен быть с четным количеством элементов")
    return None  # Возвращаем None, чтобы указать на ошибку

  mid = len(a) // 2  # Находим середину
  vals = list(a.values())  # Получаем список значений
  return sum(vals[:mid]), sum(vals[mid:]) # возвращаем сумму половин


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = sum_h(my_dict)

if result:  # Проверяем, что результат не None (т.е. словарь четный)
  first_half, second_half = result
  print("Сумма первой половины:", first_half)
  print("Сумма второй половины:", second_half)
