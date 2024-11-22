num = int(input('input:'))
while num > 9:
    res = 1
    for i in str(num):
        res *= int(i)
    num = res
print(num)