"""Программа, выполняющая набор функций"""
from math import *


def f3(x, n):
    """Ряд Маклорена функции cos(x)"""
    """
    Функция, реализующая разложение 
    математической функции cos(x) в формате ряда Маклорена
    """
    """Аргументы:"""
    """
    x (принимается из функции menu), 
    n = 5 (задано в коде)
    """
    """Возвращаемое значение: float"""
    """Исключения не генерируются"""
    """Пример использования:"""
    """
    Ввод:  1
    Вывод: 0.540302303791887
    """
    answer = 1
    for i in range(1, n+1):
        answer += ((-1)**i) * (x**(2 * i) / factorial(2 * i))
    return answer


def f9(x, m, n):
    """Ряд Маклорена функции (1 + x)^m"""
    """
    Функция, реализующая разложение 
    математической функции (1 + x)^m в формате ряда Маклорена
    """
    """Аргументы:"""
    """ 
    x (принимается из функции menu), 
    m (принимается из функции menu), 
    n = 5 (задано в коде)
    """
    """Возвращаемое значение: float"""
    """Исключения не генерируются"""
    """Пример использования:"""
    """
    Ввод:  0.5
           3
    Вывод: 3.375
    """
    answer = 1
    for i in range(1, n+1):
        m_prod = m
        for j in range(1, i):
            m_prod *= (m - j)
        answer += (m_prod * x**i) / factorial(i)
    return answer


def menu(n = 5):
    """Меню"""
    """
    Функция, реализующая меню выбора 
    исполняемых функций и проверку ввода
    """
    """Аргументы: """
    """
    n = 5 (задано в коде), 
    option (вводится пользователем), 
    x (вводится пользователем), 
    y (вводится пользователем)
    """
    """Возвращаемое значение: 0"""
    """Исключения:"""
    """
    Ввод не является числом
    Ввод превышает граничные значения x
    """
    """Пример использования:"""
    """    
    Ввод: 1
    *выбор функции 3, запрос значения x*
    Ввод: 1
    *выполнение функции 3, возврат ответа*
    
    Ввод: 2
    *выбор функции 9, запрос значения x*
    Ввод: 0.5
    *запрос значения m*
    Ввод: 3
    *выполнение функции 9, возврат ответа*
    
    Ввод: 4
    *завершение работы*
    """
    while True:
        try:
            option = int(input("Выберите одну из опций:\n"
                         "1 - Функция 3 (cos(x))\n"
                         "2 - Функция 9 ((1 + x)^m)\n"
                         # "3 - Функция 10\n"
                         "4 - Выход\n"))
        except:
            print("Допустим только ввод целых чисел")
            continue
        match option:
            case 1:
                try:
                    x = float(input("Введите X: "))
                except:
                    print("Допустим только ввод чисел")
                    continue
                print("Ответ:", f3(x, n))
            case 2:
                try:
                    x = float(input("Введите X: "))
                    m = float(input("Введите M: "))
                except:
                    print("Допустим только ввод чисел")
                    continue
                if not -1 < x < 1:
                    print("X должен быть больше -1 и меньше 1")
                    continue
                print("Ответ:", f9(x, m, n))
            case 3:
                pass
            case 4:
                return 0
            case _:
                print("Допустим только ввод чисел от 1 до 3 включительно")
                # После добавление функции 10 - от 1 до 4


menu()