def common_elements():
    lst1 = [i for i in range(0, 101) if i % 3 == 0]
    lst2 = [i for i in range(0, 101) if i % 5 == 0]
    set1 = set(lst1)
    set2 = set(lst2)
    set3 = set1.intersection(set2)
    return set3
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('Ok')