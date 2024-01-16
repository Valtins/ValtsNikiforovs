#Izveidot txt failu dati2.txt
fails = open('dati2.txt','w',encoding='utf-8') #izveidos failu ar nosaukumu dati2.txt

#ierakstīt failā sarakstu ar 3 pilsētām
saraksts = ['Liepāja\n','Sigulda\n','Daugavpils\n']
fails.writelines(saraksts) #Ieraksta vairaākas rindiņas
fails.write('\Hello, world!\n') #ieraksta vienu virkni

#pārrakstīt faila saturu uz 3 valstīm
valstis = {
    'Somija\n' : 'Fazer',
    'Latvija\n' : 'Laima',
    'Lietuva\n' : 'Rūta'
}
fails = open('dati3.txt','w',encoding='utf-8') #izveidos failu
fails.write(str(valstis))