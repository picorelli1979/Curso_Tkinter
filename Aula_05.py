from tkinter import *

def Carregar():
    Texto_Fixo['text'] = Caixa_Texto.get()

janela = Tk()
janela.title('AULA DE EXTRAIR UMA WIDGET')
janela.geometry('500x500+200+200')
janela['bg'] = 'red'

Caixa_Texto = Entry(janela)
Caixa_Texto.place(x=100,y=100, width=300, height=30) 

bt = Button(janela, text= 'PLAY', border= 5, command= Carregar)
bt.place(x= 180, y= 200, width= 100, height=25)

Texto_Fixo = Label(janela, text='Sistema Loading....', bg ='black', fg='white')
Texto_Fixo.place(x= 180, y= 400)

janela.mainloop()