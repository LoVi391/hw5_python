# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.
# import random

# playerOne = input('Введите имя первого игрока ')
# playerTwo = input('Введите имя второго игрока ')

# firstunnumber = random.randint(1, 100)
# secturnnumber = random.randint(1, 100)

# if( firstunnumber > secturnnumber): print(f'{playerOne} ходит первый')
# else: print(f'{playerTwo} ходит первый')

# num2 = 2021
# n = 0
# while num2 > 0:
#     num1 = int(input('Введите число до 28: '))
#     if num1 > 28: print('неверно, число должно быть меньше 28!')
#     else: 
#         num2 -= num1
#         print(f'Осталось {num2} конфет')
#         n = n+1
# if(n%2==0): print(f'Выиграл {playerTwo}')
# else: print(f'Выиграл {playerOne}')

# a) Добавьте игру против бота

import random

num2 = 40
while num2 > 0:
    num1 = int(input('Введите число до 28: '))
    if num1 > 28: print('неверно, число должно быть меньше 28!')
    else: 
        num2 -= num1
        if num2 <= 0: print('Вы выиграли!')
        else: 
            comp = random.randint(1, 28)
            print(f'Компьютер выбрал {comp}')
            num2 -= comp
            if num2 <= 0: print('Выиграл бот')
            print(f'Осталось {num2} конфет')