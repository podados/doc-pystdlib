






The ucnhash module
===================




(Implementation, 2.0 only) This module is an implementation module,
which provides a name to character code mapping for Unicode string
literals. If this module is present, you can use \N{} escapes to map
Unicode character names to codes.



In Python 2.1, the functionality of this module was moved to the `
**unicodedata** <unicodedata.htm>`__ module.

**Example: Using the ucnhash module**

.. sourcecode:: python

    
    # File: `ucnhash-example-1.py <ucnhash-example-1.py>`__
    
    # Python imports this module automatically, when it sees
    # the first \N{} escape
    # import ucnhash
    
    print repr(u"\N{FROWN}")
    print repr(u"\N{SMILE}")
    print repr(u"\N{SKULL AND CROSSBONES}")
    


.. sourcecode:: python

    
    u'\u2322'
    u'\u2323'
    u'\u2620'



