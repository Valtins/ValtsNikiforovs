kontakti = {'vards': [], 'numurs':[]} #kā vērtības sākumā ielikt tukšos saraksus
kontakti['vards'] = ['Anna','Zane','Jānis','Gustavs']
kontakti['numurs'] = ['12547865','45697456','26588965','12365445']
while True:
    izvele = input('ko vēlaties darīt?'
                   '1-drukāt'
                   '2-pievienot'
                   '3-izdzēst'
                   '4-iziet')
    iespeja = input()
    if iespeja == '1':
        print('Jūs uzspiedāt taustiņu 1: jūsu kontakti uz ekrāna:','\n',kontakti)
        print('-----------------------------')    
    elif iespeja == 2:
        print('Jūs uzspiedāt taustiņu 2: pievieno jaunu kontaktu:')
        vards = input('Ievadi vārdu: ')
        numurs = int(input('ievadi numuru:'))
        kontakti['vards'].append(vards)
        kontakti['numurs'].append(numurs)
        print('------------------------------')
    elif iespeja == 3:
        print('Jūs uzspiedāt taustiņu 3: izdzēst kontaktu')
        
