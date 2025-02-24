"""Игра Угадай число
компьютер сам загадывает и сам отгадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Угадываем случайное число

    Args:
        number (int, optional): Случайное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break # конец игры - выход из цыкла.
    return(count)

def score_game(random_predict) -> int:
    """Среднее кол-во попыток для угадывания из 1000 подходов 

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее кол-во попыток
    """
    count_ls = []
    np.random.seed(1) # передаем в генератор случайных чисел начальное число
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)  

#if __name__ == '__main__' :
    #RUN
    
score_game(random_predict)