def edienkarte():
    print('------------------------------')
    print('')
    print('')
    print('1.ābols un ūdens glāze')
    print('')
    print('2.soļanka')
    print('')
    print('3.šokolādes batoniņš')
    print('')
    print('4.kartupeļu biezputra ar cūkgaļas karbonādi un kvass')
    print('')
    print('5.siermaizīte un tomātu sula')
    print('')
    print('6.kartupeļu pankūkas un ābolu sula')
    print('')
    print('')
    print('------------------------------')

EdienreizuSkaits = int(input('Cik reizes dienā jūs ēdat?'))
if EdienreizuSkaits >= 6:
    print('Nebūs pa daudz?')
while EdienreizuSkaits > 0:
    EdienreizuSkaits-=1
    print(edienkarte())
    izvele= int(input('Izvēlieties no ēdienkartes sev vēlamo vienai ēdienreizei ēdienu(1/2/3/4/5/6): '))
    if izvele == '1':
        abols=49 
        print('jūsu ēdiena kaloriju daudzums ir:', abols,'kcal')
    elif izvele == '2':
        solanka = 76
        print('jūsu ēdiena kaloriju daudzums ir: ')
    elif izvele == '3':
        sokolades_batonins = 426
        print('jūsu ēdiena kaloriju daudzums ir: ')
    elif izvele == '4':
        kartupelu_biezputra = 83+149+34
        print('jūsu ēdiena kaloriju daudzums ir: ')
    elif izvele == '5':
        siermaizite = 292+57
        print('jūsu ēdiena kaloriju daudzums ir: ')
    elif izvele == '6':
        pankukas = 260+114
        print('jūsu ēdiena kaloriju daudzums ir: ')