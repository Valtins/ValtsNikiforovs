username = ('user')
parole = ('1001')
meginajumi = 5
while meginajumi >= 1:
    pareizs_username = input('Ievadiet savu lietotājvārdu: ')
    pareiza_parole = (input('Ievadiet savu paroli: '))
    if pareizs_username == 'stop' or pareiza_parole == 'stop':
        print('programmas beigas') 
        exit()
    elif pareizs_username != username or pareiza_parole != parole:
        print('Atlikušo mēģinājumu skaits ir', meginajumi)
        meginajumi -= 1
    elif pareizs_username == username and pareiza_parole == parole: 
        print('Pieslēgšanās ir veiksmīga.')
        continue
if meginajumi < 1:
    print('Jums tika doti 5 mēģinājumi!')
    exit()
    
skaitlis = int(input('Ievadiet pirmo veselo skaitli: '))
skaitlis2 = int(input('Ievadiet otro veselo skaitli: '))
skaitlis3 = skaitlis2 
while skaitlis2 > skaitlis:
    summa = skaitlis2 + skaitlis3
    skaitlis3 -= 1
    print(summa)
if skaitlis < 0 or skaitlis2 < 0:
    print('kļūda')