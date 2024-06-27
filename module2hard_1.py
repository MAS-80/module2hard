k = int(input('Введите число от 3 до 20 : '))
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