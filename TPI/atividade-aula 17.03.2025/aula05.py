from tkinter import *

tela = Tk()
tela.title("Fatec de Registro")
tela.geometry("400x320")
tela.configure(bg="#EDE8D0")
tela.resizable(True, True)
tela.maxsize(width=700, height=400)
tela.minsize(width=300, height=200)


largura_tela = tela.winfo_screenwidth()
altura_tela = tela.winfo_screenheight()

largura_janela = 400
altura_janela = 320

pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

tela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


lbl_nome = Label(tela, font="Poppins 15" ,text="Nome: ").place(x=10, y=10)
lbl_telefone = Label(tela,font="Poppins 15" ,text="Telefone: ").place(x=10, y=60)
lbl_endereco = Label(tela,font="Poppins 15", text="Endereço: ").place(x=10, y=110)
lbl_cpf = Label(tela, font= "Poppins 15",text="CPF: ").place(x=10, y=160)

btn_botao = Button(tela, text="clicar")
btn_botao.pack()

tela.mainloop()
