num = int(input('input:'))
day = num // 86400
hrs = (num % 86400) // 3600
min = ((num % 86400) % 3600) // 60
sec = (((num % 86400) % 3600) % 60)
text = "{} День, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
text1 = "{} Дня, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
text2 = "{} Дней, {:02d}:{:02d}:{:02d}".format(day, hrs, min, sec,)
if 11 <= day % 100 <= 14:
    print(text2)
elif day % 10 == 1:
    print(text)
elif 2 <= day % 10 <= 4:
    print(text1)
else:
    print(text2)
