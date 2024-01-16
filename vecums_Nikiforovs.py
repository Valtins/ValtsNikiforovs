x = int(input('Ievadiet suņa vecumu:'))
if x < 0:
    print('kļūda') 
    exit()
if x<= 2:
    suna_vecums = x*10.5
elif x > 2:
    suna_vecums = (21+((x-2)*4))
print(suna_vecums)
