def t_NUMBER(token):
    
    r'-?[0-9]+\.?[0-9]*'
    
    token.value = float(token.value)
    
    return token
