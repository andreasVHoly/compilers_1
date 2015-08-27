__author__ = 'VHLAND002'

import lex


class Lexer(object):



    #tokens
    tokens = ('ID', 'FLOAT_LITERAL_VALUE', 'ADD', 'SUB', 'MULT', 'DIV', 'EQUAL', 'OBRACKET', 'CBRACKET', 'WHITESPACE', 'COMMENT')
    # Regular expression rules for simple tokens

    t_ADD = r'\@'
    t_SUB = r'\$'
    t_MULT = r'\#'
    t_DIV = r'\&'
    t_EQUAL = r'\='
    t_OBRACKET = r'\('
    t_CBRACKET = r'\)'


    #regular expressions

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.value = '' + t.value
        return t


    def t_FLOAT_LITERAL_VALUE(self,t):
        #if we find a digit and can have 1 or more iterations of digits
        r'\d+'
        t.value = int(t.value)
        return t


    def t_COMMENT(self,t):
        #means we check for // and go up until the end of the line ie \n (specified by the .) and then have 0 or more iterations of this (*)
        r'\//.*'
        t.value = "COMMENT"
        return t

    '''
    def t_newline(t):
        r'\n+'
        t_WHITESPACE(t)
        t.lexer.lineno += len(t.value)
    '''

    def t_WHITESPACE(self,t):
        #check for either of the characters and mark them as whitespace
        r'[ \t\r\n]+'
        t.value = 'WHITESPACE'
        return t


    def t_error(self,t):
        print("Bad char '%s'" % t.value[0])
        t.lexer.skip(1)




    #builds the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)



    #testing method which received some input to be passed through
    def test(self, data):
        # Test it out


        # Give the lexer some input
        self.lexer.input(data)

        # Tokenize
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


    def importFile(self, fileName):
        inFile = open(fileName, 'r')
        data = inFile.read()
        inFile.close()
        # Give the lexer some input
        self.lexer.input(data)

        # Tokenize
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
