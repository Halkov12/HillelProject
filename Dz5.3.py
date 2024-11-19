import string
ms = input("Input:")
ms = ms.title()
ms1 = ms.replace(' ', '')
ms3 = ''.join(i for i in ms1 if i not in string.punctuation)
if len(ms3) > 140:
    ms3 = ms3[:140]
print('#' + ms3)