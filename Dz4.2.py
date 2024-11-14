#[1, 3, 5] => 30
#[6] => 36
#[0] => 0
lst = [1, 3, 5]
size = len(lst)
count = 0
if len(lst) > 0:
    for i in range(0, size, 2):
        count += lst[i]
    act = count * lst[-1]
    print(act)
else:
    print(0)
