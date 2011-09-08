






The pickle module
==================




This module is used to serialize data; that is, convert data to and
from character strings, so that they can be stored on file or sent
over a network. It’s a quite a bit slower than **marshal**, but it
can handle class instances, shared elements, and recursive data
structures, among other things.



There’s also a faster C implementatation available, `cPickle
<cpickle.htm>`__, which can usually be used as a drop-in replacement.

**Example: Using the pickle module**

.. sourcecode:: python

    
    # File: `pickle-example-1.py <pickle-example-1.py>`__
    
    import pickle
    
    value = (
        "this is a string",
        [1, 2, 3, 4],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
        )
    
    data = pickle.dumps(value)
    
    # intermediate format
    print type(data), len(data)
    
    print "-"*50
    print data
    print "-"*50
    
    print pickle.loads(data)
    


.. sourcecode:: python

    
     121
    --------------------------------------------------
    (S'this is a string'
    p0
    (lp1
    I1
    aI2
    aI3
    aI4
    a(S'more tuples'
    p2
    F1.0
    F2.3
    F4.5
    tp3
    S'this is yet another string'
    p4
    tp5
    .
    --------------------------------------------------
    ('this is a string', [1, 2, 3, 4], ('more tuples',
    1.0, 2.3, 4.5), 'this is yet another string')




On the other hand, **pickle** cannot handle code objects (but see the
**`copy_reg <copy-reg.htm>`__** module for a way to fix this).



By default, pickle uses a text-based format. You can also use a binary
format, in which numbers and binary strings are stored in a compact
binary format. The binary format usually results in smaller files.

**Example: Using the pickle module in binary mode**

.. sourcecode:: python

    
    # File: `pickle-example-2.py <pickle-example-2.py>`__
    
    import pickle
    import math
    
    value = (
        "this is a long string" * 100,
        [1.2345678, 2.3456789, 3.4567890] * 100
        )
    
    # text mode
    data = pickle.dumps(value)
    print type(data), len(data), pickle.loads(data) == value
    
    # binary mode
    data = pickle.dumps(value, 1)
    print type(data), len(data), pickle.loads(data) == value



