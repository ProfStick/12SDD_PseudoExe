'''PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:
    TODO
'''
import sys

from rply import LexerGenerator
from rply import ParserGenerator
from ast import Display, Number

# define the tokens to be used for the lexical analysis based on the EBNF
TOKENS = [('KW_BEGIN', 'BEGIN'),
        ('KW_END', 'END'),
        ('KW_DISPLAY', 'DISPLAY'),
        ('PROG_NAME', '[A-Z][a-zA-Z0-9]*'),
        ('INTEGER','-?[0-9]+'),
        ]

class Lexer(object):
    '''Defines a lexer for the PseudoExe language.'''

    def __init__(self):
        '''Inits the lexer.'''
        self.lexer = LexerGenerator()


    def _add_tokens(self):
        '''add new tokens to the lexer.'''

        for t in TOKENS:
            self.lexer.add(*t)

        # Ignore spaces
        self.lexer.ignore('\s+')
        self.lexer.ignore("\n+")

    def get_lexer(self):
        '''build and return the lexer.'''
        self._add_tokens()
        return self.lexer.build()

class Parser(object):
    '''Defines a Parser for the PseudoExe language.'''

    def __init__(self):
        '''Inits parser generator.
        
        Extracts the token names from the list of tokens (TOKENS)
        and passes them to the parser generator'''

        # extract the token names from TOKENS as a list
        tokens = [t[0] for t in TOKENS]
        self.pg = ParserGenerator(tokens)

    def parse(self):
        '''define the syntax for the language based on the EBNF.

        parses the script and passes the results to the abstract syntax tree (AST)
        '''

        @self.pg.production('program : KW_BEGIN PROG_NAME output KW_END PROG_NAME')
        def program(p):
            return p[2]

        @self.pg.production('output : KW_DISPLAY value')
        def output(p):
            return Display(p[1])

        @self.pg.production('value : INTEGER')
        def value(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
