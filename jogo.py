# Importo as funções para criar e mostrar o tabuleiro
from tabuleiro import criar_tabuleiro, exibir_tabuleiro

# Função que verifica se o jogador atual venceu a partida
def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        # Verifica se tem uma linha completa do mesmo jogador
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        # Verifica se tem uma coluna completa do mesmo jogador
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Verifica a diagonal principal (de canto superior esquerdo até o inferior direito)
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    # Verifica a diagonal secundária (de canto superior direito até o inferior esquerdo)
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    # Se não ganhou por nenhuma dessas formas, retorna False
    return False

# Função pra trocar o jogador atual (se for X vira O, se for O vira X)
def trocar_jogador(jogador):
    return "O" if jogador == "X" else "X"

# Função principal que executa uma única partida de Jogo da Velha
def jogar_uma_partida():
    tabuleiro = criar_tabuleiro()  # Começa com um tabuleiro vazio
    jogador = "X"  # O jogador X sempre começa
    jogadas = 0  # Começa com zero jogadas feitas
    vencedor = None  # Ainda não tem vencedor definido

    # Enquanto tiver menos de 9 jogadas (máximo possível em uma partida)
    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)  # Mostra o tabuleiro atualizado
        print(f"Vez do jogador {jogador}")  # Informa de quem é a vez

        try:
            # Recebe as coordenadas da jogada
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))

            # Verifica se a posição escolhida é válida e está vazia
            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador  # Marca o símbolo no tabuleiro
                jogadas += 1  # Conta mais uma jogada

                # Verifica se o jogador atual venceu
                if verificar_vitoria(tabuleiro, jogador):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador} venceu!")  # Mostra quem ganhou
                    vencedor = jogador  # Guarda o vencedor
                    break  # Termina a partida

                jogador = trocar_jogador(jogador)  # Troca a vez pro outro jogador
            else:
                print("Posição inválida ou ocupada.")  # Se a jogada for impossível
        except ValueError:
            print("Entrada inválida.")  # Se o jogador digitar algo que não seja número

    # Se ninguém ganhou após 9 jogadas, é empate
    if not vencedor:
        exibir_tabuleiro(tabuleiro)
        print("Empate!")  # Informa que a partida terminou sem vencedor

    return vencedor  # Retorna quem ganhou, ou None se empatou
