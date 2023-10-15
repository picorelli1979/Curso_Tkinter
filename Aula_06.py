from tkinter import *


janela = Tk()
janela.title('AULA DE PACK COM SIDE')
janela.geometry('500x500+200+200')
janela['bg'] = 'blue'


Container_01 = Label(janela, text='TOP', width=50)
Container_02 = Label(janela, text='LEFT')
Container_03 = Label(janela, text='RIGHT')
Container_04 = Label(janela, text='BOTTOM', width=50)

Container_01.pack(side=TOP)
Container_02.pack(side=LEFT)
Container_03.pack(side=RIGHT)
Container_04.pack(side=BOTTOM)


janela.mainloop()

# NESTA AULA APRENDEMOS A COLOCAR COM A PROPRIEDADE SIDE
# A VINCULAR A EXTREMIDADE A UM COMPONENTE 
