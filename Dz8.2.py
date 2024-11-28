import string
def is_palindrome(text):
    t2 = ''
    res = None
    for i in text:
        if i in string.punctuation or i == ' ':
            continue
        else:
            t2 += i
    if t2.lower() == t2[::-1].lower():
        res = True
    else:
        res = False
    return res
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")