valstis = {'Latvija' : '1893700',
           'Igaunija' : '1329460',
            'Omana' : '4660593',
            'Peru' : '32495510',
            'Venecuela' : '32219521',
            'Gvatemala' : '17679735',
            'Kostarika' : '5058007',
            'Urugvaja' : '3518552',
            'Indonezija' : '268074600',
            'Meksika' : '126577691'}
sakartotas_aug = sorted(valstis) # izveido mainīgos kārtošanai augošā secībā
sakartotas_dil = sorted(valstis, reverse=True)#izveido mainīgo kārtošanai dilstošā sec.

while True:
    atbilde = input('1-augoši, 2-dilstoši, 3-pievienot, 4-apskatīt visu, 5-skaitļi augoši: ')# doti izvēles varianti
    if atbilde == '1':
        print('Valstu nosaukumi augošā secībā: ',sakartotas_aug)#uzraksta izveidoto mainīgo lai sakārtotu augošā secībā valstis
    elif atbilde == '2':
        print('Valstu nosaukumi dilstošā secībā: ',sakartotas_dil)#uzraksta izveidoto mainīgo lai sakārtotu dilstošā secība valstis
    elif atbilde == '4':#Izdrukās lai spētu apskatīt valstis
        print(valstis)
    elif atbilde == '3':#jāievada valsti un iedzīvotāju skaitu
        atslega = input('Ievadiet kādu Valsti jūs vēlaties: ')
        vertiba = input('Ievadiet iedzīvotāju skaitu: ')
        pievienota_valsts = valstis[atslega] = vertiba
        print('Valsts nosaukumi ar pievienoto valsti',pievienota_valsts)
    elif atbilde == 'stop':
        exit()
    elif atbilde == '5':
        kartots=sorted(valstis,key=valstis.get)#sakārto vērtības jeb iedzīvotāju skaitu augošā secībā 
        for vertiba in kartots:
            print(vertiba,valstis[vertiba])        
    else:
        print('Ievadiet norādīto skaitli')