# Documentação

## Índice
* [Arquitetura](#arquitetura)
    * [Tecnologias](#tecnologias)
    * [Diagramas e fluxo](#diagramas-e-fluxo)


## Arquitetura

A arquitetura será *baseada em eventos*.
O cliente irá consumir e gerar eventos conforme a ação sendo executada pelo usuário.
O servidor será constituído por *microsserviços* que irão consumir e gerar eventos e dados:
- Gerenciador de partidas: Responsável por criar e gerenciar partidas
- Gerenciador de jogadores: Responsável por cadastrar novos jogadores e gerenciar a interação entre eles

### Tecnologias

- A implementação do cliente será realizada em **Java**
- A implementação do servidor será realizada em **Java**

### Diagramas e fluxo

* **Iniciar partida**: 
    - O usuário solicita uma nova partida.
    - O sistema distribui as cartas na tela, primeiro exibe as cartas com as imagens voltadas para cima, após alguns segundos vira as cartas e as exibe com as imagens voltadas para baixo, instancia o cronômetro e o contador de jogadas.

* **Jogar partida**: 
    - O usuário seleciona a primeira carta e o sistema a exibe na tela.
    - O usuário seleciona a segunda carta e o sistema exibe a mesma na tela.
    - Sistema verifica se as duas cartas selecionadas são iguais. 
    - Sistema contabiliza a jogada efetuada.
    - Caso as cartas sejam iguais, as cartas somem.
    - Caso as cartas não sejam iguais, as cartas voltam a ficar voltadas para baixo.
    - Quando todos os pares de cartas são encontrados o sistema encerra a partida.
    - Sistema exibe a pontuação.

* **Sair do jogo**: 
    - Usuário solicita sair do jogo.
    - Sistema finaliza o jogo.
