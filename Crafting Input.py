import ply.lex as lex

webpage = """This is <b>webpage!"""

tokens = ('LANGLE', # <
          'LANGLESLASH', # </
          'RANGLE', # >
          'EQUAL', # =
          'STRING', # "hello"
          'WORD', # Welcome!
          )

t_ignore = ' ' # shortcut for whitespace

def t_newline(token):
    
    r'\n'
    
    token.lexer.lineno += 1
    
    pass

def t_LANGLESLASH(token):
    
    r'</'
    
    return token

def t_LANGLE(token):
    
    r'<'
    
    return token

def t_RANGLE(token):
    
    r'>'
    
    return token

def t_EQUAL(token):
    
    r'='
    
    return token

def t_STRING(token):
    
    r'"[^"]*"'
    
    token.value = token.value[1:-1]
    
    return token

def t_WORD(token):
    
    r'[^ <>\n]+'
    
    return token

htmllexer = lex.lex()

htmllexer.input(webpage)

while True:
    
    tok = htmllexer.token()
    
    if not tok: break

    print (tok)
