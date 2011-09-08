






The marshal module
===================




This module is used to serialize data; that is, convert data to and
from character strings, so that they can be stored on file or sent
over a network.



Marshal uses a simple self-describing data format. For each data item,
the marshalled string contains a type code, followed by one or more
type specific fields. Integers are stored in little-endian order,
strings as a length field followed by the string’s contents (which
can include null bytes), tuples as a length field followed by the
objects that make up the tuple, etc.

**Example: Using the marshal module to serialize data**

.. sourcecode:: python

    
    # File: `marshal-example-1.py <marshal-example-1.py>`__
    
    import marshal
    
    value = (
        "this is a string",
        [1, 2, 3, 4],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
        )
    
    data = marshal.dumps(value)
    
    # intermediate format
    print type(data), len(data)
    
    print "-"*50
    print repr(data)
    print "-"*50
    
    print marshal.loads(data)
    


.. sourcecode:: python

    
     118
    --------------------------------------------------
    '(\004\000\000\000s\020\000\000\000this is a string
    [\004\000\000\000i\001\000\000\000i\002\000\000\000
    i\003\000\000\000i\004\000\000\000(\004\000\000\000
    s\013\000\000\000more tuplesf\0031.0f\0032.3f\0034.
    5s\032\000\000\000this is yet another string'
    --------------------------------------------------
    ('this is a string', [1, 2, 3, 4], ('more tuples',
    1.0, 2.3, 4.5), 'this is yet another string')




The marshal module can also handle code objects (it’s used to store
precompiled Python modules).

**Example: Using the marshal module to serialize code**

.. sourcecode:: python

    
    # File: `marshal-example-2.py <marshal-example-2.py>`__
    
    import marshal
    
    script = """
    print 'hello'
    """
    
    code = compile(script, "
    print type(data), len(data)
    
    print "-"*50
    print repr(data)
    print "-"*50
    
    exec marshal.loads(data)


.. sourcecode:: python

    
     81
    --------------------------------------------------
    'c\000\000\000\000\001\000\000\000s\017\000\000\00
    0\177\000\000\177\002\000d\000\000GHd\001\000S(\00
    2\000\000\000s\005\000\000\000helloN(\000\000\000\
    000(\000\000\000\000s\010\000\000\000



****



