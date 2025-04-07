#Дан словарь с четным количеством элементов. Найти суммы значений
#элементов первой и второй половин с использованием функции. Результаты вывести
#на экран.


def sum_h(a):

  if len(a) % 2 != 0:
    print("Словарь должен быть с четным количеством элементов")
    return None

  mid = len(a) // 2  
  vals = list(a.values()) 
  return sum(vals[:mid]), sum(vals[mid:])


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = sum_h(my_dict)

if result: 
  first_half, second_half = result
  print("Сумма первой половины:", first_half)
  print("Сумма второй половины:", second_half)
