print('---------------Nepieciešams ievadīt datus programma, kas aprēķina izmaksas apdrukātiem krekliem---------------')
def pasuti_tkreklus(skaits, apdruka, piegade):#Izveidota funkcija, kur ir 3 parametri.
  skaits = int(input('Cik kreklus jūs vēlētos apdrukāt?:'))

  apdruka = input('Kādas apdrukas jūs vēlieties saviem krekliem(TEKSTS,ZIME,FOTO):')#Lietotājam jāievada atbilde ar lielajiem burtiem.

  apdrukas_cena = 0#Katram apdrukas veidam ir dota cena, atkarībā ko lietotājs ievadīs.

  if apdruka == 'TEKSTS':#cena tiek izveidota katrai apdrukai pēc 
    apdrukas_cena = 5
    print('Teksts maksā 5 EUR')
  elif apdruka == 'ZIME':
    apdrukas_cena = 7
    print('Zīme maksā 7 EUR')
  elif apdruka == 'FOTO':
    apdrukas_cena = 20
    print('Foto maksā 20 EUR')
  else:
    print('Jūs esiet nepareizi ievadījis datus.')
    exit() 

  kopeja_cena = skaits * apdrukas_cena#aprēķina cenu kreklus apdruku skaitam.
  print('--------------------ČEKS--------------------')
  if kopeja_cena < 50:
    maksa_piegadei = 15
    piegade == True
    print('---Par piegādi būs japiemaksā 15 EUR, jo kopējā summa pa apdruku nepārsniedz 50 EUR---')
    print('---Jūsu pasūtijums ar visu piegādi maksā ', kopeja_cena + 15, ' EUR---')
  else:
    piegade == False#Piegāde būs nulle, ja kopēja cena ir lielāka par 50 eiro. 
    maksa_piegadei = 0
    print('---Par piegādi jums nebūs jāmaksā, jo pasūtījums pārsniedz 50 EUR---')
    print('---Jūsu pasūtijums maksā kopā ar visu piegādi ', kopeja_cena, ' EUR---')
  if kopeja_cena > 100:
    atlaide = 0.05 * kopeja_cena#Izveidota 5% atlaide
    kopeja_cena = kopeja_cena - atlaide
    print('---Jums ir piešķirta 5% atlaide, jo jūsu kopēja summa pārsniedz 100 EUR---')
    print('---Jūsu pasūtījums maksās ar atlaidi ', round(kopeja_cena), ' EUR---')

  return kopeja_cena + maksa_piegadei#Tiek aprēķināta kopēja maksa par piegādi un par kreklu apdruku.

ceks = (pasuti_tkreklus(10, 'TEKSTS', True))#Parametros tiek ievietoti 3 veidu dati, kas attiecas uz katru parametru.
ceks2 = (pasuti_tkreklus(5, 'ZIME', False))

print('{}'.format(ceks))#Uz ekrānu parādas kopēja cena par krekliem un piegādi, kas tika apkopoti funkcijā.
print('{}'.format(ceks2))