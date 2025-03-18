from tkinter import *

# Criar janela
tela = Tk()
tela.geometry("400x350")
tela.configure(background="#EDE8D0")
tela.resizable(True, True)
tela.maxsize(width=700, height=400)
tela.minsize(width=300, height=200)

# Título
lbl_titulo = Label(tela, text="Cadastro de Clientes", fg="#722F37", bg="#EDE8D0")
lbl_titulo.pack()

# Nome
lbl_nome = Label(tela, text="Nome:", fg="#722F37", bg="#EDE8D0")
lbl_nome.place(x=10, y=50)
txt_nome = Entry(tela, fg="#722F37", bg="white")
txt_nome.place(x=90, y=50)
txt_nome.insert(0, "Digite seu nome")

# Email
lbl_email = Label(tela, text="Email:", fg="#722F37", bg="#EDE8D0")
lbl_email.place(x=10, y=80)
txt_email = Entry(tela, fg="#722F37", bg="white")
txt_email.place(x=90, y=80)
txt_email.insert(0, "Digite seu email")

# Telefone
lbl_telefone = Label(tela, text="Telefone:", fg="#722F37", bg="#EDE8D0")
lbl_telefone.place(x=10, y=110)
txt_telefone = Entry(tela, fg="#722F37", bg="white")
txt_telefone.place(x=90, y=110)
txt_telefone.insert(0, "Digite seu telefone")

# Endereço
lbl_endereco = Label(tela, text="Endereço:", fg="#722F37", bg="#EDE8D0")
lbl_endereco.place(x=10, y=140)
txt_endereco = Entry(tela, fg="#722F37", bg="white")
txt_endereco.place(x=90, y=140)
txt_endereco.insert(0, "Digite seu endereço")

# Labels para exibir os dados (serão atualizados)
lbl_tituloCliente = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_tituloCliente.place(x=10, y=180)

lbl_nomeCliente = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_nomeCliente.place(x=10, y=210)

lbl_emailCliente = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_emailCliente.place(x=10, y=230)

lbl_telefoneCliente = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_telefoneCliente.place(x=10, y=250)

lbl_enderecoCliente = Label(tela, text="", fg="#722F37", bg="#EDE8D0")
lbl_enderecoCliente.place(x=10, y=270)


# Função para mostrar dados
def mostrarDados():
    lbl_tituloCliente.config(text="Dados do Cliente")
    lbl_nomeCliente.config(text="Nome: " + txt_nome.get())
    lbl_emailCliente.config(text="Email: " + txt_email.get())
    lbl_telefoneCliente.config(text="Telefone: " + txt_telefone.get())
    lbl_enderecoCliente.config(text="Endereço: " + txt_endereco.get())


# Botão para exibir dados
btn_botao = Button(tela, text="Cadastrar", command=mostrarDados)
btn_botao.place(x=10, y=310)

# Iniciar o loop principal da interface
tela.mainloop()
   