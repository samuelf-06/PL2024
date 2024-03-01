# TPC1
 
**Leitura e Processamento do Ficheiro CSV:**
    O ficheiro CSV é lido linha por linha.
    O cabeçalho é ignorado.
    Para cada linha do ficheiro, os campos são separados e os dados relevantes são extraídos, como a modalidade desportiva e a idade do atleta.

**Processamento dos Dados:**
    As modalidades desportivas são armazenadas num conjunto para garantir que apenas modalidades únicas sejam mantidas.
    O número de atletas aptos e inaptos é contabilizado.
    A distribuição dos atletas por escalão etário é calculada, agrupando os atletas em intervalos de 5 anos.

**Ordenação e Impressão dos Resultados:**
    As modalidades desportivas são ordenadas alfabeticamente e impressas.
    As percentagens de atletas aptos e inaptos são calculadas e impressas.
    A distribuição de atletas por escalão etário é impressa, mostrando o número de atletas em cada faixa etária.

**Execução da Função:**
    O código é chamado com o nome do ficheiro CSV contendo os dados dos atletas.
