num = int(input('input:'))
day = num // 86400
hrs = (num % 86400) // 3600
min = ((num % 86400) % 3600) // 60
sec = (((num % 86400) % 3600) % 60)
text = "{} День, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
text1 = "{} Дня, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
text2 = "{} Дней, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
x = str(day)
y = int(x[-1])
if y == 1:
    print(text)
elif 2 <= y <= 4:
    print(text1)
elif y > 4 or y == 0:
    print(text2)
