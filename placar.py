# Função que salva o placar atual num arquivo de texto
def salvar_placar(placar):
    # Abre (ou cria) o arquivo placar.txt no modo escrita ("w" sobrescreve o conteúdo anterior)
    with open("placar.txt", "w") as arquivo:
        # Para cada chave (X, O, empates, total), escreve a chave e o valor separados por dois-pontos
        for chave in placar:
            arquivo.write(f"{chave}:{placar[chave]}\n")

# Função que carrega o placar salvo no arquivo
def carregar_placar():
    # Crio um placar padrão com tudo zerado (caso o arquivo não exista)
    placar = {"X": 0, "O": 0, "empates": 0, "total": 0}
    try:
        # Tenta abrir o arquivo placar.txt no modo leitura
        with open("placar.txt", "r") as arquivo:
            # Lê cada linha do arquivo e separa a chave e o valor pelo sinal de dois-pontos
            for linha in arquivo:
                chave, valor = linha.strip().split(":")
                placar[chave] = int(valor)  # Converte o valor pra inteiro e atualiza o dicionário
    # Se o arquivo não existir ainda, não faz nada (usa o placar zerado)
    except FileNotFoundError:
        pass
    # Retorna o placar (carregado ou zerado)
    return placar
