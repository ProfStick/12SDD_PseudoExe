"""PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:
    TODO
"""

# sys.path.append(".")

from rply import LexerGenerator
from rply import ParserGenerator
# from ast import Sum, Display
from ast.ast import Sum, Display

TOKENS = [("TERM_BEGIN", "BEGIN"),
        ("TERM_END", "END"),
        ('OP_DISPLAY', 'Display'),
        ('OP_LET', 'Let'),
        ('OP_FOR', 'FOR'),
        ('OP_STEP', 'STEP'),
        ('OP_TO', 'TO'),
        ('OP_NEXT', 'NEXT'),
        ('PROG_NAME', '[A-Z][a-zA-Z0-9]*'),
        ('VARIABLE', '[a-z][a-zA-Z0-9]*'),
        ('INTEGER','-?[0-9]+'),
        ('OP_ASSIGN','='),
        ('OPERATION','[+-/*]'),
        ('OP_ADD','\+'),
        ]

class Lexer(object):
    """Defines a lexer for the PseudoExe language.

    Longer class information....
    
    Attributes:
        n/a
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
        self.lexer.add("UNDEF", ".")

        # Ignore spaces
        self.lexer.ignore('\s+')
        self.lexer.ignore("\n+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

class Parser(object):
    """Defines a Parser for the PseudoExe language.

    Longer class information....
    
    Attributes:
        
    """

    def __init__(self):
        """Inits parser generator.
        """
        # extract the token makes from TOKENS as a list
        tokens = [t[0] for t in TOKENS]
        self.pg = ParserGenerator(tokens)

    def parser(self):
        """Longer description of desired functionality

        Args:
            required_variable: A required argument
            optional_variable: An optional argument

        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """
        @self.pg.production('program: TERM_BEGIN PROG_NAME sequence TERM_END PROG_NAME')
        def program(p):
            pass
        
        @self.pg.production('sequence: statement')
        @self.pg.production('sequence: statement sequence')
        def sequence(p):
            pass

        @self.pg.production('statement: assignment')
        @self.pg.production('statement: output')
        @self.pg.production('statement: repetition')
        def statement(p):
            pass

        @self.pg.production('assignment: OP_LET VARIABLE OP_ASSIGN expression')
        def assignment(p):
            pass

        @self.pg.production('output: OP_DISPLAY VARIABLE')
        def output(p):
            pass

        @self.pg.production('repetition: OP_FOR OP_LET VARIABLE OP_ASSIGN INTEGER OP_TO INTEGER OP_STEP INTEGER'
            'sequence OP_NEXT VARIABLE')
        def repetition(p):
            pass
        
        @self.pg.production('expression: value')
        @self.pg.production('expression: value OPERATION value')
        def epxression(p):
            pass