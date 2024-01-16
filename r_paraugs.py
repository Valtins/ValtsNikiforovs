f = open('demo.txt','r',encoding='utf-8')#Atvērt failu
print(f.read()) #izdrukāt faila saturu

f = open('demo.txt','r',encoding='utf-8')#Atvērt failu
print(f.readline()) #nolasa pirmo rindiņu

f = open('demo.txt','r',encoding='utf-8')
print(f.read(10)) #atgriež 10 simbolus, ieskaitot tukšumzīmes

f.close() #failu vairs nevajag

