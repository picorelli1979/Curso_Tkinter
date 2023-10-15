# A PROPRIEDADE FILL TEM COMO FUNÇÃO PREENCHER TODO ESPAÇO DETERMINADO
# ELE PODE PREENCHER NO EIXO 'X' E NO EIXO 'Y'

from tkinter import *

janela = Tk()
janela.title('AULA DE FILL COM PACK')
janela.geometry('500x500+200+200')
janela['bg']='yellow'

Cont_1 = Label(janela, text= 'TOP', bg='red', fg= 'white', border=5)
Cont_2 = Label(janela, text= 'LEFT', bg='red', fg= 'white', border=5)
Cont_3 = Label(janela, text= 'RIGHT', bg='red', fg= 'white', border=5)
Cont_4 = Label(janela, text= 'BOTTOM', bg='red', fg= 'white', border=5)

Cont_1.pack(side=TOP, fill= X)
Cont_2.pack(side=LEFT, fill= Y)
Cont_3.pack(side=RIGHT, fill=Y)
Cont_4.pack(side=BOTTOM, fill=X)


janela.mainloop()