atbilde = input('Vai tu šodien brauc uz Rīgu?(j/n)')
if atbilde == 'j' :#salīdzināšana veicama ar 2 vienādības zīmēm
    print('Forši!')

tests = input('Vai šodien ir Jaunais gads?(j/n)')
if tests == 'j' :
    print('Laiks salūtam!')
else: #pie else nosacījums nebūs(tas ir tas, kas paliek pāri)
    print('bēdīgi..') #šis tiek palaists tikai tad, 
    #ja lietotājs neieraksta 'j'