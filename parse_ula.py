__author__ = 'VHLAND002'

import ply.yacc as yacc

from lex_ula import tokens
import lex_ula




'''
# program -> statement*
def p_program_statement(p):
    'program : statement*'
    p[0] = p[1]
'''


# statement -> ID = expression
def p_statement_expression(p):
    'statement : ID EQUAL expression'
    p[0] = p[1] = p[3]


# Expression -> Expression @ Term
def p_expression_add(p):
    'expression : expression ADD term'
    p[0] = float(p[1]) + float(p[3])


# Expression -> Expression $ Term
def p_expression_sub(p):
    'expression : expression SUB term'
    p[0] = float(p[1]) - float(p[3])


# Expression -> Term
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


# Term -> Term # Factor
def p_term_mult(p):
    'term : term MULT factor'
    p[0] = float(p[1]) * float(p[3])


# Term -> Term & Factor
def p_term_div(p):
    'term : term DIV factor'
    p[0] = float(p[1]) / float(p[3])


# Term -> Factor
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


# Factor -> (Expression)
def p_factor_expr(p):
    'factor : OBRACKET expression CBRACKET'
    p[0] = p[2]


# Factor -> float
def p_factor_float_literal(p):
    'factor : FLOAT_LITERAL'
    p[0] = float(p[1])


# Factor -> identifier
def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break

    if not s: continue
    result = parser.parse(s,lexer = lex_ula.lexer)
    print(result)