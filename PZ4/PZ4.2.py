#Дано целое число N (> 0). Используя операции деления нацело и взятия остатка от
#деления, найти число, полученное при прочтении числа N справа налево.

def reverse_number(N):
    reversed_number = 0
    while N > 0:
        reversed_number = reversed_number * 10 + N % 10
        N //= 10
    return reversed_number

N = int(input("Введите целое число N (> 0): "))
if N > 0:
    print("Число N, прочитанное справа налево:", reverse_number(N))
else:
    print("Ошибка: N должно быть больше 0.")
