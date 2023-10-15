from tkinter import* 
from tkinter.ttk import*

janela = Tk()
janela.title('CRIANDO UM RADIOBUTTON')
janela.geometry('300x300+200+200')
janela['bg'] = 'black'

rad_1 = Radiobutton(janela, text= 'Fabricio', value=1)
rad_2 = Radiobutton(janela, text= 'Jamile', value=2)
rad_3 = Radiobutton(janela, text= 'Micael',value=3)
rad_4 = Radiobutton(janela, text= 'Kalleo', value=4)

rad_1.grid(row=2,column=2,padx=10,pady=10)

rad_2.grid(row=2,column=3,padx=10,pady=10)

rad_3.grid(row=2,column=4,padx=10,pady=10)

rad_4.grid(row=2,column=5,padx=10,pady=10)


janela.mainloop()