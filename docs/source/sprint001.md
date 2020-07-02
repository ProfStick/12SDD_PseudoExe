## Sprint 001
The first sprint was to write the EBNF, lexer, parser, ast and main requires to run the following simple script - script001.pse:

```text
BEGIN Script001

    DISPLAY 42

END Script001
```
### Sprint001 EBNF
```ebnf
digit = '0'|'1'|...|'9';
lc_letter = 'a'|'b'|...|'z';
uc_letter = 'A'|'B'|...|'Z';

integer = <digit>, {<digit>};

programName = <uc_letter>, {<letter>};

output = 'DISPLAY', <integer>;

terminator = 'BEGIN'|'END', <programName>;

program = <terminator>, output, <terminator>;
```

### Sprint001 lexer and parser
```python
"""PseudoExe language project.

Defines a lexicon and parser for the PseudoExe language.


  Typical usage example:
    TODO
"""
import sys

from rply import LexerGenerator
from rply import ParserGenerator
from ast.ast import Display, Number

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
```

### Sprint001 Abstraxct Syntax Tree
```python
"""ast - Abstract syntax tree for pseudoexe.
"""       
        
class Number():
    '''Evaluates an integer'''
    def __init__(self, value):
        self.value = value

    def eval(self):
        return eval(self.value)


class Display():
    '''Output to the standard output.'''
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
```

### Sprint001 Main
```python
import copy
from pseudoexe.pseudoexe import Lexer, Parser

def lexer_print(tokens):
    '''prints a list of tokens from a lexer.
    
    this needs to be done inside a function
    or some weird $eof token is generated
    becasue iterating through a lexer stream
    seems to destroy it
    
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
```

### Sprint001 Output
```text
BEGIN Script001

    DISPLAY 42 

END Script001
 

Token('KW_BEGIN', 'BEGIN')
Token('PROG_NAME', 'Script001')
Token('KW_DISPLAY', 'DISPLAY')
Token('INTEGER', '42')
Token('KW_END', 'END')
Token('PROG_NAME', 'Script001')


42
```

Success!