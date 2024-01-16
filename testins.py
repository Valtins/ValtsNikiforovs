#izveido jaunu failu ar nosaukumu dati.txt(tajā pašā mapē
fails = open('ziema.txt','w',encoding='UTF-8')
#'w' arī izveido neeksistējošu failu no jauna 
#ieraksta failā datus
saraksts = ['Alūksne\n','Valmiera\n','Balvi\n']
fails.writelines(saraksts) #ieraksta vairākas rindiņas
fails.write('Es ar nepacietību gaidu pusdienas')
fails.close()

#pārrakstīt kopētā faila saturu
fails = open('ziema_copy.txt','w+',encoding='UTF-8')
fails.write('Varētu drīz iet pusdienās!')
#parāda uz ekrānu aila saturu
fails = open('ziema_copy.txt','w+',encoding='UFT-8')
print(fails.read())
fails.close()

fails = open('ziema_copy.txt','a+',encoding='UFT-8')
fails.write('\nCerams pusdienas šodien būs garšīgas')