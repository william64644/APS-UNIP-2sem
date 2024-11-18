import socket
import threading

# Configuração do servidor
host = '0.0.0.0'  # Localhost
porta = 80

clientes = []


def enviarMensagem(mensagem, socketRemetente):
    # Envia uma mensagem para todos os clientes
    for cliente in clientes:
        try:
            cliente.sendall(mensagem)
        except:
            cliente.close()
            clientes.remove(cliente)


def tratarCliente(socketCliente):
    # Lida com a comunicação com um único cliente.
    while True:
        try:
            mensagem = socketCliente.recv(1024)
            if not mensagem:  # Conexão perdida
                break
            print(f"Recebido: {mensagem.decode('utf-8')}")
            enviarMensagem(mensagem, socketCliente)
        except (socket.error, BrokenPipeError):
            print("Cliente desconectado inesperadamente")
            break
    
    # Remove o cliente da lista e fecha o socket
    clientes.remove(socketCliente)
    socketCliente.close()


def iniciarServidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"Servidor rodando em {host}:{porta}")
    while True:
        socketCliente, enderecoCliente = servidor.accept()
        print(f"Conectado com {enderecoCliente}")
        clientes.append(socketCliente)
        threading.Thread(target=tratarCliente, args=(socketCliente,)).start()


if __name__ == "__main__":
    iniciarServidor()
