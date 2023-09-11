import math

print('Vecvecākiem ir nenormāli daudz ābolu, ko viņi savāca no sava dārza. Viņi vēlās uzvārīt ievārījumu, lai āboli nesabojātos.')
print('')

cukursKg = float(input('Cukurs maksā 1.37€/kg. Cik kg cukura jūs nopirkāt?'))
samaksa = '%.2f'%(cukursKg * 1.37) #Funkcija, kas aprēķina cik samaksāja par cukuru
print('Kopā par cukuru jūs samaksājāt',samaksa,'€')

aboliKg = cukursKg

def ceks(): #Pie print funkcijas uzrakstīts 'samaksa', jo āboli vecvecākiem ir ļoti daudz, un tie nav jāpērk.
    print('-----------------------------')
    print('')
    print('Jūsu kopējās izmaksas ir',samaksa,'€')
    print('')
    print('-----------------------------')

CikSalds = input('Cik saldu ievārījumu viņi taisīs? (1.|Nedaudz| salds 2.|Salds| 3.|Ļoti| salds)')
 #Fukcija aprēķina ievārījuma daudzumu pēc tā, cik saldu to taisīs vecvecāki.
if CikSalds == 'Nedaudz':
    nedaudz = '%.2f'%(cukursKg + aboliKg * 2)
    print('Sanāks',nedaudz,'kg nedaudz salda ievārījuma')
    ceks()
elif CikSalds == 'Salds':
    salds = '%.2f'%(cukursKg + aboliKg)
    print('Sanāks',salds,'kg salda ievārījuma')
    ceks()
elif CikSalds == 'Ļoti':
    loti = '%.2f'%(cukursKg * 2 + aboliKg)
    print('Sanāks',loti,'kg ļoti salda ievārījuma')
    ceks()
else:
    print('Ievadītais saldums nav definēts.')
#Sekojām Lauras Egles un Valtera Vilņa specifikācijām!!!!!