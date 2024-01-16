print('Izvēles iespējas: maxima, aibe, saulespuke, lats, vesko')
veikals = input('Uz kur veikalu jūs gribat doties?:')
preces = int(input('Cik preces jūs esat paņēmis?:'))
nosauk = input('Ievadiet preces nosaukumu:')
cena = float(input('noskaiet preces cenu:(€)'))
def karte():# funkcija kur tiek iekļauts jautājums
    input('Vai jums ir atlaižu karte?(j/n): ')
kopsumma = 0
atbilde = str()
def cena_kopa():
    cena * preces
while atbilde == 'nē':
    if preces <= 0 or cena < 0:
        exit()
    elif veikals == 'maxima':
        maxima_atlaide = cena_kopa * 0.3
    elif veikals == 'aibe':
        karte() # izveidota funkcija ar jautājumu(vai jums ir atlaižu karte?) lai nebūtu jāraksta atkārtoti pats jautājums.
        if karte() == 'j': # uz izveidotās funkcijas jautājumu ir jāatbilda ar j vai n
            aibe_atlaide = cena_kopa * 0.4
        else:
            aibe_atlaide = cena_kopa
    elif veikals == 'saulespuke':
        print('visām precēm ir 20 % atlaide, bet ar karti 50 %')
        karte() # izveidota funkcija ar jautājumu
        if karte() == 'j': #atbilde ar j vai n
            saule_atlaide = cena_kopa * 0.5
        else:
            saule_atlaide = cena_kopa * 0.2
    elif veikals == 'lats':
        if preces >= 3:
            lats_atlaide = cena_kopa * 0.3
        else:
            lats_atlaide = cena_kopa 
        
    elif veikals == 'vesko':
        daudzums = round(preces / 2) #katra otrā prece par brīvu
        vesko_atlaide = daudzums * cena     
    gala_summa = maxima_atlaide + aibe_atlaide + saule_atlaide + lats_atlaide + vesko_atlaide + kopsumma
atbilde = input('Vai ir nopirkts viss, kas sarakstā?(jā/nē)')

if atbilde == 'jā':
    print('veikals maxima: ',maxima_atlaide,'/nveikals aibe: ',aibe_atlaide,'/nveikals saulespuķe: ',saule_atlaide,'/nveikals lats: ',lats_atlaide,'/nveikals vesko: ',vesko_atlaide)
    print('--------------------------------')
    print('kopsumma: ',gala_summa)