jautajums = input('Vai jums ir nepieciešamas grāmatas vai žurnāli, kas ir pieprasīto izdevumu sarakstā?(jā/nē)')
if jautajums == 'jā':
    publikacijas=input('kas jums ir nepieciešams?(grāmatas/žurnāli/abi)')
elif publikacijas == 'grāmatas':

    cilveks = input('Vai jūs esat?(students/personāls/klients)')
elif cilveks == 'studets':
    print('grāmatas, kas nav pieprasītos izdevumus jums izsneidz uz 15 dienām')
elif cilveks == 'personals':
                print('Grāmatas, kas nav pieprasītos izdevumus jums izsniedz uz 30 dienām')
                if cilveks == 'klients':
                    print() 

if jautajums == 'abi':
     print('visas publikācijas izsniedz ikvienam uz 10 dienām')
