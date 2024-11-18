import string
import keyword
s = input("Name:")
cont = True
if  s[0] in string.digits :
    cont = False
elif (len(s) > 1) == True and s.islower() == False:
    cont = False
elif keyword.iskeyword(s) == True:
    cont = False
for i in s:
    if i == ' ':
        cont = False
    if i in string.punctuation:
        if i == '_':
            continue
        cont = False
print(cont)