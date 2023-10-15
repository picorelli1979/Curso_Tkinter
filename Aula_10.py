#  STICK  ESSA PROPRIEDADE COLOCA O ELEMENTO NO LOCAL DETERMINADO

from tkinter import * 

janela = Tk()
janela.title('CRIANDO JANELA DE LOGIN E SENHA')
janela.geometry('500x300+200+200')

titulo = Label (janela, text= 'DIGITE SUA SENHA', bg='black', fg='white')
titulo.grid(padx = 20, pady=20)

Lb1 = Label(janela, text='Login:   ',padx=20, pady= 10)
Lb1.grid(row= 20, column= 0 )

Lb2 = Label(janela, text='Senha:   ',padx=20, pady= 10)
Lb2.grid(row=25, column=0)

Ed1 = Entry(janela, text='')
Ed1.grid(row= 20 , column= 2)

Ed2 = Entry(janela, text='')
Ed2.grid(row= 25 , column= 2 )

def Pegar_texto():
    Lb3['text'] = Ed2.get() 
    
bt = Button(janela, text='Carregar', command=Pegar_texto)
bt.grid(row= 100 , column= 2)

Lb3 = Label(janela, text='', background='black', width= 20, height= 5, fg= 'white')
Lb3.grid(row=35 , column= 2, padx= 20, pady=10)

janela.mainloop()