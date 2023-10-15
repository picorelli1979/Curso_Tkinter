from tkinter import *

janela=Tk()
janela.title('CRIANDO UMA LISTBOX')
janela.geometry('500x400+200+200')

def Test():
    Caixa_Saida_Texto = Label(janela, text=list_box.get(ACTIVE), width=30)
    Caixa_Saida_Texto.grid(row= 2, column= 3)

def Apagar():
      list_box.delete(ACTIVE)  

list_box = Listbox(janela, bg= 'red',fg='white',width= 50, height= 10)
list_box.grid(row= 3, column= 3, padx=10)

list_box.insert(0, '1. REACT')
list_box.insert(1, '2. JAVA SCRIPT')
list_box.insert(2, '3. C++')
list_box.insert(3, '4. JAVA')
list_box.insert(4, '5. PYTHON')
list_box.insert(5, '6. RUBY ON REILS')

list_box.insert(END,'7. GOLANG') # QUANDO COLOCAMOS O END NO INDEX O ELEMENTO VAI PRA O FINAL

# PARA CRIAÇÃO DE UMA LISTA NO lISTBOX, TEMOS QUE FAZER UM FOR :
# CRIAMOS A LISTA DE ITENS E FAZEMOS UM FOR POSTERIOMENTE 

item = ['Fabricio', 'Jamile', 'Micael', 'Kalleo']

for x in item:
    list_box.insert(END,x)
    
bt = Button(janela, text='CARREGAR', bg='black', fg='white', command=Test)   
bt.grid(row= 10, column= 4, pady=10) 

bt_Del = Button(janela, text='DELETAR', bg='green', fg='white', command=Apagar)   
bt_Del.grid(row= 7, column= 4, pady=10) 

#AQUI USAMOS O METODO GET() E O METODO DEL()
# O METODO GET PEGA O ELEMENTO, O METODO DEL APAGA O ELEMENTO

janela.mainloop()