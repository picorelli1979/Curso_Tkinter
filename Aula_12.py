from tkinter import * # A BIBLIOTECA GERAL
from tkinter.ttk import* # A BIBLIOTECA E AS SUBPASTAS

janela = Tk()
janela.title('CAIXA COMOBOX')
janela.geometry('300x300+200+200')
janela['bg'] = 'red'

Caixa_Combo = Combobox(janela) # Cria a caixa e combobox
Caixa_Combo['values'] = ('Fabricio','Jamile','Micael','Kalleo') # cria os itens da caixa
Caixa_Combo.current(0)# Aqui vc indica quem fica no inicio da caixa em destaque
Caixa_Combo.pack(side = TOP) # Cria seu display PACK/GRID/PLACE

janela.mainloop()