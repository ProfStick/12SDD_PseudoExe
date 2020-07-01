""" A sandpit to test code snippets.
"""
from pseudoexe import pseudoexe as pe

test_test="""
BEGIN
    Let
    Display
    4 = 2 * 2
    ==
    36 = 6 ** 2
    42 
END
"""
lexer = pe.Lexer().get_lexer()
tokens = lexer.lex(test_test)

for t in tokens:
    print(t)