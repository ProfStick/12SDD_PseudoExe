"""PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""
from rply import LexerGenerator
class Lexer(object):
    """Defines a lexer for the PseudoExe language.

    Longer class information....
    
    Attributes:
        n/a
    """

    def __init__(self):
        """Inits the lexar"""
        self.lexer = LexerGenerator()
        

    def _add_tokens(self):
        """Longer description of desired functionality

        Args:
            n/a
        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """
        self.lexer.add("INT", r'\d+')

        self.lexer.add("BEGIN", r"BEGIN")
        self.lexer.add("END", r"END")
        self.lexer.add("PRINT", r"Display")
        self.lexer.add("LET", r"Let")
        self.lexer.add("FOR", r"FOR")
        self.lexer.add("TO", r"TO")
        self.lexer.add("STEP", r"STEP")
        self.lexer.add("NEXT", r"NEXT")


        self.lexer.add("EQUALS", r"\=")
        self.lexer.add("PLUS", r"\+")
        self.lexer.add("MINUS", r"\-")
        self.lexer.add("INDICE", r"\**")
        self.lexer.add("MULTIPLY", r"\*")
        self.lexer.add("DIVIDE", r"\/")
        self.lexer.add("MOD", r"\%")        

        self.lexer.ignore('\s+')
        self.lexer.ignore('\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()


class Parser(object):
    """Defines a Parser for the PseudoExe language.

    Longer class information....
    
    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Longer description of desired functionality

        Args:
            required_variable: A required argument
            optional_variable: An optional argument

        Returns:
            None: but if it did you would describe it here

        Raises:
            NoError: but if it did you would describe it here
        """
        return None

def function_name(required_variable, optional_variable=None):
    """Short description.

    Longer description of desired functionality

    Args:
        required_variable: A required argument
        optional_variable: An optional argument

    Returns:
        None: but if it did you would describe it here

    Raises:
        NoError: but if it did you would describe it here
    """
    return None

    