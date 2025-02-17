reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQ', 'NEQ', 'LT', 'GT',
    'ASSIGN', 'EQUALS', 'LPAREN', 'RPAREN', 'UNDERSCORE',
] + list(reserved.values())