"""PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:
    TODO
"""

# sys.path.append(".")

from rply import LexerGenerator
from rply import ParserGenerator
from ast.ast import Sum, Display, Number, Sequence

TOKENS = [("TERM_BEGIN", "BEGIN"),
        ("TERM_END", "END"),
        ('OP_DISPLAY', 'Display'),
        ('PROG_NAME', '[A-Z][a-zA-Z0-9]*'),
        ('VARIABLE', '[a-z][a-zA-Z0-9]*'),
        ('INTEGER','-?[0-9]+'),
        ('OP_ASSIGN','='),
        ('OPERATION','[+-/*]'),

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

    def parse(self):
        """Longer description of desired functionality

        Args:
            required_variable: A required argument
            optional_variable: An optional argument

        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """

        @self.pg.production('program : TERM_BEGIN PROG_NAME sequence TERM_END PROG_NAME')
        def program(p):
            return p[2]

        
        @self.pg.production('sequence : sequence statement')
        def sequence(p):
            return Sequence(p)

        @self.pg.production('sequence : statement')
        def sequence_statement(p):
            return p[0]

        @self.pg.production('statement : output')
        def statememnt_out(p):
            return p[0]

        @self.pg.production('output : OP_DISPLAY value')
        def output(p):
            return Display(p[1])


        @self.pg.production('value : INTEGER')
        def value(p):
            return Number(p[0].value)


        # @self.pg.production('sequence : statement')
        # @self.pg.production('sequence : statement sequence')
        # def sequence(p):
        #     pass

        # @self.pg.production('statement : assignment')
        # @self.pg.production('statement : output')
        # @self.pg.production('statement : repetition')
        # def statement(p):
        #     pass

        # @self.pg.production('assignment : OP_LET VARIABLE OP_ASSIGN expression')
        # def assignment(p):
        #     pass


        # @self.pg.production('repetition : OP_FOR OP_LET VARIABLE OP_ASSIGN INTEGER OP_TO INTEGER OP_STEP INTEGER'
        #     ' sequence OP_NEXT VARIABLE')
        # def repetition(p):
        #     pass
        
        # @self.pg.production('expression : value')
        # @self.pg.production('expression : value OPERATION value')
        # def expression(p):
        #     pass


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()