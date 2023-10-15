# PROPRIEDADE EXPAND ELE FAZ TODOS COMPONENTES DEFINE EM ÁREA IGUAIS 
# VC PODE COLOCAR NUMERO OU TRUE = EM EXPAND  
# BOTH SIGNIFICA EM TODOS OS LADOS 

from tkinter import *

janela= Tk()
janela.title('AULA DE EXPAND COM PACK USANDO BOTH')
janela.geometry('500x500+200+200')


Cont_01= Label(janela, text='FABRICIO',bg='red',fg='white')
Cont_02= Label(janela, text='JAMILE', bg= 'yellow',fg='black')
Cont_03= Label(janela, text='MICAEL', bg= 'orange',fg='black')
Cont_04= Label(janela, text='KALLEO', bg='blue', fg='white')


Cont_01.pack(side=TOP,fill=BOTH,expand=True)
Cont_02.pack(side=TOP,fill=BOTH,expand=True)
Cont_03.pack(side=TOP,fill=BOTH,expand=True)
Cont_04.pack(side=TOP,fill=BOTH,expand=True)



janela.mainloop()