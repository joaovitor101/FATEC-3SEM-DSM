from tkinter import *

tela = Tk()
tela.geometry("400x320")
txt_nome = Entry(tela, fg="#EFFBB0", bg="#722F37", width=400)
txt_nome.pack()
txt_nome.insert(0, "Digite seu nome: ")

def clicar():
    lbl_nome = Label(tela, text="Bem Vindo " + txt_nome.get())
    lbl_nome.pack()


btn_botao = Button(tela, text="clicar", command=clicar)
btn_botao.pack()
tela.mainloop()