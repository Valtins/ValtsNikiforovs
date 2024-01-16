import math
print('Faktoriāla aprēķināšana')
print('*******************************************************')
atstarpes2 = print(' /n',' /n') 
def atstarpe(atstarpes2):#izveidota funkcija ar 2 atstrpem
    (print(atstarpes2))
while 'j': #kamēr atbilde ir 'jā' process atkartojas 
    skaitlis = int(input('ievadi veselu pozitīvu skaitli(mazāku par 13):\n ')) 
    def faktorials(skaitlis):
        (math.factorial(skaitlis))#funkcija kur skaitlis tiek aprekinats faktorials no dotā inputa
    if skaitlis >= 13:
        print('Ievadītais skaitlis ir pārāk liels!')
        exit()
    elif skaitlis < 0:
        print('skaitlim jābūt pozitīvam!') 
        exit()   
    print("Faktoriāls:", end="")
    print(math.factorial(skaitlis))#izprinte faktorialo skaitli skaitli
    atbilde = input('Vai vēlaties turpināt darbu(j-jā, citi taustiņi-nē)?\n')
    print(atstarpe)
else: 
    print(atstarpe)
    print('Paldies!')
    exit()    
        