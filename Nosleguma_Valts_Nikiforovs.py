from datetime import datetime

def sveiciens(): #Izveido funkcijus, kas rezultātā uzraksta sasveicināšanos.
    print('Esi sveicināts!')
    print('Programmā tiks apkopoti dati un pārnesti uz eksperimenta dati failu.')
    print('*********')
    return

def iegut_datus(nosaukums, vards, vieta, laiks):#Funkcija kurā ir 4 parametri ar prasītajiem kritērijiem.  
    vards = vards.capitalize() #Pārveido pirmo burtu kā lielo burtu, ja tas ir mazais
    vards = vards.replace(' ' , '')  #Noņem atstarpes.
    return f'Nosaukums eksperimentam: {nosaukums}, Laiks: {laiks}, Lietotājvārds: {vards}, Vieta: {vieta}\n'

def saglabat_datus(dati):#Izveido funkciju, kur tiks saglabāts rezultāts un pārnests uz txt failu 
    try:
        with open('eksperimenta_dati.txt', 'a', encoding='UTF-8') as file:#failam jau jābūt izveidotam
            file.writelines(dati)
        print('Dati veiksmīgi saglabāti failā "eksperimenta_dati.txt"')
    except FileExistsError:
        print(f'Kļūda: data "eksperimenta_dati.txt" nav atrasta .')
    except Exception as e:
        print(f'Kļūda: neparedzēta kļūda-{e}')

izeja = ['exit', 'stop', 'iziet'] #izveido sarakstu, lai pārbaudītu visas izejas metodes reizē

def galvena():#pēdējā funkcijā ievieto visas pārējas funcijas, kā arī visus inputus, kur tiek pārbaudītas izejas metodes.
            
            nosaukums = input('Ievadiet nosaukumu eksperimentam: ')
            if nosaukums in izeja:
                exit('Uzredzēšanos')

            vards = input('Ievadiet savu vārdu: ')
            if vards in izeja:
                exit('Uzredzēšanos')
            
            vieta = input('Ievadiet eksperimenta veikšanas vietu: ')
            if vieta in izeja:
                exit('Uzredzēšanos')
            
            laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            dati = iegut_datus(nosaukums, vards, vieta, laiks)#iegut_datus tiek pārsaukts par mainīgo, lai to varētu ievietot citā funkcijā kā rezultātu.
            saglabat_datus(dati)

sveiciens()
while True:#while cikls strādā tik ilgi līdz tu uzraksti kādu no iziešanas vārdiem
    galvena()

    
