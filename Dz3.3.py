#[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] => [[1, 2], [3]]
#[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
#[1] => [[1], []]
#[] => [[], []]
lst0 = [1, 2, 3, 4, 5, 6]
x = len(lst0) % 2
y = len(lst0) // 2
if x == 0:
    lst1 = lst0[:y]
    lst2 = lst0[y:]
    lst_lst = [lst1, lst2]
    print(lst_lst)
else:
    lst1 = lst0[:y+1]
    lst2 = lst0[y+1:]
    lst_lst = [lst1, lst2]
    print(lst_lst)