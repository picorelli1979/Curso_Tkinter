#  O  GRID FAZ O LAYOUT DE LINHAS E COLUNAS 

from tkinter import * 

janela=Tk()
janela.title('AULA DE GRID / COLUNAS E TABELAS')
janela.geometry('500x500+200+200')
janela['bg'] = 'red'

Celula_1 = Label(janela, text= 'NOME')
Celula_2 = Label(janela, text='TELEFONE')
Celula_3 = Label(janela, text='EMAIL')

Celula_1.grid(row=1, column=1, padx=10, pady=10)
Celula_2.grid(row=1, column=2, padx=10, pady=10)
Celula_3.grid(row=1, column=3, padx=10, pady=10)


janela.mainloop()