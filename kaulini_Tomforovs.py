spel_1 = str(input("Metamā kauliņa mešanas sacencības \nIevadiet pirmā spēlētāja vārdu:"))
spel_2 = str(input("Ievadiet otrā spēlētāja vādru:"))
metieni = int(input("Ievadiet metienu skaitu:"))
gal_rez_1 = 0
gal_rez_2 = 0
for i in range(1, metieni+1):
    x = str("Ievadiet spēlētāja " + spel_1 + " " + str(i) + ". metiena rezultātu:")
    rez_1 = int(input(x))
    y = str("Ievadiet spēlētāja " + spel_2 + " " + str(i) + ". metiena rezultātu:")
    rez_2 = int(input(y))
    if rez_1 > 6 or rez_1 <1 or rez_2 >6 or rez_2<0:
        print("nav pareizi")
        exit()
    else:
        gal_rez_1 = gal_rez_1 + rez_1
        gal_rez_2 = gal_rez_2 + rez_2
print("Spētājs", spel_1, "punktu summa:", gal_rez_1)
print("Spētājs", spel_2, "punktu summa:", gal_rez_2)
if gal_rez_2 == gal_rez_1:
    print("Neizšķirts!")
elif gal_rez_2 > gal_rez_1:
    print("Uzvarēja ", spel_2)
else:
    print("Uzvarēja ", spel_1)