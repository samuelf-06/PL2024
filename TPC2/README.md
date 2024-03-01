# TPC2 - Conversor de Markdown para HTML

Este é um script simples em Python que converte texto escrito em Markdown para HTML. Aqui está uma explicação sobre o que cada parte do código faz:

## Cabeçalhos
O código reconhece linhas iniciadas por "#" e as converte em tags HTML de cabeçalho, usando as tags "h1", "h2" e "h3" para os diferentes níveis de cabeçalho.

## Formatação de Texto
O script identifica texto entre "**" e o converte em negrito, usando a tag "b", e texto entre "*" para itálico, usando a tag "i".

## Listas Numeradas
Linhas começadas por números seguidos de um ponto são identificadas como itens de uma lista numerada e são envolvidas por tags "li". No final, todas as linhas são agrupadas dentro de uma lista ordenada "ol".

## Links
Qualquer texto dentro de colchetes "[ ]" seguido por uma URL entre parênteses "( )" é reconhecido como um link e transformado em uma tag de âncora HTML "a", com o texto como o conteúdo do link.

## Imagens
O script identifica linhas que começam com "![ ]" seguido por um URL de imagem e converte-as em tags de imagem HTML "img", com o texto dentro dos colchetes como texto alternativo.

Depois de executar o script, o HTML gerado pode ser copiado e colado onde for necessário.
