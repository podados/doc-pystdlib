






The struct module
==================




This module contains functions to convert between binary strings and
Python tuples. The **pack** function takes a format string and one or
more arguments, and returns a binary string. The **unpack** function
takes a string and returns a tuple.

**Example: Using the struct module**

.. sourcecode:: python

    
    # File: `struct-example-1.py <struct-example-1.py>`__
    
    import struct
    
    # native byteorder
    buffer = struct.pack("ihb", 1, 2, 3)
    print repr(buffer)
    print struct.unpack("ihb", buffer)
    
    # data from a sequence, network byteorder
    data = [1, 2, 3]
    
    buffer = struct.pack("!ihb", *data)
    
    # in Python 1.5.2 and earlier, use this instead:
    # buffer = apply(struct.pack, ("!ihb",) + tuple(data))
    
    print repr(buffer)
    print struct.unpack("!ihb", buffer)
    


.. sourcecode:: python

    
    '\001\000\000\000\002\000\003'
    (1, 2, 3)
    '\000\000\000\001\000\002\003'
    (1, 2, 3)



