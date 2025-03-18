from tkinter import *

tela = Tk()
tela.geometry("400x350")
tela.configure(background="#EDE8D0")
tela.resizable(True, True)
tela.maxsize(width=700, height=400)
tela.minsize(width=300, height=200)

# Título
lbl_titulo = Label(tela, text="Soma dos Numeros", fg="#722F37", bg="#EDE8D0")
lbl_titulo.pack()

lbl_num = Label(tela, text="Numero:", fg="#722F37", bg="#EDE8D0")
lbl_num.place(x=10, y=50)
txt_num = Entry(tela, fg="#722F37", bg="white")
txt_num.place(x=90, y=50)
txt_num.insert(0, "Digite o numero: ")

lbl_num2 = Label(tela, text="Numero 2:", fg="#722F37", bg="#EDE8D0")
lbl_num2.place(x=10, y=80)
txt_num2 = Entry(tela, fg="#722F37", bg="white")
txt_num2.place(x=90, y=80)
txt_num2.insert(0, "Digite o numero: ")

def somar():
    n1 = int(txt_num.get())
    n2 = int(txt_num2.get())
    lbl_resultado["text"] = n1 + n2

btn_botao = Button(tela, text="Somar", command=somar)
btn_botao.place(x=10, y=310)

lbl_resultado = Label(tela, text="Resultado: ", fg="#722F37", bg="#EDE8D0")
lbl_resultado.place(x=10, y=130)
lbl_resultado = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_resultado.place(x=10, y=150)

tela.mainloop()