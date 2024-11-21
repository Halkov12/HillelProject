import string
st1 = input('input:')
st2 = string.ascii_letters
a = st2.find(st1[0])
b = st2.find(st1[-1])
st3 =st2[a:b + 1 ]
print(st3)