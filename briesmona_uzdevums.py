atbilde = 'j' #piešķir vērtību j
while atbilde == 'j':
    print('nekusties!')
    atbilde = (input('Vai briesmonis ir draudzīgs?(j/n):'))
print('bēdz prom!')

skaitlis = int(input('Ievadi skaitli!'))
while skaitlis < 5:
    print(skaitlis, ':ir mazāks par 5')
    skaitlis = skaitlis + 1
print(skaitlis, ':nav mazāks par 5')

while True:
    atbilde = input('Ieraksti vārdu un piespied enter')
    print('Lūdzu, vairs neraksti " '+atbilde+'"')