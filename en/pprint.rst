






The pprint module
==================




This module is a “pretty printer” for Python data structures.
It’s useful if you have to print non-trivial data structures to the
console.

**Example: Using the pprint module**

.. sourcecode:: python

    
    # File: `pprint-example-1.py <pprint-example-1.py>`__
    
    import pprint
    
    data = (
        "this is a string", [1, 2, 3, 4], ("more tuples",
        1.0, 2.3, 4.5), "this is yet another string"
        )
    
    pprint.pprint(data)
    


.. sourcecode:: python

    
    ('this is a string',
     [1, 2, 3, 4],
     ('more tuples', 1.0, 2.3, 4.5),
     'this is yet another string')



