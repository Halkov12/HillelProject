def add_one(some_list):
    num = int("".join(map(str, some_list)))
    s = num + 1
    lst = [int(i) for i in str(s)]
    return lst
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")