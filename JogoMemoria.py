import os
import sys
import time
import random

'''
Classe que representa o estado do jogo.
'''
class Jogo:

    '''
    Construtor. Initializa o tabuleiro em forma de string
    '''
    def __init__(self):
        # Tamanho (da lateral) do tabuleiro. NECESSARIAMENTE PAR E MENOR QUE 10!
        dim = 4
        # Numero de jogadores
        nJogadores = 2
        # Numero total de pares de pecas
        self.totalDePares = dim**2 / 2
        self.vez = 0
        self.paresEncontrados = 0
        # tabuleiro = "1;8;4;5 3;7;2;6 2;6;1;7 3;6;8;4"
        tabuleiro = [[-1,-8,-4,-5],[-3,-7,-2,-6],[-2,-6,-1,-7],[-3,-6,-8,-4]]

        self.board = tabuleiro
        self.placar = [0] * nJogadores

    # --------------------------------------------------
    '''
    Salva os dados do tabuleiro para uma string.
    '''
    def save(self):
        tabuleiro = ""
        for tab in self.board:
            for elem in tab:
                tabuleiro = tabuleiro + str(elem) + ";"
            
            tabuleiro = tabuleiro + " "
            
        return tabuleiro
    
    # -------------------------------------------------
    '''
    Restaura os dados do tabuleiro a partir de uma string.
    '''
    def restore(self, data):
        tabuleiro = []
        linhas = data.split(" ")
        for lin in linhas:
            row = lin.split(";")
            tabuleiro.append(row)
        
        self.board = tabuleiro

    # -------------------------------------------------
    '''
    Imprime o tabuleiro em um formato visual.
    '''
    def printTabuleiro(self):
        # Limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')

        dim = len(self.board)-1
        # Imprime coordenadas horizontais
        coord_h = "     "
        for i in range(0, dim):
            coord_h = coord_h + " " + str(i) + " "

        # Imprime separador horizontal  
        sep_h = "-----"
        for i in range(0, dim):
            sep_h = sep_h + "---"

        print coord_h
        print sep_h

        for i in range(0, dim):
            # Imprime coordenadas verticais
            coord_v = ""
            coord_v = coord_v + " " + str(i) + " | "

            # Imprime conteudo da linha 'i'
            for j in range(0, dim):
                # Peca ja foi removida?
                if self.board[i][j] == "-":
                    coord_v = coord_v + " - "
                # Peca esta levantada?
                elif int(self.board[i][j]) >= 0:
                    coord_v = coord_v + " " + self.board[i][j] + " "
                else:
                    coord_v = coord_v + " ? "
            
            print coord_v
            
        
        print "\nVez do Jogador "+str(self.vez+1)+"\n"

        self.imprimePlacar()
        
    # -------------------------------------------------
    '''
    Fecha peca na posicao (i, j). Se posicao ja esta
    fechada ou se ja foi removida, retorna False. Retorna True
    caso contrario.
    '''
    def fechaPeca(self, i, j):
        if self.board[i][j] == '-':
            return False
        elif int(self.board[i][j]) > 0:
            self.board[i][j] = str(int(self.board[i][j])*-1)
            return True
        return False

    # -------------------------------------------------
    '''
    Remove peca na posicao (i, j). Se posicao ja esta
    removida, retorna False. Retorna True
    caso contrario.
    '''
    def removePeca(self, i, j):
        if self.board[i][j] == '-':
            return False
        else:
            self.board[i][j] = "-"
            return True
    # -------------------------------------------------
    '''
    Faz uma jogada no tabuleiro, nas posicoes dadas.
    '''
    def joga(self, row, col):
        dim = len(self.board)
        
        if row < 0 or row >= dim:
            print "Coordenada i deve ser maior ou igual a zero e menor que "+str(dim)

        if col < 0 or col >= dim:
            print "Coordenada j deve ser maior ou igual a zero e menor que "+str(dim)

        # Testa se peca ja esta aberta (ou removida)
        abrePeca = False
        if self.board[row][col] == '-':
            abrePeca = False
        elif int(self.board[row][col]) < 0:
            self.board[row][col] = str(int(self.board[row][col])*-1)
            abrePeca = True

        if abrePeca:
            print "Escolha uma peca ainda fechada!"

        self.printTabuleiro()

    #--------------------------------------------------
    def validaJogada(self, jogadas):
        coord_1 = jogadas[0]
        coord_2 = jogadas[1]

        i1, j1 = coord_1
        i2, j2 = coord_2
        # Pecas escolhidas sao iguais?
        if self.board[i1][j1] == self.board[i2][j2]:

            print "Pecas casam! Ponto para o jogador."
            self.paresEncontrados = self.paresEncontrados + 1
            self.incrementaPlacar(self.vez)
            self.removePeca(i1, j1)
            self.removePeca(i2, j2)
            time.sleep(3)
        else:
            print "Pecas nao casam!"
            time.sleep(3)
            self.fechaPeca(i1, j1)
            self.fechaPeca(i2, j2)
        
        self.vez = (self.vez + 1) % len(self.placar)
        
        self.printTabuleiro()
        
    
    #--------------------------------------------------
    '''
    Adiciona um ponto no placar para o jogador especificado.
    '''
    def incrementaPlacar(self, jogador):
        self.placar[jogador] = self.placar[jogador] + 1

    #--------------------------------------------------
    '''
    Imprime o placar atual.
    '''
    def imprimePlacar(self):
        nJogadores = len(self.placar)
        print("Placar:")
        print ("---------------------")
        for i in range(0, nJogadores):
            print ("Jogador {0}: {1:2d}".format(i + 1, self.placar[i]))