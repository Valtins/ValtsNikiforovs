import math
import random
print("     Matemātisko funkciju lietošana", "\n------------------------------------------")
a = int(input("Ievadiet veselu skaitli a:\n"))
b = float(input("Ievadiet realu skaitli b:\n"))
print("Skaitla", a, "absoluta vertiba ir ", float(abs(a)))
print("Skaitla", b, "noapalota vertiba ir", float(round(b)))
print("Skaitlis", a, "pakape 2 ir", float(a**2))
print("Skaitla", b, "kvadratsakne ir", float(math.sqrt(b)))
print("Pirmais gadījuma skaitlis ir", random.random())
print("Otrais gadijuma skaitlis ir", '%.6f'%(random.random()))
print("Gadījuma skaitlis intevālā no 10 līdz 11 ir", '%.3f'%(random.random() + 10))
print("PI vērtība ir:", math.pi)
print("PI vērtība ir:", '%.2f'%(math.pi))