from random import *
from tkinter import *
logs = Tk()


izmers = 900
audekls = Canvas(logs, width=izmers,height=izmers)
audekls.pack()


while True:
    krasa = choice(['violet','blue','cyan','purple','pink'])
    x0 = randint(0, izmers)
    y0 = randint(0, izmers)
    d = randint(0, izmers/5)
    #audekls.create_rectangle(x0,y0, x0+d, y0+d, fill=krasa)
    audekls.create_line(x0,y0, x0+d, y0+d, fill=krasa)
    logs.update()
mainloop()
