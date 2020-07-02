import copy
from pseudoexe.pseudoexe import Lexer, Parser

def lexer_print(tokens):
    '''prints a list of tokens from a lexer.
    
    this needs to be done inside a function
    or some weird $eof token is generated
    
    Args:
        tokens: a list of tokens (token_type, token_name)
    Returns:
        Nothing: 
    Raises:
        NoError: 
    '''
    lexer_stream = tokens

    for t in lexer_stream:
        print(t)
    print('\n')

def main():

    #instantiate the lexer and the parser
    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser() #TODO put this in the parser class

    # open the script and print its contents
    fn = 'script001.pse'
    with open(fn, 'r') as file:
        text = file.read()

    print(f'{text} \n')

    tokens = lexer.lex(text)

    # lexer streams seem pretty sensitive
    # if you do anything with them they break
    # so lets copy it and pass it to a function to protect it
    lexer_print(copy.copy(tokens))
    
    output = parser.parse(tokens).eval()

if __name__ == "__main__":
    main()