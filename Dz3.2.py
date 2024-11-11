
#[12, 3, 4, 10]
#[1]
#[]
#[12, 3, 4, 10, 8]
lst = [12, 3, 4, 10, 8]
if len(lst) > 0:
    last = lst[-1]
    lst.insert(0,last )
    x = lst.pop(-1)
    print(lst)
else:
    print(lst)