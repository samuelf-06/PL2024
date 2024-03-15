# TPC4: Análise Léxica

## Explicação dos Tokens

- **SELECT:** Corresponde à palavra-chave 'SELECT' em qualquer combinação de maiúsculas e minúsculas.
- **FROM:** Corresponde à palavra-chave 'FROM' em qualquer combinação de maiúsculas e minúsculas.
- **WHERE:** Corresponde à palavra-chave 'WHERE' em qualquer combinação de maiúsculas e minúsculas.
- **COMMA:** Corresponde à vírgula (',').
- **GE:** Corresponde ao operador de comparação 'maior ou igual' ('>=').
- **IDENTIFIER:** Corresponde a identificadores, ou seja, nomes de tabelas, colunas, etc.
- **NUMBER:** Corresponde a números inteiros.


## Funcionamento do Código

O código utiliza expressões regulares para identificar padrões na consulta SQL, como palavras-chave, operadores e identificadores. De seguida, transforma esses padrões nos correspondentes tokens armazenando-os numa lista. O resultado é uma lista de tokens que representam as componentes individuais da consulta SQL.
