def is_even(number):
    if number in range(0, number + 1, 2):
        return True
    else:
        return False
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')