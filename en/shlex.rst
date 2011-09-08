






The shlex module
=================




This module provides a simple lexer (also known as tokenizer) for
languages based on the Unix shell syntax.

**Example: Using the shlex module**

.. sourcecode:: python

    
    # File: `shlex-example-1.py <shlex-example-1.py>`__
    
    import shlex
    
    lexer = shlex.shlex(open("samples/sample.netrc", "r"))
    lexer.wordchars = lexer.wordchars + "._"
    
    while 1:
        token = lexer.get_token()
        if not token:
            break
        print repr(token)
    


.. sourcecode:: python

    
    'machine'
    'secret.fbi'
    'login'
    'mulder'
    'password'
    'trustno1'
    'machine'
    'non.secret.fbi'
    'login'
    'scully'
    'password'
    'noway'



