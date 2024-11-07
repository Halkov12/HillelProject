num = int(input('Введите 5и значное число:'))
num1 = num % 10
num2 = (num // 10) % 10
num3 = (num // 100) % 10
num4 = (num // 1000) % 10
num5 = (num // 10000)
num_rev = num1 * 10000 + num2 * 1000 + num3 * 100 + num4 * 10 + num5
print(num_rev)