from pseudoexe.pseudoexe import Lexer

fn = 'simple.pse'

with open(fn, 'r') as file:
    text = file.read()

print(text)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text)

for t in tokens:
    print(t)