# функция - проверка ввода числовых значений
# пример: 435, 2.9, -8, +4.7, -.9

numbers = '0123456789'
sign = '+-'

def isit_num(num):
    dot = 0
    for i in range(len(num)):
        digit = num[i]
        if digit not in numbers:
            if digit in sign and i == 0:
                continue
            elif digit == '.' and dot == 0:
                dot = 1
            else:
                return False
        else:
            continue
    return True

    
