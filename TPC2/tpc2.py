import re

def markdown_to_html(markdown_text):
    # Cabeçalhos
    markdown_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)
    
    # Bold
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown_text)
    
    # Itálico
    markdown_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown_text)
    
    # Lista numerada
    markdown_text = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = '<ol>' + markdown_text + '</ol>'
    
    # Link
    markdown_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown_text)
    
    # Imagem
    markdown_text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', markdown_text)
    
    return markdown_text

# Testando a função com exemplos
markdown_exemplo = """
# Exemplo de Cabeçalho
## Outro cabeçalho
Este é um **exemplo** de texto em Markdown.
E este é um *exemplo* de lista numerada:
1. Primeiro item
2. Segundo item
3. Terceiro item

Veja mais informações em [Google](https://www.google.com) ou na imagem a seguir:
![Logo do Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
"""

html = markdown_to_html(markdown_exemplo)
print(html)
