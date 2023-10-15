from tkinter import *

def Turn_ON():
    Caixa['bg'] = 'yellow'
    
def Turn_OFF():
    Caixa['bg'] = 'white'

janela = Tk()
janela.title('FUNÇÃO DE LIGAR E DESLIGAR')
janela.geometry('500x500+300+300')
janela['bg'] = 'black'

Titulo = Label(janela, text='AUTOMAÇÃO DE AMBIENTE',border=5, bg= 'red', fg= 'white')
Titulo.place(x= 150, y= 30, width= 200, height=30)

Caixa = Label(janela, text='')
Caixa.place(x= 165, y= 100, width= 150, height=150)

bt_1 = Button(janela, text='LIGAR', border= 5, command=Turn_ON)
bt_1.place(x = 100, y = 300, width=80, height=30)

bt_2 = Button(janela, text='DESLIGAR', border= 5, command=Turn_OFF)
bt_2.place(x = 300, y = 300, width=80, height=30)



janela.mainloop()