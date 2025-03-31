import numpy as np
import math

def predictor(number):
    """Расчитываем (находим) случайное число в списке чисел (диапазон от 1 до 100).
    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: затраченное количество попыток.
    """
    count = 0
    mu_list = []
    for i in range(1, 101):
        mu_list.append(i)
    sector = (50, 101, 1) # predict_number = 50, up_limiter = 101, low_limiter = 1
    #number = 50
    while True:
        count +=1
        def fork(predict_number, up_limiter, low_limiter) -> int:
            """Расчитываем (находим) диапазон в списке чисел, которому принадле-
            жит искомое число.
            Args:
                sector = (int(tuple), optional): первоначально заданый сектор. 
                Defaults to (50, 101, 1).

            Returns:
                int: затраченное количество попыток.
            """
            mid_idx = (predict_number - 1)
            if predict_number > number:
                up_limiter = predict_number
                low_idx = low_limiter - 1
                predict_number = math.ceil(np.mean(mu_list[low_idx : mid_idx]))

            else: # predict_number < number
                low_limiter = predict_number
                up_idx = up_limiter - 1
                predict_number = math.ceil(np.mean(mu_list[mid_idx: up_idx]))

            return predict_number, up_limiter, low_limiter
        sector = fork(*sector)
        if number == sector[0]: # predict_number
            break  # выход из цикла - Алгоритм расчитал число!
    return count
    #print(f"Алгоритм расчитал число! Это число = {number}, за {count} циклов.")
def score_game(rpedictor) -> int:
    """За какое количство попыток в среднем, за 1000 подходов, расчитывает наш алгоритм

    Args:
        rpedictor ([type]): функция предсказания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # создаем список случайных чисел

    for number in random_array:
        count_ls.append(predictor(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм расчитывает число в среднем за: {score} попыток")
    #return score
#if __name__ == "__main__":
    # RUN
score_game(predictor)