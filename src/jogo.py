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
    
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

 
    cobra_x = 300
    cobra_y = 300
    direcao = "DIREITA"

    rect_cobra = pygame.Rect(cobra_x, cobra_y, TAMANHO_BLOCO, TAMANHO_BLOCO)
    
    
    comida_x = random.randint(0, (LARGURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = random.randint(0, (ALTURA_TELA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    rect_comida = pygame.Rect(comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    


   
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)

    
    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)

    
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    
  
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }

    gema = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(500, 300))
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(200, 500))
    }

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

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
        
    """ if teclas[pygame.K_LEFT]:
            jogador["rect"].x -= velocidade
        if teclas[pygame.K_RIGHT]:
            jogador["rect"].x += velocidade
        if teclas[pygame.K_UP]:
            jogador["rect"].y -= velocidade
        if teclas[pygame.K_DOWN]:
            jogador["rect"].y += velocidade

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)
        jogador["rect"].y = limitar_valor(jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height)

        # Verificação de colisão com a Gema (antigo 'item')
        if verificar_colisao(jogador["rect"], gema["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a gema de lugar ao coletar
            gema["rect"].x += 80
            gema["rect"].y += 50

            # Se a gema sair da tela, volta para uma posição segura
            if gema["rect"].x > LARGURA_TELA - gema["rect"].width:
                gema["rect"].x = 50
            if gema["rect"].y > ALTURA_TELA - gema["rect"].height:
                gema["rect"].y = 50

        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador["rect"], inimigo["rect"]):
            vidas = tomar_dano(vidas, 1)

            # Afasta o inimigo ao colidir
            inimigo["rect"].x += 80
            inimigo["rect"].y += 50

            if inimigo["rect"].x > LARGURA_TELA - inimigo["rect"].width:
                inimigo["rect"].x = 50
            if inimigo["rect"].y > ALTURA_TELA - inimigo["rect"].height:
                inimigo["rect"].y = 50

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(gema["imagem"], gema["rect"])
        tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    pygame.quit() """