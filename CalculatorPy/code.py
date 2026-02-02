from tkinter import *
from tkinter import ttk

#cores
cor1 = "#000000" # Preta
cor2 = "#ffffff" # Branca
cor3 = "#474747" # NardoGrey
cor4 = "#fc901c" # Laranja
cor5 = "#70706f" # Cinza
#Criando a Janela
janela =Tk()
janela.title("Calculadora")
janela.geometry("376x603")
janela.config(bg=cor1)

#Criando os Frames
frame_visor = Frame(janela, width=376, height=140, bg=cor1)
frame_visor.grid(row=0, column=0)

frame_corpo = Frame(janela, width=376, height=463, bg=cor1)
frame_corpo.grid(row=1, column=0)


# Variavel todos os valores adicionados
todos_valores =''

# Criando Label
valor_texto = StringVar()

# Criando Funções
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Passando Valor Para a Tela
    valor_texto.set(todos_valores)

# Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
#Função para limpar a tela

def limpa_tela():
    global todos_valores
    todos_valores =''
    valor_texto.set(todos_valores)


app_label = Label(frame_visor, textvariable=valor_texto, width=11, height=2, padx=15, pady= 20, relief=FLAT, anchor="e", justify="right", font=("Myriad Pro", 45), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)



#Criando alguns Botôes

b_1 = Button(frame_corpo, command=limpa_tela, text="C", width=16, height=3, bg=cor5, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores("%"), text="%", width=8, height=3, bg=cor5, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=185,y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores("/"), text="/", width=8, height=3, bg=cor4, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=278, y=0)

# Botôes Segunda Coluna

b_4 = Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=93)
b_5 = Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=92,y=93)
b_6 = Button(frame_corpo, command= lambda: entrar_valores("9"), text="9", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=185,y=93)
b_7 = Button(frame_corpo, command= lambda: entrar_valores("*"), text="*", width=8, height=3, bg=cor4, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=278,y=93)

# Botôes Terceira Coluna

b_8 = Button(frame_corpo, command= lambda: entrar_valores("4"), text="4", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=186)
b_9 = Button(frame_corpo, command= lambda: entrar_valores("5"), text="5", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=92,y=186)
b_10 = Button(frame_corpo, command= lambda: entrar_valores("6"), text="6", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=185,y=186)
b_11 = Button(frame_corpo, command= lambda: entrar_valores("-"), text="-", width=8, height=3, bg=cor4, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=278,y=186)

# Botões Quarta Coluna

b_12 = Button(frame_corpo, command= lambda: entrar_valores("1"), text="1", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=279)
b_13 = Button(frame_corpo, command= lambda: entrar_valores("2"), text="2", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=92,y=279)
b_14 = Button(frame_corpo, command= lambda: entrar_valores("3"), text="3", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=185,y=279)
b_15 = Button(frame_corpo, command= lambda: entrar_valores("+"), text="+", width=8, height=3, bg=cor4, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=278,y=279)

# Botões Última Coluna

b_16 = Button(frame_corpo, command= lambda: entrar_valores("0"), text="0", width=16, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0,y=372)
b_17 = Button(frame_corpo, command= lambda: entrar_valores("."), text=".", width=8, height=3, bg=cor3, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=185,y=372)
b_18 = Button(frame_corpo, command= calcular, text="=", width=8, height=3, bg=cor4, fg=cor2, font=("Myriad Pro", 15, "bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=278,y=372)



janela.mainloop()