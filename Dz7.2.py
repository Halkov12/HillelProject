def correct_sentence(text):
    if text[-1] != '.':
        up = text[0].upper()
        txt = up + text[1:] + '.'
    else:
        up = text[0].upper()
        txt = up + text[1:]
    return txt
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
