__author__ = 'VHLAND002'


import lex_ula


def main():
    print("Program started...")
    data = '''
        testName_ 1232
        _test2
        12test
        jkl
        @#=&$()
        //testcomment
        '''

    lexer = lex_ula.Lexer()
    lexer.build();
    #lexer.test(data);
    print("\nRunning comments file now...")
    lexer.importFile("ula_samples/comments.ula")
    print("\nRunning complex file now...")
    lexer.importFile("ula_samples/complex.ula")
    print("\nRunning exprs file now...")
    lexer.importFile("ula_samples/exprs.ula")
    print("\nRunning floats file now...")
    lexer.importFile("ula_samples/floats.ula")
    print("\nRunning var assigns file now...")
    lexer.importFile("ula_samples/var_assigns.ula")

    print("\nProgram ended...")

if __name__ == "__main__":
    main()
