__author__ = 'VHLAND002'

import lex
import sys

tokens = ('ID', 'FLOAT_LITERAL', 'ADD', 'SUB', 'MULT', 'DIV', 'EQUAL', 'OBRACKET', 'CBRACKET', 'WHITESPACE', 'MLCOMMENT', 'SLCOMMENT')

#class Lexer(object):



#tokens
#tokens = ('ID', 'FLOAT_LITERAL', 'ADD', 'SUB', 'MULT', 'DIV', 'EQUAL', 'OBRACKET', 'CBRACKET', 'WHITESPACE', 'MLCOMMENT', 'SLCOMMENT')
# Regular expression rules for simple tokens

t_ADD = r'\@'
t_SUB = r'\$'
t_MULT = r'\#'
t_DIV = r'\&'
t_EQUAL = r'\='
t_OBRACKET = r'\('
t_CBRACKET = r'\)'

#regular expressions

# def t_ID(self,t)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #t.value = ('ID', t.value)
    return t


# def t_FLOAT_LITERAL(self,t)
def t_FLOAT_LITERAL(t):
    #if we find a digit and can have 1 or more iterations of digits
    #r'\d+\.?\d+'

    r'[+-]?\d+(\.\d+)?([eE][+-]?\d+)?'
    #t.value = ('FLOAT_LITERAL',t.value)
    return t


# def t_SLCOMMENT(self,t):
def t_SLCOMMENT(t):
    #means we check for // and go up until the end of the line ie \n (specified by the .) and then have 0 or more iterations of this (*)
    r'//.*'
    t.value = "COMMENT"
    return t

# TODO make this one with slcomment
#def t_MLCOMMENT(self,t):
def t_MLCOMMENT(t):
    #check for this pattern: /* any number of things other than */ [^*/] up until */
    r'\/\*+[^*/]*\*+\/'
    t.value = "COMMENT"
    return t



#def t_WHITESPACE(self,t):
def t_WHITESPACE(t):
    #check for either of the characters and mark them as whitespace
    r'[ \t\r\n]+'
    t.value = 'WHITESPACE'
    return t


#def t_error(self,t):
def t_error(t):
    print("Bad char '%s'" % t.value[0])
    t.lexer.skip(1)


def importFile(fileName, write):
    inFile = open(fileName, 'r')
    data = inFile.read()
    inFile.close()
    # Give the lexer some input
    lexer.input(data)
    #TODO chnage this to normal without _1
    fileName = fileName[0:-4] + '.tkn'
    outFile = open(fileName, 'w')

    if write:
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break

            if tok.type == 'FLOAT_LITERAL' or tok.type == 'ID':
                outFile.write(tok.type + "," + str(tok.value) + '\n')
                print(tok.type + "," + str(tok.value))
            else:
                outFile.write(str(tok.value) + '\n')
                print(str(tok.value))

        outFile.close()


    return fileName



lexer = lex.lex()
#importFile(str(sys.argv[1]))
#importFile("ula_samples/floats.ula")



'''
#fil'eName = "ula_samples/comments.tkn"
inFile = open(sys.argv[1], 'r')
#inFile = open(fileName, 'r')
data = inFile.read()
inFile.close()
# Give the lexer some input
lexer.input(data)
outFile = open(sys.argv[1][0:-4] + '_1.tkn', 'w')
#outFile = open(fileName[0:-4] + '_1.tkn', 'w')


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'FLOAT_LITERAL' or tok.type == 'ID':
        outFile.write(tok.type + "," + str(tok.value) + '\n')
        print(tok.type + "," + str(tok.value))
    else:
        outFile.write(str(tok.value) + '\n')
        print(str(tok.value))

outFile.close()
'''





