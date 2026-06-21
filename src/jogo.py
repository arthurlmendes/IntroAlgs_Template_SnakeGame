import pygame
import sys
from src.config import *
from src.funcoes import mover_cobra, verificar_colisao_bordas, verificar_colisao_autofagia, gerar_comida
from src.dados import carregar_recorde, salvar_recorde

def desenhar_texto_centralizado(tela, texto, fonte, cor, y_offset=0):
    """Função auxiliar para renderizar textos bem no centro da tela."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_offset))
    tela.blit(superficie, retangulo)

def desenhar_grade(tela):
    
    for x in range(0, LARGURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, GRADE, (x, 0), (x, ALTURA_TELA))
    for y in range(0, ALTURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, GRADE, (0, y), (LARGURA_TELA, y))

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    
    
    fonte_titulo = pygame.font.SysFont("arial", 60, bold=True)
    fonte_media = pygame.font.SysFont("arial", 28, bold=True)
    fonte_pequena = pygame.font.SysFont("arial", 20)
    
    estado = "MENU" 
    
    # Variáveis de sessão
    recorde = carregar_recorde(CAMINHO_RECORDE)
    corpo_cobra = []
    direcao = ""
    comida = []
    pontos = 0
    velocidade_atual = FPS_INICIAL

    while True:
        tela.fill(FUNDO)

        if estado == "MENU":
            desenhar_grade(tela)
            desenhar_texto_centralizado(tela, "SNAKE GAME", fonte_titulo, CABECA, -50)
            desenhar_texto_centralizado(tela, "Pressione ESPAÇO para Iniciar", fonte_pequena, BRANCO, 20)
            desenhar_texto_centralizado(tela, f"Recorde Atual: {recorde}", fonte_media, AMARELO, 80)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    # Configura as variáveis iniciais para começar a jogar
                    corpo_cobra = [[300, 300], [280, 300], [260, 300]]
                    direcao = "DIREITA"
                    pontos = 0
                    velocidade_atual = FPS_INICIAL
                    comida = gerar_comida(corpo_cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO)
                    estado = "JOGANDO"

      
        elif estado == "JOGANDO":
            relogio.tick(velocidade_atual)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key in (pygame.K_UP, pygame.K_w) and direcao != "BAIXO":
                        direcao = "CIMA"
                    elif evento.key in (pygame.K_DOWN, pygame.K_s) and direcao != "CIMA":
                        direcao = "BAIXO"
                    elif evento.key in (pygame.K_LEFT, pygame.K_a) and direcao != "DIREITA":
                        direcao = "ESQUERDA"
                    elif evento.key in (pygame.K_RIGHT, pygame.K_d) and direcao != "ESQUERDA":
                        direcao = "DIREITA"

            corpo_cobra = mover_cobra(corpo_cobra, direcao, TAMANHO_BLOCO)

            # Lógica de comer
            if corpo_cobra[0] == comida:
                pontos += 10
                comida = gerar_comida(corpo_cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO)
                if pontos % 50 == 0:
                    velocidade_atual += 1 # Aumenta a dificuldade
            else:
                corpo_cobra.pop() # Remove a cauda se não comeu

            # Verifica colisões (Derrota)
            if verificar_colisao_bordas(corpo_cobra[0], LARGURA_TELA, ALTURA_TELA) or verificar_colisao_autofagia(corpo_cobra):
                if pontos > recorde:
                    recorde = pontos
                    salvar_recorde(CAMINHO_RECORDE, recorde)
                estado = "GAMEOVER"

            # Renderização do Jogo
            desenhar_grade(tela)
            
            # Desenha a comida (com uma borda interna para parecer mais arredondada/bonita)
            pygame.draw.rect(tela, COMIDA, (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO), border_radius=4)
            
            # Desenha a cobra
            for i, segmento in enumerate(corpo_cobra):
                cor = CABECA if i == 0 else CORPO
                # Desenha o bloco com um espaçamento mínimo para separar as "escamas"
                retangulo = pygame.Rect(segmento[0] + 1, segmento[1] + 1, TAMANHO_BLOCO - 2, TAMANHO_BLOCO - 2)
                pygame.draw.rect(tela, cor, retangulo, border_radius=2)

            # Placar no topo
            texto_placar = fonte_pequena.render(f"Pontos: {pontos}   |   Recorde: {recorde}", True, BRANCO)
            tela.blit(texto_placar, (10, 10))

    
        elif estado == "GAMEOVER":
            desenhar_grade(tela)
            desenhar_texto_centralizado(tela, "GAME OVER", fonte_titulo, COMIDA, -50)
            desenhar_texto_centralizado(tela, f"Sua Pontuação: {pontos}", fonte_media, BRANCO, 20)
            desenhar_texto_centralizado(tela, "Pressione ESPAÇO para Tentar Novamente", fonte_pequena, AMARELO, 80)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    estado = "MENU" # Volta para o menu inicial

        pygame.display.flip()