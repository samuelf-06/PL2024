import json
from datetime import datetime

def carregar_stock(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados['stock']  
    except FileNotFoundError:
        return []

def guardar_stock(stock, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump({"stock": stock}, arquivo)  

def listar_produtos(stock):
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")

saldo = 0

def adicionar_moedas(moedas):
    global saldo  
    for moeda in moedas:
        if moeda.endswith('e'):
            saldo += 100  
        elif moeda.endswith('c'):
            saldo += int(moeda[:-1])

def formatar_saldo(saldo):
    euros = saldo // 100
    centimos = saldo % 100
    return f"{euros}e{centimos:02d}c" 

def selecionar_produto(stock, codigo_produto, saldo):
    for produto in stock:
        if produto['cod'] == codigo_produto:
            preco_em_centimos = int(produto['preco'] * 100)  # Convertendo o preço para centimos
            if produto['quant'] > 0 and saldo >= preco_em_centimos:
                produto['quant'] -= 1
                saldo -= preco_em_centimos
                print(f"Pode retirar o produto dispensado \"{produto['nome']}\"")
                print(f"Saldo = {saldo // 100}e{saldo % 100}c")
            else:
                print("Saldo insuficiente para satisfazer o seu pedido")
                print(f"Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {preco_em_centimos}c")
            break
    else:
        print("Produto não encontrado")


def main():
    nome_arquivo = "productStock.json"
    stock = carregar_stock(nome_arquivo)
    saldo = 0

    data_atual = datetime.now().strftime("%Y-%m-%d")
    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").upper()

        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            moedas = comando.split()[1:]
            adicionar_moedas(moedas)
            saldo_formatado = f"{saldo // 100}e{saldo % 100:02d}c"  # Formata o saldo
            print(f"maq: Saldo = {saldo_formatado}")
        elif comando.startswith("SELECIONAR"):
            codigo_produto = comando.split()[1]
            selecionar_produto(stock, codigo_produto, saldo)
        elif comando == "SAIR":
            troco = saldo
            print("maq: Pode retirar o troco:", end=" ")
            print(f"1x {troco // 100}e, 1x {troco % 100}c.")
            print("maq: Até à próxima")
            guardar_stock(stock, nome_arquivo)
            break
        else:
            print("Comando inválido")

if __name__ == "__main__":
    main()