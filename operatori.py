print('Ievadiet 3 skaitļus:')
x = int(input())
y = int(input())
z = int(input())

#loģiskais and
if x > 0 and y > 0 and z > 0:
    print('visi skaitļi lielāki par 0')
else:
    print('vismaz viens skaitlis nav lielāks/vienāds ar 0')
#loģiskais or
if x > 0 or y > 0 or z > 0:
    print('Viens skaitlis ir lielāks par 0')
else:
    print('Neviens skaitlis nav lielāks par 0')


i = 0
while i < 10:
    print('viss notiek')
    i+=1