__author__ = 'VHLAND002'

import string


letters = list(string.ascii_letters)
digits = list(string.digits)





def whitespaceDFA(expr, debug):
    if expr[0] == ' ':
        if debug:print("space recognized")
    elif expr[0] == '\t':
        if debug:print("tab recognized")
    elif expr[0] == '\n':
        if debug:print("new line recognized")
    elif expr[0] == '\r':
        if debug:print("return recognized")
    else:
        if debug:print("no match")
        return False

    return True





def operatorsDFA(expr, debug):
    if expr[0] == "@":
        if debug:print("@ sign recognized")
    elif expr[0] == "$":
        if debug:print("$ sign recognized")
    elif expr[0] == "#":
        if debug:print("# sign recognized")
    elif expr[0] == "&":
        if debug:print("& sign recognized")
    elif expr[0] == "=":
        if debug:print("= sign recognized")
    elif expr[0] == "(":
        if debug:print("( sign recognized")
    elif expr[0] == ")":
        if debug:print(") sign recognized")
    else:
        if debug:print("no match")
        return False

    return True


def numericLitDFA(expr, debug):
    #check entry character
    if expr[0] in digits:
        if debug:print("first char is a digit")
    elif expr[0] == "+":
        if debug:print("first char is a +")
    elif expr[0] == "-":
        if debug:print("first char is a -")
    else:
        return False

    #cut off first char for the rest of the evaluation
    expr = expr[1:]
    count = 0
    for i in expr:
        if i in digits:
            if debug:print("digit found")
        elif i == ".":
            if debug:print("full stop found")
            count2 = 0
            for j in range(count+1, len(expr)):
                if debug:print(expr[j])
                if expr[j] in digits:
                    if debug:print("digit found")
                elif expr[j] == "e" or expr[j] == "E":
                    if debug:print("e found")
                    count3 = 0
                    for k in range(count2+1, len(expr)):
                        if expr[k] == "+" or expr[k] == "-":
                            if debug:print("+/- found")
                            count4 = 0
                            for l in range(count3+1, len(expr)):
                                if expr[l] in digits:
                                    if debug:print("found digit")
                                else:
                                    return False
                                count4 += 1
                        else:
                            return False
                        count3 += 1

                else:
                    return False
                count2 += 1
        else:
            return False
        count += 1

    return True


def indentifierDFA(expr, debug):
    if expr[0] in letters:
         if debug:print("first char is a letter")
    elif expr[0] == "_":
         if debug:print("first char is a underscore")
    else:
        return False

    expr = expr[1:]

    for i in expr:
        if i in letters:
             if debug:print("letter found")
        elif i in digits:
             if debug:print("digit found")
        elif i == "_":
            if debug:print("underscore found")
        else:
            return False

    return True

'''
def main():
    print("Starting main in dfa.py")
    testList = ['_test', 'tester', 'test!', '_test123', '12test123']
    for i in testList:
        if indentifierDFA(i, False):
            print("acceptable lexeme of type id")
        else:
            print("not acceptable lexeme")

    testList2 = ['1236', '1', '+1!', '-1', '-123', '-12.1' , "1.45686." , "--5451.4" , "578.e", "368.4e", "368.4e-2", "368.4E4"]
    for i in testList2:
        if numericLitDFA(i, False):
            print(i,": acceptable lexeme of type numerical literals")
        else:
            print(i,": not acceptable lexeme")


if __name__ == "__main__":
    main()

'''