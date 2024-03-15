import re

tokens = {
    'SELECT': r'[Ss][Ee][Ll][Ee][Cc][Tt]',
    'FROM': r'[fF][Rr][Oo][Mm]',
    'WHERE': r'[Ww][Hh][Ee][Rr][Ee]',
    'COMMA': r',',
    'GE': r'>=',
    'IDENTIFIER': r'[a-zA-Z_]\w*',
    'NUMBER': r'\d+',
}

def analizador_lexico(sql_query):
    token_exprs = '|'.join('(?P<{}>{})'.format(token, expr) for token, expr in tokens.items())
    token_list = []
    for match in re.finditer(token_exprs, sql_query):
        token_type = match.lastgroup
        token_value = match.group()
        if token_type == 'NUMBER':
            token_value = int(token_value)
        elif token_type == 'IDENTIFIER':
            token_value = token_value.lower()  # Convertendo para minúsculas
            if token_value in ['select', 'from', 'where']:
                token_type = token_value.upper()
        if token_type != 'COMMA':
            token_list.append(token_value)
    return token_list

sql_query = "Select id, nome, salário from empregados WHERE salário >= 820"
tokens_list = analizador_lexico(sql_query)
tokens_list = [token if token != 'WHERE' else 'where' for token in tokens_list] # Replace 'WHERE' with 'where'
print(tokens_list)

