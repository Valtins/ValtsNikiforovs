
augumi = {'Izle' : 172,'Jānis' : 185, 'Lelde' : 164, 'Jēkabs' : 184, 'Līga' : 162, 'kārlis' : 164, 'Ralfs' :165, 'Dāvids' : 167, 'Liene' : 177, 'Aiga' : 184, 'Zigmunds' : 165, 'Daiga' : 180}
print(augumi)
while True: # kamēr pareizi while loop turpina darboties
        print('1-drukāt') 
        print('2-pievienot')
        print('3-izdzēst')
        print('4-iziet')
        atbilde = input('1-drukāt 2-pievienot 3-izdzēst 4-iziet:')
        if atbilde == 1: # ja atbilde ir 1, tad tiek izdrukāti visi dati
                print('Jūs izvēlējāties 1 lai apskatītu datus-',atbilde)
        elif atbilde == 2: #ja atbilde ir 2, tad pajautā datus kurus vēlas pievienot
                vards = input('Ievadiet vārdu, kuru vēlaties pievienot: ')
                augums = input('ievadiet augumu: ')
                augumi[vards] = augums#pievieno jauno atslēgu ar vērtību
                print(augumi)#izprintē visus datus
                print('vārdnīcā atrodas ',len(augumi),' dati')
        elif atbilde == 3: # ja atbilde ir 3, tad pajautā, lai izvēlas kurus datus dzēst
                dzest = input('Izvēlieties kurus datus dzēsīsiet: ')
                augumi.pop(dzest)#izdzēš datus
                print('Lietotājs izdzēsa', dzest)
                print(augumi)
        else:
                exit()#iziet no programmas


