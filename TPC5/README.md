# TPC5 - Vending Machine

Este código simula uma interação básica com uma máquina de venda automática, permitindo ao utilizador listar os produtos, adicionar moedas, selecionar produtos para compra e finalizar a transação com um comando de saída.

## Comandos disponíveis

- **Listar Produtos (LISTAR):** Quando o utilizador digita "LISTAR", a máquina exibe os produtos disponíveis. O ficheiro itera sobre a lista de produtos e imprime os detalhes de cada um.
- **Adicionar Moedas (MOEDA):** Quando o utilizador digita "MOEDA", a máquina adiciona as moedas especificadas ao saldo. O ficheiro verifica primeiro se a moeda é em euros ou em cêntimos para poder adicionar ao saldo ainda no formato normal (ex: 2,30) posteriormente este é formatado para o formato desejado (ex: 2e30c).
- **Selecionar Produto (SELECIONAR):** Quando o utilizador digita "SELECIONAR" seguido pelo código do produto desejado, a máquina verifica se o produto está disponível e se o saldo é suficiente para comprá-lo. Se sim, o produto é dispensado e o saldo é atualizado sendo fornecido um feedback ao utilizador.
- **Sair (SAIR):** Quando o utilizador digita "SAIR", a máquina calcula e exibe o troco, atualiza o stock e encerra o programa.
