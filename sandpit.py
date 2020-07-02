from pseudoexe.pseudoexe import Lexer, Parser

fn = 'simple.pse'

with open(fn, 'r') as file:
    text = file.read()

print(text)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text)

# for t in tokens:
#     print(t)

pg = Parser()
pg.parse()
parser = pg.get_parser()
output = parser.parse(tokens).eval()
