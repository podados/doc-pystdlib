






The reconvert module
=====================




This module converts old-style regular expressions, as used by the
**`regex <regex.htm>`__** module to the new style used by the **`re
<re.htm>`__** module. It can also be used as a command line tool.

**Example: Using the reconvert module**

.. sourcecode:: python

    
    # File: `reconvert-example-1.py <reconvert-example-1.py>`__
    
    import reconvert
    
    for pattern in ("abcd", "a\(b*c\)d", "\<\w+\>"):
        print pattern, "=>", reconvert.convert(pattern)
    


.. sourcecode:: python

    
    abcd => abcd
    a\(b*c\)d => a(b*c)d
    \<\w+\> => \b\w+\b



