# Importo a função que roda uma partida individual do jogo
from jogo import jogar_uma_partida

# Aqui eu importo as funções que salvam e carregam o placar em arquivo
from placar import salvar_placar, carregar_placar

# Essa função controla várias partidas seguidas do jogo da velha
def jogar_varias_partidas():
    # Carrego o placar salvo do arquivo (ou começa do zero se for a primeira vez)
    placar = carregar_placar()

    # Esse laço vai rodar infinitamente até o jogador decidir parar
    while True:
        # Mostra qual é o número da partida atual (baseado no total salvo)
        print(f"\nIniciando partida {placar['total'] + 1}")

        # Aqui eu executo uma partida e guardo quem venceu (ou None se empatou)
        vencedor = jogar_uma_partida()

        # Atualizo o número total de partidas jogadas
        placar["total"] += 1

        # Se teve um vencedor (X ou O), adiciona uma vitória pra ele
        if vencedor:
            placar[vencedor] += 1
        # Se não teve vencedor, então foi empate
        else:
            placar["empates"] += 1

        # Mostro o placar atualizado na tela
        print("\nPlacar:")
        print(f"Vitórias X: {placar['X']}")
        print(f"Vitórias O: {placar['O']}")
        print(f"Empates: {placar['empates']}")

        # Salvo o placar no arquivo pra não perder os dados
        salvar_placar(placar)

        # Pergunto se o jogador quer jogar de novo
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()

        # Se o jogador responder qualquer coisa diferente de 's', o jogo acaba
        if jogar_novamente != "s":
            print("Fim de jogo. Obrigado por jogar!")
            break  # Sai do loop e finaliza tudo

# Essa parte garante que o jogo só começa se o script for executado diretamente
if __name__ == "__main__":
    jogar_varias_partidas()

