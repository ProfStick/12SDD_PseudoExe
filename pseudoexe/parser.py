"""A parser for PseudoExe language project.

Parses a PseudoExe language script and performs syntactical analysis.

  Typical usage example:

  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

class Parser(object):
    """Summary of class here.

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

    