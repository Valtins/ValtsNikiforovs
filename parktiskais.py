sk = 7
for x in range(1,13):
    print('Cik ir ', x, 'x',sk,'?')
    atbilde = (input())

    if atbilde == 'stop':
        break
    if atbilde == 'izlaist':
        print('Tiek izlaists')
        continue
    atb = x * sk #glabā pareizās atbildes
    if int(atbilde) == atb:
        print('pareizi')   
    else:
        print('Nē, tas ir',atb)    
    

