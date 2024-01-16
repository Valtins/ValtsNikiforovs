print("Āritmētiskās progresijas elementu aprekins")
a = float(input("Ievadiet pirmo locekli!\n"))
b = float(input("Ievadiet otro locekli!\n"))
c = float(input("Ievadiet trešo locekli!\n"))
print("1. loceklis:", a)
for i in range(1, int(c)):
    a = a + b
    print(i + 1, ". loceklis:", a)
    i = i+1