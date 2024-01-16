#30 dienas Python programmēšanas valodā
vards = 'Kārlis'
uzvards = 'Cālis'
iesauka = ('vards, uzvards')
valsts = 'Latvija'
pilsēta = 'Liepāja'
vecums = '30 gadi'
gadi = '1991. g.' 
dati = (', uzvards, iesauka, vecums, valsts, pilsēta, gadi')
print('vards','\nuzvards','\niesauka','\nvalsts','\npilsēta','\nvecums','\ngadi','\ndati')
print(type(dati))
print(type(vards))
print(type(uzvards))
print(type(iesauka))
print(type(valsts))
print(type(pilsēta))
print(type(vecums))
print(type(gadi))

laiks = int(input('cikos jūs savākt?:'))
if laiks >= 23 or laiks <= 24 or laiks > 0 or laiks <= 5:
    cena_diennaktij = 0.67
elif laiks <= 22:
    cena_diennaktij = 0.57