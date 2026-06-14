import random

def mover_cobra(corpo, direcao, tamanho_bloco):
    """
    Move a cobra adicionando uma nova cabeça na direção atual.
    Retorna o corpo atualizado com a nova cabeça (a cauda é removida no loop principal se ela não comer).
    """
    cabeca = list(corpo[0])
    
    if direcao == "CIMA":
        cabeca[1] -= tamanho_bloco
    elif direcao == "BAIXO":
        cabeca[1] += tamanho_bloco
    elif direcao == "ESQUERDA":
        cabeca[0] -= tamanho_bloco
    elif direcao == "DIREITA":
        cabeca[0] += tamanho_bloco
        
    # Retorna o corpo com a nova cabeça inserida na frente
    return [cabeca] + corpo

def verificar_colisao_bordas(cabeca, largura_tela, altura_tela):
    """Retorna True se a cabeça da cobra saiu dos limites da tela."""
    x, y = cabeca[0], cabeca[1]
    return x < 0 or x >= largura_tela or y < 0 or y >= altura_tela

def verificar_colisao_autofagia(corpo):
    """Retorna True se a cabeça da cobra colidir com qualquer parte do seu próprio corpo."""
    cabeca = corpo[0]
    return cabeca in corpo[1:]

def gerar_comida(corpo_cobra, largura_tela, altura_tela, tamanho_bloco):
    """Gera uma nova coordenada para a comida alinhada à grade e fora do corpo da cobra."""
    while True:
        x = random.randint(0, (largura_tela - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
        y = random.randint(0, (altura_tela - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
        posicao_comida = [x, y]
        
        if posicao_comida not in corpo_cobra:
            return posicao_comida