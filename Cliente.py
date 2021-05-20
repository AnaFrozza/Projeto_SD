#!/usr/bin/env python
import socket
from JogoMemoria import Jogo

host = "192.168.100.41"
port = 6789 # Base 16 for hex value
 
dest = (host, port) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Recebemos a conexao Socket
s.connect(dest)

# Cria um tabuleiro de jogo vazio
tabuleiro = Jogo()

print "JOGO DA MEMORIA\n"
# print "Para sair use CTRL+X e pressione enter\n"
print "OBS:. O jogo iniciara quando todos os jogadores estiverem prontos...\n"
# msg = raw_input()

try:
    while True:

        #recebe a dados do servidor
        data = s.recv(1024)
        tabuleiro.restore(data.decode('utf-8'))

        tabuleiro.printTabuleiro()

        pecas = []
        while len(pecas) < 3:
            for i in range(0, 2):
                row = int(raw_input('Digite a linha:'))
                col = int(raw_input('Digite a coluna:'))
                
                pecas.append([row, col])

                tabuleiro.joga(row, col)

            tabuleiro.validaJogada(pecas)
            pecas = []
            
            s.sendall(tabuleiro.save().encode('utf-8'))

finally:
    print "Saindo do jogo"
    s.close()
