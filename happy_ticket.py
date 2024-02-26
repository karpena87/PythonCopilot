value = input ('Введите номер билета, состоящий из цифр ')
print ('Ваш билет: '+ value)
lenth_value = len (value)
cond_1 = lenth_value % 2  #проверка условия 1: четное количество символов
cond_2 = value.isdigit() #проверка условия 2: строка содержит только числовые символы

if cond_1 == 0 and cond_2:
    middle = lenth_value / 2 #промежуточная переменная
    i = 0
    summ_1 = int (value [i]) #сумма первой половины цифр
    while i < (middle - 1):
        i = i + 1
        summ_1 = int (value [i]) + summ_1
    print ('Сумма первой половины цифр '+ str (summ_1)) #для проверки вывод суммы

    summ_2 = 0 #сумма второй половины цифр
    while i < (lenth_value - 1):
        i = i + 1
        summ_2 = int (value [i]) + summ_2
    print ('Сумма второй половины цифр '+ str (summ_2)) #для проверки вывод суммы

    if summ_1 == summ_2:
        print ('Ваш билет счастливый!')
    else: print ('Билет не счастливый')

else:
    print ('Условия задачи не выполнены')

