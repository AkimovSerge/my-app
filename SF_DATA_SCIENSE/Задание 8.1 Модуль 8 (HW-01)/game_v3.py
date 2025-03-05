mu_list = []
for i in range(1, 101):
    mu_list.append(i)
#print(mu_list)
number = 60
predict_number = 75
mid_idx = (predict_number - 1)# находим индекс элемента в списке.
#if mu_list[mid_idx] > number:
if predict_number > number:
    predict_number = np.mean(mu_list[ : mid_idx])
    print(round(predict_number))
else:
    predict_number = np.mean(mu_list[mid_idx: ])
    print(round(predict_number))