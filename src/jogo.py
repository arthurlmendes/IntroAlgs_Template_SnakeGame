import pygame
import sys
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA_ESCURO,
    VERDE,
    VERMELHO,
    TAMANHO_BLOCO,
)

from src.funcoes import (
    limitar_valor,
    verificar_colisao,
    mover_cabeca_cobra,
)

def executar_jogo():
    """Executa o loop principal do protótipo inicial do Snake Game."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    
    cobra_x = 300
    cobra_y = 300
    direcao = "DIREITA"

    # Criando os rects para utilizar a função de colisão nativa do template
    rect_cobra = pygame.Rect(cobra_x, cobra_y, TAMANHO_BLOCO, TAMANHO_BLOCO)
    
    # Comida posicionada em um lugar aleatório para interação inicial
    comida_x = random.randint(0, (LARGURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = random.randint(0, (ALTURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    rect_comida = pygame.Rect(comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO)

    while rodando:
        relogio.tick(FPS)

        # 1. Entrada de Dados
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_UP, pygame.K_w) and direcao != "BAIXO":
                    direcao = "CIMA"
                elif evento.key in (pygame.K_DOWN, pygame.K_s) and direcao != "CIMA":
                    direcao = "BAIXO"
                elif evento.key in (pygame.K_LEFT, pygame.K_a) and direcao != "DIREITA":
                    direcao = "ESQUERDA"
                elif evento.key in (pygame.K_RIGHT, pygame.K_d) and direcao != "ESQUERDA":
                    direcao = "DIREITA"

        # Movimentação contínua da cabeça
        rect_cobra.x, rect_cobra.y = mover_cabeca_cobra(rect_cobra.x, rect_cobra.y, direcao, TAMANHO_BLOCO)

        # Limita a cobra dentro das bordas da tela neste protótipo
        rect_cobra.x = limitar_valor(rect_cobra.x, 0, LARGURA_TELA - TAMANHO_BLOCO)
        rect_cobra.y = limitar_valor(rect_cobra.y, 0, ALTURA_TELA - TAMANHO_BLOCO)

        # Elemento Interativo: Se colidir com a comida, ela muda de lugar
        if verificar_colisao(rect_cobra, rect_comida):
            rect_comida.x = random.randint(0, (LARGURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
            rect_comida.y = random.randint(0, (ALTURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO

        # 3. Renderização (Saída de dados)
        tela.fill(CINZA_ESCURO)

        # Desenha a Comida (Vermelha) e a Cobra (Verde)
        pygame.draw.rect(tela, VERMELHO, rect_comida)
        pygame.draw.rect(tela, VERDE, rect_cobra)

        pygame.display.flip()

    pygame.quit()
    sys.exit()