






The pre module
===============




(Implementation). This module is a low-level implementation module for
the 1.5.2 **`re <re.htm>`__** module. There’s usually no need to use
this module directly (and code using it may stop working in future
releases).

**Example: Using the pre module**

.. sourcecode:: python

    
    # File: `pre-example-1.py <pre-example-1.py>`__
    
    import pre
    
    p = pre.compile("[Python]+")
    
    print p.findall("Python is not that bad")
    


.. sourcecode:: python

    
    ['Python', 'not', 'th', 't']



