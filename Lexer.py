import ply.lex as lex
from tokens import tokens

#expresiones regulares
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+(\.\d*)?'
t_STRING = r'".*?"'
#control de linea para que las ignore
t_ignore = ' \t'

# saltos de linea control
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()

# obtener token con numero de linea
def analyze_code(code):
    lexer.input(code)
    tokens_with_line = []
    for token in lexer:
        tokens_with_line.append((token.type, token.value, token.lineno))
    return tokens_with_line
