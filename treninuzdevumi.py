telefoni = {
    'zimols': 'Apple',
    'modelis': '14',
    'gads': 2021
}
telefoni.update({'gads':'2022'})
print(telefoni)


skolas = {
    'nosaukums': 'Gimnazija',
    'novads': 'Sigulda',
    'skolenu_skaits': 569,
    'gads': 2019
}
print(skolas)
skolas.clear()
print('Pēc dzēšanas:',skolas)


augli = {1:'banani',2:'aboli',3:'bumbieri',4:'mango'}
print(augli)
augli.pop(2)
augli.pop(4)
print(augli)


skaitli = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
if 200 in skaitli.values():
    print('Skaitlis 200 ir vardnīcā!')