import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import sys
sys.path.append('AlgoritimoFinal/')
#sys.path.append("/home/night/Documents/UNIP/APS-UNIP-2sem/AlgoritimoFinal/")
from SES import SES

# Configuração do servidor
HOST = '3.147.81.47'
PORT = 80

s = SES()

class ClienteChat:
    def __init__(self, root):
        self.root = root
        self.root.title("Mensageiro SES")
        self.root.geometry("500x540")
        self.root.config(bg="#96d5ff")

        self.fonte = ("Arial", 22)
        self.fonteLabel = ("Arial", 22, "bold")
        self.fonteBotao = ("Arial", 20, "bold")

        self.corFundo = "#96d5ff"
        self.inputFundo = "#ffffff"
        self.corTexto = "#333333"
        self.botaoFundo = "#4CAF50"
        self.botaoTexto = "#ffffff"

        # Campos de Nome e Senha
        self.labelNome = tk.Label(
            self.root, text="Nome:", font=self.fonteLabel, bg=self.corFundo, fg=self.corTexto)
        self.labelNome.pack(padx=10, pady=(10, 0), anchor='w')
        self.entradaNome = tk.Entry(self.root, font=self.fonte, bg=self.inputFundo, fg=self.corTexto)
        self.entradaNome.pack(padx=10, pady=(0, 10), fill=tk.X)

        self.labelSenha = tk.Label(
            self.root, text="Senha:", font=self.fonteLabel, bg=self.corFundo, fg=self.corTexto)
        self.labelSenha.pack(padx=10, pady=(10, 0), anchor='w')
        self.entradaSenha = tk.Entry(self.root, font=self.fonte, bg=self.inputFundo, fg=self.corTexto, show="*")
        self.entradaSenha.pack(padx=10, pady=(0, 10), fill=tk.X)

        # Área de chat (ocupa a maior parte do espaço)
        self.areaChat = scrolledtext.ScrolledText(
            self.root, state='disabled', wrap='word', font=self.fonte, bg="#f4f4f4", fg=self.corTexto, height=8)
        self.areaChat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Frame para entrada de mensagem e botão Enviar (sempre visível)
        self.frameInferior = tk.Frame(self.root, bg=self.corFundo)
        self.frameInferior.pack(padx=10, pady=10, fill=tk.X)

        # Entrada para enviar mensagens
        self.entradaMensagem = tk.Entry(self.frameInferior, font=self.fonte, bg=self.inputFundo, fg=self.corTexto)
        self.entradaMensagem.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        self.entradaMensagem.bind("<Return>", self.enviarMensagem)

        # Botão Enviar no canto inferior direito
        self.botaoEnviar = tk.Button(self.frameInferior, text="Enviar", font=self.fonteBotao, bg=self.botaoFundo, fg=self.botaoTexto, command=self.enviarMensagem)
        self.botaoEnviar.pack(side=tk.RIGHT)

        # Conectar ao servidor
        self.socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socketCliente.connect((HOST, PORT))
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            self.root.quit()  # Sai do aplicativo se a conexão falhar

        # Iniciar escuta de mensagens recebidas
        threading.Thread(target=self.receberMensagens, daemon=True).start()

    def enviarMensagem(self, evento=None):
        mensagem = self.entradaMensagem.get().strip()
        nome = self.entradaNome.get().strip()
        senha = self.entradaSenha.get().strip()

        if mensagem and nome:  # Verifica se a mensagem e o nome não estão vazios
            mensagemComNome = f"{nome}: {mensagem}"
            mensagemComNome = s.criptografar(mensagemComNome, senha)
            try:
                self.socketCliente.sendall(mensagemComNome.encode('utf-8'))
            except (socket.error, BrokenPipeError) as e:
                print(f"Erro ao enviar mensagem: {e}")
                self.socketCliente.close()
                self.root.quit()  # Opcionalmente, sair do aplicativo
            self.entradaMensagem.delete(0, tk.END)

    def receberMensagens(self):
        while True:
            try:
                mensagem = self.socketCliente.recv(1024).decode('utf-8')
                if mensagem:
                    senha = self.entradaSenha.get().strip()
                    mensagem = s.descriptografar(mensagem, senha)
                    self.exibirMensagem(mensagem)
            except (socket.error, BrokenPipeError):
                print("Conexão perdida. Saindo...")
                self.socketCliente.close()
                self.root.quit()  # Opcionalmente, sair do aplicativo
                break

    def exibirMensagem(self, mensagem):
        self.areaChat.config(state='normal')
        self.areaChat.insert(tk.END, mensagem + "\n")
        self.areaChat.config(state='disabled')
        self.areaChat.yview(tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteChat(root)
    root.mainloop()
