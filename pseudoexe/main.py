'''PseudoExe project main script to process a *.pse script.'''

import copy
from pseudoexe import Lexer, Parser

def lexer_print(tokens):
    '''prints a list of tokens from a lexer.
    
    this needs to be done inside a function
    or some weird $eof token is generated
    because iterating through lexer streams
    seems to break them
    
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
    fn = 'scripts/script001.pse'
    with open(fn, 'r') as file:
        script = file.read()

    print(f'{script} \n')

    # now the lexical analysis
    tokens = lexer.lex(script)

    # It would be nice to print the result of the lexical analysis
    # but lexer streams seem pretty sensitive :(
    # if you do anything with them they break
    # so lets copy it and pass the copy to a function to print it
    lexer_print(copy.copy(tokens))
    
    # now the syntactical analysis
    parser.parse(tokens).eval()

if __name__ == "__main__":
    main()