# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def summ_number(number):
    summ = 0
    for char in str(number):
        if char.isdigit():
            summ += int(char)
    return summ
