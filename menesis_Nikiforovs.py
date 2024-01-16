februaris = input('Vai jūs vēlaties zināt dienas februārim?(jā/nē):')
if februaris == ('jā'):
    print(28)
    exit()
elif februaris == ('nē'):
    menesis = input('Vai jūs velaties zināt dienas jan, mar, mai, jūl, aug, okt, dec:(jā/nē)')
if menesis == ('jā'):
    print(31)
elif menesis == ('nē'):
    print(30)
else:
    print('kļūda')