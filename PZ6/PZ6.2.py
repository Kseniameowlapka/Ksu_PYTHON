def last_local_maximum_index(arr):
    n = len(arr)
    if n == 0:
        return None  # Если список пустой

    for i in range(n - 1, 0, -1):
        if arr[i] > arr[i - 1] and (i == n - 1 or arr[i] > arr[i + 1]):
            return i  # Возвращаем индекс локального максимума

    return None  # Если локальных максимумов нет

# Пример использования
arr = [1, 3, 2, 5, 4, 7, 6]
result = last_local_maximum_index(arr)
print(result)  # Выводит индекс последнего локального максимума
