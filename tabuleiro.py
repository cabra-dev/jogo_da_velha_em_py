# Função que cria um tabuleiro vazio (3x3) usando listas dentro de listas
def criar_tabuleiro():
    # Retorna uma matriz 3x3 preenchida com espaços em branco
    return [[" " for _ in range(3)] for _ in range(3)]

# Função que mostra o tabuleiro formatado no terminal
def exibir_tabuleiro(tabuleiro):
    print("\n  0   1   2")  # Cabeçalho com os índices das colunas
    for i, linha in enumerate(tabuleiro):
        # Mostra os valores da linha separados por barras verticais
        print(i, " | ".join(linha))
        # Adiciona uma linha divisória entre as linhas, menos na última
        if i < 2:
            print("  ---------")
    print()  # Pula uma linha depois de mostrar o tabuleiro
