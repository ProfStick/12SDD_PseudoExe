"""PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:
    TODO
"""

from rply import LexerGenerator
from rply import ParserGenerator
# from pse_ast.pse_ast import Display, Number

TOKENS = [('KW_BEGIN', 'BEGIN'),
    ('KW_END', 'END'),
        ('KW_DISPLAY', 'DISPLAY'),
        ('PROG_NAME', '[A-Z][a-zA-Z0-9]*'),
        ('INTEGER','-?[0-9]+'),
        ]

class Lexer(object):
    """Defines a lexer for the PseudoExe language.
    """

    def __init__(self):
        """Inits the lexer."""
        self.lexer = LexerGenerator()


    def _add_tokens(self):
        """add new tokens to the lexer

        Args:
            n/a

        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """

        for t in TOKENS:
            self.lexer.add(*t)

        
        #this is just to catch all the errors so remove when not debug
        # self.lexer.add('undef', '.')

        # Ignore spaces
        self.lexer.ignore('\s+')
        self.lexer.ignore("\n+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

class Parser(object):
    """Defines a Parser for the PseudoExe language.
    """

    def __init__(self):
        """Inits parser generator.
        """
        # extract the token makes from TOKENS as a list
        tokens = [t[0] for t in TOKENS]
        self.pg = ParserGenerator(tokens)

    def parse(self):
        """define the syntax for the language
        """

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