import ply.lex as lex
from tokens import tokens, reserved

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_ASSIGN = r'='
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_UNDERSCORE = r'_'  # Token para el guion bajo

# Expresiones regulares con acciones
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'  # Ya no incluye el guion bajo
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

# Caracteres ignorados
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]} en la línea {t.lineno}")
    t.lexer.skip(1)

tokens_order = [
    'UNDERSCORE',
    'ID',
    'NUMBER',
    'STRING',
    'EQ',
    'NEQ',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LT',
    'GT',
    'LPAREN',
    'RPAREN'
]

# Construir el lexer
lexer = lex.lex()

def analyze_code(code):
    lexer.input(code)
    tokens_with_line = []
    for token in lexer:
        tokens_with_line.append((token.type, token.value, token.lineno))
    return tokens_with_line