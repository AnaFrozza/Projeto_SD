#!/usr/bin/env python
import socket
import sys
from thread import *
from JogoMemoria import Jogo

    
host = ""
port = 6789
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Recebemos a conexao Socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # garante que o socket sera destruido (pode ser reusado) apos uma interrupcao da execucao 

try:
    s.bind((host, port))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
      
s.listen(2)

# Funcao para lidar com cada conexao (jogador)
def clientthread(conn, tabuleiro, id_jogador):
    # Sai do loop quando o jogador desconecta, pois a variavel data nao contera nenhum conteudo

    conn.sendall(tabuleiro.save().encode('utf-8'))

    while True:
        # Receiving from client
        data = conn.recv(1024)
        
        if not data: 
            print 'Jogador se foi. :('
            break

        # Converte para string e restaura no tabuleiro
        tabuleiro.restore(data.decode('utf-8'))

    # destroi o socket e encerra thread ao sair do loop
    conn.close()

listaJogadores = []

# Cria um tabuleiro de jogo vazio
tabuleiro = Jogo()

while True:
    
    # Aceita conexoes
    conn, jogador = s.accept()
    listaJogadores.append(conn)
    
    print 'Jogador ',listaJogadores.index(conn), '>> ', jogador, ' conectado '

    if(len(listaJogadores) >= 2):
        #Cria nova thread para uma nova conexao. O primeiro
        #argumento e o nome da funcao, e o segundo e uma tupla
        #com os parametros da funcao.
        for i in listaJogadores:
            start_new_thread(clientthread ,(i, tabuleiro, listaJogadores.index(i), ))
