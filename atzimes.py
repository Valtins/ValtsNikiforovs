#izveidot sarakstu 'atzīmes' ar punktiem(testā iegūtajiem)(10 rezultāti no 60 - 99)
#ar for ciklu 'iziet cauri' visam sarakstam
#ar elif nosacījuiem uz ekrāna parādīt punktus un atzīmi
# >=90 - A, >=80 - B, starp 70 un 80 - c, no 60 līdz 70 - D, ja krīt zem 60 - F
#grūtāk - var pielikt datu ievadi, atkarībā no ievadītā skaitļa, parādīt burtu. 
punkti = int(input('Ievieto punktus:'))
kopejais = []
if punkti >=90:
    atzime = 'A'
elif punkti >=80:
    atzime = 'B'
elif punkti >=70:
    atzime = 'C'
elif punkti >=60:
    atzime = 'D'
else:
    atzime = 'F'
kopejais.append([punkti, atzime])
print(kopejais)


