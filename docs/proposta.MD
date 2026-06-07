# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Snake Game

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome: Arthur Lima Mendes

## 3. Tipo de jogo


Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo: Snake 



## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

O jogo consiste em controlar uma cobra em uma grade bidimensional. Na tela, aparecerá a cobra (representada por blocos interligados), a comida (um bloco gerado aleatoriamente) e a pontuação atualizada no topo. O jogador controla a direção do movimento da cabeça da cobra. Cada vez que a cobra come a fruta, seu corpo cresce um bloco, a velocidade aumenta levemente e uma nova comida surge. O desafio é acumular a maior pontuação possível sem colidir com as paredes da janela ou com o próprio corpo da cobra.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Coletar o maior número possível de comidas para crescer o corpo da cobra e alcançar a maior pontuação (e recorde) sem colidir.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: A cobra se move continuamente na direção definida pelo jogador.

- Regra 2: Não é permitido reverter a direção instantaneamente para o sentido oposto (ex: se estiver indo para a direita, não pode ir direto para a esquerda).

- Regra 3: Cada comida coletada aumenta o tamanho da cobra em 1 bloco e soma 10 pontos ao placar.

- Regra 4: A cada 50 pontos alcançados, a velocidade do jogo aumenta gradativamente (aumento de dificuldade).

- Regra 5: O jogo salva e exibe o maior recorde (High Score) mesmo após fechar a janela.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos: 

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

Por ser um jogo do estilo arcade infinito, não há uma condição de vitória definitiva. O objetivo é superar o recorde anterior (salvo em arquivo) e pontuar o máximo possível.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

A partida termina imediatamente (Game Over) se a cabeça da cobra colidir com qualquer uma das quatro bordas da tela ou se colidir com qualquer parte do seu próprio corpo.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Uma cobra composta por uma lista de coordenadas (blocos). A cabeça é controlada pelas setas do teclado e o corpo segue o rastro do movimento.



## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

As próprias bordas da tela e o corpo crescente da própria cobra atuam como os obstáculos mortais do jogo.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

A comida (fruta), que aparece de forma aleatória na tela (respeitando a grade) e que faz a cobra crescer ao ser coletada.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

O jogador possui 1 vida por tentativa. A tela exibirá a pontuação atual (Score) e a maior pontuação já registrada na história do jogo (High Score).

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Seta para cima / Tecla W: Mover a cobra para cima
- Tecla/comando: Seta para baixo / Tecla S: Mover a cobra para baixo
- Tecla/comando: Seta para esquerda / Tecla A: Mover a cobra para a esquerda 
- Tecla/comando: Seta para direita / Tecla D: Mover a cobra para a direita
- Tecla/comando: Tecla R: Reiniciar a partida após o Game Over
- Tecla/comando: ESC: Sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

Conforme as regras do repositório padrão (Template oficial), utilizaremos a seguinte estrutura:

main.py: Arquivo principal na raiz que inicializa o Pygame e chama o loop do jogo.

src/config.py: Arquivo para armazenar constantes como dimensões da tela (ex: 600x600), tamanho do bloco da grade (ex: 20x20), velocidade e dicionário de cores (RGB).

src/funcoes.py: Funções lógicas puras (geração aleatória de comida fora do corpo da cobra, checagem de colisões), ideais para a aplicação de testes unitários.

src/arquivos.py: Funções responsáveis por ler e gravar o recorde máximo em um arquivo de texto (recorde.txt).


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

Não pretendo utilizar recursos externos complexos. Toda a parte gráfica será gerada nativamente com formas geométricas do Pygame (pygame.draw.rect) e fontes padrão do sistema para garantir leveza e foco na lógica de programação.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Controle de atualização/FPS: Ajustar a velocidade de atualização da cobra para que ela se mova de bloco em bloco de forma fluida, sem correr rápido demais.

- Dificuldade 2: Lógica de crescimento do corpo: Atualizar corretamente a lista de coordenadas da cobra (adicionar nova cabeça e remover a cauda, exceto quando ela come).

- Dificuldade 3: Evitar bugs de input: Impedir que o jogador mude a direção duas vezes muito rápido antes do próximo frame, fazendo a cobra colidir consigo mesma por engano.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

Uma janela Pygame estruturada com uma cobra se movimentando pela grade via teclado, sistema de colisão com as bordas e consigo mesma funcionando, geração de comida, pontuação básica na tela, gravação do recorde em arquivo externo e uma tela simples de "Game Over" com opção de reiniciar.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Adicionar uma tela de menu inicial para começar o jogo.
- Melhoria 2: Inserir obstáculos fixos (paredes internas) no cenário após atingir certa pontuação.
- Melhoria 3: Sistema de frutas especiais com cores diferentes que dão bônus de pontos temporários.
- Melhoria 4: Efeitos sonoros básicos (som ao comer a fruta e som de Game Over).