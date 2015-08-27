__author__ = 'VHLAND002'

import lex

#tokens
#tokens = ('ID', 'FLOAT_LITERAL_VALUE', '@', '$', '#', '&', '=', '(', ')', 'WHITESPACE', 'COMMENT')
tokens = ('ID', 'FLOAT_LITERAL_VALUE', 'ADD', 'SUB', 'MULT', 'DIV', 'EQUAL', 'OBRACKET', 'CBRACKET', 'WHITESPACE', 'COMMENT')


# Regular expression rules for simple tokens
'''
t_    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
'''

t_ADD = r'\@'
t_SUB = r'\$'
t_MULT = r'\#'
t_DIV = r'\&'
t_EQUAL = r'\='
t_OBRACKET = r'\('
t_CBRACKET = r'\)'


#regular expressions

def t_ID(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    t.value = '' + t.value
    return t


def t_FLOAT_LITERAL_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\//.*'
    t.value = "COMMENT"
    return t

'''
def t_newline(t):
    r'\n+'
    t_WHITESPACE(t)
    t.lexer.lineno += len(t.value)
'''

def t_WHITESPACE(t):
    r'[ \t\r\n]'
    t.value = 'WHITESPACE'
    return t

#t_ignore  = ' \t'

def t_error(t):
    print("Bad char '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()




def main():

    # Test it out
    data = '''
    testName_ 1232
    _test2
    12test
    jkl
    @#=&$()
    //testcomment
'''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)


if __name__ == "__main__":
    main()




