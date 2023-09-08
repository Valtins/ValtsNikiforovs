
cilveki = int(input('Cik cilvēkiem ir plānots?'))#jānosklaidro cik cilvēki vēlās braukt.
if cilveki < 0:#cilvēku skaits nevar būt negatīvs.
    print('Ievadiet pareizus datus.')
    exit()
if cilveki > 4:#nav pietiekamas vietas taksometrā.
    print('mašīnā vietas nav')
    exit()
laiks = int(input('cikos jūs velaties braukt?'))#jāzina cikos jasavāc pasažieris.
if laiks > 24 or laiks < 0:#stundas navar būt citas kā no 1-24.
    print('Ievadiet pareizus datus.')
    exit()
elif laiks >= 6: 
    cena_diennaktij = 0.57#skatoties pēc laika būs zināms cik ir jāmaksā par diennakts laiku.
else:
    cena_diennaktij = 0.67
nobraukums = int(input('Cik garu ceļa posmu vēlaties nobraukt?(km):'))#lietotājs ievada cik lielu attālumu vēlas nobraukt.
if nobraukums < 0:#ceļa garums nevar būt negatīvs.
    print('Ievadiet pareizus datus.')
    exit()
elif nobraukums > 50:#papildnosacījums.
    print('šoferis nevar tevi tik tālu aizvest, jo mašīna nobruks.')
    exit()
cena_nobraukums = nobraukums * cena_diennaktij
stavvieta = input('Vai jūs vēlaties taksi izsaukt?(j/n):')#vai lietotājs vēlas izsaukt vai nolīgt taksometru.
if stavvieta == ('j'):
    noligsana = 2.20 + 1.25#ja vēlās izsaukt, tāpat ir jāmaksā par nolīgšanu.
else:
    noligsana = 1.25#ja neizvēlās izsaukšanu tad tikai nolīgšana
gaidisana = input('vai jums būs nepieciešama pietur vieta?(j/n):')#lietotājs ievada atbildi vai vēlās apstāties kādā pieturvietā.
if gaidisana == ('j'):
    m = int(input('cik minūtes ir nepieciešamas?:'))  
    pietura = 0.13 * m #par katru minūti ir norādīta cena gaidīšanai.
    if m < 0:#minūtes nevar būt negatīvas
        print('ievadiet pareizus datus.')
        exit() 
    elif m > 20:#papildnosacījums.
        print('šoferis negaidīs tevi 20 minutes, jo viņam garlaicīgi bez cilvēkiem.')    
        exit()
elif gaidisana == ('n'):#ja cilvēks izvēlās neapstāties tad gaidīšanas cena ir 0.
    pietura = 0
z = round(noligsana, 2)#visu cenu noapaļošana
x = round(cena_nobraukums, 2)
kopsumma = cena_diennaktij + x + noligsana + pietura#izveidota kopsumma lai redzētu cik kopā ir jāmaksā.
y = round(kopsumma, 2)
print('diennakts laiks-',cena_diennaktij,'$')
print('nobraukuma cena-',x,'$')
print('gaidisanas cena-',pietura,'$')
print('noligsanas cena-',z,'$')
print('kopsumma-',y,'$')#beigās ir redzama kopējā cena par katru nosacījumu,3 ko lietotājs ir ievadījis un kopsumma uz čeka.
