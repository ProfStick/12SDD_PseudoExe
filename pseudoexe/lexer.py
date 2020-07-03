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

        pass