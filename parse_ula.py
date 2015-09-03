__author__ = 'VHLAND002'

import ply.yacc as yacc

from lex_ula import tokens
import lex_ula
import sys



#start -> program
def p_start_program(p):
    'start : program'
    p[0] = ("Start\n",p[1])

# program -> statement*
def p_program_statement(p):
    'program : statement'
    p[0] = ("Program\n",p[1])







# statement -> ID = expression
def p_statement_expression(p):
    'statement : ID EQUAL expression'
    #p[0] = p[1] = p[3]
    p[0] = ('AssignStatement',p[1],p[3])

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

t_ignore = 'WHITESPACE'

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
def p_factor_expr(p):
    'factor : OBRACKET expression CBRACKET'
    #p[0] = p[2]
    p[0] = ('AssignStatement4',p[2])




# Factor -> float
def p_factor_float_literal(p):
    'factor : FLOAT_LITERAL'
    #p[0] = float(p[1])
    p[0] = ('FloatExpression', p[1])



# Factor -> identifier
def p_factor_id(p):
    'factor : ID'
    #p[0] = p[1]
    p[0] = ('AssignStatement6',p[1])


# Error rule for syntax errors
def p_error(p):
    if p.value == 'WHITESPACE' or p.value == 'COMMENT':
        print("Skipped")
        parser.errok()
    else:
        print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


#inFile = open(sys.argv[1], 'r')

#lex_ula.importFile(str(sys.argv[1]))
inFile = open("ula_samples/comments.tkn", 'r')
data = inFile.read()
inFile.close()
# Give the lexer some input

result = parser.parse(data,lexer = lex_ula.lexer)
print(result)