first_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for k in first_list:
    result = []
    for i in range(1, int(k)):
        for j in range(2, int(k)):
            if k == i + j and i != j and i < j:
                result.append(i)
                result.append(j)
            elif k % (i + j) == 0 and i != j and i < j:
                result.append(i)
                result.append(j)


    print(f'для числа {k} код из пары чисел = :{result}')