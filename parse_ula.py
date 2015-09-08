__author__ = 'VHLAND002'

import ply.yacc as yacc

from lex_ula import tokens
import lex_ula
import sys



precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV'),
)


'''
#start -> program
def p_start(p):
    'start : program'
    p[0] = ("Start\n",p[1])

# program -> statement*
def p_program_statement(p):
    'program : statement'
    p[0] = ("Program\n",p[1])


start = 'start'
'''



# statement -> ID = expression
def p_statement_expression(p):
    'statement : ID EQUAL expression'
    #p[0] = p[1] = p[3]
    p[0] = ('AssignStatement',('ID',p[1]),p[3])
    content.append(p[0])

# Expression -> Expression @ Term
def p_expression_add(p):
    'expression : expression ADD term'
    #p[0] = float(p[1]) + float(p[3])
    p[0] = ('AddExpression',p[1],p[3])

# Expression -> Expression $ Term
def p_expression_sub(p):
    'expression : expression SUB term'
    #p[0] = float(p[1]) - float(p[3])
    p[0] = ('SubExpression',p[1],p[3])

# Expression -> Term
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    #p[0] = ('AssignStatement2',p[1])

# Term -> Term # Factor
def p_term_mult(p):
    'term : term MULT factor'
    #p[0] = float(p[1]) * float(p[3])
    p[0] = ('MulExpression',p[1],p[3])



# Term -> Term & Factor
def p_term_div(p):
    'term : term DIV factor'
    #p[0] = float(p[1]) / float(p[3])
    p[0] = ('DivExpression',p[1],p[3])

# Term -> Factor
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    #p[0] = ('AssignStatement3',p[1])


# Factor -> (Expression)
def p_factor_expression(p):
    'factor : OBRACKET expression CBRACKET'
    #p[0] = p[2]
    p[0] = ('AssignStatement4',p[2])




# Factor -> float
def p_factor_float_literal(p):
    'factor : FLOAT_LITERAL'
    #p[0] = float(p[1])
    p[0] = ('FloatExpression', ('FLOAT_LITERAL',p[1]))



# Factor -> identifier
def p_factor_id(p):
    'factor : ID'
    #p[0] = p[1]
    p[0] = ('AssignStatement6',p[1])


# Error rule for syntax errors
def p_error(p):
    '''
    if p.value == 'WHITESPACE' or p.value == 'COMMENT':
        print("Skipped")
        parser.errok()
    else:
    '''
    print("Syntax error in input!")



def convertTokenFile(name):
    print("starting... ")
    #tokFile = open(name, 'r')
    #tokFile = open("ula_samples/comments.tkn", 'r')
    #tokFile = open("ula_samples/exprs.tkn", 'r')
    #tokFile = open("ula_samples/floats.tkn", 'r')
    #data = tokFile.read()
    newData = []

    while True:
        tok = lex_ula.lexer.token()

        if not tok:
            statement = ''
            for t in range(0,len(newData)):
                statement += str(newData[t])
            content.append(str(statement))
            break

        if tok.value == 'COMMENT' or tok.value == 'WHITESPACE' :
            #print("skipped")
            continue
        elif tok.value == '=':
            statement = ''
            for t in range(0,len(newData)-1):
                statement += str(newData[t])
            content.append(str(statement))
            newData.clear()
            newData.append(previous.value)
            newData.append(tok.value)
        else:
            newData.append(tok.value)


        previous = tok

    for y in range(1,len(content)):
        #print(str(content[y]))
        mainTree.append(parser.parse(str(content[y]),lexer = lex_ula.lexer))
        #print(parser.parse(str(content[y]),lexer = lex_ula.lexer))

    #for k in content:

    #print(newData)
    #result = parser.parse(newData,lexer = lex_ula.lexer)
    #print(result)

finalData = 'Start\n\tProgram\n\t\t'
def traverseTree(tree):
    #print("\nStart...")
    #print("*"+str(tree))

    if len(tree) == 2:
        print("**"+ str(tree))
        return

    #print(tree[0])
    for i in range(0,len(tree)):


        #print("handling " + str(tree[i]))
        traverseTree(tree[i])
    '''
    for i in tree:
        if len(i) == 1:
            print(i)
            return
        else:
            traverseTree(i)
    '''




# Build the parser
parser = yacc.yacc()


#inFile = open(sys.argv[1], 'r')
# TODO renable this line for args
#tokenFile = lex_ula.importFile(str(sys.argv[1]))
#tokenFile = lex_ula.importFile("ula_samples/floats.ula",False)
#tokenFile = lex_ula.importFile("ula_samples/comments.ula",False)
print("\nexprs...")
content = []
mainTree = []
tokenFile = lex_ula.importFile("ula_samples/comments.ula",False)
convertTokenFile(tokenFile)
'''
print("\nfloats...")
content = []
tokenFile = lex_ula.importFile("ula_samples/floats.ula",False)
convertTokenFile(tokenFile)
print("\nvar_assigns...")
content = []
tokenFile = lex_ula.importFile("ula_samples/var_assigns.ula",False)
convertTokenFile(tokenFile)
print("\ncomplex...")
content = []
tokenFile = lex_ula.importFile("ula_samples/complex.ula",False)
convertTokenFile(tokenFile)
print("\ncomments...")
content = []
tokenFile = lex_ula.importFile("ula_samples/comments.ula",False)
convertTokenFile(tokenFile)
'''
traverseTree(mainTree)
'''
inFile = open("ula_samples/floats.tkn", 'r')
data = inFile.read()
inFile.close()
# Give the lexer some input

result = parser.parse(data,lexer = lex_ula.lexer,debug=True)
print(result)
'''







# TODO handling the token file
# get the token file
# ignore useless stuff
# if something usefull is encountered (ID, Float lit), add in its value
# else you add in the token type (or value, would be operators)
# what happens with the () -> ?


# TODO we need to traverse the tree


# TODO set up presedence of operators
