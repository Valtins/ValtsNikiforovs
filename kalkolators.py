a = int(input('a='))
b = int(input('b='))
darbiba = input('saskaitīšana/atņemšana/reizināšana/dalīšana:')
if darbiba == 'saskaitīšana' :
    c = a+b
elif darbiba == 'atņemšana' :
    c = a-b
elif darbiba == 'reizināšana' :
    c = a*b
elif darbiba == 'dališana' :
    c = a/b
else :
    c = 'kļūda!'
print(c)
