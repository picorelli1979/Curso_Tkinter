from tkinter import*

janela=Tk()
janela.title('CRIANDO JANELA FRAME (RETANGULAR)')
janela.geometry('600x600')


Area_1 = Frame(janela,width=300,height=200,bg='red')
Area_2 = Frame(janela,width=300,height=200,bg='blue')
Area_3 = Frame(janela,width=600,height=200,bg='black')

Area_1.grid(row=0,column=0)
Area_2.grid(row=0,column=1)
Area_3.grid(row=1,column=0, columnspan=2)

texto = Label(Area_1, width=20 ,text='FABRICIO PAIM', fg='black')
texto.grid(row= 2, column= 1)

bt = Button(Area_2, width= 30, height= 20, text='PLAY', bg='black', fg='white')
bt.grid(row= 2, column=2)

janela.mainloop()