# Função para processar os dados do arquivo CSV
def processar_dados_arquivo(nome_arquivo):
    modalidades = set()
    aptos = 0
    inaptos = 0
    total_atletas = 0
    idade_atletas = {}

    # Abre o arquivo e lê linha por linha
    with open(nome_arquivo, 'r') as arquivo:
        # Ignora o cabeçalho
        arquivo.readline()
        for linha in arquivo:
            campos = linha.strip().split(',')

            # Extrai os campos necessários
            modalidade = campos[8]
            idade = int(campos[5])
            

            # Processa os dados
            modalidades.add(modalidade)
            if len(campos) >= 13:
                # Verifica se o atleta é apto ou inapto
                if campos[-1] == 'true':
                    aptos += 1
                else:
                    inaptos += 1

            # Distribuição de atletas por escalão etário
            escalao = idade // 5 * 5
            idade_atletas[escalao] = idade_atletas.get(escalao, 0) + 1

    # Ordenando modalidades alfabeticamente
    modalidades_ordenadas = sorted(modalidades)

    # Calculando percentagem de atletas aptos e inaptos
    total_atletas = aptos + inaptos
    percentagem_aptos = (aptos / float(total_atletas)) * 100 if total_atletas != 0 else 0
    percentagem_inaptos = (inaptos / float(total_atletas)) * 100 if total_atletas != 0 else 0

    # Imprimindo resultados
    print("Lista ordenada alfabeticamente das modalidades desportivas:")
    for modalidade in modalidades_ordenadas:
        print(modalidade)

    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print("Aptos: {:.2f}%".format(percentagem_aptos))
    print("Inaptos: {:.2f}%".format(percentagem_inaptos))

    print("\nDistribuição de atletas por escalão etário:")
    for escalao, quantidade in idade_atletas.items():
        print("[{}-{}]: {}".format(escalao, escalao + 4, quantidade))

# Chamando a função com o nome do arquivo CSV
nome_arquivo = 'emd.csv'  # Substitua 'dados.csv' pelo nome do seu arquivo CSV
processar_dados_arquivo(nome_arquivo)

