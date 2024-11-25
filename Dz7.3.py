def second_index(text, some_str):
    v1 = text.replace(some_str, some_str.swapcase(), 1)
    v2 = v1.find(some_str)
    if v2 <= 0:
        v2 = None
    else:
        return v2
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
