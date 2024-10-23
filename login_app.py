import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Verifique aqui as credenciais (exemplo simples)
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login bem-sucedido", "Você está logado!")
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Login")

# Criar os rótulos e campos de entrada
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack(pady=5)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack(pady=5)

# Criar o botão de login
botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)

# Iniciar o loop da interface gráfica
janela.mainloop()

