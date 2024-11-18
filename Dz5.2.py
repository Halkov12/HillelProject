c = 'y'
c = c.lower()
while c == 'y':
    num1 = float(input('Введите первое число:'))
    num2 = float(input('Введите второе число:'))
    act = input('Введите действие:')
    if act == '+':
        print('Результат', num1 + num2)
    elif act == '-':
        print('Результат', num1 - num2)
    elif act == '*':
        print('Результат', num1 * num2)
    elif act == '/':
        if num2 == 0:
            print("На ноль делить нельзя")
        else:
            print('Результат', num1 / num2)
    c = input('Хотите продолжить Y/N ?:')