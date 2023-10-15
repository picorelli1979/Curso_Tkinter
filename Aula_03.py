from tkinter import * 

def bt_click():
    Caixa_Texto['text'] = 'SEJA BEM VINDO !!!!! USUARIO ...'
    
janela = Tk()
janela.title('AULA DE BOTÃO-FUNCIONANDO')
janela.geometry('500x500+200+200')
janela['bg'] = 'blue'

Caixa_Texto = Label(janela, text= 'Loading.....') 
Caixa_Texto.place(x = 100 , y = 200, width=300, height= 70)

bt = Button(janela,text= 'CARREGAR', command= bt_click)
bt.place(x = 50, y = 20, width= 100, height=30 )


janela.mainloop()


