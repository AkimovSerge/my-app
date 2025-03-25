import numpy as np
import math
count = 0

mu_list = []
for i in range(1, 101):
   mu_list.append(i)
prediction = (50, 101, 1) # predict_number = 50, up_limiter = 101, low_limiter = 1
number = 75
while True:
    count +=1
    def fork(predict_number, up_limiter, low_limiter) -> int: 
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
    prediction = fork(*prediction)
    if number == prediction[0]:
        break  # выход из цикла - Алгоритм расчитал число!
print(f"Алгоритм расчитал число! Это число = {number}, за {count} циклов.")