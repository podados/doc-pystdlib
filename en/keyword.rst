






The keyword module
===================




This module contains a list of the keywords used in the current
version of Python. It also provides a dictionary with the keywords as
keys, and a predicate function that can be used to check if a given
word is a Python keyword.

**Example: Using the keyword module**

.. sourcecode:: python

    
    # File: `keyword-example-1.py <keyword-example-1.py>`__
    
    import keyword
    
    name = raw_input("Enter module name: ")
    
    if keyword.iskeyword(name):
        print name, "is a reserved word."
        print "here's a complete list of reserved words:"
        print keyword.kwlist
    else:
        print name, "is a valid module name."


.. sourcecode:: python

    
    $ python keyword-example-1.py
    Enter module name: assert
    assert is a reserved word.
    here's a complete list of reserved words:
    ['and', 'assert', 'break', 'class', 'continue', 'def', 'del',
    'elif', 'else', 'except', 'exec', 'finally', 'for', 'from',
    'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or',
    'pass', 'print', 'raise', 'return', 'try', 'while']



