from tkinter import *
from tkinter.ttk import *

janela=Tk()
janela.title('AULA DE CHECKBUTTON')
janela.geometry('300x300+200+200')
janela['bg'] = 'blue'

def Test_M():
    print('O estado atual do Button : ', Estado_M.get())

def Test_F():
    print('O estado atual do Button : ', Estado_F.get())

Estado_M = StringVar()
Estado_F = StringVar()

Estado_F.set('Ligado') # NESTE CASO JÁ VIRA MARCADO O CHECKBUTTON 

Titulo = Label(janela, text='SELECIONE SEU SEXO')
Caixa_Check = Checkbutton(janela, text= 'Masculino', var= Estado_M, command=Test_M, onvalue ='Ligado', offvalue = 'Desligado')
Caixa_Check2 = Checkbutton(janela, text='Feminino', var= Estado_F, command=Test_F,onvalue ='Ligado', offvalue = 'Desligado')

Titulo.grid(row= 3, column= 1)
Caixa_Check.grid(row= 5, column=0)
Caixa_Check2.grid(row= 5, column=2)

janela.mainloop()

# NESTA AULA APRENDEMOS A CRIAR O CHECKBUTTON, E PASSAR UM ESTADO PARA ELE
# CRIAMOS UM ESTADO E DEFINIMOS UMA FUNÇÃO, USAMOS O METODO GET()
# USAMOS O ONVALUE E OFFVALUE

# PODEMOS DEFINIR O ESTADO EM 3 OPÇÕES; STRINGVAR / BOOLEANVAR / INTVAR
# DEPENDENDO DA SUA ESCOLHA ELE RETORNA O UMA STRING, TRUE E FALSE, INTEIRO