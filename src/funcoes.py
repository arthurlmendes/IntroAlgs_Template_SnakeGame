def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo mínimo e máximo"""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def mover_cabeca_cobra(x, y, direcao, tamanho_bloco):
    """Calcula a nova posição da cabeça com base na direção atual."""
    if direcao == "CIMA":
        y -= tamanho_bloco
    elif direcao == "BAIXO":
        y += tamanho_bloco
    elif direcao == "ESQUERDA":
        x -= tamanho_bloco
    elif direcao == "DIREITA":
        x += tamanho_bloco
    return x, y