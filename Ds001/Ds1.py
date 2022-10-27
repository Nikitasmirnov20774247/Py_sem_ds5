# Задача 1. Создайте программу для игры с конфетами человек против человека.
# а) Подумайте как наделить бота ""интеллектом""

try:
    from random import randint

    def player_step(player, max):
        take = int(input(f'{player} возьмите конфеты (от 1 до {max}): '))
        while take < 0 or take > max:
            take = int(input(f'{player} введите корректное количество конфет (от 1 до {max}): '))
        return take
    
    def bot_step(candies, max):
        d = candies//max
        step = candies - (d*max+1)
        if step == -1:
            step = max -1
        elif step == 0:
            step = max
        return step

    def game_candies():
        player = input('Введите имя: ')
        bot = "Bot"
        candies = 2021
        max = 28
        player_change = randint(0,1)
        scoreplayer = 0
        scorebot = 0

        if player_change == True:
            print(f'---Первый ходит {player}---')
        else:
            print(f'---Первый ходит {bot}---')

        while candies > max:
            if player_change == True:
                take1 = player_step(player, max)
                candies -= take1
                player_change = False
                scoreplayer += take1
                print(f'{player} - взял {take1} конфет. Всего осталось {candies} конфет. Счёт конфет {player} = {scoreplayer} \n')
            else:
                take2 = bot_step(candies, max)
                candies -= take2
                player_change = True
                scorebot += take2
                print(f'{bot} - взял {take2} конфет. Всего осталось {candies} конфет. Счёт конфет {bot} = {scorebot} \n')   
        
        if player_change == True:
            print(f'$$$ Выиграл {player}! - финальный счёт = {scoreplayer + candies} $$$')
        else:
            print(f'$$$ Выиграл {bot}! - финальный счёт = {scorebot + candies} $$$')

    game_candies()
except: 
    print('!! Введите целое число !!')