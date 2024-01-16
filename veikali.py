print('Izvēles iespējas: maxima, aibe, saulespuke, lats, vesko')
veikals = input('Uz kur veikalu jūs gribat doties?:')
preces = int(input('Cik preces jūs esat paņēmis?:'))
nosauk = input('Ievadiet preces nosaukumu:')
cena = float(input('noskaiet preces cenu:(€)'))
kopsumma = 0
atbilde = str()
while atbilde == 'nē':
    if preces <= 0 or cena < 0:
        exit()
    elif veikals == 'maxima':
        maxima_atlaide = cena * 0.3
    elif veikals == 'aibe':
        print('atlaide ar karti ir 40%.')
        x = input('Vai jums ir atlaižu karte?:(j/n)')
        if x == 'j':
            aibe_atlaide = preces * cena * 0.4
        else:
            aibe_atlaide = cena * preces
    elif veikals == 'saulespuke':
        print('visām precēm ir 20 % atlaide, bet ar karti 50 %')
        y = input('Vai jums ir atlaižu karte?:(j/n)')
        if y == 'j':
            saule_atlaide = cena * preces * 0.5
        else:
            saule_atlaide = cena * preces * 0.2
    elif veikals == 'lats':
        if preces >= 3:
            lats_atlaide = cena * preces * 0.3
        else:
            lats_atlaide = cena *preces 
        
    elif veikals == 'vesko':
        daudzums = round(preces / 2) #katra otrā prece par brīvu
        vesko_atlaide = daudzums * cena     
    gala_summa = maxima_atlaide + aibe_atlaide + saule_atlaide + lats_atlaide + vesko_atlaide + kopsumma
atbilde = input('Vai ir nopirkts viss, kas sarakstā?(jā/nē)')

if atbilde == 'jā':
    print('veikals maxima: ',maxima_atlaide,'/nveikals aibe: ',aibe_atlaide,'/nveikals saulespuķe: ',saule_atlaide,'/nveikals lats: ',lats_atlaide,'/nveikals vesko: ',vesko_atlaide)
    print('--------------------------------')
    print('kopsumma: ',gala_summa)






