from src.funcoes import mover_cobra, verificar_colisao_bordas, verificar_colisao_autofagia

def test_movimentacao_cobra_para_direita():
    corpo_inicial = [[100, 100], [80, 100]]
    # Move para a direita adicionando 20px no eixo X da cabeça
    novo_corpo = mover_cobra(corpo_inicial, "DIREITA", 20)
    assert novo_corpo[0] == [120, 100]

def test_colisao_com_borda_esquerda():
    cabeca_fora = [-20, 100]
    assert verificar_colisao_bordas(cabeca_fora, 600, 600) is True

def test_colisao_com_borda_direita():
    cabeca_fora = [600, 100]
    assert verificar_colisao_bordas(cabeca_fora, 600, 600) is True

def test_autofagia_detectada():
    # Cabeça [100, 100] ocupando o mesmo lugar de um segmento do corpo
    corpo_colidindo = [[100, 100], [120, 100], [120, 120], [100, 100]]
    assert verificar_colisao_autofagia(corpo_colidindo) is True

def test_autofagia_ausente():
    corpo_saudavel = [[140, 100], [120, 100], [100, 100]]
    assert verificar_colisao_autofagia(corpo_saudavel) is False