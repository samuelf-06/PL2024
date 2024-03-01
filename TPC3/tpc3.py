import re

def calculadora_de_soma(texto):
    # Inicializa a variável para controlar se a soma está ativa
    soma_ativa = False
    # Inicializa a soma atual com um valor inicial
    soma_atual = 8

    # Compila um padrão regex para encontrar números, 'on', 'off' e '=' no texto
    padrao = re.compile(r'([Oo][Nn]|[Oo][Ff]{2}|=|\d+)', re.IGNORECASE)
    # Encontra todas as correspondências no texto
    matches = padrao.finditer(texto)

    # Itera sobre as correspondências encontradas
    for match in matches:
        # Obtém o tipo de correspondência atual
        tipo = match.group()

        # Se o tipo for 'on', ativa a soma
        if 'on' == tipo.lower():
            soma_ativa = True
            
        # Se o tipo for 'off', desativa a soma
        if 'off' == tipo.lower():
            soma_ativa = False
            
        # Se o tipo for um número e a soma estiver ativa, adiciona à soma atual
        if tipo.isdigit() and soma_ativa:
            soma_atual += int(tipo) 
            
        # Se o tipo for '=', imprime a soma atual
        if '=' == tipo:         
            print(f'Resultado da soma: {soma_atual}')
            
# Texto de entrada para a função
texto_entrada = "1iMRE7r=HtzkAon8o2sdXVtM0oLoffzNxZi4t5eqOpZNEqCJaLonK1mMTy3d22WoffaJ8uH6sgDxy2xMJoNRQZ7aAmkmhF4N91eTqqzequb4eYpA34DIojequZtnvw6LyrPxme0eqZbYZPon82fFbYKoffQXTonOnjjAAzS4=eq1tKe0VQuS89yuoffLoNCs8rV24P3Eeq1GeAtonjvTK0A5KmKAEaOon1=deqQcZrZ5MBu58HzkequWQ5XC9Fon83ctoffFHaEQFtN9aIonfjAq9eqW0L6F9W4=eq=2pOQRUgAM56DKoffZ6BYeq7sYononKZV=eq0K9KdW=VononAid6Uon6GeoffW=onD=OffonEQ=offG=39MoNyOn=EQOff7offOn5DSOffOn9OnW=43Uk=OffOnON" 
# Chama a função calculadora_de_soma com o texto de entrada
calculadora_de_soma(texto_entrada)
