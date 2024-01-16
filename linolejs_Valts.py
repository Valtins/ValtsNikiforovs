import math
linoleja_cena = float(input('Ievadi linoleja cenu m^2: '))
platums = float(input('Ievadi ruļļa platumu m: '))
telpa = float(input('Ievadi telpas platību m^2: '))
apaksklajs = input('Vai vēlaties ieklāt apakšklāju?(jā/nē):')
if apaksklajs == 'jā':
    cena_apaksklajam = float(input('Ievadiet apakšklāja cenu uz m^2:'))
else:
    cena_apaksklajam = 0
nepieciesams = math.ceil(telpa)
atlikums = nepieciesams - telpa
kopeja_apaksklaja_cena = cena_apaksklajam * nepieciesams
izmaksas = (nepieciesams * linoleja_cena) + cena_apaksklajam
garums = round(telpa / platums) 
print('–-----------------------------')
print('Nepieciešams ',nepieciesams,'m^2')
print() 
print('Atlikums ',atlikums,'m^2')
print()
print('izmaksas ',izmaksas, 'euro')
print()
if apaksklajs == 'jā':    
    print('Apakšklājs ',kopeja_apaksklaja_cena, 'euro' )
    print('------------------------------')
