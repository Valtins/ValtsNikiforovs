#tiek realizēta decimālskaitļu ievade
#aprēķināts izteiksmes (x+y)*(x-y)/x-y rezultāts



print('Ievadiet savu vārdu:')
vards = input()
print('Jūsu vārds ir:',vards)

print('Ievadiet decimālskaitli:')
x = float(input())#jāveic konvertēšana, jo input9 f- ja datus atgriež teksta veidā
print('Ievadītais skaitlis: ',x)
print('Ievadiet decimālskaitli:')
y = float(input()) #jāveic konvertēšana, jo input9 f- ja datus atgriež teksta veidā
print('Ievadītais skaitlis: ',y)

rezultāts = (x+y)*(x-y)//(y-x)
print('rezultāts:',rezultāts)

