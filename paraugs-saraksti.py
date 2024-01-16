'''darzeni = ['zirņi','burkāni','kartupeļi','batātes','gurķi']
print('Orģinālais saraksts', darzeni)
darzeni.sort()
print('Sakārtot ar sort', darzeni)'''

'''viens = [5,4,6,1,8,2,7]
print(sorted(viens)) #atgriež jaunu sarakstu nemainot orģinālo.
print('Orģinālais',viens)'''

'''darzeni_kartots = sorted(darzeni,reverse=True)
print('apgriezts',darzeni_kartots)'''


saraksts = ['viens','divi','trīs','pieci','septiņi','deviņi']
saraksti_augosi = sorted(saraksts,key=len) #pēc garuma augoši
saraksti_dilstosi = sorted(saraksts,key=len,reverse=True)
print(saraksti_augosi)
print(saraksti_dilstosi)

strs = ['rīts', 'Vakars', 'pusdienas', 'KOMPLEKSIŅŠ','ZEMENES']
strs.sort() #nevar likt printā, tad neiet
print('Kārtots:', strs)
print('kārtot ar str.lower;',sorted(strs, key=str.lower))#ignorē uppercase
print('kārtot ar str.lower;',sorted(strs, key=str.upper))#ignorē lowercase
print('kārtot ar str.lower;',sorted(strs, key=str.lower,reverse=True))#ignorē upperrcase