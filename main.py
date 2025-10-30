from jogo import jogar_uma_partida
from placar import salvar_placar, carregar_placar
import os

def jogar_varias_partidas(modo_automatico=False):
    placar = carregar_placar()
    jogadas_auto = [
        (0, 0), (0, 1), (1, 1), (1, 0), (2, 2)
    ]  # Jogadas automáticas (X vence)
    indice = 0

    while True:
        print(f"\nIniciando partida {placar['total'] + 1}")

        if modo_automatico:
            # Modo sem input — simula jogadas
            vencedor = jogar_uma_partida_automatica(jogadas_auto)
        else:
            vencedor = jogar_uma_partida()

        placar["total"] += 1
        if vencedor:
            placar[vencedor] += 1
        else:
            placar["empates"] += 1

        print("\nPlacar:")
        print(f"Vitórias X: {placar['X']}")
        print(f"Vitórias O: {placar['O']}")
        print(f"Empates: {placar['empates']}")
        salvar_placar(placar)

        if modo_automatico:
            break  # No modo automático, roda apenas uma partida

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            print("Fim de jogo. Obrigado por jogar!")
            break


def jogar_uma_partida_automatica(jogadas):
    """Versão automática da função jogar_uma_partida()"""
    from tabuleiro import criar_tabuleiro, exibir_tabuleiro
    from jogo import verificar_vitoria, trocar_jogador

    tabuleiro = criar_tabuleiro()
    jogador = "X"
    jogadas_feitas = 0

    for linha, coluna in jogadas:
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            jogadas_feitas += 1
            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu automaticamente!")
                return jogador
            jogador = trocar_jogador(jogador)

    exibir_tabuleiro(tabuleiro)
    print("Empate automático!")
    return None


if __name__ == "__main__":
    # Detecta se está no GitHub Actions
    modo_automatico = os.getenv("GITHUB_ACTIONS") == "true"
    jogar_varias_partidas(modo_automatico)
