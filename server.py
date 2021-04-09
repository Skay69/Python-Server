import socket
import threading

ip = '1.1.1.1' # Ip da Maquina.
porta = 80 # Porta, eu escolhi a porta do apache mesmo.

c = ip,porta # Junção do ip e porta.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definição do servidor.

server.bind(c) # Ligando o servidor.
server.listen(5) # Ouvindo o servidor.

print('[*] Escutando %s%d' %(ip,porta)) # Escutando o ip, e a porta...

def handle_client(client_socket): # Uma função para enviar coisas pro client como um "chat"
	request = client_socket.recv(1024)
	print('[*] Recebido %s'%(request)) # Quando recebebendo requests.
	client_socket.send(bytes(input(""), 'utf-8')) 
	client_socket.close() # Fecha a conexão.

while True:
	client, addr = server.accept() # aceita o cliente
	print('[*] Conexao aceita de: %s%d' %(addr[0], addr[1])) # informações do cliente
	client_handler = threading.Thread(target=handle_client, args=(client,)) 
	client_handler.start() # Inicia a função de enviar informações pro client.
