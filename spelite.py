import random
gajieni = ['akmens','papīrs','šķēres']

cilveka_gajiens = input('Ievadi savu gājienu: ')
datora_gajiens = random.choice(gajieni)
 
print(f'Cilvēks: {cilveka_gajiens} VS {datora_gajiens}')
if cilveka_gajiens == datora_gajiens:
    print('neizšķirts!')

elif cilveka_gajiens == 'akmens' and datora_gajiens == 'šķēres' :
    print('Cilvēks uzvarēja!')

elif cilveka_gajiens == 'papīrs' and datora_gajiens == 'akmens' :
    print('Cilvēks uzvarēja!')

elif cilveka_gajiens == 'šķēres' and datora_gajiens == 'papīrs' :
    print('Cilvēks uzvarēja!')

else:
    print('L, tu zaudēji!')