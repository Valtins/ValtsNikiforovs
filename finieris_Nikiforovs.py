plāksnes_garums = 250.0 #platums un garums ņemts no mājaslapas
plāksnes_platums = 125.0 
plāksnes_augstums = 1.5 #jau tiek izvēlēts viens biezums 1.5 cm
plāksnes_cena = 60.40
listes_cena = 6.56 * 12 # nepieciešamas 12 listes
stūra_savienojumi = 0.80 * 8 #nepieciešami 8 stūra savienojumi 
augstums = 9 #podesta augstums jau ir dots 9 cm 
skaits = int(input('Cik podesti tiek pasūtīti?: ')) #skaits nosaka cik daudz tāda paša daudzuma materiali būs vajadzīgi
podestu_platumi = float(input('Kāds ir doto podestu platums?: '))
podestu_garumi = float(input('Kāds ir doto podestu garums?: ')) 
print('Podesta augstums ir', augstums,'cm')
print('Tiek pasūtīti ', skaits,'podestu.')
print('Doto podestu platumi ir doti ',podestu_platumi,'cm')
print('Doto podestu garumi ir doti ',podestu_garumi,'cm')
print()
plaksnu_daudzums = (podestu_platumi * podestu_garumi) / (250.0 * 125.0) #jāaprēķina cik daudz plākšņu ir nepieciešams vienam podestam
kopā = (6 + plaksnu_daudzums) * skaits
print('Jums kopā būs nepieciešami', 8 * skaits,'stūra svieojumi' )
print('Jums kopā būs nepieciešamas', 12 * skaits,'listes' )
print('Jums kopā būs nepieciešams', kopā,'saplākšņu')
print()
print('Kopējās izmaksas ir:', (listes_cena + stūra_savienojumi + (plāksnes_cena * kopā)) * skaits)
