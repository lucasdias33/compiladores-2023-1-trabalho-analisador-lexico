import re

regex_patterns = {
    'palavras_chave': r'\b(int|char|long|short|float|double|void|if|else|for|while|do|break|continue|struct|switch|case|default|return)\b',
    'operadores': r'(\+|\-|\*|\/|\+\+|\-\-|\!|\&|\%|\->|\=\=|\!\=|\|\||\&\&|\+=|\-=|\*=|\/=|<|>|<=|>=|\=)',
    'delimitadores': r'(\(|\)|\[|\]|\{|\}|\;|\,)',
    'int_literal': r'\d+',
    'float_literal': r'\d+\.\d+',
    'string_literal': r'\".*?\"',
    'char_literal': r'\'.*?\'',
    'identificador': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
}

regex_pattern = '|'.join('(?P<%s>%s)' % pair for pair in regex_patterns.items())

def tokenizar(codigo):
    tokens = []
    for match in re.finditer(regex_pattern, codigo):
        tipo = match.lastgroup
        valor = match.group(tipo)
        if tipo == 'palavras_chave':
            tipo = valor.upper()
        tokens.append({'tipo': tipo, 'valor': valor})
    return tokens

codigo = '''
int main()
{
    printf("Hello World");
    int a = 10;
    float b = 3.14;
    char c = 'A';
    a= 10 + b;
    return 0;
}
'''

tokens = tokenizar(codigo)
for token in tokens:
    print(token['tipo'], token['valor'])