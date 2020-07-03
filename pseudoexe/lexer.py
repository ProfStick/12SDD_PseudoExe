"""PseudoExe language lexer.

Defines a lexicon for the PseudoExe language.


  Typical usage example:
    #instantiate the lexer and the parser
    lexer = Lexer().get_lexer()
    
    # open the script and print its contents
    fn = 'script_name.pse'
    with open(fn, 'r') as file:
        script = file.read()

    print(f'{script} \n')

    tokens = lexer.lex(script)
"""

from rply import LexerGenerator

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
        self.lexer.ignore('\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
