






The sre module
===============




(Implementation). This module is a low-level implementation module for
the 2.0 **`re <re.htm>`__** module. There’s usually no need to use
this module directly (and code using it may stop working in future
releases).

**Example: Using the sre module**

.. sourcecode:: python

    
    # File: `sre-example-1.py <sre-example-1.py>`__
    
    import sre
    
    text = "The Bookshop Sketch"
    
    # a single character
    m = sre.match(".", text)
    if m: print repr("."), "=>", repr(m.group(0))
    
    # and so on, for all 're' examples...
    


.. sourcecode:: python

    
    '.' => 'T'



