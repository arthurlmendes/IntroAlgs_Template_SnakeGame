import pygame
import sys
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA_ESCURO,
    VERDE,
    VERDE_ESCURO,
    VERMELHO,
    BRANCO,
    TAMANHO_BLOCO,
    CAMINHO_RECORDE
)
from src.funcoes import (
    mover_cobra,
    verificar_colisao_bordas,
    verificar_colisao_autofagia,
    gerar_comida
)
from src.dados import carregar_recorde, salvar_recorde

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    
    # Fonte para renderizar o Score na tela
    fonte = pygame.font.SysFont("Arial", 24)
    
    # Estado inicial do jogo (Semana 3)
    # Corpo representado por uma lista de segmentos [x, y]
    corpo_cobra = [[300, 300], [280, 300], [260, 300]]
    direcao = "DIREITA"
    velocidade_atual = FPS
    
    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    
    comida = gerar_comida(corpo_cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO)
    
    rodando = True
    game_over = False

    while rodando:
        # Loop de Game Over (Permite reiniciar com 'R' ou sair com 'ESC')
        while game_over:
            tela.fill(CINZA_ESCURO)
            texto_game_over = fonte.render("GAME OVER! Pressione R para Reiniciar ou ESC para Sair", True, VERMELHO)
            tela.blit(texto_game_over, (LARGURA_TELA // 2 - texto_game_over.get_width() // 2, ALTURA_TELA // 2))
            pygame.display.flip()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if evento.key == pygame.K_r:
                        # Reinicia as variáveis do jogo
                        corpo_cobra = [[300, 300], [280, 300], [260, 300]]
                        direcao = "DIREITA"
                        pontos = 0
                        velocidade_atual = FPS
                        comida = gerar_comida(corpo_cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO)
                        game_over = False

        # Loop de Jogo Normal
        relogio.tick(velocidade_atual)

        # 1. Captura de Eventos / Entradas
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

        # 2. Movimentação da Cobra
        corpo_cobra = mover_cobra(corpo_cobra, direcao, TAMANHO_BLOCO)

        # Interação: Verificação de colisão com a comida
        if corpo_cobra[0] == comida:
            pontos += 10
            comida = gerar_comida(corpo_cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO)
            
            # Mecânica de Dificuldade: Aumenta a velocidade a cada 50 pontos
            if pontos % 50 == 0:
                velocidade_atual += 1
                
            # Atualiza e salva o recorde imediatamente se for superado
            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)
        else:
            # Se não comeu a comida, remove o último segmento para manter o tamanho estável
            corpo_cobra.pop()

        # Condições Game Over
        if verificar_colisao_bordas(corpo_cobra[0], LARGURA_TELA, ALTURA_TELA) or verificar_colisao_autofagia(corpo_cobra):
            game_over = True

        # 3. Renderização dos Gráficos
        tela.fill(CINZA_ESCURO)
        
        # Desenha a Comida
        pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        
        # Desenha a Cobra (Cabeça com uma cor diferente do corpo)
        for i, segmento in enumerate(corpo_cobra):
            cor = VERDE if i == 0 else VERDE_ESCURO
            pygame.draw.rect(tela, cor, (segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

        # Desenha a Interface de Pontos na Tela
        superficie_pontos = fonte.render(f"Pontos: {pontos}  |  Recorde: {recorde}", True, BRANCO)
        tela.blit(superficie_pontos, (15, 15))

        pygame.display.flip()

    pygame.quit()
    sys.exit()